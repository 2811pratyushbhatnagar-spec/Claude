#!/usr/bin/env python3
"""Frobenius-Schur indicator table + commutant/complex-structure census.

REGISTER: non-canon, Tier-3, demonstration-grade. Pure stdlib (no numpy).
For each small group G and explicit irrep rho:
  nu(rho) = (1/|G|) * sum_g chi(g^2)        (complex character chi)
  commutant dim_R of the REALIFIED representation  (solve XM=MX, Gaussian elim)
  census of complex structures J in the commutant (J^2 = -I):
    dim 1 (R)  -> none;  dim 2 (C) -> exactly {+J,-J};  dim 4 (H) -> 2-sphere.
Known math throughout (Schur, Frobenius-Schur); the computation is the deposit.
"""
import cmath, math

# ---------- tiny linear algebra (floats, tolerance) ----------
TOL = 1e-9

def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

def realify(M):
    """Complex d x d -> real 2d x 2d, a+bi -> [[a,-b],[b,a]] blocks."""
    d = len(M)
    R = [[0.0] * (2 * d) for _ in range(2 * d)]
    for i in range(d):
        for j in range(d):
            a, b = M[i][j].real, M[i][j].imag
            R[2 * i][2 * j], R[2 * i][2 * j + 1] = a, -b
            R[2 * i + 1][2 * j], R[2 * i + 1][2 * j + 1] = b, a
    return R

def kernel_basis(rows, ncols):
    """Basis of the kernel of the linear system rows . x = 0 (Gaussian elim)."""
    M = [r[:] for r in rows]
    pivots, r = [], 0
    for c in range(ncols):
        piv = None
        for i in range(r, len(M)):
            if abs(M[i][c]) > TOL:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and abs(M[i][c]) > TOL:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        pivots.append(c)
        r += 1
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fc in free:
        v = [0.0] * ncols
        v[fc] = 1.0
        for ri, pc in enumerate(pivots):
            v[pc] = -M[ri][fc]
        basis.append(v)
    return basis

def commutant_basis(mats):
    """Real basis of {X : X M = M X for all M in mats}; X is n x n."""
    n = len(mats[0])
    rows = []
    for M in mats:
        for i in range(n):
            for j in range(n):
                row = [0.0] * (n * n)  # (XM - MX)_{ij} = 0
                for k in range(n):
                    row[i * n + k] += M[k][j]
                    row[k * n + j] -= M[i][k]
                rows.append(row)
    return [[v[i * n + j] for j in range(n)] if False else v for v in kernel_basis(rows, n * n)]

def unflatten(v, n):
    return [[v[i * n + j] for j in range(n)] for i in range(n)]

def j_census(comm_vs, n):
    """Classify solutions of J^2=-I inside span(comm_vs)."""
    d = len(comm_vs)
    if d == 1:
        return "none (commutant = R; a^2 = -1 unsolvable)"
    if d == 2:
        B = [unflatten(v, n) for v in comm_vs]
        # K := traceless direction; check K^2 = lambda*I with lambda<0, rescale.
        for C in B:
            t = trace(C) / n
            K = [[C[i][j] - (t if i == j else 0.0) for j in range(n)] for i in range(n)]
            nrm = max(abs(K[i][j]) for i in range(n) for j in range(n))
            if nrm < TOL:
                continue
            K2 = mat_mul(K, K)
            lam = trace(K2) / n
            off = max(abs(K2[i][j] - (lam if i == j else 0.0)) for i in range(n) for j in range(n))
            if off < 1e-7 and lam < 0:
                return "exactly {+J, -J}  (canonical pair)"
        return "dim 2 but no J found (unexpected)"
    if d == 4:
        return "2-sphere of J's (quaternionic; no canonical choice)"
    return f"commutant dim {d}: J-set infinite (no canonical pair)"

# ---------- groups: abstract elements + explicit complex irreps ----------
def Zn_case(n, k):
    els = list(range(n))
    w = lambda a: cmath.exp(2j * math.pi * k * a / n)
    chi = lambda a: w(a)                       # 1-dim complex irrep
    nu = sum(chi((2 * a) % n) for a in els).real / n
    rot = lambda a: [[math.cos(2 * math.pi * k * a / n), -math.sin(2 * math.pi * k * a / n)],
                     [math.sin(2 * math.pi * k * a / n), math.cos(2 * math.pi * k * a / n)]]
    real_mats = [rot(a) for a in els]          # real form (realified irrep)
    return nu, real_mats

def Dn_case(n, k):
    els = [(a, e) for a in range(n) for e in (0, 1)]
    def sq(g):
        a, e = g
        return ((2 * a) % n, 0) if e == 0 else (0, 0)
    def chi(g):
        a, e = g
        return 2 * math.cos(2 * math.pi * k * a / n) if e == 0 else 0.0
    nu = sum(chi(sq(g)) for g in els) / len(els)
    def rho(g):
        a, e = g
        c, s = math.cos(2 * math.pi * k * a / n), math.sin(2 * math.pi * k * a / n)
        R = [[c, -s], [s, c]]
        return R if e == 0 else mat_mul(R, [[1.0, 0.0], [0.0, -1.0]])
    return nu, [rho(g) for g in els]

def Q8_case():
    I2 = [[1, 0], [0, 1]]
    i_m = [[1j, 0], [0, -1j]]
    j_m = [[0, 1], [-1, 0]]
    k_m = mat_mul(i_m, j_m)
    neg = lambda M: [[-x for x in row] for row in M]
    els = [I2, neg(I2), i_m, neg(i_m), j_m, neg(j_m), k_m, neg(k_m)]
    nu = sum(trace(mat_mul(M, M)).real for M in els) / 8.0
    return nu, [realify(M) for M in els]

def type_of(nu):
    return {1: ("R", "real"), 0: ("C", "complex"), -1: ("H", "quaternionic")}[round(nu)]

CASES = [
    ("Z3,  k=1", *Zn_case(3, 1)),
    ("Z4,  k=1", *Zn_case(4, 1)),
    ("Z5,  k=1", *Zn_case(5, 1)),
    ("Z5,  k=2", *Zn_case(5, 2)),
    ("D4, 2dim", *Dn_case(4, 1)),
    ("D5, 2dim", *Dn_case(5, 1)),
    ("Q8, 2dim", *Q8_case()),
]

print(f"{'group/irrep':<11} {'nu':>4}  {'type':<13} {'commutant':<14} J-structures in commutant")
print("-" * 95)
for name, nu, real_mats in CASES:
    basis = commutant_basis(real_mats)
    d = len(basis)
    sym, tname = type_of(nu)
    alg = {1: "R (dim 1)", 2: "C (dim 2)", 4: "H (dim 4)"}.get(d, f"dim {d}")
    print(f"{name:<11} {nu:>+4.1f}  {sym} {tname:<11} {alg:<14} {j_census(basis, len(real_mats[0]))}")
print("-" * 95)
print("Trichotomy: R -> no J;  C -> canonical +/-J;  H -> continuum of J's, none canonical.")
