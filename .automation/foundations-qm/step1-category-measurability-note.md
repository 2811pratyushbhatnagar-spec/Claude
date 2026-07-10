# Step-1 Lemma, Categorical Linking, ω-Measurability, Literature Contact — Note v3

**Register:** NON-CANON · Tier-3 · nothing promoted · canon read-only.
**Banding:** [KNOWN] textbook/standard · [CONJ] ours, sketch-grade ·
[LIT-CONTACTED] verified against live web search this session (titles/abstracts
level — **full texts not read**; coverage, not existence).

---

## 1. Step-1 lemma — PROVED (with the compactness boundary exhibited)

**Lemma.** G compact, ρ : G → GL(V) real finite-dimensional. Then
dim{invariant symmetric bilinear forms} = 1 **iff** V is irreducible.
Equivalently: **every reducible real rep of a compact group has a ≥2-dimensional
space of invariant symmetric forms.** No "accidental uniqueness" exists.

*Proof.* Averaging gives an invariant inner product ⟨,⟩ [KNOWN]. (⟹, contrapositive):
if V is reducible, pick a proper nonzero invariant W; its orthogonal complement is
invariant [KNOWN complete reducibility], and the orthogonal projection P_W is
self-adjoint and commutes with every ρ(g). Then ⟨x, y⟩ and ⟨P_W x, P_W y⟩ are two
linearly independent invariant symmetric forms (W ≠ 0, V). This single argument
subsumes both requested cases (sums of inequivalent irreps; multiplicities) —
no case analysis needed. (⟸): invariant forms ≅ commutant via B(x,y) = ⟨x,Ty⟩,
symmetric ⟺ T self-adjoint; for irreducible V the commutant is ℝ, ℂ, or ℍ
[KNOWN Schur], and its self-adjoint part is ℝ·I in all three cases — for ℂ and ℍ
the positive involution is conjugation (a self-adjoint J with J² = −I would
violate positivity of J*J), so the fixed part is ℝ. Hence dim = 1. ∎ [CONJ
packaging; every ingredient KNOWN]

**Compactness is load-bearing.** Counterexample for non-compact G: the unipotent
flow t ↦ [[1,t],[0,1]] on ℝ². Reducible-indecomposable (unique invariant line, no
complement), yet its invariant symmetric forms are exactly ℝ·(x₂y₂ ⊗) — dimension
1. Machine-checked (`step1_and_omega.py`, section A: sym-dim 1, reducible). Note
the unique form is degenerate; requiring a positive-definite representative
(as our operational metric does) excludes it — but averaging, hence the whole
lemma, is unavailable without compactness anyway. In our theorem Aut(K̄) is
compact from hypothesis X, so the lemma applies. Battery: 7 compact cases all
consistent (irreducibles → 1; every reducible → 2, 3, or 4).

## 2. Categorical rigor of the linking lemma — PROVED (terminality)

**The category.** Fix a behaviour β = (S, E, p). Define **R(β)**: objects are
*state-generated realizations* (V, σ, ε): V a finite-dimensional real vector
space, σ : S → V with V = span σ(S), ε : E → V*, reproducing the table
(⟨ε(e), σ(s)⟩ = p(s, e)) and preserving mixtures. Morphisms (V,σ,ε) → (V′,σ′,ε′):
linear φ : V → V′ with φ∘σ = σ′ and φ*∘ε′ = ε (states pushed, effects pulled;
the table is then preserved automatically). [CONJ formalization]

**Theorem (terminality).** The minimal realization M(β) — V̄ = span{p(s,·)} ⊆
ℝ^E, σ̄(s) = p(s,·), ε̄(e) = ev_e — is the **terminal object** of R(β).
*Sketch.* For any object, φ(v) := ⟨ε(·), v⟩ defines a morphism to M(β)
(well-defined into V̄ because V is state-generated); any morphism must send
σ(s) ↦ σ̄(s), which determines it on span σ(S) = V, so it is unique. ∎ [CONJ]

**Corollaries (what "functorial enough" means, precisely).**
1. Terminal objects are unique up to *unique* isomorphism, so any two
   realizations have canonically isomorphic quotients [KNOWN category theory].
2. M is invariant under behaviour equivalence: M(β) depends only on the
   quotient behaviour β̄ (indistinguishability classes), since span{p(s,·)}
   sees only classes. Behaviour isomorphisms β̄₁ ≅ β̄₂ induce pairing
   isomorphisms M(β₁) ≅ M(β₂), compatibly with composition (a functor from the
   groupoid of quotient behaviours to the groupoid of separating pairings). [CONJ]
3. Hence Sym(β̄) ≅ Aut(M(β)) canonically, and everything downstream —
   the representation on V̄₀, its commutant, the invariant-form counts
   (sym, antisym), the FS type, the J-census — transports along the unique
   isomorphism: they are **invariants of observable behaviour**. This is the
   precise repaired linking lemma. [CONJ]
4. The v2 counterexample is now located exactly: doubling a state's *label*
   changes β (not the realization within R(β)), and Sym(β) ⊊ Sym(β̄) —
   symmetry breaking lives at the labelled-behaviour level; the quotient
   functor erases it. Groupoid-level functoriality (isos) is what holds and
   is all the lemma needs; M is *not* claimed functorial for arbitrary
   behaviour morphisms with effect-side contravariance subtleties — flagged
   out of scope. [CONJ, honest boundary]

## 3. Measurability of ω — DISPROVED AS STATED; sharp partial truths survive

**ChatGPT's target:** "ω is exactly the unique antisymmetric component
recoverable from observable transition probabilities on two-parameter
interference families."

**Obstruction (why it fails as stated).** Prepare-and-measure statistics are
evaluations of the duality pairing V̄₀* × V̄₀ → ℝ. A sym/antisym decomposition
of two-argument data is defined only when both arguments live in the *same*
space — i.e., only after a state↔effect identification. The duality pairing
has **no intrinsic antisymmetric component**. [CONJ, elementary]

**What survives — three graded statements.**
**(3a) Uniqueness does real work (the positive core).** Equivariant
state→effect identifications L (L∘g = (g⁻¹)*∘L) correspond to invariant
bilinear forms; under the theorem's condition (b) these form exactly the
2-parameter family {a·m + b·ω}. Machine-checked (section B: dim = 2).
Consequence: **any** equivariant transition rule t(x, y) has antisymmetric
part = λω for some λ ∈ ℝ. So *whatever* static antisymmetry an interference
family exhibits, it is automatically ω-proportional — if you see any
antisymmetry at all, you have measured ω up to the allowed scale and sign. [CONJ]
**(3b) But λ can vanish — and in quantum theory it does.** QM's transition
probability |⟨ψ|φ⟩|² is symmetric; the physical identification is the
metric one (λ = 0), and ω is invisible in static prepare-measure tables.
So guaranteed static recoverability is FALSE, with QM itself as the failure
witness. [KNOWN fact, CONJ framing]
**(3c) Dynamical recovery (the guaranteed route, when available).** If the
theory possesses an *enactable* one-parameter reversible family with
symmetry-transparent generator (commuting with all data symmetries — under
condition (b) this forces generator ∝ J), then the second-order response of
transition probabilities, ∂²P/∂t∂θ at 0 for P(t,θ) = p(g_t s(θ), e_f),
tabulates ½·m(f, J ẋ) = ½·ω(f, ẋ): the observable Hessian of a genuine
two-parameter interference experiment *is* ω. Machine-checked (section C:
max deviation 3.6e−9 over tomographic effect directions). Availability of
this route is exactly the D5/dynamical reading — U(1) ⊆ Aut(K̄); the ℤ₃
pinwheel has canonical ω but **no** enactable flow, so for it ω is
definable-not-measurable-dynamically. The invariance/dynamics separation
reappears at the measurability level, consistently. [CONJ]
**(3d) Weakest sense (always available).** ω is *behaviour-definable*: average
any antisymmetric form over the compact Aut(K̄) (Haar projection onto the
1-dimensional invariant space, then normalize) — an explicit reconstruction
from the observable behaviour, using only symmetries of the data. [CONJ]

**Verdict line:** static antisymmetry, if present, is necessarily ω (3a); its
presence is not guaranteed — QM hides it (3b); dynamical interference
measures it whenever the complex structure is physically enacted (3c); and it
is always definable from behaviour (3d). ChatGPT's biconditional holds
precisely in the D5 regime and fails in general — the pinwheel and QM
bracket it from both sides.

## 4. Literature contact — [LIT-CONTACTED, titles/abstract level]

Live web search this session (arXiv/PNAS/SciPost surfaced; **full texts not
read from this container** — verdicts below are overlap assessments, not
defeat certificates):

- **Moretti–Oppio, arXiv:1611.09029** (+ quaternionic sequel 1709.x): from
  Poincaré symmetry on a *real Hilbert space*, the commutant classification
  of irreducible real von Neumann algebras yields a natural complex structure
  **"unique up to sign"** commuting with all observables. **This is our exact
  mechanism** (commutant trichotomy + symmetry ⟹ canonical ±J) in the
  Hilbert/vN setting with a specific continuous group. Heaviest overlap found.
- **Stueckelberg (1960)**: the ancestral J-commuting-with-observables
  complexification of real QM. [KNOWN lineage]
- **Alfsen–Shultz** (*State Spaces of Operator Algebras*; PNAS "Orientation in
  operator algebras"; Connes 1974): state space determines the Jordan product;
  the C*-product requires one extra datum, an **orientation** — the opposite
  algebra has identical order/norm. Their orientation/dynamical-correspondence
  = our D5 reading; the opposite-algebra ambiguity = our ±J-up-to-conjugation
  at the operator-algebra level. Spirit-level overlap: "complex = Jordan +
  orientation" is their headline.
- **GPT reconstructions** (Hardy 2001; Masanes–Müller 2011; Müller Les Houches
  notes 2011.01286; Barnum–Wilce): complex numbers enter via **Continuous
  Reversibility** — a literal continuous transitive dynamical group — i.e.,
  the D5 route. No (1,1) form-count criterion or invariance-route theorem
  surfaced in the search results.

**Honest downgrade.** The *mechanism* is established territory (Stueckelberg →
Alfsen–Shultz/Connes → Moretti–Oppio). Surviving residual-novelty candidates,
none defeated but none deeply searched: (i) the **bare-GPT operational
criterion** — unique metric + unique orientation form, with irreducibility
*derived* (§1); (ii) **finite-group sufficiency** and the pinwheel witness
separating invariance from dynamics (all found literature uses continuous
groups or dynamical axioms); (iii) the **two traps** showing both uniqueness
clauses necessary; (iv) the **measurability quantification** (§3: λω, QM as
λ = 0, D5 ⟺ guaranteed dynamical recovery). Next literature step if pursued:
read Moretti–Oppio §on uniqueness and A–S orientation chapters in full;
search "finite symmetry group" + "complex structure" + GPT specifically.

## 5. Ledger and artifacts

- KNOWN: averaging/complete reducibility; Schur trichotomy; positive
  involutions on ℂ, ℍ; terminal-object uniqueness; QM transition symmetry.
- CONJ (sketch-grade, ours): Lemma §1 packaging + unipotent boundary; category
  R(β), terminality, corollaries 2–4; the §3 obstruction, (3a)–(3d), and
  verdict; §4 overlap assessments.
- Artifacts: `step1_and_omega.py` + `step1_and_omega_table.txt` (verbatim
  output: battery A 8 rows, identification dim B, response Hessian C).
- Sources (titles/abstracts consulted):
  [Moretti–Oppio](https://arxiv.org/abs/1611.09029) ·
  [Alfsen–Shultz orientation, PNAS](https://www.pnas.org/doi/10.1073/pnas.95.12.6596) ·
  [A–S book](https://link.springer.com/chapter/10.1007/978-1-4612-0147-2_5) ·
  [Müller lecture notes](https://arxiv.org/abs/2011.01286) ·
  [SciPost version](https://scipost.org/SciPostPhysLectNotes.28) ·
  [Earman, "Why √−1?"](https://philsci-archive-dev.library.pitt.edu/23612/1/Why%20i%206.23.24.pdf)
