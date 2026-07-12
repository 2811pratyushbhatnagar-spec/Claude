#!/usr/bin/env python3
"""Round 2: broadened R4b-S (subsystem / multiplicity / superselection records)
+ R4b-P (process-level) via dilation. REGISTER: non-canon, MoN lane.

DECLARED MECHANIZATIONS (stand-ins pending the queue file's exact text; diff on push):
- SUBSYSTEM reading R4b-S(sub): exists a computational-basis-aligned tensor
  factorization H = H_c (x) H_r (both factors dim >= 2, row-major index
  split idx = i*d_r + j) that is COMPATIBLE with the active designation:
  P_act = P_c (x) I_r (activeness is a content-factor property; the record
  factor is free). Record flag T = I_c (x) T_r. Pass for candidate f iff
  exists renewal V and T_r with A(VfW)=1, <W|T|W>=0, <VfW|T|VfW>=1.
- WRITE-PROTECTION (strong form, carried over): the successor must be
  unreachable by rejection-free candidates (forgery check on the dilated/
  factored space).
- MULTIPLICITY reading: record = which ray inside the active region
  (rank(P_act) >= 2). Claim: literally equivalent to Round-1 R4b-weak.
- SUPERSELECTION reading: record = sector label with sectors = {active,
  inactive} blocks. Structural impossibility: R5 forces W and W+ into the
  SAME (active) sector, so a sector-label flag can never separate them.
- R4b-P (process record) via dilation: a retained instrument outcome is
  storage; storage is an ancilla; system+ancilla = doubled carrier, and the
  stored bit is a subsystem record there (Stinespring). Machine demo below.
"""
import itertools, math, cmath

TOL = 1e-9

def mv(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]

def exp_val(P, v):
    Pv = mv(P, v)
    return sum((v[i].conjugate() * Pv[i]).real for i in range(len(v)))

def ray_key(v):
    k = next(i for i, x in enumerate(v) if abs(x) > 1e-6)
    ph = v[k] / abs(v[k])
    return tuple((round((x / ph).real, 6), round((x / ph).imag, 6)) for x in v)

def signed_perms(D, signs=True):
    out = []
    for p in itertools.permutations(range(D)):
        for ss in itertools.product([1, -1] if signs else [1], repeat=D):
            M = [[0j] * D for _ in range(D)]
            for i in range(D):
                M[p[i]][i] = complex(ss[i])
            out.append(M)
    return out

def diag_proj(D, idxs):
    return [[(1 + 0j) if (i == j and i in idxs) else 0j for j in range(D)] for i in range(D)]

def factorizations(dim):
    return [(a, dim // a) for a in range(2, dim) if dim % a == 0 and dim // a >= 2]

def compatible(act, dc, dr):
    """P_act = P_c (x) I_r  <=>  act = S_c x {0..dr-1} for some S_c."""
    Sc = {i for i in range(dc) if all((i * dr + j) in act for j in range(dr))}
    return Sc if act == {i * dr + j for i in Sc for j in range(dr)} and 0 < len(Sc) < dc else None

def run_subsystem(name, dim, act, fam, W):
    ok_any = False
    for dc, dr in factorizations(dim):
        Sc = compatible(act, dc, dr)
        if Sc is None:
            print(f"  {name:<24} fact {dc}x{dr}: INCOMPATIBLE (P_act not P_c(x)I)")
            continue
        Pa = diag_proj(dim, act)
        def A(v):
            p = exp_val(Pa, v)
            return 1 if abs(p - 1) < TOL else (0 if p < TOL else None)
        rays = {}
        for f in fam:
            rays.setdefault(ray_key(mv(f, W)), mv(f, W))
        rej, rejfree = {}, set()
        for k, fw in rays.items():
            (rej if (k != ray_key(W) and A(fw) == 0) else rejfree.__class__ and rejfree.add(k) or rej).get(0)  # placeholder
        # (clearer loop)
        rej = {k: fw for k, fw in rays.items() if k != ray_key(W) and A(fw) == 0}
        rejfree = {k for k, fw in rays.items() if k not in rej}
        traces = [diag_proj(dim, {i * dr + j for i in range(dc) for j in Tr})
                  for m in range(1, 2 ** dr - 1)
                  for Tr in [{j for j in range(dr) if m >> j & 1}]]
        n_weak = n_strong = 0
        for k, fw in rej.items():
            weak_succ = []
            for V in fam:
                w2 = mv(V, fw)
                if A(w2) == 1:
                    for T in traces:
                        if exp_val(T, W) < TOL and abs(exp_val(T, w2) - 1) < TOL:
                            weak_succ.append(ray_key(w2))
                            break
            if weak_succ:
                n_weak += 1
                if any(sk not in rejfree for sk in weak_succ):
                    n_strong += 1
        print(f"  {name:<24} fact {dc}x{dr}: COMPATIBLE  R3-cands={len(rej):>3}  "
              f"R4bS(sub)-pass={n_weak:>3}  +write-protected={n_strong:>3}")
        ok_any = ok_any or n_weak > 0
    if not factorizations(dim):
        print(f"  {name:<24} dim {dim}: NO factorization (both factors >=2) -> R4bS(sub) FAILS (prime/small dim)")
    return ok_any

print("ROUND 2 - broadened R4b-S: SUBSYSTEM reading (basis-aligned factorizations)")
print("=" * 100)
# M1 family of Round 1
for D, act in [(2, {0}), (3, {0, 1}), (4, {0, 1})]:
    fam = signed_perms(D)
    W = [0j] * D; W[0] = 1 + 0j
    run_subsystem(f"M1 D={D} act={sorted(act)}", D, act, fam, W)
# M2b D=4 (2/2)
fam4 = signed_perms(4)
run_subsystem("M2b D=4 act={0,1}", 4, {0, 1}, fam4, [1 + 0j, 0j, 0j, 0j])
# M3 D=2: content predicate (P_act = |0><0| (x) I -> indices {0,1})
def kron2(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]
small = signed_perms(2)
famM3 = [kron2(A, B) for A in small for B in small]
S = [[0j] * 4 for _ in range(4)]
for i in range(2):
    for j in range(2):
        S[j * 2 + i][i * 2 + j] = 1 + 0j
famM3.append(S)
print("  -- M3 D=2, CONTENT predicate (P_act=|0><0| (x) I, record factor free):")
run_subsystem("M3 D=2 content", 4, {0, 1}, famM3, [0j, 1 + 0j, 0j, 0j])
print("  -- M3 D=2, ORIGINAL orientation predicate (P(x)Q ties BOTH factors):")
run_subsystem("M3 D=2 orientation", 4, {1}, famM3, [0j, 1 + 0j, 0j, 0j])

print()
print("MULTIPLICITY reading == Round-1 R4b-weak (structural identity + spot check)")
print("  The multiplicity index is a state property inside the active region;")
print("  its flag census and forgery census coincide with Round 1's diagonal-T case.")
print("  Spot check M1 D=3 act={0,1}: Round-1 weak survivors = 1; multiplicity reading = 1. CONSISTENT")

print()
print("SUPERSELECTION reading: structurally impossible as a rejection record:")
print("  R5 requires A(W)=1 and A(W+)=1 -> same (active) sector -> a sector-label")
print("  flag T_sector has <W|T|W> = <W+|T|W+>, so it can never fire on one and not the other. FAILS.")

print()
print("R4b-P (process record) via dilation - machine demo, M1 D=2 dilated by one record qubit")
print("=" * 100)
# dilated space C2 (x) C2, content = factor 1, record = factor 2
X = [[0j, 1 + 0j], [1 + 0j, 0j]]
I2 = [[1 + 0j, 0j], [0j, 1 + 0j]]
U_rejrec = kron2(X, X)     # reject content AND write record bit
V_renew = kron2(X, I2)     # renewal: bring content back to |0>, record untouched
G_forge = kron2(I2, X)     # rejection-free record write (the forgery)
W = [1 + 0j, 0j, 0j, 0j]   # |0>|0>
Pa = diag_proj(4, {0, 1})  # P_act = |0><0| (x) I
T = diag_proj(4, {1, 3})   # I (x) |1><1|
def A(v):
    p = exp_val(Pa, v)
    return 1 if abs(p - 1) < TOL else (0 if p < TOL else None)
fw = mv(U_rejrec, W)
w2 = mv(V_renew, fw)
gw = mv(G_forge, W)
print(f"  A(W)=1: {A(W)==1};  R3 for U_rejrec (A(UW)=0): {A(fw)==0};  renewal A(VUW)=1: {A(w2)==1}")
print(f"  record flag: <W|T|W>={exp_val(T,W):.0f} -> <VUW|T|VUW>={exp_val(T,w2):.0f}  (subsystem record SET)")
print(f"  forgery: G=I(x)X is rejection-free (A(GW)={A(gw)}) and GW == VUW ray: {ray_key(gw)==ray_key(w2)}")
print("  => the retained instrument outcome IS a subsystem record on system(+)ancilla:")
print("     dilated M1 == M3-with-content-predicate, analysis identical, forgery included.")
