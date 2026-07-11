"""Priority-1, N3b (QUEUE #1): NON-UNIQUENESS of the minimal observation-preserving realization.
E2 showed the minimal quotient can fail to EXIST (family not meet-closed). N3b shows the other
face of pole N3: drop determinism and the minimal realization can fail to be UNIQUE.

Deterministic Moore machines have a UNIQUE minimal realization (Myhill-Nerode). NFAs do NOT:
there are regular languages with several non-isomorphic STATE-MINIMAL NFAs (Kameda-Weiner 1970;
Arnold-Dicky-Nivat 1992). Here we SEARCH for the smallest such witness and CERTIFY it exactly.

Certificates for the reported pair (A, B), both n=3, start=state0, alphabet {0,1}:
  (1) same language: identical canonical MINIMAL DFA signature AND an exact product-BFS equivalence.
  (2) minimality: brute force ALL <=2-state NFAs (every start set) -> none accepts L, so min NFA size = 3.
  (3) non-isomorphic: no bijection fixing the start state maps A onto B (checked over all perms).
=> the minimal realization is NOT unique once F is nondeterministic. Requires only the std lib.
Reproduce: python3 nfa_nonunique_min.py"""
import random, itertools
from collections import deque

SYMS = (0, 1)

def stepmask(delta, S, sym):            # union of transitions from the set-of-states S (bitmask)
    out = 0; b = S; i = 0
    d = delta[sym]
    while b:
        if b & 1: out |= d[i]
        b >>= 1; i += 1
    return out

def reachable(delta, n):                # NFA states reachable from state0 (individual states)
    seen = 1; frontier = 1
    while frontier:
        nf = 0; b = frontier; i = 0
        while b:
            if b & 1:
                for sym in SYMS: nf |= delta[sym][i]
            b >>= 1; i += 1
        new = nf & ~seen; seen |= nf; frontier = new
    return seen

def productive(delta, accept, n):       # states from which some string reaches an accepting state
    prod = accept
    while True:
        add = 0
        for i in range(n):
            if (1 << i) & prod: continue
            if any(delta[sym][i] & prod for sym in SYMS): add |= (1 << i)
        if add & ~prod: prod |= add
        else: return prod

def determinize(delta, accept, start=1):
    trans = {}; order = [start]; idx = {start: 0}; i = 0
    while i < len(order):
        S = order[i]; i += 1; row = []
        for sym in SYMS:
            T = stepmask(delta, S, sym)
            if T not in idx: idx[T] = len(order); order.append(T)
            row.append(idx[T])
        trans[idx[S]] = row
    acc = set(j for S, j in idx.items() if S & accept)
    return trans, 0, acc, len(order)

def min_dfa_sig(delta, accept, start=1):        # canonical minimal-DFA signature = exact language invariant
    trans, s0, acc, ns = determinize(delta, accept, start)
    cls = [1 if s in acc else 0 for s in range(ns)]
    while True:
        keys = {}; newcls = [0] * ns
        for s in range(ns):
            k = (cls[s], cls[trans[s][0]], cls[trans[s][1]])
            if k not in keys: keys[k] = len(keys)
            newcls[s] = keys[k]
        if newcls == cls: break
        cls = newcls
    rep = {}
    for s in range(ns): rep.setdefault(cls[s], s)
    remap = {cls[s0]: 0}; order = [cls[s0]]; dq = deque([cls[s0]])
    while dq:
        c = dq.popleft(); s = rep[c]
        for sym in SYMS:
            tc = cls[trans[s][sym]]
            if tc not in remap: remap[tc] = len(order); order.append(tc); dq.append(tc)
    tr = tuple((remap[cls[trans[rep[c]][0]]], remap[cls[trans[rep[c]][1]]]) for c in order)
    accset = frozenset(remap[cls[s]] for s in range(ns) if s in acc)
    return (len(order), accset, tr)

def canon_nfa(delta, accept, n):        # canonical form, start=state0 fixed -> permute the other n-1 states
    best = None
    for p in itertools.permutations(range(1, n)):
        perm = [0] + list(p)
        nd = []
        for sym in SYMS:
            row = [0] * n
            for i in range(n):
                m = delta[sym][i]; nm = 0; b = m; j = 0
                while b:
                    if b & 1: nm |= (1 << perm[j])
                    b >>= 1; j += 1
                row[perm[i]] = nm
            nd.append(tuple(row))
        na = 0; b = accept; j = 0
        while b:
            if b & 1: na |= (1 << perm[j])
            b >>= 1; j += 1
        cand = (tuple(nd), na)
        if best is None or cand < best: best = cand
    return best

def equiv(A, B):                        # exact product-BFS equivalence of two NFAs (delta,accept,start)
    (dA, accA, sA), (dB, accB, sB) = A, B
    seen = {(sA, sB)}; dq = deque([(sA, sB)])
    while dq:
        SA, SB = dq.popleft()
        if bool(SA & accA) != bool(SB & accB): return False
        for sym in SYMS:
            TA, TB = stepmask(dA, SA, sym), stepmask(dB, SB, sym)
            if (TA, TB) not in seen: seen.add((TA, TB)); dq.append((TA, TB))
    return True

def exists_small_nfa(target_sig, upto=2):    # any NFA with <=upto states (any start set) with language==target?
    for n in range(1, upto + 1):
        masks = range(1 << n)
        for accept in range(1 << n):
            for d0 in itertools.product(masks, repeat=n):
                for d1 in itertools.product(masks, repeat=n):
                    delta = [d0, d1]
                    for start in range(1, 1 << n):
                        if min_dfa_sig(delta, accept, start) == target_sig:
                            return (delta, accept, start)
    return None

def random_nfa(n=3):
    d0 = tuple(random.randrange(1 << n) for _ in range(n))
    d1 = tuple(random.randrange(1 << n) for _ in range(n))
    return [d0, d1], random.randrange(1, 1 << n)

if __name__ == "__main__":
    random.seed(0); n = 3
    buckets = {}; minimal3 = {}; found = None
    for it in range(400000):
        delta, accept = random_nfa(n)
        if reachable(delta, n) != (1 << n) - 1: continue          # trim: all states reachable
        if productive(delta, accept, n) != (1 << n) - 1: continue  # trim: all states productive
        sig = min_dfa_sig(delta, accept); cf = canon_nfa(delta, accept, n)
        b = buckets.setdefault(sig, {})
        if cf in b: continue
        b[cf] = (delta, accept)
        if len(b) >= 2:
            if sig not in minimal3:
                minimal3[sig] = exists_small_nfa(sig, 2) is None   # no <=2-state NFA => min size is 3
            if minimal3[sig]:
                found = (sig, list(b.items())[:2], it); break
    if not found:
        print("no witness in sample"); raise SystemExit
    sig, pair, it = found
    (cfA, (dA, aA)), (cfB, (dB, aB)) = pair
    A = (dA, aA, 1); B = (dB, aB, 1)
    def show(name, d, acc):
        print(f"  {name}: start=q0  accept={{" + ",".join(f'q{i}' for i in range(n) if acc & (1<<i)) + "}")
        for sym in SYMS:
            for i in range(n):
                tgt = [f'q{j}' for j in range(n) if d[sym][i] & (1<<j)]
                if tgt: print(f"      q{i} --{sym}--> {{{','.join(tgt)}}}")
    print(f"WITNESS found after {it} samples.  Language L = canonical minimal DFA {sig}")
    print("\nNFA A"); show("A", dA, aA)
    print("NFA B"); show("B", dB, aB)
    print("\nCERTIFICATES")
    print("  (1) same language  : min-DFA sig equal =", min_dfa_sig(dA,aA)==min_dfa_sig(dB,aB),
          " ; exact product-BFS equiv(A,B) =", equiv(A, B))
    small = exists_small_nfa(sig, 2)
    print("  (2) minimality     : any <=2-state NFA accepts L?", small, " -> min NFA size = 3 (both A,B minimal)")
    print("  (3) non-isomorphic : canon(A)==canon(B)?", cfA == cfB, " (False => non-isomorphic as start-fixed NFAs)")
    print("\nPIN: deterministic minimal realization is UNIQUE (Myhill-Nerode); the NONDETERMINISTIC one is NOT.")
    print("     Two non-isomorphic 3-state minimal NFAs accept the same L => pole N3 in its NON-UNIQUENESS face,")
    print("     the trace-side twin of E2's NON-EXISTENCE. (Bisimulation quotient stays unique; trace-min does not.)")
