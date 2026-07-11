"""Priority-1 worked example: the distinguishability form D on a tiny (S,F,O).
Deterministic Moore machine (single update F). Computes:
  - sharp D  : observational-equivalence classes (= minimal realization / Myhill-Nerode)
  - graded D : behavioural pseudometric d(x,y)=2^{-k}, k=first step observations differ (0 if never)
  - the quotient, and which degenerate 'nothing' pole occurs (N1 constant-O / N2 all-distinct / interior).
Reproduce:  python3 D_worked_example.py"""

def obs_classes(S, F, O):
    # partition refinement to observational equivalence (monotone: only splits)
    sig = {}
    for s in S:                       # initialise by observation
        sig.setdefault(O[s], len(sig))
    block = {s: sig[O[s]] for s in S}
    while True:
        newsig, newblock = {}, {}
        for s in S:
            key = (block[s], block[F[s]])   # my block + my successor's block
            newsig.setdefault(key, len(newsig))
            newblock[s] = newsig[key]
        if len(set(newblock.values())) == len(set(block.values())):
            return newblock                 # no new split -> stable
        block = newblock

def graded_metric(S, F, O):
    d = {}
    for x in S:
        for y in S:
            a, b, n, seen, dist = x, y, 0, set(), 0.0
            while (a, b) not in seen:
                if O[a] != O[b]:
                    dist = 2.0 ** (-n); break
                seen.add((a, b)); a, b, n = F[a], F[b], n + 1
            d[(x, y)] = dist
    return d

def pole(classes, S):
    k = len(set(classes.values()))
    if k == 1:      return "N1  (all one class: observation collapses -> D trivial)"
    if k == len(S): return "N2  (all singletons: everything distinguishable, no reduction)"
    return f"INTERIOR ({k} classes of {len(S)} states: proper reduction)"

def run(name, S, F, O):
    cl = obs_classes(S, F, O)
    d  = graded_metric(S, F, O)
    groups = {}
    for s in S: groups.setdefault(cl[s], []).append(s)
    print(f"=== {name} ===")
    print("  observation O :", {s: O[s] for s in S})
    print("  sharp classes :", [sorted(v) for v in groups.values()])
    print("  pole          :", pole(cl, S))
    reps = {c: min(v) for c, v in groups.items()}
    qO = {c: O[reps[c]] for c in groups}
    qF = {c: cl[F[reps[c]]] for c in groups}
    print("  quotient obs  :", {f"C{c}": qO[c] for c in groups})
    print("  quotient F    :", {f"C{c}": f"C{qF[c]}" for c in groups})
    print("  graded d (nonzero, x<y):",
          {f"{x},{y}": d[(x, y)] for x in S for y in S if x < y and d[(x, y)] > 0})
    print()

if __name__ == "__main__":
    S = [0, 1, 2, 3, 4]
    F = {0: 1, 1: 4, 2: 3, 3: 4, 4: 4}
    Omain = {0: 'x', 1: 'x', 2: 'x', 3: 'y', 4: 'y'}
    run("main (S,F,O)", S, F, Omain)
    run("variant N1  (O constant = y)", S, F, {s: 'y' for s in S})
    run("variant N2  (O all distinct)", S, F, {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'})
