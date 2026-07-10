# Round 5 — Is the Pinwheel's {±J} the Alfsen–Shultz Orientation? — Candidate Note

**Register:** NON-CANON · Tier-3 · nothing promoted · canon read-only. Promotion
is the steward's decision; this note reports verified vs open only.
**Banding:** [KNOWN] · [CONJ] (ours, sketch-grade) · [VERIFIED-ADV] (survived a
dedicated adversarial agent pass this session) · [LIT-PARTIAL] (search-snippet
level only — see coverage note).
**Retrieval coverage:** arXiv full text is 403-blocked from this container
(arxiv.org, export.arxiv, ar5iv, mirrors — all denied at CONNECT; logged).
Döring 1411.5558 was reached at metadata/snippet level only. **The task
prompt's citation keys (Def 3.2, Prop 3.4, A–S 4.2/6.18/7.103/Lemma 7.100)
could not be verified against the paper**; citing literature (Barnum et al.
1904.03753) points to A–S *Geometry of State Spaces* **Theorem 6.15** for the
dynamical-correspondence characterization. Nothing below asserts Döring's
internal numbering.

---

## Verdict up front

**The identification does NOT go through — and the failure is structural, not
numerical.** The pinwheel never enters Alfsen–Shultz's domain: its convex body
is not the state space of any JB-algebra [VERIFIED-ADV], and even its minimal
Jordan completion (the rebit spin factor V₂, imported via the canonical
metric) admits **no dynamical correspondence at all** — the A–S/Döring set of
associative products is *empty*, not two-element [VERIFIED-ADV, two
independent proofs]. Conversely, where the A–S ℤ₂ is nontrivial (the qubit),
our (1,1) form-criterion **fails** (no invariant antisymmetric *form* on the
Bloch ℝ³) [VERIFIED-ADV]. So: **same output type (a ℤ₂ conjugation torsor),
provably not the same invariant** — the two invariants have (in every case
examined) disjoint supports. The honest relation is pattern-level, and the
adversarial pass sharpened where the pattern actually lives (§5).

## 1. Construction (tasks 1–2 as executed)

Pinwheel: Aut(K) = ℤ₃ exactly (360 rotations + 360 reflections sampled; only
0°/120°/240° survive — distinct radii kill reflections). Form counts (1,1);
canonical J = rot 90° from ω via the unique isotropic metric; J² = −I and
[J, rot120°] = 0 at machine zero. Complexification (V̄₀, ±J) ≅ ℂ±, conjugate
pair — fine at state-space level. **But step 2's "two candidate associative
products" cannot be constructed**: Döring's Def-3.2-style machinery needs a
Jordan algebra of observables first, and:

- **The pinwheel body is not a JB state space.** Finite-dim JB-algebras =
  JvW classification (ℝ, spin factors Vₙ, Hₙ(ℝ/ℂ/ℍ), Albert) [KNOWN]; every
  non-associative factor has a continuum of pure states; finitely many
  extreme points ⟹ associative ⟹ simplex; 6 extreme points ⟹ Δ⁵, dimension
  5 ≠ 2. [VERIFIED-ADV — adversary confirmed classification correctly
  invoked, edge cases H₂ = spin factors checked]
- **Minimal Jordan import lands on the rebit V₂** (spin factor on ℝ⊕ℝ²,
  using the canonical metric; Jordan axioms machine-checked). Its state
  space is the disc ⊋ K — already an import beyond the pinwheel's data,
  flagged [CONJ].

## 2. The rebit obstruction (task 3's answer): the product set is EMPTY

**Theorem-grade after the adversarial pass:** V₂ is not the self-adjoint part
of ANY complex associative *-algebra. Proof chain, with the two gaps the
adversary found now closed:

1. If V₂ = A_sa then dim_ℂ A = 3, and A is automatically unital (the Jordan
   unit is a two-sided unit: ea+ae = 2a and e² = e force ea = ae = a). [VERIFIED-ADV]
2. **Semisimplicity (gap closed):** the Jacobson radical J(A) is *-invariant,
   so J(A)_sa is a nilpotent Jordan ideal of V₂; V₂ ≅ Sym₂(ℝ) is a *simple*
   unital Jordan algebra, so J(A) = 0. (Positivity/JB axioms not needed.
   Load-bearing: idempotent counting alone would NOT kill non-semisimple
   candidates — T₂(ℂ) has a continuum of idempotents.) [VERIFIED-ADV]
3. Wedderburn over ℂ: 3 = Σnᵢ² ⟹ A ≅ ℂ³ (machine-enumerated).
4. **Involutions (gap closed):** on ℂ³ the conjugate-linear involutions are
   entrywise conjugation composed with a permutation of order ≤ 2. Identity:
   A_sa = ℝ³, exactly 8 idempotents. Swap (z₁,z₂,z₃)* = (z̄₂,z̄₁,z̄₃): a genuine
   non-C* *-algebra whose sa part ≅ ℂ⊕ℝ is associative with 4 idempotents.
   V₂ has a **continuum** of idempotents ((½, y), |y| = ½ — machine-checked)
   and is non-associative; Jordan isomorphisms biject idempotents. Both cases
   die. [VERIFIED-ADV]
5. Hence, via the A–S characterization (a JB(W)-algebra is the sa part of a
   C*/vN algebra **iff** it admits a dynamical correspondence [LIT-PARTIAL,
   snippet-confirmed; A–S Thm 6.15 per citing literature]): **the set of
   dynamical correspondences on V₂ is empty.**
6. **Independent direct proof, no A–S theorem** [VERIFIED-ADV + machine,
   `round5_dyncorr_check.py`]: der(V₂) is 1-dimensional (= so(2), abelian) —
   computed, kernel dimension 1 — while [L_{e₁}, L_{e₂}] ≠ 0 (the rotation
   generator; computed exactly). A dynamical correspondence needs
   [ψ_a, ψ_b] = −[L_a, L_b]: LHS lies in an abelian algebra, RHS ≠ 0.
   Contradiction. **The obstruction is Lie-algebraic: so(2) is too small.**

**Attribution audit (correction to this round's own first draft):** the
emptiness statement is *ours-from-A–S*, NOT a statement in Döring's paper —
his classification parametrizes products *where at least one exists*. The
script's original print line overstated this and has been corrected in-place.
Döring's completeness theorem moreover explicitly excludes ℂ⊕ℂ and type I₂
summands [LIT-PARTIAL] — the vN-side edge cases; the rebit sits outside the
vN world altogether.

## 3. The real-algebra loophole — closed, with a moral

V₂ *is* the symmetric part of the **real** algebra M₂(ℝ). But transpose is an
isomorphism M₂(ℝ) → M₂(ℝ)^op **fixing Sym₂(ℝ) pointwise** ((ab)ᵀ = bᵀaᵀ at
machine zero; symmetric = transpose-fixed by definition), so ab vs ba is pure
gauge relative to all observables: **no orientation ℤ₂ over ℝ either.**
Contrast M₂(ℂ): transpose on Hermitians is entrywise conjugation (σ_y ↦ −σ_y)
— a *nontrivial* Jordan automorphism (time-reversal-like) — which is exactly
why the two orderings of M₂(ℂ) are genuinely inequivalent and the qubit's ℤ₂
is real. The asymmetry's source: over ℝ, "symmetric" is *defined by* the
transpose; over ℂ, "Hermitian" is defined by conjugate-transpose, leaving a
residual conjugation. [VERIFIED-ADV]

## 4. Control and converse mismatch

**Control (M₂(ℂ), where A–S applies):** both products share the Jordan part;
product swap flips ψ_a = (i/2)[a,·] to −ψ_a (machine zero); ψ_a is skew,
ψ_a(a) = 0; a★b = c·ab + (1−c)·ba is associative at c ∈ {0,1} and fails
associativity at the Jordan midpoint c = ½ (deviation 1.42). The central-
projection ℤ₂ ⟺ the sign of ψ ⟺ i ↔ −i. Döring's picture verified on the
factor where it lives. [machine]

**Converse mismatch (qubit):** Bloch-ball affine automorphisms = **O(3)**
exactly (SO(3) from unitaries + transpose reflection; universal-NOT included —
positive-not-CP maps are still affine bijections) [VERIFIED-ADV]. Invariant
antisymmetric **forms** on ℝ³: dimension 0 under SO(3) (machine: kernel dim 0;
Λ²ℝ³ ≅ adjoint, no trivial summand), and O(3) can only shrink it. Parity
makes it over-determined (no nondegenerate antisym form in odd dimension at
all). So our (1,1) criterion fails for the qubit while the A–S ℤ₂ is
nontrivial. [VERIFIED-ADV]

## 5. Where the pattern actually lives (the adversary's sharpening)

The qubit's orientation IS carried by a canonical antisymmetric invariant —
but a **product**, not a form: Hom(Λ²ℝ³, ℝ³)^{SO(3)} = ℝ·(cross product) =
the su(2) bracket = the dynamical correspondence, unique up to scale,
**det-equivariant under O(3)** (transpose flips its sign — that sign *is* the
orientation ℤ₂). So the corrected typology:

| | invariant object | ℤ₂ carried by | nontrivial on |
|---|---|---|---|
| ours (Round 3/4) | antisymmetric **form** ω on V̄₀ | sign of ω = ±J | pinwheel-type theories (finite Aut, complex FS type) |
| Alfsen–Shultz | antisymmetric **product** (bracket) on the algebra | sign of bracket = c ∈ {0,1} = i ↔ −i | qubit-type theories (Jordan, vN-realizable) |

Same abstract pattern — *the residual freedom after all symmetric data is a
single conjugation ℤ₂ on a one-dimensional antisymmetric invariant* — but
instantiated on different carriers (scalar-valued Λ²V̄₀* vs V-valued
Λ²A → A), with **disjoint supports in every example examined** (pinwheel:
form-ℤ₂ live, product-side empty; qubit: product-ℤ₂ live, form-side empty;
rebit: both empty). [CONJ] Whether a common generalization exists — one
invariant on a setting containing both, restricting to ω here and to the
bracket there — is the genuinely new open question this round produces. A
natural candidate target: invariant elements of Hom(Λ²W, U) for the
Aut-representation pair (W, U) = (V̄₀, ℝ) vs (A_sa, A_sa). Not constructed;
explicitly open. [CONJ, open]

## 6. What was verified vs what remains open

**Verified this round** (adversarial agents + machine, artifacts below):
pinwheel Aut/J construction; pinwheel ∉ JB state spaces; rebit ≠ sa-part of
any complex *-algebra (gaps closed: semisimplicity, swap involution); rebit
dynamical-correspondence set empty (two proofs, one theorem-free);
real-loophole closure via transpose; M₂(ℂ) control (c ∈ {0,1} ⟺ ±ψ ⟺ ±i);
qubit form-count 0 under O(3).

**Open / unverified:** Döring's exact Def 3.2/Prop 3.4 wording and his A–S
citation numbers (arXiv blocked — needs a human or an unblocked fetch);
whether the "disjoint supports" observation is a theorem (is there NO theory
where both invariants are simultaneously defined and nontrivial? plausible —
needs: Jordan-realizable + complex-FS-type traceless Aut-rep — candidate
proof direction: Jordan state spaces have "too much" symmetry for complex
type on V̄₀, cf. adjoint reps carrying only symmetric invariants; NOT proved);
the common-generalization construction of §5. **No promotion implied; the
steward decides.**

## Artifacts

- `round5_orientation.py` (+ attribution fix) / `round5_output.txt` — sections
  A–E, all machine-zero or as printed.
- `round5_dyncorr_check.py` — the direct emptiness proof (der(V₂) dim 1,
  [L_{e₁}, L_{e₂}] ≠ 0), appended to `round5_output.txt`.
- Adversarial-pass results: workflow wf_b42ec631-71b (three agents:
  Döring-fetch [partial, coverage logged], rebit-refutation [confirmed +
  gaps closed], mismatch-refutation [confirmed + product/form sharpening]).
