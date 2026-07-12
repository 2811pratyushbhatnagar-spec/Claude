# The Operational Complexification Theorem — Candidate Note v2

**Register:** NON-CANON · Tier-3 · nothing promoted · canon read-only.
**Venue:** remote container clone, `.automation/` only; no `status.json` here.
**Banding:** [KNOWN] = textbook/standard; [CONJ] = this note's constructions,
proof-sketch grade, not referee-checked. **Literature status: NOT QUERIED
from this container** (Alfsen–Shultz, GPT-reconstruction literature — e.g.
Hardy, Masanes–Müller, Barnum et al. — must be contacted before any novelty
claim; retrieval coverage, not existence, per Verification Instrument v1.0).

Supersedes-in-part: `complexification-note.md` (v1). The v1 equivalence
assumed irreducibility via a hypothesis; v2 removes it — irreducibility is
now **derived**. V1's census argument is unchanged and reused.

---

## 1. Raw operational data and the two flagged steps

**D0 (Theory).** A theory is a triple (S, E, p): preparations S, yes/no
measurements E, probability table p : S × E → [0,1]. No linear structure, no
group, no representation is part of the data. [KNOWN framing]

**Step 1 — linearization (flagged, standard).** Allowing coin-flip mixtures
of preparations and of measurements equips S and E with convex structure;
the universal linearization gives real vector spaces V, V* with K = conv(S)
and effects in the order interval [0, u]. This is the standard GPT move; it
introduces linear algebra but no symmetry. [KNOWN]

**D1 (Hypothesis X — finiteness, closure, nontriviality).**
(X1) finite tomography: finitely many effects determine all statistics;
(X2) closure: the set of state statistics is closed and bounded;
(X3) nontriviality: at least two operationally distinct states.
Consequence: the **minimal observation-preserving quotient** (identify
states/effects with identical statistics) is a compact convex body K̄ in a
finite-dimensional real space V̄ = ℝ·b ⊕ V̄₀ (b the barycenter, V̄₀ the
traceless part). [KNOWN]

**D2 (Symmetry of the data — flagged for circularity).** A symmetry is a
pair of bijections (α : S̄ → S̄, β : Ē → Ē) preserving mixtures and the
table: p(αω, βe) = p(ω, e). *Circularity audit:* each symmetry is an
individual, operationally definable object (definable from (S, E, p) alone);
their totality automatically forms a group G = Aut(K̄), and by X it is a
**compact** subgroup of GL(V̄₀) [KNOWN, John-ellipsoid argument]. We never
impose group structure as data — but every invariance-style notion of
"canonical" quantifies over all symmetries, so the group is *derived, not
smuggled*. This is the honest boundary of "group-free": a canonicity question
cannot even be posed without quantifying over the data's self-equivalences.
What is NOT presupposed: which group it is, that it is nontrivial, any
representation-theoretic property (irreducibility, type, commutant). Those
appear only in the realization theorem below.

**D3 (Operational two-state functionals).** A *metric candidate* is a
symmetric bilinear form m on V̄₀, positive definite, invariant under every
symmetry of the data; an *orientation form* is an antisymmetric bilinear
form ω ≠ 0 on V̄₀ invariant under every symmetry. Both are definable from
the data (via Step 1's linearization); neither is itself a probability —
"operational" here means *definable from (S, E, p) without external
choices*, flagged. Operational gloss: a metric = an intrinsic
distinguishability-distance the symmetries cannot deform; an orientation
form = the data's own notion of "clockwise" on two-parameter families of
states. [CONJ packaging]

**D4 (Canonical equivariant J).** J ∈ GL(V̄₀), J² = −I, commuting with every
symmetry of the data, such that the set of all such J is exactly {+J, −J}.

## 2. The theorem

**Theorem (Operational Complexification).** [CONJ, sketch-grade] Let a theory
satisfy X. Then the following are equivalent:

**(a)** the minimal quotient admits a canonical equivariant complex
structure ±J (sense D4);

**(b)** *operational condition:* the theory admits an invariant metric that
is **unique up to overall units**, and an invariant orientation form that is
**unique up to overall scale and sign**;

**(c)** *mathematical realization:* V̄₀ is an irreducible real representation
of Aut(K̄) of **complex Frobenius–Schur type** (real commutant ≅ ℂ; for
finite/compact groups, FS indicator ν = 0 on the associated complex irrep).

Moreover, under these conditions J is *constructed* from the operational
data: J = the unique operator with ω(x, y) = m(x, Jy), normalized by
J² = −I; the residual sign of ω is exactly the ±J ambiguity.

*Proof sketch.*
(b) ⟹ (c): Fix any invariant inner product (exists, G compact [KNOWN]).
Invariant bilinear forms ↔ commutant G′ via B(x,y) = ⟨x, Ty⟩; the
symmetric/antisymmetric split of forms is intrinsic and matches the
self-adjoint/skew split of G′. Counting per isotypic block [KNOWN counts,
translation ours]: Mat(m,ℝ) contributes (m(m+1)/2, m(m−1)/2) to
(sym, antisym); Mat(m,ℂ) contributes (m², m²); Mat(m,ℍ) contributes
(m(2m−1), m(2m+1)); wait — only the m = 1 values are load-bearing and were
machine-checked: ℝ: (1,0); ℂ: (1,1); ℍ: (1,3); and every direct sum or
multiplicity adds to the symmetric count (verified numerically for the trap
cases). sym-dim = 1 already forces a single isotypic component with
multiplicity 1, i.e. **irreducibility is a consequence of metric-uniqueness,
not a hypothesis**. Given irreducibility, antisym-dim = (0, 1, 3) for type
(ℝ, ℂ, ℍ); uniqueness of ω forces type ℂ. ∎(sketch)
(c) ⟹ (a): commutant ≅ ℂ = {a + bJ₀}; (a + bJ₀)² = −I ⟺ a = 0, b = ±1;
J-set = {±J₀}. [KNOWN, v1]
(a) ⟹ (c): any equivariant J preserves isotypic components, so the J-census
is the product of per-block censuses, each of size 0, 2, or ∞ (never 1)
[CONJ, v1 census]; total = 2 forces exactly one block of type Mat(1, ℂ). ∎

**Empirical certificate** (`invariant_forms.py`, output archived): nine
cases; (sym, antisym) = (1,1) exactly on the complex-type rows (Z₃, Z₄, Z₅
rotations); D₄/D₅ give (1,0) — no orientation form, no J; Q8 gives (1,3) —
J's exist, none canonical; and the two **traps** demonstrate necessity of
*both* uniqueness clauses: D₄⊕D₄ gives (3,1) and Z₃⊕(fixed axis) gives
(2,1) — a *unique orientation form* with a *non-unique metric*, J's exist
but no canonical one. Orientation-uniqueness alone is NOT sufficient; this
is exactly the gap that would have made a sloppier operational condition
false.

**Non-circularity audit of (b).** (b) mentions: mixtures, statistics,
indistinguishability, symmetries-of-the-data (D2, flagged), and two-argument
functionals over the linearization (D3, flagged). It does not mention:
groups as structure, representations, irreducibility, commutants, characters,
or FS indicators. Those occur only in (c). The contribution, if the
literature check comes back clean, is precisely: *an operational criterion
(rigid metric + rigid orientation) whose mathematical realization is
Frobenius–Schur complex type.*

## 3. The linking lemma (Task 2): disproved as stated, proved as repaired

**Naive statement.** "Passing to the minimal observation-preserving
realization does not change the automorphism representation except by
equivalence." — **FALSE.** [CONJ counterexample]
*Counterexample (redundancy breaks symmetry).* Take any theory with quotient
K̄ and a symmetry g with gs₀ = s₁ ≠ s₀. Build a redundant realization whose
preparation set carries **two** labels for s₀ and one for every other state.
A symmetry of the redundant data must be a bijection of preparations
covering a quotient symmetry; over s₀ the fiber has size 2, over s₁ size 1,
so no bijection covers g. Hence Sym(redundant data) ⊊ Aut(K̄): the redundant
realization's own automorphism representation can be a **proper** subgroup's,
and its FS type can differ (e.g. break complex type to trivial). Redundancy
can *break* symmetry; dually, gauge relabelings of identical copies add
kernel. So "the realization's automorphism rep" is not invariant.

**Repaired statement.** "The minimal quotient — hence Aut(K̄), its
representation on V̄₀, its commutant, its FS type, and the J-census — depends
only on the observational equivalence class of the theory." — **TRUE.**
[CONJ, sketch]
*Sketch.* The minimal quotient satisfies a universal property: it is the
unique (up to unique isomorphism of state/effect pairings) realization with
separating pairing generated by the images of S and E. Any two realizations
with the same observable behaviour have canonically isomorphic quotients;
the canonical isomorphism intertwines the two automorphism groups and their
representations; commutants, form-dimensions, FS type, and J-census
transport. ∎(sketch)

**Consequence.** FS type is an invariant of *observable behaviour* — but
only when computed where the theorem computes it: on the minimal quotient,
with the quotient's own symmetries. Computing it from a redundant
realization's symmetry group is not well-defined across realizations (the
counterexample), which is itself an operationally meaningful moral:
*redundant descriptions can hide the complex structure; the quotient is
where the theory's true symmetry lives.*

## 4. Canonicality (Task 3): the exact sense

±J is **forced by the operational data, coordinate-free**, in this exact
sense:

1. **No basis, no realization choice.** J is built as ω♯ (orientation form
   raised by the metric, normalized) — both inputs unique up to scale by
   (b), and both transport along the canonical isomorphism of §3. So J is
   not an artifact of any chosen realization. [CONJ]
2. **The pair {+J, −J} is absolutely canonical; the elements are not.** The
   two members are the two square roots of −1 in the commutant ≅ ℂ, i.e.
   the choice between them is the choice of ω's sign — the theory's two
   orientations. Under condition (b) every symmetry of the data *preserves*
   orientation (an orientation-reversing symmetry would send ω ↦ −ω,
   contradicting invariance unless ω = 0), so nothing inside the theory can
   prefer +J to −J. The ambiguity is exactly **complex conjugation**: the
   two complexifications (V̄₀, +J) and (V̄₀, −J) are conjugate-isomorphic,
   and no operational statement separates them. [CONJ; the QM analogue —
   i vs −i, conjugate representations, Wigner — is KNOWN]
3. **Refinement (± orbit).** If one weakens D4 to allow symmetries that
   conjugate J to −J (gJg⁻¹ ∈ {±J}), orientation-reversing symmetries are
   re-admitted; the index-≤2 orientation-preserving subgroup commutes with
   J and the theorem applies to it, with the outer elements acting
   antilinearly — the standard real-form-of-complex-type picture. Then the
   canonical object is the unordered pair even more explicitly. [KNOWN]

**Summary sentence.** Canonical = determined by the observable behaviour
alone, up to complex conjugation — precisely the freedom quantum theory
itself cannot remove.

## 5. Ledger

- KNOWN: GPT linearization; compactness of Aut(K̄); real Schur trichotomy;
  invariant-form counts for irreducibles (classical, translation checked by
  machine); conjugate-representation freedom in QM.
- CONJ (sketch-grade, ours): D3/D4 formalizations; the theorem's (a)⟺(b)⟺(c)
  with irreducibility derived; the trap analysis; the redundancy-breaks-
  symmetry counterexample; the universal-property repair; the canonicality
  analysis §4.
- NOT QUERIED: all literature contact. Before any novelty claim, check at
  minimum: Alfsen–Shultz orientation theory; Hardy 2001; Masanes–Müller;
  Barnum–Wilce; Wilce's "4.5 axioms" line; anything on "GPT + complex
  structure + symplectic/orientation."

## 6. Artifacts

- `invariant_forms.py` — invariant sym/antisym form census, 9 cases incl.
  both traps; pure stdlib. Output: `invariant_forms_table.txt` (verbatim).
- v1 artifacts (`complexification-note.md`, `fs_indicator.py`,
  `fs_table.txt`) retained; v1's Theorem A census reused in (a)⟹(c).
