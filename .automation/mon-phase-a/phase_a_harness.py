#!/usr/bin/env python3
"""Phase A harness: frozen rejection predicate R1-R5 + determinacy, run
exhaustively over declared finite candidate families for models M1/M2a/M2b/M3.

REGISTER: non-canon, Tier-3 worker computation for the MoN lane (separate
framework from reversible-contact canon). Frozen input: Journal/
mon-two-nothing-kernel-2026-07-11.md sections 7-8, relayed verbatim 2026-07-12.

DECLARED MECHANIZATIONS (choices, stated before results):
- Admissible family Adm = signed permutation unitaries of the computational
  basis, plus the DFT matrix F and F-dagger, plus model-named candidates
  (rank-1 reflections are included as diag sign-flips; M3 adds swap S and
  tensor products A(x)B and S.(A(x)B)). Finite, declared, exhaustive over
  itself. NO silent caps: this is a discretization of U(D), stated as such.
- Predicate A(x): 1 if <x|P_act|x> = 1; 0 if (model has P_inact) <x|P_inact|x> = 1,
  or for M1 if <x|P_act|x> = 0; else UNDEFINED (fails R3's definiteness).
  P_act, P_inact fixed per model BEFORE enumeration (schema below).
- M2a's active designation is a FRAME RAY-SET, not a projector: A(x)=1 iff x
  is a computational-basis ray, 0 iff x is a Fourier-frame ray, else undefined.
  Flagged: this predicate is non-projective (operationally weaker), by design
  of M2a itself.
- R4a: all candidates unitary => pass by construction (recorded, not tested).
- R4b-WEAK (state record): exists diagonal projector T (diagonal => commutes
  with all diagonal P_act; the trace family, fixed pre-enumeration) and
  renewal V in Adm with A(V f W) = 1, <W|T|W> = 0, <VfW|T|VfW> = 1.
- R4b-STRONG (history record): some weak witness successor W+ is UNFORGEABLE:
  no rejection-free g in Adm (g failing R3) reaches W+ from W up to phase.
- R5: exists renewal V in Adm with A(V f W) = 1 (definite).
- ~op: two candidates equivalent iff f(W) = g(W) up to global phase (ray
  equality on the fixed W). Determinacy = number of surviving rays.
All checks exact to 1e-9 on floats.
"""
import math, cmath, itertools

TOL = 1e-9

def mv(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]

def dag_apply(P, v):  # <v|P|v> for projector P
    Pv = mv(P, v)
    return sum((v[i].conjugate() * Pv[i]).real for i in range(len(v)))

def ray_key(v):
    # normalize global phase by first significant component; round to grid
    k = next(i for i, x in enumerate(v) if abs(x) > 1e-6)
    ph = v[k] / abs(v[k])
    w = [x / ph for x in v]
    return tuple((round(x.real, 6), round(x.imag, 6)) for x in w)

def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]

def signed_perms(D, signs="pm"):
    out = []
    sgn = [1, -1] if signs == "pm" else [1]
    for p in itertools.permutations(range(D)):
        for ss in itertools.product(sgn, repeat=D):
            M = [[0.0 + 0j] * D for _ in range(D)]
            for i in range(D):
                M[p[i]][i] = ss[i]
            out.append(M)
    return out

def dft(D):
    w = cmath.exp(2j * math.pi / D)
    return [[w ** (i * j) / math.sqrt(D) for j in range(D)] for i in range(D)]

def diag_proj(D, idxs):
    return [[(1.0 + 0j) if (i == j and i in idxs) else 0j for j in range(D)] for i in range(D)]

def diag_projectors(D):
    for mask in range(1, 2 ** D - 1):
        yield diag_proj(D, {i for i in range(D) if mask >> i & 1})

def run_model(name, dim, family, W, predicate, note=""):
    """predicate(v) -> 1 / 0 / None."""
    rays = {}
    for f in family:
        fw = mv(f, W)
        rays.setdefault(ray_key(fw), fw)
    ray_list = list(rays.values())
    # per-ray conditions
    res = {}
    aW = predicate(W)
    assert aW == 1, f"{name}: A(W) must be 1"
    for key, fw in rays.items():
        r2 = ray_key(fw) != ray_key(W)
        a = predicate(fw)
        r3 = (a == 0)
        res[key] = {"fw": fw, "R2": r2, "R3": r3}
    # renewal reachability: rays reachable from each fw via family, with A=1
    # (dedupe: successor rays from a given ray don't depend on representative)
    succ_cache = {}
    def successors(fw):
        k = ray_key(fw)
        if k not in succ_cache:
            s = {}
            for V in family:
                w2 = mv(V, fw)
                if predicate(w2) == 1:
                    s[ray_key(w2)] = w2
            succ_cache[k] = s
        return succ_cache[k]
    # rejection-free reachable rays from W (for forgery check)
    rejection_free = set()
    for key, d in res.items():
        if not d["R3"]:
            rejection_free.add(key)
    traces = list(diag_projectors(dim))
    for key, d in res.items():
        succ = successors(d["fw"])
        d["R5"] = len(succ) > 0
        weak = []
        for sk, w2 in succ.items():
            for T in traces:
                if dag_apply(T, W) < TOL and abs(dag_apply(T, w2) - 1) < TOL:
                    weak.append((sk, True))
                    break
        d["R4b_weak"] = len(weak) > 0
        d["R4b_strong"] = any(sk not in rejection_free for sk, _ in weak)
    survivors_weak = [k for k, d in res.items() if d["R2"] and d["R3"] and d["R5"] and d["R4b_weak"]]
    survivors_strong = [k for k, d in res.items() if d["R2"] and d["R3"] and d["R5"] and d["R4b_strong"]]
    nR3 = sum(1 for d in res.values() if d["R3"])
    print(f"{name:<26} rays={len(ray_list):>4}  R3-pass={nR3:>3}  "
          f"R1-R5(weak)={len(survivors_weak):>3}  det(weak)={len(survivors_weak):>3}  "
          f"R1-R5(strong)={len(survivors_strong):>3}  {note}")
    return res, survivors_weak, survivors_strong

print("Phase A — R1-R5 + determinacy over declared families (all exact, ray-deduped)")
print("=" * 110)

# ---------- M1: pointed single carrier ----------
for D, act in [(2, {0}), (3, {0, 1}), (4, {0, 1})]:
    P = diag_proj(D, act)
    fam = signed_perms(D) + [dft(D), [list(r) for r in zip(*[[x.conjugate() for x in row] for row in dft(D)])]]
    W = [0j] * D; W[0] = 1.0 + 0j
    def predM1(v, P=P):
        p = dag_apply(P, v)
        return 1 if abs(p - 1) < TOL else (0 if p < TOL else None)
    run_model(f"M1 D={D} |act|={len(act)}", D, fam, W, predM1)

# ---------- M2a: two frames on one carrier ----------
for D in (2, 3):
    F = dft(D)
    comp_rays = {ray_key([1.0 + 0j if i == k else 0j for i in range(D)]) for k in range(D)}
    four_rays = {ray_key(mv(F, [1.0 + 0j if i == k else 0j for i in range(D)])) for k in range(D)}
    fam = signed_perms(D) + [F, [list(r) for r in zip(*[[x.conjugate() for x in row] for row in F])]]
    W = [0j] * D; W[0] = 1.0 + 0j
    def predM2a(v):
        k = ray_key(v)
        if k in comp_rays: return 1
        if k in four_rays: return 0
        return None
    run_model(f"M2a D={D} (frame pred.)", D, fam, W, predM2a,
              note="predicate NON-PROJECTIVE (frame ray-sets)")

# ---------- M2b: orthogonal active/inactive subspaces ----------
for D, act in [(2, {0}), (4, {0, 1})]:
    Pa, Pi = diag_proj(D, act), diag_proj(D, set(range(D)) - act)
    fam = signed_perms(D) + [dft(D)]
    W = [0j] * D; W[0] = 1.0 + 0j
    def predM2b(v, Pa=Pa, Pi=Pi):
        if abs(dag_apply(Pa, v) - 1) < TOL: return 1
        if abs(dag_apply(Pi, v) - 1) < TOL: return 0
        return None
    run_model(f"M2b D={D} A/I={len(act)}/{D-len(act)}", D, fam, W, predM2b)

# ---------- M3: doubled carrier ----------
for D in (2, 3):
    dim = D * D
    small = signed_perms(D, "pm" if D == 2 else "p")  # cap signs at D=3 (declared)
    S = [[0j] * dim for _ in range(dim)]
    for i in range(D):
        for j in range(D):
            S[j * D + i][i * D + j] = 1.0 + 0j
    fam = [kron(A, B) for A in small for B in small]
    fam += [[list(row) for row in ( [ [sum(S[i][k]*M[k][j] for k in range(dim)) for j in range(dim)] for i in range(dim)] )] for M in fam[:len(fam)]]
    fam.append(S)
    # symmetric predicate: P_act = |0><0| (x) |0><0|  (swap-invariant)
    Psym = diag_proj(dim, {0})
    W = [0j] * dim; W[0] = 1.0 + 0j
    def predSym(v, P=Psym):
        p = dag_apply(P, v)
        return 1 if abs(p - 1) < TOL else (0 if p < TOL else None)
    res, sw, ss = run_model(f"M3 D={D} SYMMETRIC pred", dim, fam, W, predSym,
                            note="R3 for swap expected FAIL (A(SW)=1)")
    # orientation predicate: P_act = P(x)Q, P_inact = Q(x)P, disjoint
    if D == 2:
        act_idx, inact_idx = {1}, {2}          # |0>|1> and |1>|0>
        Wo = [0j] * dim; Wo[1] = 1.0 + 0j
    else:
        act_idx = {0 * D + 1, 0 * D + 2}       # |0>(x){|1>,|2>}  rank 2
        inact_idx = {1 * D + 0, 2 * D + 0}     # {|1>,|2>}(x)|0>
        Wo = [0j] * dim; Wo[1] = 1.0 + 0j
    Pa, Pi = diag_proj(dim, act_idx), diag_proj(dim, inact_idx)
    def predOri(v, Pa=Pa, Pi=Pi):
        if abs(dag_apply(Pa, v) - 1) < TOL: return 1
        if abs(dag_apply(Pi, v) - 1) < TOL: return 0
        return None
    run_model(f"M3 D={D} ORIENTATION pred rk{len(act_idx)}", dim, fam, Wo, predOri)

print("=" * 110)
print("Named-candidate spot checks:")
# swap under symmetric predicate at D=2
D, dim = 2, 4
S = [[0j] * 4 for _ in range(4)]
for i in range(2):
    for j in range(2):
        S[j * 2 + i][i * 2 + j] = 1.0 + 0j
W = [1.0 + 0j, 0j, 0j, 0j]
print(f"  swap, symmetric pred:  A(SW) = 1 (unchanged ray) -> R3 FAIL confirmed: {ray_key(mv(S,W)) == ray_key(W)}")
Wo = [0j, 1.0 + 0j, 0j, 0j]
print(f"  swap, orientation pred: S|01> = |10> in inactive -> R3 PASS confirmed: {ray_key(mv(S,Wo)) != ray_key(Wo)}")
