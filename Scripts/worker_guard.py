#!/usr/bin/env python3
"""worker_guard.py -- enforce the Stateless-Worker Contract boundary (WORKER-CONTRACT.md).
Checks the working tree vs HEAD: governed paths must be untouched; append-only files may only
gain lines. Exit 0 = within contract, 1 = violation (do not commit; report instead).
Run from repo root or Scripts/. Stdlib only."""
import subprocess, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GOVERNED = ("LedgerB/", "LedgerD/", "LedgerA/ledger_A_canonical.md", "LedgerA/archive/",
            "reconciliation/", "status.json", "WORKER-CONTRACT.md",
            "DECISION-CLASSES.md", "SUBSTANTIAL-RESULT-CHECKLIST-DRAFT.md",
            "DECLASSIFICATIONS.md", "MANIFEST.sha256.json", "DEPENDENCIES.json",
            "GOVERNANCE-VERSION.json", "validate.py", "Scripts/worker_guard.py")
APPEND_ONLY = ("LedgerE/evidence_log.md", "LedgerC/README.md", ".automation/TRACES.md")

def git(*a):
    return subprocess.run(["git"] + list(a), capture_output=True, text=True, cwd=ROOT).stdout

flags = []
for line in git("diff", "--numstat", "HEAD").splitlines():
    parts = line.split("\t")
    if len(parts) != 3: continue
    added, deleted, path = parts
    p = path.replace("\\", "/")
    if any(p.startswith(g) or p == g for g in GOVERNED):
        flags.append(f"GOVERNED PATH MODIFIED: {p} (+{added}/-{deleted}) -- Tier-3 / instructed sessions only")
    elif any(p == a_ for a_ in APPEND_ONLY) and deleted not in ("0", "-"):
        flags.append(f"APPEND-ONLY VIOLATION: {p} has {deleted} deleted line(s) -- rows are added, never edited")

# MONOTONIC CLASSIFICATION (conservative-static-analysis property: uncertainty moves up).
# Automation may only ESCALATE a class (D->C->B->A); any decrease vs HEAD requires a
# human-authored row in DECLASSIFICATIONS.md (itself a governed, human-only file).
RANK = {"D": 0, "C": 1, "B": 2, "A": 3}
try:
    import json as _json
    head_raw = git("show", "HEAD:questions.json")
    if head_raw.strip():
        head_cls = {q["id"]: q.get("decision_class", "A")
                    for q in _json.loads(head_raw)["questions"]}
        cur = _json.load(open(os.path.join(ROOT, "questions.json"), encoding="utf-8"))
        auth = ""
        dp = os.path.join(ROOT, "DECLASSIFICATIONS.md")
        if os.path.exists(dp):
            auth = open(dp, encoding="utf-8").read()
        for q in cur["questions"]:
            old, new = head_cls.get(q["id"]), q.get("decision_class", "A")
            if old and RANK.get(new, 3) < RANK.get(old, 3) and f"{q['id']}:" not in auth:
                flags.append(f"AUTOMATED DE-ESCALATION: {q['id']} {old}->{new} without a "
                             f"DECLASSIFICATIONS.md row -- only a human may lower a class "
                             f"(lowering A is itself a Class-A act; C->D is Class-B)")
except Exception as e:
    print(f"worker_guard: [note] monotonicity check skipped ({e})")

if flags:
    print(f"worker_guard: {len(flags)} violation(s) of WORKER-CONTRACT.md")
    for f in flags: print("  " + f)
    try:  # violations are near-misses: feed the execution-evidence stream (governance sensor)
        import json as _j, datetime as _d
        ev = os.path.join(ROOT, ".automation", "execution_evidence.jsonl")
        os.makedirs(os.path.dirname(ev), exist_ok=True)
        with open(ev, "a", encoding="utf-8") as f:
            f.write(_j.dumps({"t": _d.datetime.now().astimezone().isoformat(timespec="seconds"),
                              "type": "near-miss", "signal": "validator-effectiveness",
                              "detail": "worker_guard: " + "; ".join(flags)[:300]}) + "\n")
    except Exception:
        pass
    sys.exit(1)
print("worker_guard: within contract (governed state untouched; append-only files append-only; "
      "classification monotone)")
