"""Priority-5.5 (frontier): what selects QUANTUM inside the locally-tomographic-with-entanglement class?
The gbit showed local tomography can hold WITH entanglement (PR box). Quantum is the sub-theory that HAS
entanglement (beats classical) but FORBIDS PR boxes. The cleanest computable discriminator is the CHSH tier:
    classical / local  <= 2      (deterministic strategies)
    quantum            <= 2*sqrt(2) ~ 2.828   (Tsirelson bound)
    boxworld / PR box  = 4       (algebraic max)
So quantum sits STRICTLY BETWEEN classical and boxworld. Tsirelson's 2*sqrt(2) is a CONSEQUENCE of the complex
inner-product (Hilbert) structure; the PRINCIPLE that caps correlations there (rules out PR boxes) is the open
reconstruction question (information causality, macroscopic locality, ...). Requires numpy. Reproduce: python3 chsh_tiers.py"""
import itertools
import numpy as np

X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)

# --- classical / local-hidden-variable bound: max over deterministic +-1 assignments ---
def chsh(a0, a1, b0, b1):
    return a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1
classical = max(abs(chsh(*v)) for v in itertools.product([1, -1], repeat=4))

# --- quantum: singlet with optimal measurement settings ---
psi = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)      # |01> - |10>  (singlet)
rho = np.outer(psi, psi.conj())
def E(A, B):
    return np.trace(rho @ np.kron(A, B)).real
A0, A1 = Z, X
B0, B1 = (Z + X) / np.sqrt(2), (Z - X) / np.sqrt(2)           # unit Bloch vectors -> eigenvalues +-1
S_q = E(A0, B0) + E(A0, B1) + E(A1, B0) - E(A1, B1)
quantum = abs(S_q)

# --- PR box (boxworld): P(ab|xy) = 1/2 iff a xor b = x and y ---
Epr = {(x, y): (1.0 if (x & y) == 0 else -1.0) for x in (0, 1) for y in (0, 1)}
prbox = abs(Epr[(0, 0)] + Epr[(0, 1)] + Epr[(1, 0)] - Epr[(1, 1)])

if __name__ == "__main__":
    print(f"classical / local  max|CHSH| = {classical:.4f}   (deterministic strategies)")
    print(f"quantum (singlet)  |CHSH|    = {quantum:.4f}   (Tsirelson 2*sqrt2 = {2*np.sqrt(2):.4f})")
    print(f"boxworld / PR box  |CHSH|    = {prbox:.4f}   (algebraic max)")
    print(f"\nstrict tiering:  {classical:.3f}  <  {quantum:.3f}  <  {prbox:.3f}   -> {classical < quantum < prbox}")
    print("\nPIN: quantum is the sub-theory that BEATS classical (entanglement: CHSH>2) yet OBEYS Tsirelson (CHSH<=2sqrt2,")
    print("     forbidding PR boxes). That places quantum STRICTLY between the classical simplex and boxworld inside the")
    print("     locally-tomographic-with-entanglement class. WHAT caps it at 2sqrt2 (rules out PR boxes) = the open")
    print("     reconstruction principle (Tsirelson bound is a consequence of Hilbert structure; info-causality etc. are")
    print("     candidate *principles*). This is the precise next question, and whether the framework SUPPLIES it is open.")
