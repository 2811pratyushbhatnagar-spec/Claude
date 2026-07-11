"""Priority-1, E5 (part 2 of the continuous-observation variant): the GRAMIAN reading.
Companion to continuous_observation_metric.py (weighted-L1, identity read-out, trivial kernel).
This half adds what that one lacks: a NONTRIVIAL minimal observation-preserving quotient,
and a D that is a genuine POSITIVE REAL BILINEAR FORM (the 'positive-form' ladder rung).

Setup (discrete-time LTI, partial read-out):
  x_{t+1} = A x_t,  y_t = C x_t,   A = diag(0.8, 0.5, 0.9, 0.3),  C = [1 1 0 0],  state R^4.
  L2 graded distinguishability:
     D(x,x')^2 = sum_{t>=0} |y_t(x) - y_t(x')|^2 = (x-x')^T W (x-x'),
  W = sum_t (A^T)^t C^T C A^t  = the observability Gramian
    = unique fixed point of  W = A^T W A + C^T C   (discrete Lyapunov).
  Diagonal A gives the exact closed form  W_ij = C_i C_j / (1 - lam_i lam_j).

Claims verified below:
  (1) rank(observability matrix O) = 2  =>  minimal observation-preserving quotient
      R^4 / ker(W) ~= R^2  (4 -> 2);  ker W = span{e3, e4} = unobservable subspace (Kalman).
  (2) W(observable block) = [[25/9, 5/3], [5/3, 4/3]] EXACTLY; Lyapunov residual ~ 0;
      truncated-trajectory sum (T=600) agrees to ~1e-12.
  (3) D is a PSEUDOmetric: D(e3,0) = D(e4,0) = 0 with e3,e4 != 0 (collapsed by the quotient);
      strictly positive definite ON the quotient (eigs of the 2x2 block > 0).
  (4) genuinely CONTINUOUS grades: D(a*e1, 0) = (5/3)*a  -> a continuum, not E1's {0,1/2,1}.
  (5) NOT an ultrametric: D(e1,-e1) = 10/3 > max(D(e1,0), D(0,-e1)) = 5/3.
  (6) PARALLELOGRAM LAW HOLDS (contrast: the weighted-L1 half FAILS it) => D comes from a
      real inner product on the quotient -- the positive-(bi)linear-form rung is REACHED.
      Exact: |e1+e2|_W^2 + |e1-e2|_W^2 = 67/9 + 7/9 = 74/9 = 2*(25/9) + 2*(4/3).
  What is STILL missing to quantum: complex sesquilinearity + a NON-SIMPLEX convex state
  body (E4) -- that step is the Hardy/CDP reconstruction frontier, not a toy computation.

Requires numpy (scipy optional cross-check).  Reproduce: python3 continuous_graded_D_gramian.py
"""
import numpy as np

F = np.array  # brevity
A = np.diag([0.8, 0.5, 0.9, 0.3])
C = F([[1.0, 1.0, 0.0, 0.0]])
n = 4
lam = np.diag(A)

# ---- (1) observability matrix, rank, quotient dimension
O = np.vstack([C @ np.linalg.matrix_power(A, t) for t in range(n)])
rank_O = np.linalg.matrix_rank(O)
print(f"(1) rank(O) = {rank_O}  =>  minimal quotient 4 -> {rank_O};  ker = unobservable subspace")
assert rank_O == 2

# ---- (2) Gramian three ways: closed form, Lyapunov fixed point, trajectory sum
W_closed = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        W_closed[i, j] = C[0, i] * C[0, j] / (1.0 - lam[i] * lam[j])

W_sum = np.zeros((n, n))
M = np.eye(n)
for t in range(600):                       # ||A||<1 -> converged far below 1e-12 by t=600
    W_sum += M.T @ (C.T @ C) @ M
    M = A @ M

resid = np.linalg.norm(A.T @ W_closed @ A + C.T @ C - W_closed)
agree = np.linalg.norm(W_sum - W_closed)
print(f"(2) W(obs block) = {W_closed[:2, :2].tolist()}  (exact [[25/9,5/3],[5/3,4/3]])")
print(f"    Lyapunov residual ||A'WA + C'C - W|| = {resid:.2e};  |trajectory-sum - closed| = {agree:.2e}")
assert resid < 1e-12 and agree < 1e-12
assert np.allclose(W_closed[:2, :2], [[25/9, 5/3], [5/3, 4/3]], atol=1e-15)
try:                                       # optional scipy cross-check
    from scipy.linalg import solve_discrete_lyapunov
    W_scipy = solve_discrete_lyapunov(A.T, C.T @ C)
    print(f"    scipy solve_discrete_lyapunov agrees: {np.allclose(W_scipy, W_closed, atol=1e-10)}")
except ImportError:
    print("    (scipy not installed - skipped optional cross-check)")

W = W_closed
D = lambda x, y: float(np.sqrt((F(x, dtype=float) - F(y, dtype=float)) @ W @ (F(x, dtype=float) - F(y, dtype=float))))
e1, e2, e3, e4 = np.eye(4)
z = np.zeros(4)

# ---- (3) pseudometric: kernel collapses e3,e4; positive definite on the quotient
eigs = np.linalg.eigvalsh(W[:2, :2])
print(f"(3) D(e3,0) = {D(e3, z)}   D(e4,0) = {D(e4, z)}   (distinct states, distance 0 -> PSEUDOmetric)")
print(f"    W e3 = W e4 = 0: {np.allclose(W @ e3, 0) and np.allclose(W @ e4, 0)};  quotient eigs = {eigs.round(5).tolist()} > 0")
assert D(e3, z) == 0.0 and D(e4, z) == 0.0 and eigs.min() > 0

# ---- (4) continuum of grades
alphas = (0.1, 0.25, 0.5, 0.75, 1.0)
grades = [D(a * e1, z) for a in alphas]
print(f"(4) D(a*e1, 0) for a=.1,.25,.5,.75,1 : {[round(g, 6) for g in grades]}   = (5/3)*a  -> CONTINUUM (vs E1's {{0,1/2,1}})")
assert all(abs(g - 5 / 3 * a) < 1e-12 for g, a in zip(grades, alphas))
print(f"    D(e1,0) = {D(e1, z):.6f} (=5/3)   D(e2,0) = {D(e2, z):.6f} (=2/sqrt(3))   D(e1,e2) = {D(e1, e2):.6f} (=sqrt(7)/3)")

# ---- (5) not an ultrametric
lhs, rhs = D(e1, -e1), max(D(e1, z), D(z, -e1))
print(f"(5) strong triangle: D(e1,-e1) = {lhs:.4f} <= max = {rhs:.4f} ?  {lhs <= rhs + 1e-12}  -> NOT ultrametric")
assert lhs > rhs

# ---- (6) parallelogram law HOLDS -> real inner-product (positive-form rung reached)
pl = D(e1 + e2, z) ** 2 + D(e1 - e2, z) ** 2
pr = 2 * D(e1, z) ** 2 + 2 * D(e2, z) ** 2
print(f"(6) parallelogram: {pl:.6f} == {pr:.6f} ?  {abs(pl - pr) < 1e-12}   (= 74/9; weighted-L1 half FAILS this)")
assert abs(pl - pr) < 1e-12

print()
print("ALL CHECKS PASSED - E5/Gramian verified.")
print("PIN: continuous observation + partial read-out -> D = positive REAL bilinear form,")
print("     kernel = unobservable subspace, minimal quotient 4->2 (Kalman).  Rung reached:")
print("     linear/normed (L1 half) AND positive real form (this half).  Missing to quantum:")
print("     complex sesquilinear + non-simplex state body = E4 frontier, Hardy/CDP.")
