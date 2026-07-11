"""Priority-1, QUEUE item 1 (E5): continuous-observation variant.
Goal: show that with REAL-valued observations + discounting, the behavioural graded D
is a GENUINELY CONTINUOUS metric (a whole continuum of values, not the discrete
ultrametric {2^-k} of E1), and identify 'what geometry it wants'.

Setup (linear contraction, closed form):
  state s in R^n ; F(s) = M s, M = diag(lam_i), 0<lam_i<1 ; O(s) = s (identity read).
  discounted behavioural distance
     d(x,y) = sum_{k>=0} g^k * ||F^k x - F^k y||_1
            = sum_i |x_i - y_i| * sum_k (g*lam_i)^k
            = sum_i w_i |x_i - y_i|,      w_i = 1/(1 - g*lam_i).
  => a WEIGHTED L1 (Manhattan) metric on the observation space.

Contrasts verified below:
  (1) values form a CONTINUUM (prop. to |x-y|), NOT in {2^-k} -> genuinely continuous.
  (2) collinear x<y<z: d(x,z) = d(x,y)+d(y,z) -> ADDITIVE -> strong triangle FAILS
      -> NOT an ultrametric (E1's ultrametric was an artifact of SYMBOLIC observation).
  (3) geometry it wants = normed (weighted L1): a length space with midpoints, still
      NOT Hilbert (parallelogram law fails, L1 != L2). To reach the Hilbert rung, O must
      feed a POSITIVE QUADRATIC form, not merely a norm -> forward pin to E4/reconstruction.
Requires numpy.  Reproduce: python3 continuous_observation_metric.py"""
import numpy as np

g = 0.5                       # discount
lam = np.array([0.5, 0.9])    # per-coordinate contraction (diagonal F)
w = 1.0 / (1.0 - g * lam)     # closed-form weights

def d_closed(x, y):
    return float(np.sum(w * np.abs(np.asarray(x, float) - np.asarray(y, float))))

def d_trunc(x, y, K=4000):    # independent numeric check via the actual discounted sum
    x = np.asarray(x, float); y = np.asarray(y, float)
    tot = 0.0; fx = x.copy(); fy = y.copy()
    for k in range(K):
        tot += (g ** k) * np.sum(np.abs(fx - fy)); fx = lam * fx; fy = lam * fy
    return float(tot)

if __name__ == "__main__":
    print("weights w =", w.round(4), " (closed form 1/(1-g*lam))")
    A, B, C = [0.0, 0.0], [0.5, 0.0], [1.0, 0.0]           # collinear on coord 0
    dab, dbc, dac = d_closed(A, B), d_closed(B, C), d_closed(A, C)
    print("\n[continuum] d(0,t):", [round(d_closed([0, 0], [t, 0]), 4) for t in (0.1, 0.25, 0.5, 0.75, 1.0)])
    print("   -> a continuum of values (linear in t), NOT {1, 1/2, 1/4, ...}")
    print(f"[additive]  d(A,B)={dab:.4f}  d(B,C)={dbc:.4f}  d(A,C)={dac:.4f}")
    print(f"   strong triangle (ultrametric)  d(A,C) <= max: {dac:.3f} <= {max(dab, dbc):.3f} ? {dac <= max(dab, dbc) + 1e-9}  -> NOT ultrametric")
    print(f"   ordinary triangle TIGHT (additive):           {dac:.3f} == {dab + dbc:.3f} ? {abs(dac - (dab + dbc)) < 1e-9}  -> B is a metric MIDPOINT")
    P, Q = [0.3, -0.7], [0.9, 0.4]
    print(f"\n[check] closed={d_closed(P, Q):.6f}  truncated-sum={d_trunc(P, Q):.6f}  agree? {abs(d_closed(P, Q) - d_trunc(P, Q)) < 1e-6}")
    u, v = np.array([1.0, 0.0]), np.array([0.0, 1.0])
    nrm = lambda z: d_closed(np.zeros(2), z)
    lhs = nrm(u + v) ** 2 + nrm(u - v) ** 2
    rhs = 2 * nrm(u) ** 2 + 2 * nrm(v) ** 2
    print(f"[geometry]  weighted-L1 metric on R^2, w={w.round(4)}")
    print(f"   parallelogram law  |u+v|^2+|u-v|^2 == 2|u|^2+2|v|^2 ? {lhs:.3f} == {rhs:.3f} ? {abs(lhs - rhs) < 1e-9}  -> FAILS => NOT Hilbert (L1 != L2)")
    print("\nPIN: continuous observation -> genuinely continuous NORMED metric (weighted L1),")
    print("     additive/geodesic (not ultrametric); Hilbert needs a POSITIVE QUADRATIC form (-> E4/reconstruction).")
