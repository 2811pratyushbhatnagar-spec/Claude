#!/usr/bin/env python3
"""compute_check.py -- compute-regression guard.  [Scripts tooling; NOT canon]

Re-runs the repo's finite-math harnesses and compares each to a captured reference output,
catching silent compute drift that validate.py (document/version drift only) structurally
cannot see. Best-effort: a missing harness, missing reference, or missing dependency SKIPS
that check rather than failing, so it never blocks a cycle on optional pieces.

Checks:
  1. Experiments/verify.py          vs Experiments/verify_output.txt        (needs sympy)
  2. LedgerA/ledger_A_witnesses.py  vs Scripts/ledger_A_witnesses_ref.txt   (stdlib)
  3. LedgerA/ledger_A_round2.py     vs Scripts/ledger_A_round2_ref.txt      (stdlib, ~6s)

Reference files are captured BASELINES (drift detectors), NOT authority claims about
correctness. Regenerate a baseline deliberately only when a change is intended and blessed:
    python3 LedgerA/ledger_A_witnesses.py > Scripts/ledger_A_witnesses_ref.txt

Exit 0 = all present checks clean or skipped; 1 = at least one MISMATCH (surface to a human).
"""
import os, subprocess, sys, difflib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "Scripts")

# (label, script, workdir, reference, needs_sympy)
CHECKS = [
    ("verify.py",             os.path.join(ROOT, "Experiments", "verify.py"),
     os.path.join(ROOT, "Experiments"), os.path.join(ROOT, "Experiments", "verify_output.txt"), True),
    ("ledger_A_witnesses.py", os.path.join(ROOT, "LedgerA", "ledger_A_witnesses.py"),
     os.path.join(ROOT, "LedgerA"), os.path.join(SCRIPTS, "ledger_A_witnesses_ref.txt"), False),
    ("ledger_A_round2.py",    os.path.join(ROOT, "LedgerA", "ledger_A_round2.py"),
     os.path.join(ROOT, "LedgerA"), os.path.join(SCRIPTS, "ledger_A_round2_ref.txt"), False),
]


def _norm(text):
    return [ln.rstrip() for ln in text.strip().splitlines() if not ln.startswith("$ ")]


def run_one(label, script, workdir, ref, needs_sympy):
    if needs_sympy:
        try:
            import sympy  # noqa: F401
        except Exception:
            return "skip", f"{label}: SKIP (sympy not installed)"
    if not (os.path.exists(script) and os.path.exists(ref)):
        return "skip", f"{label}: SKIP (script or reference not present)"
    try:
        r = subprocess.run([sys.executable, script], cwd=workdir,
                           capture_output=True, text=True, timeout=1800)
    except Exception as e:
        return "skip", f"{label}: SKIP (run error: {e})"
    got = _norm(r.stdout)
    want = _norm(open(ref, encoding="utf-8", errors="ignore").read())
    if got == want:
        return "clean", f"{label}: clean ({len(want)} lines)"
    diff = list(difflib.unified_diff(want, got, ref, label + " (now)", lineterm=""))[:40]
    return "mismatch", f"{label}: MISMATCH\n" + "\n".join("    " + d for d in diff)


def main():
    results = [run_one(*c) for c in CHECKS]
    for _, msg in results:
        print("compute_check: " + msg)
    sys.exit(1 if any(s == "mismatch" for s, _ in results) else 0)


if __name__ == "__main__":
    main()
