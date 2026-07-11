"""Priority-1, E4 (the crux rung): simplex -> complex-projective.
Classical bit  = probability simplex over {0,1} (a segment); distance = |p-q| (L1/TV);
                 every mixture has a UNIQUE decomposition into the two pure states.
Qubit          = density matrices on C^2 = the Bloch BALL; distance = trace distance
                 = 1/2 ||rho-sigma||_1 = 1/2 * Euclidean(Bloch vectors); a mixed state
                 has NON-UNIQUE pure-state decompositions -> NOT a simplex.
This EXHIBITS the classical-vs-quantum contrast; it does NOT derive quantum (the forcing
= 'why the non-simplex complex body' = the open Hardy/CDP reconstruction question).
Requires numpy:  pip install numpy --break-system-packages
Reproduce:       python3 qubit_vs_bit.py"""
import numpy as np, cmath

def pure(theta, phi=0.0):
    a = np.cos(theta / 2); b = cmath.exp(1j * phi) * np.sin(theta / 2)
    psi = np.array([a, b], dtype=complex); return np.outer(psi, psi.conj())

k0, k1 = pure(0), pure(np.pi)                        # |0> (+z), |1> (-z)
kp, km = pure(np.pi / 2, 0), pure(np.pi / 2, np.pi)  # |+> (+x), |-> (-x)
I2 = np.eye(2) / 2                                   # maximally mixed (Bloch centre)

def trace_dist(r, s):
    return 0.5 * np.sum(np.abs(np.linalg.eigvalsh(r - s)))

if __name__ == "__main__":
    print("=== QUANTUM (qubit) ===")
    dz, dx = 0.5 * k0 + 0.5 * k1, 0.5 * kp + 0.5 * km
    print("  I/2 as 1/2|0><0|+1/2|1><1| == I/2 ?", np.allclose(dz, I2),
          "  as 1/2|+><+|+1/2|-><-| == I/2 ?", np.allclose(dx, I2))
    print("  SAME mixed state, TWO different pure ensembles {|0>,|1>} vs {|+>,|->} => NON-UNIQUE decomposition => NOT a simplex")
    t01, t0p, t1p = trace_dist(k0, k1), trace_dist(k0, kp), trace_dist(k1, kp)
    print(f"  trace distances: T(|0>,|1>)={t01:.4f} (orthogonal)  T(|0>,|+>)={t0p:.4f}  T(|1>,|+>)={t1p:.4f}  (=1/sqrt2)")
    print(f"  triangle T(0,1) <= T(0,+)+T(+,1):  {t01:.3f} <= {t0p+t1p:.3f}  (NOT tight -> a SPHERE, not a segment)")
    print("=== CLASSICAL (bit) ===")
    print("  simplex over {0,1} = segment [0,1]; distance |p-q| (L1/TV); mixture p=1/2 has the UNIQUE decomposition into pure states.")
    print("=== PIN ===")
    print("  classical: simplex + L1/TV + UNIQUE decomposition.  quantum: Bloch ball + trace distance + NON-UNIQUE decomposition.")
    print("  remaining gap = 'why the non-simplex complex body?' = quantum reconstruction (Hardy/CDP), open.")
