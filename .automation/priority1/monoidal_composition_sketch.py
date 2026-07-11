"""Priority-5.5 (ChatGPT's recommended next STRUCTURE): the symmetric monoidal composition law on
observable systems. First bounded question: what does the DEFAULT (Cartesian) composition do?

Autonomous observable system  M = (S, F: S->S, O: S->Obs).  Observation stream  obs_M(s) = (O(s),O(Fs),O(F^2 s),...).
Cartesian composition  M1 (x) M2 = (S1 x S2,  F1 x F2,  (s1,s2)|->(O1 s1, O2 s2)).

Tested here (small machines, exact):
  (1) observations FACTOR:  obs_{M1(x)M2}(s1,s2) = pair( obs_{M1}(s1), obs_{M2}(s2) )  -> joint observables are exactly
      pairs of local ones  =>  LOCAL TOMOGRAPHY holds trivially.
  (2) minimal realization COMMUTES with (x):  the observational-equivalence quotient of M1(x)M2 equals
      quotient(M1) x quotient(M2);  #classes(M1(x)M2) = #classes(M1) * #classes(M2)  (so N_AB = N_A N_B).
Conclusion: the DEFAULT tensor puts observable systems in the CLASSICAL / locally-tomographic corner. So the quantum
reconstruction content is NOT in 'having a tensor' but in CHOOSING a NON-Cartesian one (where joint observables exceed
local pairs) -- exactly where Hardy/CDP place their composite-system axiom. Uses only the std lib.
Reproduce: python3 monoidal_composition_sketch.py"""
from itertools import product

def stream(F, O, s, depth):
    out = []; x = s
    for _ in range(depth):
        out.append(O[x]); x = F[x]
    return tuple(out)

def obs_classes(S, F, O, depth=None):
    """Observational-equivalence classes (states with identical infinite observation stream).
    For a finite machine, streams are eventually periodic; depth = |S|+1 suffices to separate."""
    d = (len(S) + 2) if depth is None else depth
    sig = {s: stream(F, O, s, d) for s in S}
    reps = {}; cls = {}
    for s in S:
        reps.setdefault(sig[s], len(reps)); cls[s] = reps[sig[s]]
    return cls, len(reps)

def cartesian(M1, M2):
    (S1, F1, O1), (S2, F2, O2) = M1, M2
    S = list(product(S1, S2))
    F = {(a, b): (F1[a], F2[b]) for (a, b) in S}
    O = {(a, b): (O1[a], O2[b]) for (a, b) in S}
    return S, F, O

if __name__ == "__main__":
    # M1: {0,1,2}, 0 and 1 observationally equivalent (x then y^inf); 2 = y^inf.  min = 2 classes.
    M1 = (['0', '1', '2'], {'0': '2', '1': '2', '2': '2'}, {'0': 'x', '1': 'x', '2': 'y'})
    # M2: {p,q}, distinct (0,1^inf vs 1^inf).  already minimal = 2 classes.
    M2 = (['p', 'q'], {'p': 'q', 'q': 'q'}, {'p': '0', 'q': '1'})

    c1, n1 = obs_classes(*M1); c2, n2 = obs_classes(*M2)
    S12, F12, O12 = cartesian(M1, M2); c12, n12 = obs_classes(S12, F12, O12)
    print(f"#classes  M1={n1}  M2={n2}  M1(x)M2={n12}   N_AB == N_A*N_B ? {n12} == {n1*n2} -> {n12 == n1 * n2}")

    # (1) observations factor
    depth = 6
    fact = all(
        stream(F12, O12, (a, b), depth) == tuple(zip(stream(*M1[1:], a, depth), stream(*M2[1:], b, depth)))
        for (a, b) in S12)
    print("observations FACTOR  obs(A(x)B)=pair(obs A,obs B) ?", fact, " -> joint observables = local pairs (local tomography)")

    # (2) minimization commutes with (x): class of (a,b) determined by (class1 a, class2 b), bijectively
    joint_from_local = {}
    ok = True
    for (a, b) in S12:
        key = (c1[a], c2[b])
        if key in joint_from_local:
            ok &= (joint_from_local[key] == c12[(a, b)])
        else:
            joint_from_local[key] = c12[(a, b)]
    injective = len(set(joint_from_local.values())) == len(joint_from_local)
    print("minimization COMMUTES with (x)  class(a,b)=(class a,class b) ?", ok and injective,
          f"  (distinct joint classes {len(set(joint_from_local.values()))} == {n1}*{n2})")

    print("\nPIN: the DEFAULT (Cartesian) tensor on observable systems is the CLASSICAL / locally-tomographic corner —")
    print("     observations factor into local pairs and minimal realization commutes with (x) (N_AB=N_A N_B).")
    print("     So quantum reconstruction is NOT 'having a tensor' but CHOOSING a NON-Cartesian one (joint observables")
    print("     beyond local pairs) — precisely Hardy Axiom 4 / CDP local distinguishability as a CHOICE, not a freebie.")
