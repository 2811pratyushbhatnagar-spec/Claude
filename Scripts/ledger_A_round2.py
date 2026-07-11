# Ledger A — round-2 harness: exhaustive enumeration + R-series independent reproduction
# Register: internal computation. Fixed algebra = minimal transitive groupoid:
#   I={0,1}, C={e0,e1,f,g}, comp: f;g=e0, g;f=e1, identities absorb. inv={(f,g),(g,f)}.
# Effects: E0 on S0, E1 on S1, F: S0->S1, G: S1->S0. Enumerate ALL assignments.

from itertools import product

def compose(R, S):
    return frozenset((a, c) for (a, b) in R for (b2, c) in S if b == b2)

def conv(R):
    return frozenset((b, a) for (a, b) in R)

def diag(X):
    return frozenset((x, x) for x in X)

def rels(A, B):
    pairs = [(a, b) for a in A for b in B]
    for mask in range(1 << len(pairs)):
        yield frozenset(p for i, p in enumerate(pairs) if mask >> i & 1)

def eqs(E0, E1, F, G):
    # the 8 composition equations of the groupoid, as (lhs_composed, rhs_composite) pairs
    return [(compose(E0, E0), E0), (compose(E1, E1), E1),
            (compose(E0, F), F), (compose(F, E1), F),
            (compose(E1, G), G), (compose(G, E0), G),
            (compose(F, G), E0), (compose(G, F), E1)]

def classify(F, G, S0, S1):
    det  = all(len([t for (s, t) in F if s == s0]) <= 1 for s0 in S0) and \
           all(len([t for (s, t) in G if s == s1]) <= 1 for s1 in S1)
    tot  = all(any(s == s0 for (s, t) in F) for s0 in S0) and \
           all(any(s == s1 for (s, t) in G) for s1 in S1)
    inj  = all(len([s for (s, t) in F if t == t1]) <= 1 for t1 in S1) and \
           all(len([s for (s, t) in G if t == t0]) <= 1 for t0 in S0)
    w1   = conv(F) <= G and conv(G) <= F          # return-EXISTENCE (every effect undoable)
    w2   = G <= conv(F) and F <= conv(G)          # return-EXCLUSIVITY (undo only undoes)
    return det, tot, inj, w1, w2

def run(S0, S1, fix_ids=None, id_constraint=None, modes=('eq', 'sup', 'sub')):
    out = {m: [] for m in modes}
    E0s = [diag(S0)] if fix_ids else [E for E in rels(S0, S0)
           if id_constraint != 'sub' or E <= diag(S0)]
    E1s = [diag(S1)] if fix_ids else [E for E in rels(S1, S1)
           if id_constraint != 'sub' or E <= diag(S1)]
    total = 0
    for E0 in E0s:
        for E1 in E1s:
            for F in rels(S0, S1):
                for G in rels(S1, S0):
                    total += 1
                    ee = eqs(E0, E1, F, G)
                    ok = {'eq':  all(l == r for l, r in ee),
                          'sup': all(l <= r for l, r in ee),   # composed <= composite
                          'sub': all(r <= l for l, r in ee)}   # composite <= composed
                    for m in modes:
                        if ok[m]:
                            out[m].append((E0, E1, F, G))
    return total, out

S0 = ('a', 'a2'); S1 = ('b', 'b2')

print('=== |S|=2, identities FREE (full 65,536 space) ===')
total, out = run(S0, S1)
print(f'space = {total}')
for m in ('eq', 'sup', 'sub'):
    survivors = out[m]
    stats = [classify(F, G, S0, S1) for (E0, E1, F, G) in survivors]
    nondet = sum(1 for s in stats if not s[0])
    subdiag = sum(1 for (E0, E1, F, G) in survivors if E0 <= diag(S0) and E1 <= diag(S1))
    print(f'F-{m}: survivors={len(survivors)}  nondeterministic={nondet}  ids-subdiagonal={subdiag}')
# exhibit one nondeterministic F-eq survivor
for (E0, E1, F, G) in out['eq']:
    det, *_ = classify(F, G, S0, S1)
    if not det:
        print('  nondet F-eq witness:', dict(E0=sorted(E0), E1=sorted(E1), F=sorted(F), G=sorted(G)))
        break

print('\n=== |S|=2, A3 STRICT (E=Id): R1 at small scale ===')
total, out = run(S0, S1, fix_ids=True)
for m in ('eq', 'sup', 'sub'):
    survivors = out[m]
    stats = [classify(F, G, S0, S1) for (E0, E1, F, G) in survivors]
    print(f'F-{m}: survivors={len(survivors)} | all det={all(s[0] for s in stats)} '
          f'all total={all(s[1] for s in stats)} all inj={all(s[2] for s in stats)} '
          f'| w1(existence) always={all(s[3] for s in stats)} w2(exclusivity) always={all(s[4] for s in stats)}')
    if not all(s[3] for s in stats):
        print(f'   w1 holds in {sum(1 for s in stats if s[3])}/{len(stats)}')
    if not all(s[4] for s in stats):
        print(f'   w2 holds in {sum(1 for s in stats if s[4])}/{len(stats)}')

print('\n=== |S|=2, PARTIAL-IDENTITY variant (E <= Id): does R1 collapse survive? ===')
total, out = run(S0, S1, id_constraint='sub')
print(f'space = {total}')
survivors = out['eq']
stats = [classify(F, G, S0, S1) for (E0, E1, F, G) in survivors]
pbij = sum(1 for s in stats if s[0] and s[2])   # deterministic + injective = partial bijection
forced = all(E0 == compose(F, G) and E1 == compose(G, F) for (E0, E1, F, G) in survivors)
print(f'F-eq survivors={len(survivors)} | partial bijections={pbij}/{len(survivors)} '
      f'| any nondet={any(not s[0] for s in stats)} | any total-bij={sum(1 for s in stats if s[0] and s[1] and s[2])}')
print(f'identities forced to dom/ran sub-diagonals: {forced}')

print('\n=== |S|=3, A3 STRICT, prune (enumerate F,G only): R1 replication ===')
S0 = ('a', 'a2', 'a3'); S1 = ('b', 'b2', 'b3')
total, out = run(S0, S1, fix_ids=True)
print(f'space = {total}')
for m in ('eq', 'sup', 'sub'):
    survivors = out[m]
    stats = [classify(F, G, S0, S1) for (E0, E1, F, G) in survivors]
    print(f'F-{m}: survivors={len(survivors)} | all det+total+inj='
          f'{all(s[0] and s[1] and s[2] for s in stats)} '
          f'| w1 always={all(s[3] for s in stats)} w2 always={all(s[4] for s in stats)}'
          + (f' | w1 in {sum(1 for s in stats if s[3])}, w2 in {sum(1 for s in stats if s[4])}'
         if survivors else ''))

print('\n=== |S|=3, PARTIAL-IDENTITY variant, prune to E0=dom-diag forced check ===')
# partial-identity at |S|=3: enumerate F,G; identities determined as E0=F;G, E1=G;F, require <= Id
cnt = pb = nd = 0
for F in rels(S0, S1):
    for G in rels(S1, S0):
        E0, E1 = compose(F, G), compose(G, F)
        if not (E0 <= diag(S0) and E1 <= diag(S1)): continue
        if all(l == r for l, r in eqs(E0, E1, F, G)):
            cnt += 1
            det, tot, inj, w1, w2 = classify(F, G, S0, S1)
            if det and inj: pb += 1
            if not det: nd += 1
print(f'F-eq (E=F;G <= Id forced): survivors={cnt} partial-bijections={pb} nondet={nd}')
# expected: number of partial injections 3->3 = sum_k C(3,k)^2 k! = 1+9+18+6 = 34
