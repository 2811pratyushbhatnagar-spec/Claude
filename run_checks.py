# One-command Tier-1 runner: validate (drift/governance), consistency, then regression.
import subprocess, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
rc = 0
for t in ("validate.py", "tests/test_consistency.py", "tests/test_regression.py"):
    print(f"\n===== {t} =====")
    r = subprocess.run([sys.executable, os.path.join(HERE, t)], cwd=HERE)
    rc |= r.returncode
print("\n" + ("ALL TIER-1 CHECKS PASS" if rc == 0 else "TIER-1 CHECKS FAILED"))
sys.exit(rc)
