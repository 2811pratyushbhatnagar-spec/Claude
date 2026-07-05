#!/usr/bin/env python3
"""
compute_check.py -- compute-regression guard.  [Scripts tooling; NOT canon]

Re-runs Experiments/verify.py and compares its output to the recorded
Experiments/verify_output.txt. Catches silent math/compute drift that validate.py --
which only checks document/version drift -- structurally cannot see. This earns its place
by the same rule validate.py states: a new check is justified only if it catches a failure
nothing else catches.

Best-effort: if sympy is missing it SKIPS (exit 0) rather than failing, so it never blocks
a cycle on a missing optional dependency. Stdlib only otherwise.

Exit 0 = reproduces (or skipped); 1 = MISMATCH (surface to a human).
"""
import os, subprocess, sys, difflib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # repo root == Scripts/..
EXP = os.path.join(ROOT, "Experiments")
VERIFY = os.path.join(EXP, "verify.py")
SAVED = os.path.join(EXP, "verify_output.txt")


def _norm(lines):
    # ignore a leading "$ python3 verify.py" shell-prompt line and trailing blanks
    return [ln.rstrip() for ln in lines if not ln.startswith("$ ")]


def main():
    try:
        import sympy  # noqa: F401
    except Exception:
        print("compute_check: SKIP (sympy not installed; optional check)")
        sys.exit(0)
    if not (os.path.exists(VERIFY) and os.path.exists(SAVED)):
        print("compute_check: SKIP (verify.py or verify_output.txt missing)")
        sys.exit(0)

    r = subprocess.run([sys.executable, VERIFY], cwd=EXP, capture_output=True, text=True, timeout=1800)
    got = _norm(r.stdout.strip().splitlines())
    saved = _norm(open(SAVED, encoding="utf-8", errors="ignore").read().strip().splitlines())

    if got == saved:
        print(f"compute_check: clean  (verify.py reproduces {len(saved)} lines)")
        sys.exit(0)

    print("compute_check: MISMATCH  (verify.py output differs from verify_output.txt)")
    for d in difflib.unified_diff(saved, got, "verify_output.txt", "verify.py (now)", lineterm=""):
        print("  " + d)
    sys.exit(1)


if __name__ == "__main__":
    main()
