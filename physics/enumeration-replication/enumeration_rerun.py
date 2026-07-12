#!/usr/bin/env python3
"""
Enumeration rerun -- 2026-07-03.
Historical target: April 2026 session "Axiom formulation audit and recovery".
Recorded fingerprint: 6561 tables (nu.nu = E pinned) -> 17 (associativity)
-> 2 (first-generated activity) -> 1 (active regeneration)
-> unique survivor a.b = a+b+1 mod 3, labels nu=0, E=1, I=2.
Stage 1: verbatim conditions (pure verification).
Stages 2-3: candidate formalizations tested against the recorded fingerprint.

Transcribed verbatim from the 2026-07-03 session artifact for independent
replication in a third environment (remote container), 2026-07-09.
"""
from itertools import product

NU, E, I = 0, 1, 2
CELLS = [(i, j) for i in range(3) for j in range(3) if (i, j) != (0, 0)]
SHIFTED = tuple(tuple((a + b + 1) % 3 for b in range(3)) for a in range(3))


def all_tables():
    for vals in product(range(3), repeat=8):
        T = [[None] * 3 for _ in range(3)]
        T[0][0] = 1  # pinned: nu.nu = E  (convention E := nu.nu; axiom nu.nu != nu)
        for (i, j), v in zip(CELLS, vals):
            T[i][j] = v
        yield tuple(tuple(r) for r in T)


def assoc(T, n=3):
    R = range(n)
    return all(T[T[a][b]][c] == T[a][T[b][c]] for a in R for b in R for c in R)


def closure(T, seed):
    S = set(seed)
    grew = True
    while grew:
        grew = False
        for a in list(S):
            for b in list(S):
                c = T[a][b]
                if c not in S:
                    S.add(c)
                    grew = True
    return S


# --- candidate formalizations (reconstruction band) ---
FGA = {
    "EE_ne_E    [E.E != E]":                    lambda T, n=3: T[E][E] != E,
    "left_act   [all x: E.x != x]":             lambda T, n=3: all(T[E][x] != x for x in range(n)),
    "right_act  [all x: x.E != x]":             lambda T, n=3: all(T[x][E] != x for x in range(n)),
    "two_sided  [all x: E.x!=x and x.E!=x]":    lambda T, n=3: all(T[E][x] != x and T[x][E] != x for x in range(n)),
}
AR = {
    "EE_eq_nu   [E.E = nu]":                    lambda T: T[E][E] == NU,
    "nu_in_img  [some a.b = nu]":               lambda T: any(T[a][b] == NU for a in range(3) for b in range(3)),
    "rows_nu    [all x, some y: x.y = nu]":     lambda T: all(any(T[x][y] == NU for y in range(3)) for x in range(3)),
    "gen_nuE    [nu, E each generate Omega]":   lambda T: closure(T, {NU}) == {0, 1, 2} and closure(T, {E}) == {0, 1, 2},
    "verbatim   [non-idempotent x generate]":   lambda T: all(closure(T, {x}) == {0, 1, 2} for x in range(3) if T[x][x] != x),
    "lit_apr28  [a,b in {nu,E}: a.b != I]":     lambda T: all(T[a][b] != I for a in (NU, E) for b in (NU, E)),
}


def main():
    tables = list(all_tables())
    print(f"tables with nu.nu = E pinned          : {len(tables)}   (recorded: 6561)")
    A = [T for T in tables if assoc(T)]
    print(f"stage 1  associativity survivors      : {len(A)}   (recorded: 17)")
    print()
    print("-- single-filter action on the associative survivors --")
    for name, f in FGA.items():
        print(f"  FGA {name:42s} -> {len([T for T in A if f(T)])}")
    for name, r in AR.items():
        print(f"  AR  {name:42s} -> {len([T for T in A if r(T)])}")
    print()
    print("-- full fingerprint scan --")
    print("   need: |FGA(A)| = 2, |AR(FGA(A))| = 1, survivor = shifted table,")
    print("         redundancy |AR(A)| = 1 (record: FGA redundant given AR at n=3)")
    hits = []
    for fn, f in FGA.items():
        S2 = [T for T in A if f(T)]
        for rn, r in AR.items():
            S3 = [T for T in S2 if r(T)]
            red = [T for T in A if r(T)]
            if len(S2) == 2 and len(S3) == 1 and S3[0] == SHIFTED and len(red) == 1:
                hits.append((fn, rn, S2))
    if not hits:
        print("   NO candidate pair reproduces the full recorded fingerprint.")
    seen_rival = None
    for fn, rn, S2 in hits:
        rival = [T for T in S2 if T != SHIFTED][0]
        seen_rival = rival
        print(f"   MATCH  FGA = {fn.split()[0]}  ;  AR = {rn.split()[0]}")
    if seen_rival:
        print("   the rival table eliminated by AR (the 'second survivor'):")
        for row in seen_rival:
            print(f"      {row}")
    print()
    T = SHIFTED
    ident = [e for e in range(3) if all(T[e][x] == x and T[x][e] == x for x in range(3))]
    sg = {0: 1, 1: 0, 2: 2}
    autom = all(sg[T[a][b]] == T[sg[a]][sg[b]] for a in range(3) for b in range(3))
    latin = all(sorted(T[a]) == [0, 1, 2] for a in range(3)) and \
            all(sorted(T[a][b] for a in range(3)) == [0, 1, 2] for b in range(3))
    print("-- forced properties of the unique survivor (none used as filters) --")
    print(f"  two-sided identity                  : {ident}   (recorded: I = 2)")
    print(f"  sigma = (nu<->E, I fixed) is autom. : {autom}")
    print(f"  Latin square (+assoc+id => group)   : {latin}")
    print(f"  E.E = nu                            : {T[E][E] == NU}")
    print(f"  nu.E = E.nu = I                     : {T[NU][E] == I and T[E][NU] == I}")
    print()
    print("-- |Omega| = 2 exclusion (carrier {nu, E}, nu.nu = E pinned) --")
    twos = []
    for vals in product(range(2), repeat=3):
        T2 = [[1, None], [None, None]]
        for (i, j), v in zip([(0, 1), (1, 0), (1, 1)], vals):
            T2[i][j] = v
        T2 = tuple(tuple(r) for r in T2)
        if assoc(T2, 2):
            twos.append(T2)
    print(f"  associative 2-element tables        : {len(twos)}")
    for name, f in FGA.items():
        k = len([T for T in twos if f(T, 2)])
        print(f"  after FGA {name:40s}: {k}   (recorded: 0)")


if __name__ == "__main__":
    main()
