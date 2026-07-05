#!/usr/bin/env python3
"""
verify.py -- reproducible checks accompanying the Carry-Set Separation note.

Requires: sympy   (pip install sympy)
Run:      python3 verify.py

Two independent, FINITE checks (neither proves the uniform-in-e conjecture):

  (A) Carry-set injectivity on G-orbits for all odd primes up to INJ_BOUND.
      By the note's Section 3 this is equivalent to K(e) = D(e).

  (B) Direct certificate that K_P(e) = D(e) AS SPACES (not merely equal
      dimensions) for small e:
        (i)  D(e) subset of K_P(e):  every orbit-difference generator
             e_i - e_j (i,j in one G-orbit) annihilates the data matrix M
             (columns i, j of M are identical, i.e. N_i(p)=N_j(p) for all
             sampled p).
        (ii) dim K_P(e) = dim D(e)   (exact rational rank of M).
      (i) and (ii) together force K_P(e) = D(e) exactly. Reporting the
      dimension alone would be weaker; the containment (i) is what makes the
      dimension comparison identify the space.
"""

from sympy import isprime, primitive_root, Matrix

# --- group G = < m -> m^{-1},  m -> -1-m >  acting on {1,...,e-2} ------------
def orbits(e):
    I = list(range(1, e - 1)); idx = {m: i for i, m in enumerate(I)}
    inv = lambda m: pow(m, -1, e); tau = lambda m: (-1 - m) % e
    gens = [tuple(idx[inv(m)] for m in I), tuple(idx[tau(m)] for m in I)]
    seen = [False] * len(I); orbs = []
    for s in range(len(I)):
        if seen[s]:
            continue
        comp = [s]; seen[s] = True; st = [s]
        while st:
            x = st.pop()
            for g in gens:
                y = g[x]
                if not seen[y]:
                    seen[y] = True; comp.append(y); st.append(y)
        orbs.append([I[i] for i in comp])
    return orbs

# --- carry set (CM type)  Phi_m = { t in (Z/e)^x : t + (m t mod e) < e } -----
def Phi(e, m):
    return [t for t in range(1, e) if t + (m * t) % e < e]

def canon(e, S):                       # canonical form of a subset under t -> u t
    best = None
    for u in range(1, e):
        mask = 0
        for s in S:
            mask |= 1 << ((u * s) % e)
        if best is None or mask < best:
            best = mask
    return best

def injective_on_orbits(e):            # <=> K(e) = D(e)
    reps = [o[0] for o in orbits(e)]
    forms = [canon(e, Phi(e, m)) for m in reps]
    return len(set(forms)) == len(forms)

# --- direct certificate that K_P(e) = D(e) as spaces ------------------------
def N_vector(e, p):
    g = primitive_root(p); ind = {}; x = 1
    for k in range(p - 1):
        ind[x] = k; x = (x * g) % p
    I = list(range(1, e - 1)); N = [0] * len(I)
    # NB: v ranges 2..p-1, so (1 - v) is a nonzero unit mod the prime p and
    # ind[(1 - v) % p] is always defined. Do NOT extend the range to include
    # v = 1 (that would index ind[0], which is absent).
    for v in range(2, p):
        a = ind[v]; b = ind[(1 - v) % p]
        for i, m in enumerate(I):
            if (a + m * b) % e == 0:
                N[i] += 1
    return N

def primes_cong1(e, count):
    out = []; p = 2
    while len(out) < count:
        p += 1
        if isprime(p) and p % e == 1:
            out.append(p)
    return out

def KD_certificate(e):
    I = list(range(1, e - 1)); idx = {m: i for i, m in enumerate(I)}
    orbs = orbits(e)                          # orbits are lists of VALUES m in I
    rows = [N_vector(e, p) for p in primes_cong1(e, len(I) + 8)]
    M = Matrix(rows)
    # (i) D subset K_P: columns equal within each orbit  (M.(e_i - e_j) = 0).
    # Map orbit VALUES to column POSITIONS via idx before indexing rows.
    contain = all(all(rows[r][idx[o[0]]] == rows[r][idx[j]] for r in range(len(rows)))
                  for o in orbs for j in o[1:])
    # (ii) equal dimensions
    dimK = len(I) - M.rank(); dimD = len(I) - len(orbs)
    return contain, dimK, dimD, (contain and dimK == dimD)

if __name__ == "__main__":
    INJ_BOUND = 250
    primes = [e for e in range(5, INJ_BOUND + 1) if isprime(e)]
    fail = next((e for e in primes if not injective_on_orbits(e)), None)
    print(f"(A) carry-set injectivity on G-orbits, odd primes 5..{INJ_BOUND} "
          f"({len(primes)} primes): "
          f"{'holds for ALL (no colliding prime)' if fail is None else f'FAILS at e={fail}'}")

    print("(B) certificate  K_P(e) = D(e)  as spaces:")
    for e in [7, 11, 13, 17, 19, 23]:
        contain, dK, dD, ok = KD_certificate(e)
        print(f"    e={e:>2}:  D subset K_P = {contain},  dim K_P={dK:>2}, dim D={dD:>2}"
              f"   =>  K_P = D certified: {ok}")
