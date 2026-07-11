"""Priority-1, E6 (the aggregation experiment ChatGPT proposed after E5).
CONTROLLED: hold everything from E5 fixed (same linear system F=diag(lam), same discount g,
same real observation O(s)=s). Change ONLY the temporal aggregation of the observation error:
    L1 (E5):   d1(x,y)      = sum_k g^k * ||F^k(x-y)||_1
    L2 (E6):   d2(x,y)      = ( sum_k g^k * ||F^k(x-y)||_2^2 )^(1/2)

Closed forms (F diagonal so the geometric series separates coordinatewise):
    d1(x,y)   = sum_i w_i |x_i-y_i|,      w_i = 1/(1 - g*lam_i)          -> weighted L1 (a NORM, not from inner product)
    d2(x,y)^2 = sum_i q_i (x_i-y_i)^2,    q_i = 1/(1 - g*lam_i^2)        -> a POSITIVE QUADRATIC FORM

So d2 is the metric of the inner product <u,v>_Q = sum_i q_i u_i v_i. By Jordan-von Neumann,
a norm obeys the parallelogram law IFF it comes from an inner product. Prediction: L2 aggregation
=> parallelogram law HOLDS (Euclidean), while the E5 L1 aggregation FAILS. This isolates the
'normed -> inner-product' rung as driven by the AGGREGATION FUNCTIONAL alone -- NOTHING quantum.
The quantum-reconstruction gap (why complex / non-simplex, E4) begins only AFTER this rung.
Requires numpy.  Reproduce: python3 aggregation_L2_vs_L1.py"""
import numpy as np

g = 0.5
lam = np.array([0.5, 0.9])
w = 1.0 / (1.0 - g * lam)          # L1 weights (E5)
q = 1.0 / (1.0 - g * lam**2)       # L2 quadratic-form weights (E6); needs g*lam^2 < 1

def d1(x, y):                      # E5 aggregation
    return float(np.sum(w * np.abs(np.asarray(x, float) - np.asarray(y, float))))

def d2(x, y):                      # E6 aggregation
    dxy = np.asarray(x, float) - np.asarray(y, float)
    return float(np.sqrt(np.sum(q * dxy**2)))

def d2_trunc(x, y, K=6000):        # independent check via the actual discounted sum
    dxy = np.asarray(x, float) - np.asarray(y, float); tot = 0.0; v = dxy.copy()
    for k in range(K):
        tot += (g ** k) * np.sum(v**2); v = lam * v
    return float(np.sqrt(tot))

def parallelogram(dist):           # |u+v|^2 + |u-v|^2  vs  2|u|^2 + 2|v|^2
    u, v = np.array([1.0, 0.0]), np.array([0.0, 1.0]); z = np.zeros(2)
    lhs = dist(z, u + v) ** 2 + dist(z, u - v) ** 2
    rhs = 2 * dist(z, u) ** 2 + 2 * dist(z, v) ** 2
    return lhs, rhs, abs(lhs - rhs) < 1e-9

if __name__ == "__main__":
    print(f"g={g}, lam={lam}   L1 weights w={w.round(4)}   L2 form q={q.round(4)}  (g*lam^2={ (g*lam**2).round(4) } < 1 ok)")
    print(f"\n[closed vs truncated] d2([0,0],[1,1]) closed={d2([0,0],[1,1]):.6f}  truncated={d2_trunc([0,0],[1,1]):.6f}  agree? {abs(d2([0,0],[1,1])-d2_trunc([0,0],[1,1]))<1e-6}")
    l1_lhs, l1_rhs, l1_ok = parallelogram(d1)
    l2_lhs, l2_rhs, l2_ok = parallelogram(d2)
    print(f"\n[E5  L1 aggregation]  parallelogram: {l1_lhs:.4f} == {l1_rhs:.4f} ? {l1_ok}   -> {'HOLDS' if l1_ok else 'FAILS => not inner-product (mere norm)'}")
    print(f"[E6  L2 aggregation]  parallelogram: {l2_lhs:.4f} == {l2_rhs:.4f} ? {l2_ok}   -> {'HOLDS => inner-product (Euclidean)!' if l2_ok else 'FAILS'}")
    # confirm d2 really is <.,.>_Q: polarization identity recovers the quadratic form
    u, v = np.array([0.3, -0.7]), np.array([0.9, 0.4]); z = np.zeros(2)
    ip_polar = 0.25 * (d2(z, u + v) ** 2 - d2(z, u - v) ** 2)   # real inner product via polarization
    ip_form = float(np.sum(q * u * v))
    print(f"\n[inner product] polarization {ip_polar:.6f} == quadratic form <u,v>_Q {ip_form:.6f} ? {abs(ip_polar-ip_form)<1e-9}")
    print("\nPIN: switching ONLY the aggregation L1->L2 turns the behavioural metric into a EUCLIDEAN")
    print("     inner-product metric (parallelogram holds; Jordan-von Neumann). So 'normed -> inner-product'")
    print("     is a SEPARATE functional-analysis rung driven by the AGGREGATION, BELOW the quantum-")
    print("     reconstruction gap (why complex / non-simplex, E4). Geometry inherits the aggregation.")
