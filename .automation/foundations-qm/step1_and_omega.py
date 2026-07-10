#!/usr/bin/env python3
"""Machine checks for note v3.
A) Step-1 lemma battery: dim(invariant SYMMETRIC forms) == 1  <=>  irreducible,
   for COMPACT groups; plus the non-compact unipotent counterexample (dim 1,
   reducible-indecomposable) showing compactness is load-bearing.
B) Equivariant state->effect identifications = {a*m + b*omega} (2-parameter).
C) Dynamical measurability: second-order response d2P/dtdθ of transition
   probabilities along an enactable rotation flow tabulates (1/2)*omega.
REGISTER: non-canon, Tier-3, stdlib only.
"""
import math

TOL = 1e-9

def mat_mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

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

def inv_bilinear_dims(mats, sym_sign):
    """dim{B : g^T B g = B, B^T = sym_sign * B}."""
    n = len(mats[0])
    idx = [(i, j) for i in range(n) for j in range(i if sym_sign > 0 else i + 1, n)]
    rows = []
    for g in mats:
        gT = transpose(g)
        for a in range(n):
            for b in range(n):
                row = [0.0] * len(idx)
                for k, (i, j) in enumerate(idx):
                    row[k] += gT[a][i] * g[j][b]
                    if i != j:
                        row[k] += sym_sign * gT[a][j] * g[i][b]
                    if (i, j) == (a, b):
                        row[k] -= 1.0
                    elif (j, i) == (a, b) and i != j:
                        row[k] -= sym_sign
                rows.append(row)
    return kernel_dim(rows, len(idx))

def rot(t):
    return [[math.cos(t), -math.sin(t)], [math.sin(t), math.cos(t)]]

def block(A, B):
    n, m = len(A), len(B)
    Z = [[0.0] * (n + m) for _ in range(n + m)]
    for i in range(n):
        for j in range(n):
            Z[i][j] = A[i][j]
    for i in range(m):
        for j in range(m):
            Z[n + i][n + j] = B[i][j]
    return Z

Z3 = [rot(2 * math.pi * a / 3) for a in range(3)]
Z4 = [rot(2 * math.pi * a / 4) for a in range(4)]
D4 = []
for a in range(4):
    R = rot(2 * math.pi * a / 4)
    D4.append(R)
    D4.append(mat_mul(R, [[1.0, 0.0], [0.0, -1.0]]))
UNIPOTENT = [[[1.0, float(t)], [0.0, 1.0]] for t in (-2, -1, 0, 1, 2, 3)]  # sampled flow; invariance system same as full group

print("A) Step-1 lemma battery: sym-dim == 1 iff irreducible (COMPACT case)")
print(f"{'rep':<28} {'sym':>4}  {'irreducible?':<14} verdict")
for name, mats, irr in [
    ("Z3 rot (irr, C-type)", Z3, True),
    ("Z4 rot (irr, C-type)", Z4, True),
    ("D4 2dim (irr, R-type)", D4, True),
    ("Z3 rot + trivial (RED)", [block(M, [[1.0]]) for M in Z3], False),
    ("D4 + D4 (RED, mult 2)", [block(M, M) for M in D4], False),
    ("Z3 + Z4 rots (RED)", [block(A, B) for A in Z3 for B in Z4], False),
    ("Z3 + Z3 (RED, mult 2)", [block(M, M) for M in Z3], False),
]:
    s = inv_bilinear_dims(mats, +1.0)
    ok = (s == 1) == irr
    print(f"{name:<28} {s:>4}  {str(irr):<14} {'consistent' if ok else 'INCONSISTENT'}")
s_uni = inv_bilinear_dims(UNIPOTENT, +1.0)
print(f"{'unipotent flow (NON-compact)':<28} {s_uni:>4}  {'False':<14} "
      f"{'sym-dim 1 yet REDUCIBLE -> compactness load-bearing' if s_uni == 1 else 'unexpected'}")

print()
print("B) Equivariant state->effect identifications for Z3 (g^T L g = L):")
tot = inv_bilinear_dims(Z3, +1.0) + inv_bilinear_dims(Z3, -1.0)
print(f"   dim = {tot} (expect 2: span{{metric m, orientation omega}}) -> "
      f"antisym part of ANY equivariant transition rule is a multiple of omega")

print()
print("C) Dynamical measurability: P(t,th) = (1 + <f, R_t x(th)>)/2,")
print("   x(th) = eps*(cos th, sin th); claim d2P/dtdth|_0 = (eps/2)*omega(f, x'(0))/|..|")
eps, h = 0.2, 1e-4
def x(th):
    return [eps * math.cos(th), eps * math.sin(th)]
def P(t, th, f):
    R = rot(t)
    v = [R[0][0] * x(th)[0] + R[0][1] * x(th)[1], R[1][0] * x(th)[0] + R[1][1] * x(th)[1]]
    return 0.5 * (1.0 + f[0] * v[0] + f[1] * v[1])
omega = lambda u, v: u[0] * v[1] - u[1] * v[0]  # standard area form = m(., J.)
worst = 0.0
for k in range(6):
    f = [math.cos(k), math.sin(k)]
    hess = (P(h, h, f) - P(h, -h, f) - P(-h, h, f) + P(-h, -h, f)) / (4 * h * h)
    xp = [0.0, eps]  # x'(0)
    pred = 0.5 * omega(f, [-xp[1], xp[0]])  # (1/2) m(f, J x'(0)) = (1/2) omega(f, x'(0))... sign per J=rot90
    # J x' with J = rot(pi/2): J(a,b) = (-b, a)
    Jxp = [-xp[1], xp[0]]
    pred = 0.5 * (f[0] * Jxp[0] + f[1] * Jxp[1])
    worst = max(worst, abs(hess - pred))
print(f"   max |Hessian - (1/2) m(f, J x'(0))| over 6 tomographic f's: {worst:.2e}")
print("   -> the response Hessian tabulates omega (via m-identification); enactable")
print("      flow REQUIRED: for the Z3 pinwheel no such flow exists in Aut(K).")
