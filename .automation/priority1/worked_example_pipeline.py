"""Priority-4 (ChatGPT's recommended next step): ONE completely worked example carried through the
ENTIRE pipeline, tying BOTH framework objects together:
    representation family (Rep)  ->  preservation criterion (P)  ->  representation-invariant I(C,O,Rep,P)
    ->  minimal quotient  ->  existence / uniqueness  ->  distinguishability form D.

System: discrete-time LTI  x_{k+1}=A x_k + B u_k,  y_k = C x_k, with a mode that is BOTH unobservable
and uncontrollable so the pipeline genuinely reduces:
    A = diag(0.5, 0.8, 0.3),  B = [1,1,0]^T,  C = [1,1,0].
Mode 3 (eigenvalue 0.3): C_3=0 (unobservable) and B_3=0 (uncontrollable) -> not in the minimal realization.

Stages verified below:
  (1) Rep      : similarity x |-> T x gives (A,B,C) |-> (T A T^-1, T B, C T^-1) — a different REPRESENTATION.
  (2) P        : preserve the input-output map (Markov parameters g_k = C A^k B / transfer function).
  (3) I        : g_k are Rep-INVARIANT: C' A'^k B' = C A^k B for every invertible T  -> the invariant object.
  (4) quotient : Kalman — minimal realization dim = Hankel rank = # modes both obs & ctrb (here 2, not 3).
  (5) exist/uniq: the minimal realization EXISTS and is UNIQUE UP TO SIMILARITY (the Rep group) — the linear
                  analog of E8's 'uniqueness is a property of the equivalence, not the object'.
  (6) D        : observability Gramian W solves A^T W A - W + C^T C = 0;  D(x,y)^2=(x-y)^T W (x-y);
                 ker W = unobservable subspace = exactly the states the quotient identifies (D=0).
Requires numpy, scipy.  Reproduce: python3 worked_example_pipeline.py"""
import numpy as np
from scipy.linalg import solve_discrete_lyapunov

np.set_printoptions(precision=4, suppress=True)
A = np.diag([0.5, 0.8, 0.3]); B = np.array([[1.0], [1.0], [0.0]]); C = np.array([[1.0, 1.0, 0.0]])
n = 3

def markov(A, B, C, K=6):
    return np.array([float((C @ np.linalg.matrix_power(A, k) @ B).item()) for k in range(K)])

def obs_matrix(A, C):
    return np.vstack([C @ np.linalg.matrix_power(A, k) for k in range(n)])

def ctrb_matrix(A, B):
    return np.hstack([np.linalg.matrix_power(A, k) @ B for k in range(n)])

if __name__ == "__main__":
    print("=== (2)/(3) invariant I: Markov parameters g_k = C A^k B ===")
    g = markov(A, B, C); print("  g_0..g_5 =", g, "  (= 0.5^k + 0.8^k)")

    print("\n=== (1) Rep: change representation by a random similarity T (same system, new coordinates) ===")
    rng = np.random.default_rng(0); T = rng.normal(size=(n, n))
    while abs(np.linalg.det(T)) < 0.3: T = rng.normal(size=(n, n))
    Ap, Bp, Cp = T @ A @ np.linalg.inv(T), T @ B, C @ np.linalg.inv(T)
    gp = markov(Ap, Bp, Cp)
    print("  A' != A ?", not np.allclose(Ap, A), "  C' != C ?", not np.allclose(Cp, C),
          "  -> representation changed")
    print("  g'_k == g_k (invariant) ?", np.allclose(g, gp), "   max|g'-g| =", float(np.max(np.abs(g - gp))))

    print("\n=== (4) minimal quotient (Kalman): ranks + Hankel order ===")
    Ob = obs_matrix(A, C); Ct = ctrb_matrix(A, B)
    Hank = np.array([[g[i + j] for j in range(3)] for i in range(3)])
    print("  rank observability =", np.linalg.matrix_rank(Ob), " (unobservable dim =", n - np.linalg.matrix_rank(Ob), ")")
    print("  rank controllability =", np.linalg.matrix_rank(Ct))
    print("  Hankel rank = minimal realization order =", np.linalg.matrix_rank(Hank), " (< n=3 -> genuine reduction)")

    print("\n=== (5) existence + uniqueness UP TO SIMILARITY ===")
    Am, Bm, Cm = np.diag([0.5, 0.8]), np.array([[1.0], [1.0]]), np.array([[1.0, 1.0]])
    S = np.array([[1.0, 1.0], [0.0, 1.0]])                      # any invertible 2x2
    Am2, Bm2, Cm2 = S @ Am @ np.linalg.inv(S), S @ Bm, Cm @ np.linalg.inv(S)
    g1, g2 = markov(Am, Bm, Cm), markov(Am2, Bm2, Cm2)
    print("  two minimal 2D realizations (related by S); same Markov params ?", np.allclose(g1, g2))
    print("  and both equal the 3D system's g_k ?", np.allclose(g1, g[:len(g1)]),
          "  -> minimal realization unique UP TO the Rep group, exists (dim 2)")

    print("\n=== (6) distinguishability form D = observability Gramian ===")
    W = solve_discrete_lyapunov(A.T, C.T @ C)
    print("  W =\n", W)
    closed = np.array([[4 / 3, 5 / 3, 0], [5 / 3, 25 / 9, 0], [0, 0, 0]])
    print("  matches closed form [[4/3,5/3,0],[5/3,25/9,0],[0,0,0]] ?", np.allclose(W, closed))
    evals, evecs = np.linalg.eigh(W)
    kernel = evecs[:, np.isclose(evals, 0)]
    print("  ker W (unobservable subspace) spanned by e3 ?",
          np.allclose(np.abs(kernel[:, 0]) / np.max(np.abs(kernel[:, 0])), [0, 0, 1]))
    x, y = np.array([2.0, -1.0, 5.0]), np.array([2.0, -1.0, -9.0])   # differ ONLY in the e3 (unobservable) coord
    d2 = float((x - y) @ W @ (x - y))
    print(f"  D(x,y)^2 for x,y differing only in e3 = {d2:.6f}  -> D=0: identified by the quotient (indistinguishable)")
    u, v = np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0])
    print(f"  D(e1,e2)^2 = {float((u-v)@W@(u-v)):.4f}  (>0: observable directions carry a positive REAL form)")

    print("\nPIN: one system carried end-to-end — Rep (similarity) -> P (preserve I/O) -> I (Markov params, invariant)")
    print("     -> minimal quotient (Kalman, 3->2) -> exists & unique up to the Rep group -> D = observability Gramian")
    print("     (ker = the quotiented unobservable subspace). Ties I(C,O,Rep,P) to the (S,F,O) minimal quotient and D.")
