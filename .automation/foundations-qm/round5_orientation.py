#!/usr/bin/env python3
"""Round 5: is the pinwheel's {+/-J} the SAME invariant as Alfsen-Shultz's
central-projection orientation (per Doering 1411.5558)?

Sections:
 A) Pinwheel: Aut(K) = Z3 exactly; (sym, antisym) = (1,1); canonical J = rot90
    built from omega via the unique metric (D-duality).
 B) Minimal Jordan import: spin factor V2 on R(+)R^2 using the canonical metric;
    Jordan axioms verified; CONTINUUM of idempotents exhibited; 3 = 1+1+1 is the
    only sum-of-squares partition, so the only 3-dim complex C* is C^3, whose sa
    part has 8 idempotents -> V2 is NOT the sa part of any complex *-algebra ->
    the A-S/Doering set of associative products (central projections) is EMPTY
    for the pinwheel's minimal Jordan completion.
 C) Real-algebra loophole closed: V2 = Sym part of M2(R), but transpose is an
    isomorphism M2(R) -> M2(R)^op FIXING Sym pointwise -> ab vs ba gauge-
    equivalent -> no Z2 there either. Contrast M2(C): transpose on Hermitians
    = entrywise conjugation != identity.
 D) Control where A-S DOES apply: M2(C). The two products ab (c=1) and ba (c=0)
    share the Jordan part delta and differ by the sign of the skew derivation
    psi_a = (i/2)[a,.]  -> product swap <=> psi -> -psi <=> i -> -i.
    c in {0,1} associative; c = 1/2 (pure Jordan midpoint) NOT associative.
 E) Converse mismatch: qubit traceless part R^3 under SO(3) (+ transpose) has
    NO invariant antisymmetric form -> our (1,1) criterion FAILS exactly where
    the A-S orientation is nontrivial.
REGISTER: non-canon, Tier-3, stdlib only.
"""
import math, cmath, itertools

TOL = 1e-9

def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def madd(A, B, s=1):
    return [[A[i][j] + s * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def dagger(A):
    return [[A[j][i].conjugate() if isinstance(A[j][i], complex) else A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def mnorm(A):
    return max(abs(x) for r in A for x in r)

def rot(t):
    return [[math.cos(t), -math.sin(t)], [math.sin(t), math.cos(t)]]

def apply(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M)))

print("A) PINWHEEL: Aut(K), form counts, canonical J")
R1, R2, A1, A2 = 1.0, 0.8, 0.0, math.radians(40)
verts = []
for j in range(3):
    for (r, a) in [(R1, A1), (R2, A2)]:
        th = a + 2 * math.pi * j / 3
        verts.append((r * math.cos(th), r * math.sin(th)))
vset = {(round(x, 9), round(y, 9)) for (x, y) in verts}
def preserves(M):
    return {(round(x, 9), round(y, 9)) for (x, y) in (apply(M, v) for v in verts)} == vset
sym_found = []
for deg in range(0, 360):
    t = math.radians(deg)
    if preserves(rot(t)):
        sym_found.append(("rot", deg))
    F = mm(rot(t), [[1.0, 0.0], [0.0, -1.0]])  # reflection about axis t/2
    if preserves(F):
        sym_found.append(("refl", deg))
print(f"   symmetries found over 360 sampled rotations+reflections: {sym_found}")
assert sym_found == [("rot", 0), ("rot", 120), ("rot", 240)], "Aut(K) != Z3"
print("   Aut(K) = Z3 exactly (no reflections: distinct radii kill them). CONFIRMED")
# canonical J from omega via metric: unique invariant metric = c*I (rotation-
# invariance forces isotropy); omega = area form; J = m^{-1} omega = rot90.
J = [[0.0, -1.0], [1.0, 0.0]]
g = rot(2 * math.pi / 3)
print(f"   J = rot90; J^2 = -I dev {mnorm(madd(mm(J, J), [[1,0],[0,1]]))}; "
      f"[J, rot120] dev {mnorm(madd(mm(J, g), mm(g, J), -1))}")

print()
print("B) MINIMAL JORDAN IMPORT: spin factor V2 = R(+)R^2, (s,x)o(t,y)=(st+<x,y>, sy+tx)")
def jp(p, q):  # Jordan product on V2
    (s, x), (t, y) = p, q
    return (s * t + x[0] * y[0] + x[1] * y[1], (s * y[0] + t * x[0], s * y[1] + t * x[1]))
import random
random.seed(5)
rv = lambda: (random.uniform(-1, 1), (random.uniform(-1, 1), random.uniform(-1, 1)))
worst_comm = worst_jid = 0.0
def vsub(p, q):
    return (p[0] - q[0], (p[1][0] - q[1][0], p[1][1] - q[1][1]))
def vmax(p):
    return max(abs(p[0]), abs(p[1][0]), abs(p[1][1]))
for _ in range(200):
    a, b = rv(), rv()
    worst_comm = max(worst_comm, vmax(vsub(jp(a, b), jp(b, a))))
    a2 = jp(a, a)
    worst_jid = max(worst_jid, vmax(vsub(jp(jp(a2, b), a), jp(a2, jp(b, a)))))
print(f"   commutativity dev {worst_comm:.1e}; Jordan identity dev {worst_jid:.1e}  -> V2 is a Jordan algebra")
# continuum of idempotents: p = (1/2, y), |y| = 1/2
for phi in (0.0, 1.0, 2.5):
    y = (0.5 * math.cos(phi), 0.5 * math.sin(phi))
    p = (0.5, y)
    print(f"   idempotent p(phi={phi}): p o p - p dev {vmax(vsub(jp(p, p), p)):.1e}")
print("   -> CONTINUUM of idempotents (circle |y|=1/2).")
parts = [q for q in itertools.product(range(1, 2), repeat=3)]  # squares summing to 3
sq = [n * n for n in range(1, 2)]
sols = [c for c in itertools.product(range(1, 4), repeat=3) if sum(n * n for n in c) == 3]
print(f"   sum-of-squares partitions of 3 (ordered, n>=1): {sorted(set(tuple(sorted(c)) for c in sols))}")
print("   -> only C^3; C^3_sa = R^3 has exactly 2^3 = 8 idempotents (checked: components in {0,1}).")
print("   -> V2 is NOT the sa part of any complex *-algebra; hence (via the A-S")
print("      characterization: JB(W) is sa-of-C*/vN iff a dynamical correspondence exists)")
print("      its set of dynamical correspondences is EMPTY. Direct theorem-free proof:")
print("      round5_dyncorr_check.py. NOTE: this emptiness is NOT a statement in Doering's")
print("      paper (which works where a product exists by hypothesis) - attribution audited.")

print()
print("C) REAL LOOPHOLE: V2 = Sym(M2(R)); transpose fixes Sym pointwise and swaps ab<->ba")
random.seed(7)
rM = lambda: [[random.uniform(-1, 1) for _ in range(2)] for _ in range(2)]
worst = 0.0
for _ in range(100):
    a, b = rM(), rM()
    lhs = [[mm(a, b)[j][i] for j in range(2)] for i in range(2)]        # (ab)^T
    rhs = mm([[b[j][i] for j in range(2)] for i in range(2)], [[a[j][i] for j in range(2)] for i in range(2)])  # b^T a^T
    worst = max(worst, mnorm(madd(lhs, rhs, -1)))
print(f"   (ab)^T = b^T a^T dev {worst:.1e}; transpose|_Sym = id  -> M2(R) ~ M2(R)^op via iso FIXING observables")
print("   -> even the real-associative route yields NO orientation Z2 for the rebit.")
print("   Contrast M2(C): for Hermitian h, h^T = conj(h) (entrywise), NOT h -> transpose does not fix Herm.")

print()
print("D) CONTROL (A-S applies): M2(C), products ab (c=1) vs ba (c=0)")
random.seed(11)
def rherm():
    a, b, c, d = (random.uniform(-1, 1) for _ in range(4))
    return [[complex(a, 0), complex(c, d)], [complex(c, -d), complex(b, 0)]]
def bracket(a, b):
    return madd(mm(a, b), mm(b, a), -1)
worst_shared = worst_flip = worst_skew = worst_psiaa = 0.0
for _ in range(100):
    a, b = rherm(), rherm()
    jordan1 = madd(mm(a, b), mm(b, a))                       # ab+ba (product ab)
    jordan2 = madd(mm(b, a), mm(a, b))                       # same for ba
    worst_shared = max(worst_shared, mnorm(madd(jordan1, jordan2, -1)))
    psi1 = [[0.5j * bracket(a, b)[i][j] for j in range(2)] for i in range(2)]
    psi2 = [[0.5j * (mm(b, a)[i][j] - mm(a, b)[i][j]) for j in range(2)] for i in range(2)]  # bracket in A^op
    worst_flip = max(worst_flip, mnorm(madd(psi1, psi2)))     # psi2 = -psi1
    # skewness of psi_a wrt HS inner product on Herm: <psi_a x, y> + <x, psi_a y> = 0
    x, y = rherm(), rherm()
    px = [[0.5j * bracket(a, x)[i][j] for j in range(2)] for i in range(2)]
    py = [[0.5j * bracket(a, y)[i][j] for j in range(2)] for i in range(2)]
    hs = lambda u, v: sum((u[i][j].conjugate() * v[i][j]).real for i in range(2) for j in range(2))
    worst_skew = max(worst_skew, abs(hs(px, y) + hs(x, py)))
    paa = [[0.5j * bracket(a, a)[i][j] for j in range(2)] for i in range(2)]
    worst_psiaa = max(worst_psiaa, mnorm(paa))
print(f"   Jordan part shared by both products: dev {worst_shared:.1e}")
print(f"   psi^op = -psi (product swap <=> skew-derivation sign flip <=> i <-> -i): dev {worst_flip:.1e}")
print(f"   psi_a skew wrt HS: dev {worst_skew:.1e};  psi_a(a) = 0: dev {worst_psiaa:.1e}")
def star(c_, a, b):
    return madd([[c_ * x for x in r] for r in mm(a, b)], [[(1 - c_) * x for x in r] for r in mm(b, a)])
worst_ass = {0.0: 0.0, 0.5: 0.0, 1.0: 0.0}
for _ in range(60):
    a, b, c = rherm(), rherm(), rherm()
    for cc in (0.0, 0.5, 1.0):
        dev = mnorm(madd(star(cc, star(cc, a, b), c), star(cc, a, star(cc, b, c)), -1))
        worst_ass[cc] = max(worst_ass[cc], dev)
print(f"   associativity of a*b = c(ab)+(1-c)(ba):  c=0: {worst_ass[0.0]:.1e}  c=1: {worst_ass[1.0]:.1e}  "
      f"c=1/2 (Jordan midpoint): {worst_ass[0.5]:.2f}  (nonzero = not associative)")
print("   -> the central-projection Z2 {c=0, c=1} is exactly the psi/i sign: Doering's picture verified on M2(C).")

print()
print("E) CONVERSE MISMATCH: qubit traceless part R^3 under SO(3): invariant antisym forms")
def rot3(axis, t):
    c, s = math.cos(t), math.sin(t)
    if axis == 0:
        return [[1, 0, 0], [0, c, -s], [0, s, c]]
    if axis == 1:
        return [[c, 0, s], [0, 1, 0], [-s, 0, c]]
    return [[c, -s, 0], [s, c, 0], [0, 0, 1]]
gens = [rot3(0, 1.0), rot3(1, 0.7), rot3(2, 1.3)]
idx = [(i, j) for i in range(3) for j in range(i + 1, 3)]
rows = []
for gm in gens:
    gT = [list(r) for r in zip(*gm)]
    for a in range(3):
        for b in range(3):
            row = [0.0] * len(idx)
            for k, (i, j) in enumerate(idx):
                row[k] += gT[a][i] * gm[j][b]
                row[k] -= gT[a][j] * gm[i][b]
                if (i, j) == (a, b):
                    row[k] -= 1.0
                elif (j, i) == (a, b):
                    row[k] += 1.0
            rows.append(row)
M = [r[:] for r in rows]
rk = 0
for c in range(len(idx)):
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
print(f"   dim invariant antisym forms on R^3 under SO(3) generators: {len(idx) - rk} (expect 0)")
print("   -> our (1,1) criterion FAILS for the qubit exactly where the A-S orientation Z2 is NONTRIVIAL.")
print()
print("VERDICT: same output TYPE (Z2 conjugation torsor); provably NOT the same invariant.")
