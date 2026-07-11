#!/usr/bin/env python3
"""
cycle_check.py -- deterministic heartbeat for the reversible-contact research cycle.

PROCEDURES ONLY. This never edits canon, never touches a ledger, never makes a
governance decision. It runs validate.py, fingerprints the canon, detects whether
anything changed since the last run, and prints a heartbeat (or a delta summary).
Governance moves (promote conjecture->theorem, admit Ledger C, change Ledger B,
add ontology, publish) are human-only and are never performed here.

Usage:
    python cycle_check.py [--repo PATH] [--state-dir PATH] [--json] [--no-save]

Defaults: repo = parent of this script (works when installed in <repo>/Scripts/);
state-dir = <repo>/Scripts. State is written as create-only timestamped files so it
persists even on mounts that forbid unlink/rename. Exit 0 = validate clean, 1 = flagged.
"""
import argparse, glob, hashlib, json, os, subprocess, sys, datetime


def find_repo(script_dir, override):
    if override:
        return os.path.abspath(override)
    parent = os.path.dirname(script_dir)
    for cand in (parent, script_dir):
        if os.path.exists(os.path.join(cand, "status.json")):
            return cand
    d = script_dir
    for _ in range(5):
        if os.path.exists(os.path.join(d, "status.json")):
            return d
        d = os.path.dirname(d)
    return parent


def canon_manifest(repo):
    """Sorted [(relpath, sha256, size)] over status.json + every tracked *.md."""
    files = []
    sj = os.path.join(repo, "status.json")
    if os.path.exists(sj):
        files.append(sj)
    for p in glob.glob(os.path.join(repo, "**", "*.md"), recursive=True):
        rel = os.path.relpath(p, repo)
        if rel.split(os.sep)[0].startswith(".git"):
            continue
        files.append(p)
    manifest = []
    for p in sorted(set(files)):
        rel = os.path.relpath(p, repo).replace(os.sep, "/")
        with open(p, "rb") as f:
            data = f.read()
        manifest.append((rel, hashlib.sha256(data).hexdigest(), len(data)))
    return manifest


def canon_hash(manifest):
    h = hashlib.sha256()
    for rel, fh, _ in manifest:
        h.update(rel.encode()); h.update(b"\0"); h.update(fh.encode()); h.update(b"\n")
    return h.hexdigest()


def run_validate(repo):
    vp = os.path.join(repo, "validate.py")
    if not os.path.exists(vp):
        return None, "validate.py not found"
    try:
        r = subprocess.run([sys.executable, vp], cwd=repo,
                           capture_output=True, text=True, timeout=120)
        out = (r.stdout or "").strip()
        if r.stderr.strip():
            out += "\n" + r.stderr.strip()
        return r.returncode, out.strip()
    except Exception as e:
        return None, "validate error: %s" % e


def git_head(repo):
    try:
        r = subprocess.run(["git", "-C", repo, "rev-parse", "--short", "HEAD"],
                           capture_output=True, text=True, timeout=15)
        if r.returncode == 0 and r.stdout.strip():
            d = subprocess.run(["git", "-C", repo, "status", "--porcelain"],
                               capture_output=True, text=True, timeout=15)
            return r.stdout.strip() + ("-dirty" if d.stdout.strip() else "")
    except Exception:
        pass
    return None


def latest_ledgerE(repo):
    p = os.path.join(repo, "LedgerE", "evidence_log.md")           # canonical name post-unification
    if not os.path.exists(p):
        p = os.path.join(repo, "LedgerE", "ledger_E_evidence_log.md")  # legacy fallback
    if not os.path.exists(p):
        return None
    latest = None
    with open(p, encoding="utf-8", errors="ignore") as f:
        for line in f:
            s = line.strip()
            if s.startswith("## "):
                latest = s[3:].strip()
    return latest


def load_status(repo):
    try:
        return json.load(open(os.path.join(repo, "status.json")))
    except Exception:
        return None


def ledger_line(status):
    if not status:
        return "status.json unreadable"
    out = []
    for k in ("A", "B", "C", "D", "E"):
        i = status.get("ledgers", {}).get(k, {})
        out.append("%s %s/%s" % (k, i.get("version", "?"), i.get("state", "?")))
    return " · ".join(out)


def latest_state(state_dir):
    files = sorted(glob.glob(os.path.join(state_dir, ".cycle_state.*.json")))
    return files[-1] if files else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo")
    ap.add_argument("--state-dir", dest="state_dir")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-save", action="store_true")
    ap.add_argument("--no-bf", action="store_true", help="skip the brute-force chunk step")
    ap.add_argument("--bf-budget", type=float, default=240.0, help="seconds per brute-force chunk")
    args = ap.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo = find_repo(script_dir, args.repo)
    state_dir = args.state_dir or os.path.join(repo, "Scripts")

    vcode, vout = run_validate(repo)
    manifest = canon_manifest(repo)
    chash = canon_hash(manifest)
    ghead = git_head(repo)
    status = load_status(repo)
    ver = ledger_line(status)
    e_latest = latest_ledgerE(repo)
    now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    head_id = ghead if ghead else "canon:" + chash[:12]
    validate_clean = (vcode == 0)

    prev = {}
    pf = latest_state(state_dir)
    if pf:
        try:
            prev = json.load(open(pf))
        except Exception:
            prev = {}

    prev_hash = prev.get("canon_hash")
    first_run = prev_hash is None
    material_change = (not first_run) and (
        prev_hash != chash or bool(prev.get("validate_clean")) != validate_clean)

    changed = []
    if not first_run:
        pm = {r: fh for r, fh, _ in prev.get("manifest", [])}
        cm = {r: fh for r, fh, _ in manifest}
        for k in sorted(set(pm) | set(cm)):
            if pm.get(k) != cm.get(k):
                changed.append(("added: " if k not in pm else
                                "removed: " if k not in cm else "modified: ") + k)

    if not validate_clean:
        heartbeat = "validate FLAGGED -- see below -- " + head_id
    elif first_run:
        heartbeat = "cycle baseline established, validate clean -- " + head_id
    elif not material_change:
        heartbeat = "cycle clean, no material change -- " + head_id
    else:
        heartbeat = "cycle: material change detected -- " + head_id

    result = {
        "timestamp": now, "heartbeat": heartbeat,
        "validate_clean": validate_clean, "validate_output": vout,
        "canon_hash": chash, "git_head": ghead, "ledgers": ver,
        "ledgerE_latest": e_latest, "first_run": first_run,
        "material_change": bool(material_change), "changed_files": changed,
        "manifest": manifest,
    }

    if args.json:
        printable = {k: v for k, v in result.items() if k != "manifest"}
        print(json.dumps(printable, indent=2))
    else:
        print(heartbeat)
        print("  validate: " + (vout.splitlines()[0] if vout else "n/a"))
        print("  ledgers : " + ver)
        print("  canon   : %s   git: %s" % (chash[:12], ghead or "none (content-hash mode)"))
        if e_latest:
            print("  LedgerE : latest snapshot -- " + e_latest)
        if material_change and changed:
            print("  changes since last run:")
            for c in changed[:40]:
                print("    - " + c)
        if not validate_clean and vout:
            print("  --- validate output ---")
            for ln in vout.splitlines():
                print("  " + ln)
        print("  governance: promote / C-admit / B-change / D-add / publish are human-only (not done here).")

    if not args.no_save:
        try:
            os.makedirs(state_dir, exist_ok=True)
            stamp = now.replace(":", "").replace("-", "").replace("+", "p").replace("T", "-")
            path = os.path.join(state_dir, ".cycle_state.%s.%d.json" % (stamp, os.getpid()))
            with open(path, "x") as f:
                json.dump(result, f, indent=2)
        except Exception as e:
            sys.stderr.write("  [note] could not persist state: %s\n" % e)

    # TOKEN GATE (governance v2 / resource rule L1): deterministic software decides whether AI
    # is needed; AI never decides whether deterministic software should have run. A no-op cycle
    # requires NO model reasoning. Adversarial passes are scheduled reasoning and exempt.
    reasoning_needed = (not validate_clean) or material_change or first_run
    gate = ("STAGE-0 GATE (deterministic): reasoning-required -- context is COMPUTED, not chosen: "
            "changed objects + dependency closure only, never 'load the repo'" if reasoning_needed else
            "STAGE-0 GATE (deterministic): no-op -- fingerprint+validate+hash-compare found no change; "
            "model may exit immediately (adversarial/destroy passes are scheduled reasoning, exempt)")
    print("  " + gate)
    if reasoning_needed and changed:
        try:  # dependency closure: name the producers whose declared deps changed
            decl = json.load(open(os.path.join(repo, "DEPENDENCIES.json"), encoding="utf-8"))["declarations"]
            changed_names = [c.split(": ", 1)[-1] for c in changed]
            affected = [k for k, v in decl.items() if any(cn in v for cn in changed_names)]
            if affected:
                print("  dependency-closure -> affected producers: " + ", ".join(affected))
        except Exception:
            print("  HALT-NOT-DEGRADE: dependency declarations unreadable -- halt, never guess scope")
    try:  # run ledger (deterministic side of the token instrumentation)
        auto_dir = os.path.join(repo, ".automation")
        os.makedirs(auto_dir, exist_ok=True)
        with open(os.path.join(auto_dir, "run_ledger.jsonl"), "a", encoding="utf-8") as f:
            f.write(json.dumps({"t": now, "outcome":
                    ("flagged" if not validate_clean else
                     "change" if material_change else "no-op"),
                    "validate_clean": validate_clean, "files_changed": len(changed),
                    "gate": "reasoning" if reasoning_needed else "no-op",
                    "model_tokens": None}) + "\n")  # wrapper session appends token counts
        if not validate_clean:  # execution-evidence stream: the ONLY thing that reopens governance,
            # and only under a PRE-REGISTERED observation signal (GOVERNANCE-VERSION.json schema)
            with open(os.path.join(auto_dir, "execution_evidence.jsonl"), "a", encoding="utf-8") as f:
                f.write(json.dumps({"t": now, "type": "failure", "signal": "validator-effectiveness",
                                    "detail": "validate flagged: " + vout.splitlines()[0]}) + "\n")
    except Exception as e:
        sys.stderr.write("  [note] run-ledger append failed: %s\n" % e)

    # Brute-force chunk step (resumable; PROCEDURES ONLY; see WORKER-CONTRACT.md).
    # Guarded so a failure here never breaks the heartbeat. Skip with --no-bf.
    if not args.no_bf and validate_clean:
        try:
            bf = os.path.join(script_dir, "brute_force_step.py")
            if os.path.exists(bf):
                r = subprocess.run([sys.executable, bf, "--repo", repo,
                                    "--budget", str(args.bf_budget)],
                                   capture_output=True, text=True, timeout=args.bf_budget + 120)
                for ln in (r.stdout or "").strip().splitlines():
                    print("  " + ln)
                if r.returncode != 0 and r.stderr.strip():
                    print("  [bf-step note] " + r.stderr.strip().splitlines()[-1])
        except Exception as e:
            sys.stderr.write("  [note] brute-force step skipped: %s\n" % e)

    sys.exit(0 if validate_clean else 1)


if __name__ == "__main__":
    main()
