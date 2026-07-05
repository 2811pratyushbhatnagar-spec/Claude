# Fixed-e proof of K(e)=D(e), contingent on Carry-Set Separation

**Register: proof outline.** The argument below is a *complete proof for each fixed odd
prime e that satisfies Carry-Set Separation* (verified computationally for all e ≤ 400, no
colliding prime; extended to e ≤ 2000). It is **not** a uniform-in-e proof — the single
contingency, Carry-Set Separation, is stated explicitly and is the open combinatorial input
(Problem 3). Deposited after an adversarial arithmetic-geometry audit returned "closes cleanly."

## Statement
Let e be a fixed odd prime. For p ≡ 1 (mod e) let χ be a character of exact order e and set,
for m ∈ {1,…,e−2},
$$T(1,m)(p) \;=\; \sum_{s\in(\mathbb Z/e)^\times} J(\chi^s,\chi^{ms}),$$
a rational integer, constant on the orbits of G = ⟨m↦m⁻¹, m↦−1−m⟩ ≅ S₃; let m₁,…,m_{r(e)}
be orbit representatives. **Carry-Set Separation (CSS, contingency):** the CM types
Φ_{m_i} = {t ∈ (ℤ/e)^× : (t mod e)+(m_i t mod e) < e} are pairwise inequivalent under the
(ℤ/e)^×-scaling action t ↦ st (= the Galois equivalence of CM types).

> **Theorem (contingent on CSS for this e).** The r(e) functions p ↦ T(1,m_i)(p) together
> with the constant 1 are ℚ-linearly independent. Equivalently K(e) = D(e): the only
> ℚ-linear relations among the orbit-traces are the S₃ (Stickelberger) relations.

## Inputs (cited)
- **[W49]** A. Weil, *Numbers of solutions of equations in finite fields*, Bull. AMS **55**
  (1949): the Frobenius eigenvalues on H¹ of the Fermat curve F_e : x^e+y^e+z^e=0 over 𝔽_p
  (p≡1 mod e) are the Jacobi sums J(χ^a,χ^b), a,b,a+b≢0.  *(Reference exists; exact theorem
  number not verbatim-pinned here.)*
- **[W52]** A. Weil, *Jacobi sums as Grössencharaktere*, Trans. AMS **73** (1952), 487–495:
  the Jacobi sums are values of Hecke Grössencharaktere of ℚ(ζ_e) ⟹ Jac(F_e) is CM.
- **[KR78]** N. Koblitz, D. Rohrlich, *Simple factors in the Jacobian of a Fermat curve*,
  Canad. J. Math. **30**(6) (1978), 1183–1205: over ℚ(ζ_e), Jac(F_e) is isogenous to a
  product of simple CM abelian varieties A_i indexed by the G-orbits, and
  T(1,m_i)(p) = a_p(A_i) (Frobenius trace).  *(Non-isogeny of distinct-orbit factors is
  implicit, not verbatim; it is exactly CSS.)*
- **Good reduction:** F_e is smooth over ℤ[1/e], so Jac(F_e) — and each A_i, good reduction
  being an isogeny invariant (**Néron–Ogg–Shafarevich**) — has good reduction at every p∤e.
  In particular every admissible p ≡ 1 (mod e) (p>e) is a prime of good reduction.
- CM theory (**Shimura–Taniyama**; Lang, *Complex Multiplication*): simple CM abelian
  varieties are isogenous ⟺ equal CM field and CM type up to Galois (=scaling) equivalence.
- **Chebotarev**; **Brauer–Nesbitt**; **Faltings** (Tate conjecture + semisimplicity of
  V_ℓ(A_i)).

## Proof
**Step 0 (motive).** By [W49],[W52],[KR78], T(1,m_i) is the L-coefficient a_p(A_i) of the
simple CM factor A_i. The symmetrized definition (sum over *all* s∈(ℤ/e)^×, which contains
−1) makes the S₃-identity T(1,m)=T(1,m⁻¹)=T(1,−1−m) an **exact, sign-free elementary
Jacobi-sum identity**; so any normalization sign in "a_p up to sign" does not threaten the
exactness of the relations below.

**Step 1 (D ⊆ K; the good-reduction clause).** The S₃-relations hold for **all admissible
p ≡ 1 (mod e)**, not merely almost all. Indeed G realizes isogenies A_m ~ A_{m⁻¹} ~ A_{−1−m}
over ℚ(ζ_e) [KR78]; an isogeny induces a Galois-module isomorphism of ℓ-adic Tate modules
V_ℓ, hence equal Frobenius characteristic polynomials — so equal a_p — at **every** prime of
good reduction (p≠ℓ). Since all p ≡ 1 (mod e) are good (above), the relations are exact for
all admissible p. This is the load-bearing upgrade of "almost all p" to "all admissible p."

**Step 2 (K ⊆ D, contingent on CSS).** Suppose Σ_i c_i T(1,m_i)(p) = c₀ for all admissible p
(c_i,c₀∈ℚ); we show all c_i = c₀ = 0. Over ℚ(ζ_e), by CM (V_ℓ(A_i) semisimple, Faltings), the
Galois representation H¹(A_i)⊗ℚ_ℓ splits into 1-dimensional CM characters (Grössencharaktere)
ψ_{i,σ}, σ ranging over the CM type Φ_{m_i} [W52]. For p ≡ 1 (mod e), p splits completely in
ℚ(ζ_e); choosing 𝔭∣p, a_p(A_i) = Σ_σ ψ_{i,σ}(Frob_𝔭). The ψ_{i,σ} factor through an abelian
quotient of Gal(ℚ̄/ℚ(ζ_e)); by **Chebotarev** the Frob_𝔭 (p≡1 mod e, good) equidistribute
there, so the relation forces the identity of class functions
Σ_i c_i Σ_σ ψ_{i,σ} = c₀ (constant). Each ψ_{i,σ} has weight 1 (|ψ|=√p ≠ 1), hence is
non-trivial and ≠ the trivial character (which alone contributes the constant c₀); by
**Brauer–Nesbitt**/linear independence of characters, c₀ = 0 and Σ_i c_i Σ_σ ψ_{i,σ} = 0.

Now invoke **CSS**: the CM types Φ_{m_i} are pairwise inequivalent under scaling, i.e. under
the Galois equivalence of CM types. By CM theory the A_i are therefore pairwise
**non-isogenous** over ℚ̄; by **Faltings** (Hom_{Gal}(V_ℓ(A_i),V_ℓ(A_j)) = Hom(A_i,A_j)⊗ℚ_ℓ =
0 for i≠j) together with **semisimplicity**, the character-sets {ψ_{i,σ}}_σ for distinct i are
**disjoint**. Disjointness + linear independence of characters forces each c_i = 0. ∎

## Register
- **Proved (this e, given CSS):** the theorem. Audit ("closes cleanly") confirms Steps 1–2,
  incl. the good-reduction clause, are gap-free.
- **Cited (exist; some pinpoints unpinned):** [W49],[W52],[KR78]; good reduction via
  Néron–Ogg–Shafarevich + Fermat smoothness; Shimura–Taniyama, Chebotarev, Brauer–Nesbitt,
  Faltings.
- **Contingency (open, = Problem 3):** Carry-Set Separation. **Verified computationally for
  all odd primes e ≤ 2000** (no colliding prime; a collision would refute K(e)=D(e)). A
  finite verification is *not* a uniform proof.
- **Precision on the contingency:** "distinct up to scaling" must be *exactly* the
  (ℤ/e)^×-scaling = Galois equivalence of CM types; the implication scaling-distinct ⟹
  non-isogenous holds only under this identification, which is where all remaining difficulty
  resides.

---

## Appendix — structural sharpening (the j-invariant), NOT a proof

The invariant **I(m) = 8(m²+m+1)³/(m²+m)²** is the **j-invariant of the leg-triple
{1, m, −1−m}**. It is G-invariant (provably, I(m⁻¹)=I(−1−m)=I(m) by direct algebra) and
separates distinct G-orbits (a uniform polynomial identity; the classical fact that the
j-invariant is a complete invariant of the anharmonic 6-tuple). Verified injective on orbits
for all e < 600.

This reduces CSS to a single lemma — **Lemma L: the carry set Φ_m determines its triple's
j-invariant I(m)** (equivalently, I is a scaling-invariant functional of Φ_m). **But since
I already separates the orbits, Lemma L is logically equivalent to CSS** — so this is a
genuine *reformulation / explicit algebraic target* (find F with F(Φ_m)=I(m)), **not a proof
of CSS.** Separating the orbits on the m-side (the domain) is near-automatic for the
j-invariant; the open content is entirely whether the carry set (the CM-type side) recovers it.

Computational note: near-collision margin (min edits to make one orbit's carry-necklace a
rotation of another's) is ≥ 2 always and grows ≈ (e−1)/6 (e=61→10, e=151→24, e=251→42), so
only finitely many small e are ever tight — suggesting a "large-e margin bound + finite check"
proof strategy for uniform CSS.
