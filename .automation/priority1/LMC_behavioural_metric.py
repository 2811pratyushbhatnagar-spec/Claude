"""Priority-1, QUEUE item 1 (E3): labelled Markov chain / probabilistic automaton.
Compute the DGJP behavioural pseudometric d = least fixed point of
    Delta(d)(s,t) = 1 if label(s)!=label(t)  else  c * Kantorovich_d(P_s, P_t),
Kantorovich = optimal-transport distance (LP), then TEST whether d is an ultrametric.

Chain: x,y,z all labelled 'm' step to absorbing sinks A('a'),B('b'):
    x->A(1)   y->A(1/2)+B(1/2)   z->B(1).
Verified result: d(x,y)=d(y,z)=1/2, d(x,z)=1 -> strong triangle FAILS (NOT an
ultrametric), ordinary triangle tight; y is the convex midpoint; the states embed
on the simplex over {A,B} with L1/total-variation distance.

Requires scipy:  pip install scipy --break-system-packages
Reproduce:       python3 LMC_behavioural_metric.py"""
from scipy.optimize import linprog

states = ['x', 'y', 'z', 'A', 'B']
label  = {'x': 'm', 'y': 'm', 'z': 'm', 'A': 'a', 'B': 'b'}
trans  = {'x': {'A': 1.0}, 'y': {'A': 0.5, 'B': 0.5}, 'z': {'B': 1.0},
          'A': {'A': 1.0}, 'B': {'B': 1.0}}
c = 1.0
n = len(states); idx = {s: i for i, s in enumerate(states)}
P = {s: [trans[s].get(t, 0.0) for t in states] for s in states}

def kantorovich(p, q, D):
    cost = [D[i][j] for i in range(n) for j in range(n)]
    A_eq, b_eq = [], []
    for i in range(n):                                  # row sums = p
        A_eq.append([1.0 if a == i else 0.0 for a in range(n) for b in range(n)]); b_eq.append(p[i])
    for j in range(n):                                  # col sums = q
        A_eq.append([1.0 if b == j else 0.0 for a in range(n) for b in range(n)]); b_eq.append(q[j])
    return linprog(cost, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * (n * n), method='highs').fun

D = [[0.0] * n for _ in range(n)]
for _ in range(200):
    new = [[0.0] * n for _ in range(n)]
    for a in states:
        for b in states:
            if a == b: continue
            new[idx[a]][idx[b]] = 1.0 if label[a] != label[b] else c * kantorovich(P[a], P[b], D)
    if max(abs(new[i][j] - D[i][j]) for i in range(n) for j in range(n)) < 1e-12:
        D = new; break
    D = new

d = lambda a, b: D[idx[a]][idx[b]]
xy, yz, xz = d('x', 'y'), d('y', 'z'), d('x', 'z')
if __name__ == "__main__":
    print("behavioural pseudometric on the LMC (c=%.2f):" % c)
    print(f"  d(x,y)={xy:.4f}  d(y,z)={yz:.4f}  d(x,z)={xz:.4f}")
    print(f"  strong triangle (ULTRAMETRIC):  d(x,z) <= max(d(x,y),d(y,z))?  {xz:.3f} <= {max(xy,yz):.3f}  ->  {xz <= max(xy,yz)+1e-9}")
    print(f"  ordinary triangle:              d(x,z) <= d(x,y)+d(y,z)?       {xz:.3f} <= {xy+yz:.3f}  ->  {xz <= xy+yz+1e-9}")
    print(f"  convex/linear: y the MIDPOINT of x,z?  {abs(xy-yz)<1e-9 and abs(xz-(xy+yz))<1e-9}")
    print("  => states embed on the simplex over {A,B}; distance = |p(A)-q(A)| = L1/total-variation.")
