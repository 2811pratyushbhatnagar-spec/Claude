"""
audit_enum_independent.py -- FROM-SCRATCH independent audit enumerator.

Written directly from the spec of Ledger A v0.2 (reversible-contact
structures); does NOT import or reuse any existing harness.

SETTING
-------
Minimal transitive groupoid: interfaces I0, I1; morphisms
    e0 : I0 -> I0,  e1 : I1 -> I1,  c : I0 -> I1,  c' : I1 -> I0
with c'.c = e0, c.c' = e1 (c, c' mutually inverse).
States: n states per interface.  Each morphism f gets an effect
step(f) subset States(dom) x States(cod), an arbitrary relation.

F-eq (functoriality-as-equality) on this groupoid is exactly the
8-condition system (relational composition ';' read left-to-right,
i.e. step(f);step(g) for composite g.f):

    (1) E0;E0 = E0        (2) E1;E1 = E1
    (3) E0;R  = R         (4) R;E1  = R
    (5) E1;S  = S         (6) S;E0  = S
    (7) R;S   = E0        (8) S;R   = E1

where E0 = step(e0), E1 = step(e1), R = step(c), S = step(c').

Regimes:  STRICT  E0 = E1 = Delta (diagonal)
          PARTIAL E0, E1 subset Delta (sub-diagonals, otherwise free)
          FREE    E0, E1 arbitrary.

RET-exists : Delta subset R;S      RET-! : R;S subset Delta
F-sup (oplax): step(f);step(g) subset step(g.f)  (composed subset composite)
F-sub        : step(g.f) subset step(f);step(g)  (composite subset composed)

ENCODING
--------
A relation on n x n is a bitmask: bit (i*n + j) set  <=>  (i,j) in relation.
Relational composition is precomputed as a full table T[a][b] = a;b.
"""

from math import comb, factorial
import time


# ----------------------------------------------------------------------
# core relational machinery (bitmask relations)
# ----------------------------------------------------------------------

def diag(n):
    d = 0
    for i in range(n):
        d |= 1 << (i * n + i)
    return d


def build_compose_table(n):
    """T[a][b] = relational composition a;b for all relations on [n]x[n]."""
    nb = n * n
    nrel = 1 << nb
    rowmask = (1 << n) - 1
    rows = [tuple((r >> (i * n)) & rowmask for i in range(n))
            for r in range(nrel)]
    # rowor[b][m] = union of rows j of b over all j in the bit-set m
    rowor = []
    for b in range(nrel):
        rb = rows[b]
        t = [0] * (1 << n)
        for m in range(1, 1 << n):
            low = m & (-m)
            t[m] = t[m ^ low] | rb[low.bit_length() - 1]
        rowor.append(t)
    T = [[0] * nrel for _ in range(nrel)]
    for a in range(nrel):
        ra = rows[a]
        Ta = T[a]
        for b in range(nrel):
            rb = rowor[b]
            out = 0
            for i in range(n):
                out |= rb[ra[i]] << (i * n)
            Ta[b] = out
    return T


def transpose(r, n):
    t = 0
    for i in range(n):
        for j in range(n):
            if (r >> (i * n + j)) & 1:
                t |= 1 << (j * n + i)
    return t


def single_valued(r, n):
    rowmask = (1 << n) - 1
    for i in range(n):
        row = (r >> (i * n)) & rowmask
        if row & (row - 1):
            return False
    return True


def total(r, n):
    rowmask = (1 << n) - 1
    return all((r >> (i * n)) & rowmask for i in range(n))


def is_bijection(r, n):
    rt = transpose(r, n)
    return (total(r, n) and single_valued(r, n)
            and total(rt, n) and single_valued(rt, n))


def is_partial_bijection(r, n):
    return single_valued(r, n) and single_valued(transpose(r, n), n)


def dom_diag(r, n):
    """Diagonal relation on the domain of r."""
    rowmask = (1 << n) - 1
    d = 0
    for i in range(n):
        if (r >> (i * n)) & rowmask:
            d |= 1 << (i * n + i)
    return d


def ran_diag(r, n):
    return dom_diag(transpose(r, n), n)


def subset(a, b):
    return (a | b) == b


# ----------------------------------------------------------------------
# the 8-condition systems
# ----------------------------------------------------------------------

def feq(T, e0, e1, r, s):
    """All 8 F-eq equalities."""
    return (T[e0][e0] == e0 and T[e1][e1] == e1 and
            T[e0][r] == r and T[r][e1] == r and
            T[e1][s] == s and T[s][e0] == s and
            T[r][s] == e0 and T[s][r] == e1)


def fsup(T, e0, e1, r, s):
    """All 8 oplax inclusions: composed subset composite."""
    return (subset(T[e0][e0], e0) and subset(T[e1][e1], e1) and
            subset(T[e0][r], r) and subset(T[r][e1], r) and
            subset(T[e1][s], s) and subset(T[s][e0], s) and
            subset(T[r][s], e0) and subset(T[s][r], e1))


def fsub(T, e0, e1, r, s):
    """All 8 lax inclusions: composite subset composed."""
    return (subset(e0, T[e0][e0]) and subset(e1, T[e1][e1]) and
            subset(r, T[e0][r]) and subset(r, T[r][e1]) and
            subset(s, T[e1][s]) and subset(s, T[s][e0]) and
            subset(e0, T[r][s]) and subset(e1, T[s][r]))


# ----------------------------------------------------------------------
# enumerations
# ----------------------------------------------------------------------

def enum_strict(T, n):
    """STRICT: E0 = E1 = Delta fixed; enumerate all (R,S) pairs."""
    D = diag(n)
    nrel = 1 << (n * n)
    return [(D, D, r, s)
            for r in range(nrel) for s in range(nrel)
            if feq(T, D, D, r, s)]


def enum_full(T, n, e0_choices, e1_choices):
    """Brute-force F-eq over explicit E0/E1 choice sets and all R, S."""
    nrel = 1 << (n * n)
    out = []
    for e0 in e0_choices:
        for e1 in e1_choices:
            for r in range(nrel):
                Te0r = T[e0][r]
                if Te0r != r:          # cheap early prune (condition 3)
                    continue
                for s in range(nrel):
                    if feq(T, e0, e1, r, s):
                        out.append((e0, e1, r, s))
    return out


def enum_reduced(T, n, regime):
    """
    Exact reduction: F-eq conditions (7),(8) force E0 = R;S and E1 = S;R.
    Hence enumerating (R,S) and setting E0,E1 to the forced values IS the
    full enumeration over the regime's (E0,E1,R,S) space: each (R,S)
    admits at most one surviving (E0,E1).  (Cross-validated against the
    brute-force enum_full at n=2 below.)
    """
    D = diag(n)
    nrel = 1 << (n * n)
    out = []
    for r in range(nrel):
        Tr = T[r]
        for s in range(nrel):
            e0 = Tr[s]
            e1 = T[s][r]
            if regime == "strict":
                if e0 != D or e1 != D:
                    continue
            elif regime == "partial":
                if not (subset(e0, D) and subset(e1, D)):
                    continue
            # remaining conditions (1)-(6)
            if (T[e0][e0] == e0 and T[e1][e1] == e1 and
                    T[e0][r] == r and T[r][e1] == r and
                    T[e1][s] == s and T[s][e0] == s):
                out.append((e0, e1, r, s))
    return out


def enum_pairs(T, n, checker):
    """Enumerate (R,S) pairs at strict identities under `checker`."""
    D = diag(n)
    nrel = 1 << (n * n)
    return [(r, s)
            for r in range(nrel) for s in range(nrel)
            if checker(T, D, D, r, s)]


# ----------------------------------------------------------------------
# reporting helpers
# ----------------------------------------------------------------------

def rel_str(r, n, names_dom, names_cod):
    pairs = [(i, j) for i in range(n) for j in range(n)
             if (r >> (i * n + j)) & 1]
    return "{" + ", ".join(f"({names_dom[i]},{names_cod[j]})"
                           for i, j in pairs) + "}"


def check_mark(ok):
    return "OK" if ok else "** MISMATCH **"


RESULTS = {}


def record(key, value, deposited=None):
    RESULTS[key] = (value, deposited)
    tag = ""
    if deposited is not None:
        tag = f"   [deposited {deposited}] {check_mark(value == deposited)}"
    print(f"  {key} = {value}{tag}")


# ----------------------------------------------------------------------
# main audit
# ----------------------------------------------------------------------

def main():
    t0 = time.time()
    print("=" * 72)
    print("INDEPENDENT AUDIT ENUMERATION -- F-eq on the minimal transitive")
    print("groupoid (2 interfaces, inverse pair c,c'), Ledger A v0.2 check")
    print("=" * 72)

    # ------------------------------------------------------------------ n=2
    n = 2
    D2 = diag(2)
    T2 = build_compose_table(2)
    nrel2 = 1 << 4
    sub_diag2 = [m for m in range(nrel2) if subset(m, D2)]
    all2 = list(range(nrel2))
    I0 = ["a", "a2"]
    I1 = ["b", "b2"]

    # --- (1) n=2 STRICT ------------------------------------------------
    print("\n(1) n=2 STRICT  (E0=E1=Delta; all 256 (R,S) pairs;")
    print("    equivalently the 65,536 full space restricted to strict ids)")
    strict2 = enum_strict(T2, 2)
    record("n2_strict_survivors", len(strict2), 2)
    all_bij = all(is_bijection(r, 2) and s == transpose(r, 2)
                  for (_, _, r, s) in strict2)
    record("n2_strict_all_bijections_with_S_eq_RT", all_bij, True)
    for (_, _, r, s) in strict2:
        print(f"    survivor: R={rel_str(r,2,I0,I1)}  S={rel_str(s,2,I1,I0)}")

    # --- (2) n=2 PARTIAL -----------------------------------------------
    print("\n(2) n=2 PARTIAL  (E0,E1 subset Delta free; R,S free;")
    print(f"    brute force over {len(sub_diag2)}x{len(sub_diag2)}x16x16 = "
          f"{len(sub_diag2)**2 * 256} quadruples)")
    partial2_full = enum_full(T2, 2, sub_diag2, sub_diag2)
    partial2_red = enum_reduced(T2, 2, "partial")
    record("n2_partial_survivors", len(partial2_full), 7)
    record("n2_partial_formula_sum_C(2,k)^2_k!",
           sum(comb(2, k) ** 2 * factorial(k) for k in range(3)), 7)
    record("n2_partial_reduced_equals_bruteforce",
           sorted(partial2_full) == sorted(partial2_red), True)
    ids_forced = all(e0 == dom_diag(r, 2) and e1 == ran_diag(r, 2)
                     for (e0, e1, r, s) in partial2_full)
    record("n2_partial_ids_forced_to_dom/ran_subdiagonals", ids_forced, True)
    all_pbij = all(is_partial_bijection(r, 2) and s == transpose(r, 2)
                   for (_, _, r, s) in partial2_full)
    record("n2_partial_all_partial_bijections_S_eq_RT", all_pbij, True)
    nondet_p2 = sum(1 for (_, _, r, s) in partial2_full
                    if not (single_valued(r, 2) and single_valued(s, 2)))
    record("n2_partial_nondeterministic", nondet_p2, 0)

    # --- (3) n=2 FREE ---------------------------------------------------
    print("\n(3) n=2 FREE  (all 16^4 = 65,536 quadruples brute force)")
    free2_full = enum_full(T2, 2, all2, all2)
    free2_red = enum_reduced(T2, 2, "free")
    record("n2_free_survivors", len(free2_full), 56)
    record("n2_free_reduced_equals_bruteforce",
           sorted(free2_full) == sorted(free2_red), True)
    # nondeterminism, three candidate definitions
    nd_R = sum(1 for (_, _, r, _) in free2_full if not single_valued(r, 2))
    nd_RS = sum(1 for (_, _, r, s) in free2_full
                if not (single_valued(r, 2) and single_valued(s, 2)))
    nd_any = sum(1 for (e0, e1, r, s) in free2_full
                 if not all(single_valued(x, 2) for x in (e0, e1, r, s)))
    record("n2_free_nondet_R_not_single_valued", nd_R)
    record("n2_free_nondet_R_or_S_not_single_valued", nd_RS, 37)
    record("n2_free_nondet_any_of_E0_E1_R_S", nd_any)
    # deposited witness: E0={(a,a)}, E1={(b,b),(b,b2)}, R={(a,b),(a,b2)},
    # S={(b,a)}; encoding bit (i*n+j):
    wE0, wE1, wR, wS = 0b0001, 0b0011, 0b0011, 0b0001
    w_ok = feq(T2, wE0, wE1, wR, wS)
    w_in = (wE0, wE1, wR, wS) in free2_full
    record("n2_free_witness_satisfies_Feq", w_ok, True)
    record("n2_free_witness_in_survivor_list", w_in, True)
    record("n2_free_witness_is_nondeterministic",
           not single_valued(wR, 2), True)

    # ------------------------------------------------------------------ n=3
    n = 3
    D3 = diag(3)
    print("\nbuilding n=3 composition table (512 x 512) ...")
    T3 = build_compose_table(3)
    nrel3 = 1 << 9
    sub_diag3 = [m for m in range(nrel3) if subset(m, D3)]

    # --- (4a) n=3 STRICT -------------------------------------------------
    print("\n(4a) n=3 STRICT  (E0=E1=Delta; all 512x512 = 262,144 pairs)")
    strict3 = enum_strict(T3, 3)
    record("n3_strict_survivors", len(strict3), 6)
    record("n3_strict_equals_3_factorial", len(strict3) == factorial(3), True)
    all_bij3 = all(is_bijection(r, 3) and s == transpose(r, 3)
                   for (_, _, r, s) in strict3)
    record("n3_strict_all_bijections_with_S_eq_RT", all_bij3, True)

    # --- (4b) n=3 PARTIAL -----------------------------------------------
    print("\n(4b) n=3 PARTIAL  (E0,E1 subset Delta, R,S free;")
    print("     exact reduced enumeration over 262,144 (R,S) pairs --")
    print("     conditions (7),(8) force E0=R;S, E1=S;R, so each (R,S)")
    print("     admits at most one (E0,E1); reduction cross-validated")
    print("     against brute force at n=2 above)")
    partial3 = enum_reduced(T3, 3, "partial")
    record("n3_partial_survivors", len(partial3), 34)
    record("n3_partial_formula_sum_C(3,k)^2_k!",
           sum(comb(3, k) ** 2 * factorial(k) for k in range(4)), 34)
    ids_forced3 = all(e0 == dom_diag(r, 3) and e1 == ran_diag(r, 3)
                      for (e0, e1, r, s) in partial3)
    record("n3_partial_ids_forced_to_dom/ran_subdiagonals", ids_forced3, True)
    all_pbij3 = all(is_partial_bijection(r, 3) and s == transpose(r, 3)
                    for (_, _, r, s) in partial3)
    record("n3_partial_all_partial_bijections_S_eq_RT", all_pbij3, True)
    nondet_p3 = sum(1 for (_, _, r, s) in partial3
                    if not (single_valued(r, 3) and single_valued(s, 3)))
    record("n3_partial_nondeterministic", nondet_p3, 0)

    # --- (5) R2: F-sup / F-sub at strict identities ----------------------
    print("\n(5) R2: F-sup (oplax) at strict identities")
    for nn, T, dep_pairs, dep_ret1, dep_rete in ((2, T2, 49, 49, 2),
                                                 (3, T3, 1650, 1650, 6)):
        D = diag(nn)
        sup_pairs = enum_pairs(T, nn, fsup)
        ret_bang = sum(1 for (r, s) in sup_pairs if subset(T[r][s], D))
        ret_ex = sum(1 for (r, s) in sup_pairs if subset(D, T[r][s]))
        record(f"n{nn}_fsup_pairs", len(sup_pairs), dep_pairs)
        record(f"n{nn}_fsup_RETbang", ret_bang, dep_ret1)
        record(f"n{nn}_fsup_RETexists", ret_ex, dep_rete)
        print(f"    n={nn}: RET-! {ret_bang}/{len(sup_pairs)}, "
              f"RET-exists {ret_ex}/{len(sup_pairs)}")

    print("\n(5') R2 dual: F-sub at strict identities")
    for nn, T, dep_pairs, dep_rete, dep_ret1 in ((2, T2, 31, 31, 2),
                                                 (3, T3, 25057, 25057, 6)):
        D = diag(nn)
        sub_pairs = enum_pairs(T, nn, fsub)
        ret_ex = sum(1 for (r, s) in sub_pairs if subset(D, T[r][s]))
        ret_bang = sum(1 for (r, s) in sub_pairs if subset(T[r][s], D))
        record(f"n{nn}_fsub_pairs", len(sub_pairs), dep_pairs)
        record(f"n{nn}_fsub_RETexists", ret_ex, dep_rete)
        record(f"n{nn}_fsub_RETbang", ret_bang, dep_ret1)
        print(f"    n={nn}: RET-exists {ret_ex}/{len(sub_pairs)}, "
              f"RET-! {ret_bang}/{len(sub_pairs)}")

    # --- summary ----------------------------------------------------------
    print("\n" + "=" * 72)
    mismatches = [k for k, (v, d) in RESULTS.items()
                  if d is not None and v != d]
    if mismatches:
        print("MISMATCHES vs deposited v0.2 counts:")
        for k in mismatches:
            v, d = RESULTS[k]
            print(f"  {k}: got {v}, deposited {d}")
    else:
        print("ALL CHECKED VALUES MATCH THE DEPOSITED v0.2 COUNTS.")
    print(f"total runtime: {time.time() - t0:.1f} s")
    print("=" * 72)
    return 0 if not mismatches else 1


if __name__ == "__main__":
    raise SystemExit(main())
