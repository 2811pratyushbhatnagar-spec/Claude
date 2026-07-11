"""Priority-1, E7 (QUEUE #2): the rebit / LOCAL-TOMOGRAPHY witness for real-vs-complex.
Both models (Claude taxonomy + live ChatGPT) converged: past the inner-product rung (E6), the
genuine remaining step is 'why COMPLEX (not real) Hilbert'. The canonical witness (Wootters;
Araki; Hardy) is the two-qubit pair
    rho_pm = ( I(x)I  ±  sigma_y(x)sigma_y ) / 4.
Claim tested: rho_+ and rho_- have IDENTICAL statistics for every product of REAL-QM local
observables {I, sigma_x, sigma_z} (sigma_y is excluded in real QM), identical local marginals,
yet are GLOBALLY distinct (trace distance 1, distinguished by the real-symmetric global observable
sigma_y(x)sigma_y). => real QM FAILS local tomography; complex QM satisfies it. So LOCAL TOMOGRAPHY
is exactly the axiom that forces C over R. Also does the Wootters dimension count:
    real:    #{P(x)Q : P,Q in {I,sx,sz}} spans 9  <  dim(real-symmetric 4x4)=10   (gap 1 = the sy(x)sy dir)
    complex: #{P(x)Q : P,Q in {I,sx,sy,sz}} spans 16 = dim(Hermitian 4x4)=16       (no gap)
Requires numpy.  Reproduce: python3 rebit_local_tomography.py"""
import numpy as np

I = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
kron = np.kron

rho_p = (kron(I, I) + kron(sy, sy)) / 4
rho_m = (kron(I, I) - kron(sy, sy)) / 4

def is_state(r):
    herm = np.allclose(r, r.conj().T)
    psd = np.min(np.linalg.eigvalsh(r)) > -1e-12
    tr1 = abs(np.trace(r) - 1) < 1e-12
    return herm, psd, tr1, np.allclose(r.imag, 0)

def partial_trace_B(r):           # 2x2 (x) 2x2 -> trace out second factor
    R = r.reshape(2, 2, 2, 2)
    return np.trace(R, axis1=1, axis2=3)

def partial_trace_A(r):
    R = r.reshape(2, 2, 2, 2)
    return np.trace(R, axis1=0, axis2=2)

def trace_dist(a, b):
    return 0.5 * np.sum(np.abs(np.linalg.eigvalsh(a - b)))

def span_rank(ops):               # real dimension of the span of a set of 4x4 operators
    M = np.array([np.concatenate([o.real.ravel(), o.imag.ravel()]) for o in ops])
    return np.linalg.matrix_rank(M, tol=1e-9)

if __name__ == "__main__":
    print("rho_+ valid (herm,psd,tr1,real)?", is_state(rho_p), " eig:", np.linalg.eigvalsh(rho_p).round(3))
    print("rho_- valid (herm,psd,tr1,real)?", is_state(rho_m), " eig:", np.linalg.eigvalsh(rho_m).round(3))
    print("local marginals equal & maximally mixed?",
          np.allclose(partial_trace_B(rho_p), I / 2), np.allclose(partial_trace_A(rho_p), I / 2),
          np.allclose(partial_trace_B(rho_m), I / 2), np.allclose(partial_trace_A(rho_m), I / 2))

    real_local = {'I': I, 'sx': sx, 'sz': sz}          # sy EXCLUDED in real QM
    maxdiff = 0.0
    for pn, P in real_local.items():
        for qn, Q in real_local.items():
            e_p = np.trace(rho_p @ kron(P, Q)).real
            e_m = np.trace(rho_m @ kron(P, Q)).real
            maxdiff = max(maxdiff, abs(e_p - e_m))
    print(f"\nmax |<rho_+ ,P(x)Q> - <rho_- ,P(x)Q>| over all real-local products (P,Q in I,sx,sz): {maxdiff:.2e}")
    print("  => IDENTICAL under every real-QM LOCAL measurement.")

    eyy_p = np.trace(rho_p @ kron(sy, sy)).real
    eyy_m = np.trace(rho_m @ kron(sy, sy)).real
    print(f"\nglobal observable sigma_y(x)sigma_y:  <rho_+>={eyy_p:+.3f}  <rho_->={eyy_m:+.3f}  (differ)")
    print(f"trace distance T(rho_+,rho_-) = {trace_dist(rho_p, rho_m):.3f}   => perfectly distinguishable GLOBALLY")

    # Wootters dimension count
    rl = [kron(P, Q) for P in (I, sx, sz) for Q in (I, sx, sz)]
    cl = [kron(P, Q) for P in (I, sx, sy, sz) for Q in (I, sx, sy, sz)]
    sym_dim = span_rank([E + E.T for E in [np.zeros((4, 4)) for _ in range(1)]])  # placeholder, replaced below
    # ambient dims computed directly:
    real_sym_basis = []
    for a in range(4):
        for b in range(a, 4):
            E = np.zeros((4, 4)); E[a, b] = 1; E[b, a] = 1
            real_sym_basis.append(E.astype(complex))
    herm_basis = []
    for a in range(4):
        for b in range(4):
            E = np.zeros((4, 4), dtype=complex)
            if a == b:
                E[a, a] = 1
            elif a < b:
                E[a, b] = 1; E[b, a] = 1
            else:
                E[a, b] = 1j; E[b, a] = -1j
            herm_basis.append(E)
    print(f"\n[Wootters count]  REAL:   local-products span {span_rank(rl)}  vs  dim(real-symmetric 4x4)={span_rank(real_sym_basis)}  -> gap {span_rank(real_sym_basis)-span_rank(rl)} (the sigma_y(x)sigma_y direction)")
    print(f"[Wootters count]  COMPLEX: local-products span {span_rank(cl)}  vs  dim(Hermitian 4x4)={span_rank(herm_basis)}  -> gap {span_rank(herm_basis)-span_rank(cl)}")
    print("\nPIN: real QM FAILS local tomography (1 global dim, the rho_± / sigma_y(x)sigma_y direction, invisible to")
    print("     local measurements); complex QM satisfies it (16=16). LOCAL TOMOGRAPHY is the axiom forcing C over R.")
    print("     This is E4-support: it does not DERIVE C, it isolates the single reconstruction axiom at the frontier.")
