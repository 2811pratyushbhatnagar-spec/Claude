#!/usr/bin/env python3
"""
enumerate.py -- Carry-Set Separation (CSS) convergence probe.  [Experiments tooling; NOT canon]

This adds enumeration REACH without adding or altering any mathematics: it imports the
exact checks from verify.py (never reimplements them) and drives them over a configurable
range. It only computes and records -- it promotes nothing, admits nothing.

Purpose: the "convergence probe" queued in priorities.md. Push CSS Check A (carry-set
injectivity on G-orbits) to higher prime bounds and flag the first colliding prime if one
ever appears -- a single collision would be a genuine counterexample and is a HUMAN matter.
Optionally re-run the Check B space-certificate for a list of e.

Usage:
    python enumerate.py [--bound 600] [--certify 7,11,13,17,19,23] [--out enumerate_output.txt]

Exit 0 = no collision in range (CSS corroborated); 1 = colliding prime found (surface it).

NOTE on the Ledger-A frontier (R1 / |S|=3 / n=4): that enumeration is a DIFFERENT object
(the reversible-contact signature + W-series witnesses). Its definitions are not present in
this repo (LedgerA/ is empty), so it is deliberately NOT implemented here -- see
.automation/R1-enumeration-BLOCKED.md. Fabricating a signature would violate the framework's
own honesty register.
"""
import argparse, os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sympy import isprime
from verify import injective_on_orbits, KD_certificate  # exact, session-validated math


def probe_injectivity(bound):
    primes = [e for e in range(5, bound + 1) if isprime(e)]
    for e in primes:
        if not injective_on_orbits(e):
            return primes, e
    return primes, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bound", type=int, default=600, help="upper prime bound for Check A")
    ap.add_argument("--certify", type=str, default="7,11,13,17,19,23",
                    help="comma-separated e values for the Check B certificate ('' to skip)")
    ap.add_argument("--out", type=str, default=None, help="filename (in Experiments/) to save output")
    args = ap.parse_args()

    lines = [f"# CSS convergence probe -- {datetime.datetime.now().astimezone().isoformat(timespec='seconds')}"]
    primes, collision = probe_injectivity(args.bound)
    if collision is None:
        lines.append(f"(A) carry-set injectivity on G-orbits, odd primes 5..{args.bound} "
                     f"({len(primes)} primes): holds for ALL (no colliding prime)")
    else:
        lines.append(f"(A) carry-set injectivity on G-orbits, odd primes 5..{args.bound} "
                     f"({len(primes)} primes): *** COLLISION at e={collision} -- CANDIDATE COUNTEREXAMPLE ***")

    certify = [int(x) for x in args.certify.split(",") if x.strip()]
    if certify:
        lines.append("(B) certificate  K_P(e) = D(e)  as spaces:")
        for e in certify:
            contain, dK, dD, ok = KD_certificate(e)
            lines.append(f"    e={e:>3}:  D subset K_P = {contain},  dim K_P={dK:>3}, dim D={dD:>3}"
                         f"   =>  K_P = D certified: {ok}")

    text = "\n".join(lines)
    print(text)
    if args.out:
        outp = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.out)
        with open(outp, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        print(f"\n[saved] {os.path.relpath(outp)}")
    sys.exit(1 if collision is not None else 0)


if __name__ == "__main__":
    main()
