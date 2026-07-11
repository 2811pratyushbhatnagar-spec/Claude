#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_enum_n4.py -- n=4 CONVERGENCE PROBE for Ledger A v0.2 (reversible-contact structures).

SETTING (minimal transitive groupoid):
  Interfaces I0, I1; morphisms e0:I0->I0, e1:I1->I1, c:I0->I1, c':I1->I0 with
  c'.c = e0, c.c' = e1.  Effects are relations on n-state fibers:
  E0 = step(e0), E1 = step(e1), R = step(c), S = step(c').
  Full F-eq system:
    (1) E0;E0 = E0   (2) E1;E1 = E1
    (3) E0;R  = R    (4) R;E1  = R
    (5) E1;S  = S    (6) S;E0  = S
    (7) R;S   = E0   (8) S;R   = E1

(A) STRICT (E0 = E1 = Delta): count all (R,S) with R;S = Delta and S;R = Delta.
    Theorem R1 predicts exactly n! survivors: R the graph of a bijection, S = R^T.
(B) PARTIAL (E0, E1 <= Delta, otherwise free): count all F-eq solutions
    (E0,E1,R,S).  Prediction: sum_k C(n,k)^2 k!  (n=4: 209).  Also verify:
      - E0 forced to exactly Delta_dom(R), E1 to exactly Delta_ran(R);
      - every survivor is a partial bijection with S = R^T;
      - nondeterministic survivors = 0.

METHOD (constraint propagation -- NOT blind 2^32 brute force):
  Relations are tuples of n row-bitmasks.  For each of the 2^(n^2) candidate
  relations R we DERIVE the tiny set of S that could possibly satisfy the
  system, then verify every remaining equation explicitly.

  Soundness of the pruning (these are necessary consequences, so the derived
  candidate set is a superset of all true solutions; the explicit final check
  then does the counting):

  STRICT.  Let pre(b) = { a : (a,b) in R }.
    * Delta <= S;R  gives, for each b, some a in S(b,.) with b in R(a,.),
      i.e. S(b,.) meets pre(b); in particular |pre(b)| >= 1.
    * R;S <= Delta  gives: for a in pre(b), every a' in S(b,.) satisfies
      (a,a') in R;S <= Delta, so a' = a.  Hence S(b,.) = {a} and pre(b) = {a}
      (two distinct preimages a, a'' would force a = a'' the same way).
    * S;R <= Delta  gives R(a,.) <= {b}; with b in R(a,.) this pins
      R(a,.) = {b}.
    So per R there is AT MOST ONE candidate S, and it exists only when every
    column of R is a singleton whose preimage row is the matching singleton.
    We then check R;S = Delta and S;R = Delta explicitly.

  PARTIAL.  Necessary consequences of (5),(7),(8):
    * (7),(8) force E0 = R;S and E1 = S;R (so counting solutions = counting
      (R,S) pairs whose induced E0,E1 are sub-diagonal and pass (1)-(6)).
    * E1 <= Delta and (5) E1;S = S give: S(b,.) nonempty  =>  (b,b) in E1 =
      S;R  =>  exists a in S(b,.) with b in R(a,.).
    * R;S <= Delta then pins S(b,.) = {a} and pre(b) = {a} exactly as above;
      S;R <= Delta pins R(a,.) = {b}.
    So per b:  S(b,.) is empty, OR the unique {a} with pre(b) = {a} and
    R(a,.) = {b}.  At most 2^n candidate S per R (in practice far fewer);
    each candidate is verified against ALL eight equations explicitly.

CROSS-VALIDATION (machinery check against deposited v0.2 counts):
  * FREE n=2: blind enumeration of all 16^4 = 65,536 quadruples (E0,E1,R,S)
    against the eight equations -> deposited 56 survivors, 37 nondeterministic.
  * STRICT n=2 -> 2, n=3 -> 6 = 3!.   PARTIAL n=2 -> 7, n=3 -> 34.

Run:  python audit_enum_n4.py
"""

import itertools
import json
import time
from math import comb, factorial


# ----------------------------------------------------------------------------
# bitmask relation algebra: a relation on n x n is a tuple of n row-bitmasks
# ----------------------------------------------------------------------------

def compose(A, B):
    """Relational composition A;B.  (A;B)(i,.) = union of B(j,.) for j in A(i,.)."""
    out = []
    for row in A:
        r = 0
        m = row
        while m:
            lo = m & -m
            r |= B[lo.bit_length() - 1]
            m ^= lo
        out.append(r)
    return tuple(out)


def columns(R, n):
    """pre[b] = bitmask of a with (a,b) in R (column masks / preimage sets)."""
    pre = [0] * n
    for a in range(n):
        m = R[a]
        while m:
            lo = m & -m
            pre[lo.bit_length() - 1] |= 1 << a
            m ^= lo
    return pre


def transpose(R, n):
    return tuple(columns(R, n))


def diag(n):
    return tuple(1 << i for i in range(n))


def is_subdiag(E, n):
    return all((E[i] & ~(1 << i)) == 0 for i in range(n))


def single_valued(R):
    """Every row has at most one element (deterministic forward step)."""
    return all((row & (row - 1)) == 0 for row in R)


def is_partial_bijection(R, n):
    return single_valued(R) and single_valued(transpose(R, n))


def popcount_rel(R):
    return sum(bin(row).count("1") for row in R)


# ----------------------------------------------------------------------------
# (A) STRICT identities:  R;S = Delta  and  S;R = Delta
# ----------------------------------------------------------------------------

def strict_enumerate(n):
    """Count (R,S) with R;S = Delta, S;R = Delta via candidate derivation.
    Returns (count, survivors, r_space_size)."""
    D = diag(n)
    survivors = []
    r_space = 0
    for R in itertools.product(range(1 << n), repeat=n):
        r_space += 1
        pre = columns(R, n)
        S = [0] * n
        ok = True
        for b in range(n):
            p = pre[b]
            if p == 0 or (p & (p - 1)):          # 0 or >=2 preimages: no S(b,.) possible
                ok = False
                break
            a = p.bit_length() - 1
            if R[a] != (1 << b):                 # S;R <= Delta with b in R(a,.) forces R(a,.)={b}
                ok = False
                break
            S[b] = 1 << a
        if not ok:
            continue
        S = tuple(S)
        # explicit verification of the strict system (no shortcut trusted here)
        if compose(R, S) == D and compose(S, R) == D:
            survivors.append((R, S))
    return len(survivors), survivors, r_space


def strict_verify_R1(survivors, n):
    """Check every strict survivor is a bijection graph with S = R^T."""
    bad = []
    for R, S in survivors:
        if not is_partial_bijection(R, n):
            bad.append((R, S, "not a partial bijection"))
            continue
        if popcount_rel(R) != n:
            bad.append((R, S, "not total/surjective (not a full bijection)"))
            continue
        if S != transpose(R, n):
            bad.append((R, S, "S != R^T"))
    return bad


# ----------------------------------------------------------------------------
# (B) PARTIAL identities:  E0, E1 <= Delta, full eight-equation F-eq system
# ----------------------------------------------------------------------------

def partial_enumerate(n):
    """Count F-eq solutions (E0,E1,R,S) with E0,E1 <= Delta.
    Returns (count, survivors)."""
    survivors = []
    for R in itertools.product(range(1 << n), repeat=n):
        pre = columns(R, n)
        # derived per-row options for S (see module docstring for soundness)
        opts = []
        for b in range(n):
            o = [0]                               # empty row always a candidate
            p = pre[b]
            if p and not (p & (p - 1)):           # exactly one preimage a ...
                a = p.bit_length() - 1
                if R[a] == (1 << b):              # ... and R(a,.) = {b}
                    o.append(1 << a)
            opts.append(o)
        for S in itertools.product(*opts):
            E0 = compose(R, S)                    # forced by eq (7)
            E1 = compose(S, R)                    # forced by eq (8)
            if not is_subdiag(E0, n) or not is_subdiag(E1, n):
                continue
            # explicit check of ALL eight equations
            if compose(E0, E0) != E0 or compose(E1, E1) != E1:
                continue
            if compose(E0, R) != R or compose(R, E1) != R:
                continue
            if compose(E1, S) != S or compose(S, E0) != S:
                continue
            # (7),(8) hold by construction: R;S = E0, S;R = E1
            survivors.append((E0, E1, R, S))
    return len(survivors), survivors


def partial_verify(survivors, n):
    """Verify deposited structural claims on PARTIAL survivors."""
    report = {
        "identities_forced_dom_ran": True,
        "all_partial_bijections_with_S_eq_RT": True,
        "nondet_R": 0,                # R not single-valued
        "nondet_any": 0,              # any of E0,E1,R,S not single-valued
        "by_k": {},                   # survivors by k = |dom(R)|
        "violations": [],
    }
    for E0, E1, R, S in survivors:
        dom = tuple((1 << a) if R[a] else 0 for a in range(n))
        ran_mask = 0
        for row in R:
            ran_mask |= row
        ran = tuple((1 << b) if (ran_mask >> b) & 1 else 0 for b in range(n))
        if E0 != dom or E1 != ran:
            report["identities_forced_dom_ran"] = False
            report["violations"].append(("dom/ran", R, S, E0, E1))
        if not (is_partial_bijection(R, n) and S == transpose(R, n)):
            report["all_partial_bijections_with_S_eq_RT"] = False
            report["violations"].append(("partial-bijection/S=R^T", R, S, E0, E1))
        if not single_valued(R):
            report["nondet_R"] += 1
        if not (single_valued(R) and single_valued(S)
                and single_valued(E0) and single_valued(E1)):
            report["nondet_any"] += 1
        k = sum(1 for row in R if row)
        report["by_k"][k] = report["by_k"].get(k, 0) + 1
    return report


# ----------------------------------------------------------------------------
# cross-validation: blind FREE enumeration at n=2 (65,536 quadruples)
# ----------------------------------------------------------------------------

def free_bruteforce(n):
    """Blind enumeration of ALL (E0,E1,R,S) against the eight F-eq equations.
    Only feasible for n=2 (16^4 = 65,536).  Returns dict of counts."""
    total = strict_hits = partial_hits = 0
    nondet_R = nondet_any = 0
    D = diag(n)
    rng = range(1 << (n * n))

    def unpack(x):
        return tuple((x >> (n * i)) & ((1 << n) - 1) for i in range(n))

    for e0x in rng:
        E0 = unpack(e0x)
        if compose(E0, E0) != E0:
            continue
        for e1x in rng:
            E1 = unpack(e1x)
            if compose(E1, E1) != E1:
                continue
            for rx in rng:
                R = unpack(rx)
                if compose(E0, R) != R or compose(R, E1) != R:
                    continue
                for sx in rng:
                    S = unpack(sx)
                    if compose(E1, S) != S or compose(S, E0) != S:
                        continue
                    if compose(R, S) != E0 or compose(S, R) != E1:
                        continue
                    total += 1
                    if not single_valued(R):
                        nondet_R += 1
                    if not (single_valued(R) and single_valued(S)
                            and single_valued(E0) and single_valued(E1)):
                        nondet_any += 1
                    if E0 == D and E1 == D:
                        strict_hits += 1
                    if is_subdiag(E0, n) and is_subdiag(E1, n):
                        partial_hits += 1
    return {"total": total, "strict": strict_hits, "partial": partial_hits,
            "nondet_R": nondet_R, "nondet_any": nondet_any}


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------

def main():
    t_all = time.perf_counter()
    results = {}

    print("=" * 76)
    print("Ledger A v0.2 -- n=4 convergence probe (audit_enum_n4.py)")
    print("=" * 76)

    # -- cross-validation of the checker machinery: FREE n=2 blind enumeration
    t0 = time.perf_counter()
    free2 = free_bruteforce(2)
    dt = time.perf_counter() - t0
    print("\n[cross-check] FREE n=2 blind enumeration of 65,536 quadruples "
          f"({dt:.2f}s)")
    print(f"  F-eq survivors: {free2['total']}   (deposited: 56)")
    print(f"  nondeterministic (R not single-valued):   {free2['nondet_R']}")
    print(f"  nondeterministic (any effect nondet):     {free2['nondet_any']}"
          "   (deposited: 37)")
    print(f"  restricted to strict ids:  {free2['strict']}   (deposited: 2)")
    print(f"  restricted to partial ids: {free2['partial']}   (deposited: 7)")
    results["free_n2"] = {**free2, "seconds": round(dt, 3)}

    # -- (A) STRICT and (B) PARTIAL for n = 2, 3, 4
    deposited_strict = {2: 2, 3: 6, 4: 24}
    deposited_partial = {2: 7, 3: 34, 4: 209}
    for n in (2, 3, 4):
        pred_s = factorial(n)
        pred_p = sum(comb(n, k) ** 2 * factorial(k) for k in range(n + 1))

        t0 = time.perf_counter()
        cnt_s, surv_s, r_space = strict_enumerate(n)
        dt_s = time.perf_counter() - t0
        bad = strict_verify_R1(surv_s, n)

        t0 = time.perf_counter()
        cnt_p, surv_p = partial_enumerate(n)
        dt_p = time.perf_counter() - t0
        rep = partial_verify(surv_p, n)

        print(f"\n--- n = {n} "
              f"(R-space enumerated: {r_space:,}; naive pair space 2^{2*n*n} = {2**(2*n*n):,}) ---")
        print(f"  (A) STRICT  R;S=Delta & S;R=Delta : {cnt_s}   "
              f"[predicted n! = {pred_s}; deposited {deposited_strict[n]}]   "
              f"wall {dt_s:.3f}s")
        print(f"      R1 structure (bijection graph, S=R^T) violations: {len(bad)}")
        print(f"  (B) PARTIAL F-eq solutions        : {cnt_p}   "
              f"[predicted sum C(n,k)^2 k! = {pred_p}; deposited {deposited_partial[n]}]   "
              f"wall {dt_p:.3f}s")
        print(f"      identities forced to Delta_dom/Delta_ran : "
              f"{rep['identities_forced_dom_ran']}")
        print(f"      all partial bijections with S = R^T      : "
              f"{rep['all_partial_bijections_with_S_eq_RT']}")
        print(f"      nondeterministic survivors (R / any)     : "
              f"{rep['nondet_R']} / {rep['nondet_any']}   [predicted 0]")
        by_k = {k: rep["by_k"].get(k, 0) for k in range(n + 1)}
        pred_by_k = {k: comb(n, k) ** 2 * factorial(k) for k in range(n + 1)}
        print(f"      by k=|dom(R)|: {by_k}   [predicted {pred_by_k}]")

        results[f"n{n}"] = {
            "strict_count": cnt_s, "strict_predicted": pred_s,
            "strict_R1_violations": len(bad), "strict_seconds": round(dt_s, 3),
            "partial_count": cnt_p, "partial_predicted": pred_p,
            "partial_seconds": round(dt_p, 3),
            "identities_forced_dom_ran": rep["identities_forced_dom_ran"],
            "partial_bij_S_eq_RT": rep["all_partial_bijections_with_S_eq_RT"],
            "nondet_R": rep["nondet_R"], "nondet_any": rep["nondet_any"],
            "by_k": by_k, "by_k_predicted": pred_by_k,
        }

    total_dt = time.perf_counter() - t_all
    print(f"\nTotal wall time: {total_dt:.2f}s")
    results["total_seconds"] = round(total_dt, 3)

    ok = (results["n4"]["strict_count"] == 24
          and results["n4"]["partial_count"] == 209
          and results["n4"]["strict_R1_violations"] == 0
          and results["n4"]["nondet_R"] == 0
          and results["n4"]["identities_forced_dom_ran"]
          and results["n4"]["partial_bij_S_eq_RT"]
          and results["n2"]["strict_count"] == 2
          and results["n3"]["strict_count"] == 6
          and results["n2"]["partial_count"] == 7
          and results["n3"]["partial_count"] == 34
          and free2["total"] == 56)
    print("VERDICT:", "ALL CHECKS PASS -- n=4 converges to R1 predictions"
          if ok else "DISCREPANCY DETECTED -- see above")
    print("\nJSON summary:")
    print(json.dumps(results, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
