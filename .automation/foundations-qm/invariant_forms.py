#!/usr/bin/env python3
"""Invariant-form census: dim of symmetry-invariant symmetric / antisymmetric
bilinear forms on the traceless state space, per candidate theory.

REGISTER: non-canon, Tier-3, demonstration-grade, pure stdlib.
Claim under test (operational theorem, note section 2):
    canonical +/-J  <=>  (dim invariant symmetric, dim invariant antisymmetric)
                          == (1, 1)   [unique metric AND unique orientation]
Includes the two TRAP rows showing why BOTH uniqueness conditions are needed:
  - doubled real rep  D4+D4 : unique orientation form but 3-dim metrics -> no canonical J
  - rot + fixed axis  Z3+1  : unique orientation form but 2-dim metrics -> no canonical J
"""
import math

TOL = 1e-9

def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]

def transpose(A):
    return [list(r) for r in zip(*A)]

def kernel_dim(rows, ncols):
    M = [r[:] for r in rows]
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(M)) if abs(M[i][c]) > TOL), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and abs(M[i][c]) > TOL:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        r += 1
    return ncols - r

def invariant_form_dims(mats):
    """dim{B sym : g^T B g = B all g}, dim{B antisym : same} on R^n."""
    n = len(mats[0])
    sym_idx = [(i, j) for i in range(n) for j in range(i, n)]         # B[i][j]=B[j][i]
    asym_idx = [(i, j) for i in range(n) for j in range(i + 1, n)]    # B[i][j]=-B[j][i]
    def dims(idx, sign):
        rows = []
        for g in mats:
            gT = transpose(g)
            # (g^T B g - B)_{ab} = 0 ; B parametrized by idx with symmetry `sign`
            for a in range(n):
                for b in range(n):
                    row = [0.0] * len(idx)
                    for k, (i, j) in enumerate(idx):
                        # contribution of B_ij (and its mirrored entry) to (g^T B g)_{ab}
                        row[k] += gT[a][i] * g[j][b]
                        if i != j:
                            row[k] += sign * gT[a][j] * g[i][b]
                        # subtract B_ab itself
                        if (i, j) == (min(a, b), max(a, b)) or (i, j) == (a, b):
                            pass
                    # subtract B_{ab}
                    for k, (i, j) in enumerate(idx):
                        if (i, j) == (a, b):
                            row[k] -= 1.0
                        elif (j, i) == (a, b):
                            row[k] -= sign * 1.0
                    rows.append(row)
        return kernel_dim(rows, len(idx))
    return dims(sym_idx, 1.0), dims(asym_idx, -1.0)

def rot(t):
    return [[math.cos(t), -math.sin(t)], [math.sin(t), math.cos(t)]]

def block_diag(A, B):
    n, m = len(A), len(B)
    Z = [[0.0] * (n + m) for _ in range(n + m)]
    for i in range(n):
        for j in range(n):
            Z[i][j] = A[i][j]
    for i in range(m):
        for j in range(m):
            Z[n + i][n + j] = B[i][j]
    return Z

def Zn(n, k):
    return [rot(2 * math.pi * k * a / n) for a in range(n)]

def Dn(n, k):
    F = [[1.0, 0.0], [0.0, -1.0]]
    out = []
    for a in range(n):
        R = rot(2 * math.pi * k * a / n)
        out.append(R)
        out.append(mat_mul(R, F))
    return out

def Q8_real():
    def realify(M):
        d = len(M)
        R = [[0.0] * (2 * d) for _ in range(2 * d)]
        for i in range(d):
            for j in range(d):
                a, b = M[i][j].real, M[i][j].imag
                R[2*i][2*j], R[2*i][2*j+1], R[2*i+1][2*j], R[2*i+1][2*j+1] = a, -b, b, a
        return R
    i_m = [[1j, 0], [0, -1j]]
    j_m = [[0, 1], [-1, 0]]
    k_m = mat_mul(i_m, j_m)
    I2 = [[1, 0], [0, 1]]
    neg = lambda M: [[-x for x in row] for row in M]
    return [realify(M) for M in [I2, neg(I2), i_m, neg(i_m), j_m, neg(j_m), k_m, neg(k_m)]]

CASES = [
    ("Z3  rot (pinwheel core)", Zn(3, 1)),
    ("Z4  rot",                 Zn(4, 1)),
    ("Z5  rot",                 Zn(5, 1)),
    ("D4  2dim",                Dn(4, 1)),
    ("D5  2dim",                Dn(5, 1)),
    ("Q8  realified",           Q8_real()),
    ("TRAP: D4+D4 doubled",     [block_diag(M, M) for M in Dn(4, 1)]),
    ("TRAP: Z3 + fixed axis",   [block_diag(M, [[1.0]]) for M in Zn(3, 1)]),
    ("Z3+Z3 doubled",           [block_diag(M, M) for M in Zn(3, 1)]),
]

print(f"{'case':<24} {'sym':>4} {'antisym':>8}   verdict")
print("-" * 78)
for name, mats in CASES:
    s, a = invariant_form_dims(mats)
    verdict = "CANONICAL +/-J" if (s, a) == (1, 1) else (
        "no J possible (no orientation form)" if a == 0 else
        "J's exist but NOT canonical")
    print(f"{name:<24} {s:>4} {a:>8}   {verdict}")
print("-" * 78)
print("claim: canonical +/-J  <=>  (sym, antisym) == (1, 1)  [unique metric + unique orientation]")
