#!/usr/bin/env python3
"""stage0_gate.py -- THE deterministic Stage-0 gate (constitutional router; governance v2).

PURE SCRIPT, NO MODEL. Replaces research-cycle-5h + automation-audit-5h with one gated path:
    fingerprint repo -> validate (constitutional core FIRST, root of trust) -> hash-compare.
- NO-OP path (the common case): one-line heartbeat, exit 0. ZERO model tokens.
- CHANGE path: write .automation/escalation_brief.md (the delta + its dependency closure --
  the ONLY context a model session should load; bounded output; honor all invariants), exit 10.
- HALT path (halt-not-degrade): validate failure / unreadable state / missing declarations ->
  exit 1, evidence record. NEVER skip a validator; budget scarcity slows, never degrades.
Folded from the old two: validate, drift-detect (fingerprint diff), staleness/automation-gap scan.
NOT folded: the brute-force chunk (manual until proven cheap) and model reasoning (spawned only
when this gate opens). Invariant: deterministic software decides whether AI is needed.
"""
import glob, hashlib, json, os, subprocess, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENERATED = ("SNAPSHOT.md", "DECISIONS.md", "EVIDENCE-RIVER.md", "snapshot.json", "status.html")
STATE = os.path.join(ROOT, ".automation", "gate_state.json")

def now(): return datetime.datetime.now().astimezone().isoformat(timespec="seconds")

def canonical_files():
    out = []
    for p in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
        rel = os.path.relpath(p, ROOT)
        top = rel.split(os.sep)[0]
        if top.startswith(".git") or top == ".automation" or os.path.basename(p) in GENERATED:
            continue
        out.append(p)
    for j in ("status.json", "questions.json", "counts.json", "DEPENDENCIES.json",
              "GOVERNANCE-VERSION.json", "MANIFEST.sha256.json"):
        p = os.path.join(ROOT, j)
        if os.path.exists(p): out.append(p)
    out += glob.glob(os.path.join(ROOT, "Scripts", "*.py")) + glob.glob(os.path.join(ROOT, "tests", "*.py"))
    return sorted(set(out))

def manifest():
    m = {}
    for p in canonical_files():
        rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
        m[rel] = hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]
    return m

def append(fname, rec):
    os.makedirs(os.path.join(ROOT, ".automation"), exist_ok=True)
    with open(os.path.join(ROOT, ".automation", fname), "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")

def main():
    ts = now()
    # 1. validate -- constitutional core first (root of trust), then everything else
    r = subprocess.run([sys.executable, os.path.join(ROOT, "validate.py")],
                       capture_output=True, text=True, cwd=ROOT, timeout=300)
    vline = (r.stdout or "").strip().splitlines()[0] if r.stdout else "validate: no output"
    if r.returncode != 0:
        print(f"GATE HALT | {vline} | {ts}")
        for ln in (r.stdout or "").splitlines()[1:6]: print("  " + ln)
        append("run_ledger.jsonl", {"t": ts, "outcome": "flagged", "gate": "halt", "model_tokens": 0})
        append("execution_evidence.jsonl", {"t": ts, "type": "failure",
                "signal": "validator-effectiveness", "detail": vline})
        sys.exit(1)
    # 2. fingerprint + staleness (drift-detect + automation-gap scan, deterministic)
    cur = manifest()
    fp = hashlib.sha256(json.dumps(cur, sort_keys=True).encode()).hexdigest()
    sys.path.insert(0, os.path.join(ROOT, "Scripts"))
    try:
        from brute_force_step import check_stale_packets
        stale = check_stale_packets(ROOT)
        stale = [s for s in stale if s.startswith("STALE") or s.startswith("UNPARSEABLE")]
    except Exception as e:
        print(f"GATE HALT | staleness scan unavailable ({e}) -- halt-not-degrade | {ts}")
        sys.exit(1)
    prev = {}
    if os.path.exists(STATE):
        try: prev = json.load(open(STATE, encoding="utf-8"))
        except Exception:
            print(f"GATE HALT | gate state unreadable -- halt-not-degrade | {ts}"); sys.exit(1)
    json.dump({"fp": fp, "manifest": cur, "t": ts}, open(STATE, "w", encoding="utf-8"))
    if not prev:
        print(f"GATE baseline | {vline} | canon {fp[:12]} | {ts}")
        append("run_ledger.jsonl", {"t": ts, "outcome": "baseline", "gate": "no-op", "model_tokens": 0})
        return
    # 3. compare
    if prev.get("fp") == fp and not stale:
        print(f"GATE no-op | {vline} | canon {fp[:12]} | {ts} | zero model tokens")
        append("run_ledger.jsonl", {"t": ts, "outcome": "no-op", "gate": "no-op", "model_tokens": 0})
        return
    # 4. CHANGE -> escalate: computed context only (delta + dependency closure), bounded output
    pm = prev.get("manifest", {})
    changed = sorted(set(k for k in set(pm) | set(cur) if pm.get(k) != cur.get(k)))
    producers = []
    try:
        decl = json.load(open(os.path.join(ROOT, "DEPENDENCIES.json"), encoding="utf-8"))["declarations"]
        producers = [k for k, v in decl.items() if any(c in v for c in changed)]
    except Exception:
        print(f"GATE HALT | dependency declarations unreadable -- halt-not-degrade | {ts}"); sys.exit(1)
    brief = [f"# ESCALATION BRIEF — generated {ts} (Stage-0 gate; Class-D artifact)",
             "", "Reasoning is required. Load ONLY the files below + their dependency closure —",
             "never the whole repository. Bounded output; evidence pointers over re-explanation.",
             "Honor: worker contract, monotonic classes, never-certify, halt-not-degrade.",
             "", "## Changed since last gate pass"]
    brief += [f"- {c}" for c in changed[:60]]
    if producers: brief += ["", "## Affected producers (dependency closure)"] + [f"- {p}" for p in producers]
    if stale: brief += ["", "## Stale packets (regenerate before review)"] + [f"- {s}" for s in stale]
    open(os.path.join(ROOT, ".automation", "escalation_brief.md"), "w", encoding="utf-8").write("\n".join(brief) + "\n")
    print(f"GATE OPEN — reasoning required | {len(changed)} changed | brief: .automation/escalation_brief.md | {ts}")
    append("run_ledger.jsonl", {"t": ts, "outcome": "change", "gate": "reasoning",
                                "files_changed": len(changed), "model_tokens": None})
    sys.exit(10)

if __name__ == "__main__":
    main()
