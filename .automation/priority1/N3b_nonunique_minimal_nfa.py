#!/usr/bin/env python3
"""
N3b -- non-uniqueness of the MINIMAL trace-equivalent realization under nondeterminism.
[non-canon candidate computation; pure python, no deps, no randomness; exhaustive]

Contrast with E1 (deterministic Moore machine: minimal realization exists and is
UNIQUE up to isomorphism, Myhill-Nerode). Claim verified here: for nondeterministic
systems under TRACE equivalence, minimality no longer pins the object.

Witness language (unary alphabet {a}, finite): L = {a, aa}  (accepted lengths {1,2}).

Verified exhaustively:
 (1) NO 1- or 2-state NFA accepts L, even allowing multiple initial states
     -> minimal realization size = 3.
 (2) Enumerate ALL 3-state NFAs (initial state 0); count those accepting L and
     group into isomorphism classes -> MANY non-isomorphic minimal realizations
     (also counted restricted to trim = every state reachable & co-accessible).
 (3) Two explicit witnesses:
        A = deterministic chain: 0-a->1, 1-a->2, F={1,2}
        B = proper-nondet fork : 0-a->{1,2}, 2-a->{1}, F={1}
     Both accept exactly L; NOT isomorphic (|F| differs; canonical forms differ);
     A is deterministic (a partial DFA), B is properly nondeterministic.
 (4) A and B are trace-equivalent but NOT BISIMILAR (linear vs branching time):
     the finer, branching-time equivalence separates the two minimal objects.
 (5) Determinize + minimize both: the minimal DFAs are ISOMORPHIC (unique) --
     determinism restores the canonical quotient (Myhill-Nerode; cf. E1).

Pole: N3 (uniqueness failure of the best/minimal object), at the sharp/trace rung.
"""
from itertools import product, permutations, combinations

TARGET = frozenset({1, 2})   # accepted word lengths of L = {a, aa}


def powerset(n):
    return [frozenset(c) for r in range(n + 1) for c in combinations(range(n), r)]


def accepted_lengths(n, I, delta, F):
    """Exact accepted-length set of a unary NFA (None if infinite).
    The reachable-subset sequence is eventually periodic; a final subset in the
    cycle => infinitely many accepted lengths."""
    seen, seq, S = {}, [], frozenset(I)
    while S not in seen:
        seen[S] = len(seq)
        seq.append(S)
        S = frozenset(q for s in S for q in delta[s])
    cycle = seq[seen[S]:]
    if any(C & F for C in cycle):
        return None
    return frozenset(k for k, Sk in enumerate(seq) if Sk & F)


def enumerate_accepting(n, initials):
    P = powerset(n)
    found, checked = [], 0
    for I in initials:
        for delta in product(P, repeat=n):
            for F in P:
                checked += 1
                if accepted_lengths(n, I, delta, F) == TARGET:
                    found.append((I, delta, F))
    return found, checked


def canon(nfa, n, perms):
    """Canonical form under the given state-permutations (isomorphism classes)."""
    I, delta, F = nfa
    best = None
    for p in perms:
        I2 = tuple(sorted(p[q] for q in I))
        F2 = tuple(sorted(p[q] for q in F))
        d2 = [None] * n
        for q in range(n):
            d2[p[q]] = tuple(sorted(p[r] for r in delta[q]))
        key = (I2, tuple(d2), F2)
        if best is None or key < best:
            best = key
    return best


def is_trim(n, I, delta, F):
    R, frontier = set(I), set(I)
    while frontier:
        nxt = {q for s in frontier for q in delta[s]} - R
        R |= nxt
        frontier = nxt
    if R != set(range(n)):
        return False
    rev = [set() for _ in range(n)]
    for q in range(n):
        for r in delta[q]:
            rev[r].add(q)
    C, frontier = set(F), set(F)
    while frontier:
        nxt = {q for s in frontier for q in rev[s]} - C
        C |= nxt
        frontier = nxt
    return C == set(range(n))


def bisimilar(nfaX, nfaY, n):
    """Greatest bisimulation on the disjoint union (finality = base observation);
    returns whether the two initial states are bisimilar."""
    IX, dX, FX = nfaX
    IY, dY, FY = nfaY
    N = 2 * n
    delta = [set(dX[q]) for q in range(n)] + [{n + r for r in dY[q]} for q in range(n)]
    final = [q in FX for q in range(n)] + [q in FY for q in range(n)]
    R = {(p, q) for p in range(N) for q in range(N) if final[p] == final[q]}
    changed = True
    while changed:
        changed = False
        R2 = set()
        for (p, q) in R:
            ok = all(any((p2, q2) in R for q2 in delta[q]) for p2 in delta[p]) \
             and all(any((p2, q2) in R for p2 in delta[p]) for q2 in delta[q])
            if ok:
                R2.add((p, q))
            else:
                changed = True
        R = R2
    i0, j0 = next(iter(IX)), n + next(iter(IY))
    return (i0, j0) in R


def min_dfa(nfa, n):
    """Subset-construct (complete, incl. dead state) then Moore-minimize."""
    I, delta, F = nfa
    states, order, trans = {}, [], {}
    def idx(S):
        if S not in states:
            states[S] = len(order)
            order.append(S)
        return states[S]
    from collections import deque
    dq = deque([frozenset(I)])
    q0 = idx(frozenset(I))
    while dq:
        S = dq.popleft()
        T = frozenset(q for s in S for q in delta[s])
        if T not in states:
            idx(T)
            dq.append(T)
        trans[states[S]] = states[T]
    fin = {states[S] for S in order if S & F}
    m = len(order)
    cls = [1 if i in fin else 0 for i in range(m)]
    while True:
        sig = [(cls[i], cls[trans[i]]) for i in range(m)]
        remap, new = {}, []
        for s in sig:
            new.append(remap.setdefault(s, len(remap)))
        if new == cls:
            break
        cls = new
    k = len(set(cls))
    d = {cls[i]: cls[trans[i]] for i in range(m)}
    f = frozenset(cls[i] for i in fin)
    return k, cls[q0], d, f


def dfa_canon(k, q0, d, f):
    """Canonical form of a reachable unary complete DFA: finality flags in visit
    order + index where the rho-shape cycles back."""
    seen, seq, q = {}, [], q0
    while q not in seen:
        seen[q] = len(seq)
        seq.append(q)
        q = d[q]
    return tuple(int(s in f) for s in seq), seen[q]


if __name__ == "__main__":
    fs = frozenset
    print("N3b -- non-uniqueness of minimal trace-equivalent realizations, L = {a, aa}")
    print("=" * 76)

    # (1) minimality: sizes 1 and 2 impossible (even with multiple initial states)
    one, c1 = enumerate_accepting(1, [fs({0})])
    two, c2 = enumerate_accepting(2, [I for I in powerset(2) if I])
    print(f"(1) 1-state NFAs checked: {c1:4d}  accepting L: {len(one)}")
    print(f"    2-state NFAs checked: {c2:4d}  accepting L: {len(two)}  (multi-initial allowed)")
    assert not one and not two
    print("    => minimal realization size = 3")

    # (2) all 3-state realizations (initial state 0) + isomorphism classes
    three, c3 = enumerate_accepting(3, [fs({0})])
    perms_fix0 = [p for p in permutations(range(3)) if p[0] == 0]
    classes = {}
    for nfa in three:
        classes.setdefault(canon(nfa, 3, perms_fix0), []).append(nfa)
    trim = [nfa for nfa in three if is_trim(3, *nfa)]
    trim_classes = {}
    for nfa in trim:
        trim_classes.setdefault(canon(nfa, 3, perms_fix0), []).append(nfa)
    print(f"(2) 3-state NFAs checked: {c3}  accepting exactly L: {len(three)}")
    print(f"    isomorphism classes of minimal realizations: {len(classes)}")
    print(f"    trim (all states reachable & co-accessible): {len(trim)} "
          f"in {len(trim_classes)} isomorphism classes")
    assert len(trim_classes) >= 2

    # (3) explicit witnesses
    A = (fs({0}), (fs({1}), fs({2}), fs()), fs({1, 2}))       # det chain
    B = (fs({0}), (fs({1, 2}), fs(), fs({1})), fs({1}))       # nondet fork
    LA = accepted_lengths(3, *A)
    LB = accepted_lengths(3, *B)
    print(f"(3) A (det chain 0->1->2, F={{1,2}})        accepts lengths {sorted(LA)}")
    print(f"    B (fork 0->{{1,2}}, 2->1, F={{1}})        accepts lengths {sorted(LB)}")
    assert LA == LB == TARGET
    assert canon(A, 3, perms_fix0) != canon(B, 3, perms_fix0)
    detA = all(len(s) <= 1 for s in A[1])
    detB = all(len(s) <= 1 for s in B[1])
    assert is_trim(3, *A) and is_trim(3, *B)
    print(f"    trace-equivalent: YES   isomorphic: NO   A deterministic: {detA}   "
          f"B deterministic: {detB}")

    # (4) trace-equivalent but NOT bisimilar
    assert bisimilar(A, A, 3) and bisimilar(B, B, 3)
    bAB = bisimilar(A, B, 3)
    print(f"(4) A ~bisim~ B : {bAB}   (trace-equal yet branching-time DISTINGUISHES them)")
    assert not bAB

    # (5) determinization restores canonical uniqueness (Myhill-Nerode / E1)
    cA, cB = dfa_canon(*min_dfa(A, 3)), dfa_canon(*min_dfa(B, 3))
    print(f"(5) minimal DFA of A: flags {cA[0]}, cycle back to index {cA[1]}")
    print(f"    minimal DFA of B: flags {cB[0]}, cycle back to index {cB[1]}")
    assert cA == cB
    print("    => minimal DFAs ISOMORPHIC (unique canonical quotient, size "
          f"{len(cA[0])} complete/incl. dead state)")

    print("=" * 76)
    print("VERDICT: nondeterminism + trace equivalence => minimal realization exists")
    print("but is NOT unique (pole N3, uniqueness half); uniqueness is a property of")
    print("the EQUIVALENCE: bisimulation (branching) or determinism (trace=bisim, E1)")
    print("restores the canonical minimal quotient.")
