#!/usr/bin/env python3
"""Direct (A-S-theorem-free) proof that the rebit V2 admits NO dynamical
correspondence, machine-checked:
  - der(V2) (Jordan derivations) has dimension 1 (= so(2), abelian),
  - but [L_e1, L_e2] != 0,
so condition (i) of a dynamical correspondence, [psi_a, psi_b] = -[L_a, L_b],
is unsatisfiable: LHS lives in an abelian algebra, RHS is nonzero.
REGISTER: non-canon, Tier-3, stdlib only.
"""
TOL = 1e-9
B = [(1.0, (0.0, 0.0)), (0.0, (1.0, 0.0)), (0.0, (0.0, 1.0))]  # 1, e1, e2

def jp(p, q):
    (s, x), (t, y) = p, q
    return (s * t + x[0] * y[0] + x[1] * y[1], (s * y[0] + t * x[0], s * y[1] + t * x[1]))

def tov(p):
    return [p[0], p[1][0], p[1][1]]

def top(v):
    return (v[0], (v[1], v[2]))

def L(a):
    return [[tov(jp(a, b))[i] for b in B] for i in range(3)]

def mm(A, Bm):
    return [[sum(A[i][k] * Bm[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def msub(A, Bm):
    return [[A[i][j] - Bm[i][j] for j in range(3)] for i in range(3)]

# derivations: D with D(x o y) = Dx o y + x o Dy for basis pairs -> linear system in 9 unknowns
rows = []
for x in B:
    for y in B:
        xy = jp(x, y)
        for i in range(3):
            row = [0.0] * 9
            # D(xy)_i = sum_j D[i][j] * tov(xy)[j]
            for j in range(3):
                row[i * 3 + j] += tov(xy)[j]
            # (Dx o y)_i: Dx = sum_j D[.][j] x_j -> jp is bilinear; column contribution
            for j in range(3):
                for k in range(3):
                    ek = [0.0, 0.0, 0.0]; ek[k] = 1.0
                    contrib = tov(jp(top(ek), y))[i]
                    row[k * 3 + j] -= contrib * tov(x)[j]
                    contrib2 = tov(jp(x, top(ek)))[i]
                    row[k * 3 + j] -= contrib2 * tov(y)[j]
            rows.append(row)
M = [r[:] for r in rows]
rk = 0
for c in range(9):
    piv = next((i for i in range(rk, len(M)) if abs(M[i][c]) > TOL), None)
    if piv is None:
        continue
    M[rk], M[piv] = M[piv], M[rk]
    pv = M[rk][c]
    M[rk] = [x / pv for x in M[rk]]
    for i in range(len(M)):
        if i != rk and abs(M[i][c]) > TOL:
            f = M[i][c]
            M[i] = [x - f * y for x, y in zip(M[i], M[rk])]
    rk += 1
dim_der = 9 - rk
print(f"dim der(V2) = {dim_der}  (expect 1: so(2) rotations of the spin part; abelian)")

C = msub(mm(L(B[1]), L(B[2])), mm(L(B[2]), L(B[1])))  # [L_e1, L_e2]
nrm = max(abs(x) for r in C for x in r)
print(f"[L_e1, L_e2] max entry = {nrm}  (expect nonzero: it is the rotation generator)")
print("rows of [L_e1, L_e2]:", C)
assert dim_der == 1 and nrm > 0.5
print()
print("CONCLUSION: any linear psi into der(V2) has [psi_a, psi_b] = 0 (abelian target),")
print("but a dynamical correspondence needs [psi_a, psi_b] = -[L_a, L_b] != 0.")
print("=> V2 admits NO dynamical correspondence. Direct proof; no Alfsen-Shultz theorem used.")
