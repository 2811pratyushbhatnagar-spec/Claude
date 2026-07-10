# Canonical Complex Structures on Observational Quotients — Candidate Note

**Register:** NON-CANON · Tier-3 · nothing promoted · canon read-only.
**Venue note:** task contract specified the local Windows repo (`status.json`
source of truth); executed instead in the remote container clone under
`.automation/` — no `status.json` exists here, so nothing was updated; this
note is the only state. All banding below marks **[KNOWN]** (textbook /
literature) vs **[CONJ]** (this note's constructions and packagings;
proof-sketch temperature, not referee-checked).

---

## 0. Agreed background (restated, one line each)

- "Take J with J² = −I and complexify" is trivial: a real space with such a J
  *is* a complex space (i := J). Content must live upstream. [KNOWN]
- Real question: when does the observational-equivalence quotient of a real
  operational theory carry a **canonical** J? [task]
- With a symmetry group present, this is Schur/Frobenius–Schur (real commutant
  ∈ {ℝ, ℂ, ℍ}) and Kähler/Marsden–Weinstein territory. [KNOWN]
- Crux (ChatGPT): FS is a theorem about *group* representations; the quotient
  question assumes *no* group. Does canonical complexification always import a
  U(1)/group (collapse), or is there a group-free theory whose quotient
  complexifies (genuinely new)? [task]

## 1. Formalization (Task 1)

**D1 (Real GPT).** A real ordered vector space V (finite-dimensional here),
state cone C ⊂ V generating, order unit u ∈ V* strictly positive on C∖{0};
normalized states K = {ω ∈ C : u(ω) = 1} compact convex; effects
E = {e ∈ V* : 0 ≤ e ≤ u on C}. [KNOWN — standard GPT]

**D2 (Observational quotient / minimal realization).** ω₁ ∼ ω₂ iff
e(ω₁) = e(ω₂) for all e ∈ E; dually for effects. Quotient V̄ = V/N,
N = {v : e(v) = 0 ∀e ∈ span E}. On V̄ the state–effect pairing is separating.
Write V̄ = ℝ·(barycenter direction) ⊕ V̄₀ with V̄₀ the traceless part (the
linear span of differences of normalized states). [KNOWN — standard]

**D3 (Symmetries).** G := Aut(K) = affine bijections of K, identified (after
fixing the barycenter as origin) with a **compact** subgroup of GL(V̄₀):
it is bounded (preserves a bounded open body) and closed. [KNOWN — John-ellipsoid
argument]

**D4 (Canonical J — invariance reading).** A complex structure on the quotient
is J ∈ GL(V̄₀), J² = −I. Since anything *definable from the operational data
alone* is fixed by every automorphism of the data, "canonical" is formalized
as: J lies in the commutant G′ = {X : Xg = gX ∀g ∈ G}, and the theory
determines it **up to sign**, i.e. {X ∈ G′ : X² = −I} = {+J, −J}. [CONJ —
this note's formalization choice; the definability⇒invariance step is standard]

**D5 (Compatible J — dynamical reading).** J is *dynamically compatible* if
additionally e^{tJ} ∈ Aut(K) for all t — the complex phases are physical
reversible dynamics. (This is the Alfsen–Shultz "orientation / dynamical
correspondence" flavor.) [KNOWN frame, CONJ packaging]

## 2. Results (Tasks 2–3)

**Theorem A (canonicity collapses to Frobenius–Schur — for the theory's own
automorphism group).** [CONJ packaging; each ingredient KNOWN]
Let (V̄, K, u) be a minimal realization, G = Aut(K), acting on V̄₀. Then the
quotient carries a canonical complex structure (D4) **iff** V̄₀ is a
G-irreducible real representation of **complex Frobenius–Schur type**
(real commutant ≅ ℂ; for finite/compact G equivalently ν(χ) = 0 on the
corresponding complex irrep).

*Sketch (⟸).* Commutant ≅ ℂ = {a + bJ₀}: solving (a+bJ₀)² = −I forces a = 0,
b = ±1 — exactly {±J₀}. [KNOWN — real Schur lemma]

*Sketch (⟹).* Any canonical J lies in G′ (D4). G compact ⟹ G′ ≅ ⊕ᵢ Mat(mᵢ, Dᵢ),
Dᵢ ∈ {ℝ, ℂ, ℍ}. Census of solutions of X² = −I: Mat(m,ℝ) — none for m odd,
infinitely many for m even; Mat(m,ℂ) — infinitely many for m ≥ 2 (conjugates
of diag(i,−i,…) plus ±iI); ℍ — a 2-sphere {ai+bj+ck : a²+b²+c² = 1};
direct sums — a product of censuses, so two ℂ-summands already give four J's
(two unordered pairs, no canonical selection). The count is exactly 2 iff
G′ ≅ ℂ, i.e. V̄₀ irreducible of complex type. ∎ [CONJ — elementary but ours]

*Remark 1 (± refinement).* If reflections act, "canonical" may only mean
g J g⁻¹ ∈ {±J}; then the index-≤2 subgroup G⁺ commutes with J and Theorem A
applies to G⁺, with the outer elements acting antilinearly — the standard
real-form-of-complex-type picture. [KNOWN]

*Remark 2 (weaker canonicity).* If one accepts "canonical up to inner
symmetry of the commutant," complex-type isotypic components with multiplicity
also qualify via the center of Mat(m,ℂ) (central J's = {±iI}). The strict
reading in D4 pins Theorem A as stated. [CONJ note]

**Theorem B (dynamical reading ⟺ literal U(1)).** [CONJ packaging]
J is dynamically compatible (D5) iff {e^{tJ}} is a U(1) subgroup of Aut(K)
acting on V̄₀ with all weights ±1 (single-speed rotation). In particular
D5 ⟹ U(1) ≤ Aut(K) *by construction* — the dynamical reading collapses to a
group **trivially**, and single-weight U(1) invariance plus irreducibility
recovers the FS-complex case. Conversely a U(1) ≤ Aut(K) with multi-weight
action has skew generator A with A² ≠ −I; the polar part J = A(−A²)^{−1/2}
satisfies J² = −I and commutes with the U(1) but need **not** preserve K —
multi-weight U(1)s do not automatically hand you a compatible J. [CONJ]

**Proposition C (the two readings separate — smallest witness).** [CONJ —
construction ours; ingredients elementary]
Take K ⊂ ℝ² = V̄₀: the convex hull of the six points at polar coordinates
(1, 0°), (0.8, 40°) and their rotations by ±120°. Then:
- Aut(K) = ℤ₃ exactly (the two vertex orbits have distinct radii, so no
  reflection can preserve K; only the 120° rotations survive);
- V̄₀ = ℝ² is ℤ₃-irreducible of complex type (rotation by 120°; ν = 0 — see
  the Z3 row of the script's table), so by Theorem A the theory carries a
  **canonical ±J** (the 90° rotation, up to sign);
- yet e^{tJ} ∉ Aut(K) for generic t: there is **no U(1) of dynamics**.
So: canonical complexification **without** any continuous group — but not
group-free: the finite intrinsic group ℤ₃ does all the work.

**Verdict line for the crux (Task 3).** The genuinely-new branch is **empty
under the invariance reading**: if Aut(K) is trivial, the commutant is all of
End(V̄₀), the J-census is either empty (dim V̄₀ odd) or a large homogeneous
space (dim even) — never a canonical pair. Canonicity *requires* a nontrivial
intrinsic symmetry group, and then Theorem A says the answer is exactly
Schur/FS for that group. What ChatGPT's crux got wrong — and this is the
sharpening, not a defeat — is the *size* of the imported group: canonical J
does **not** require a U(1). A finite cyclic group (ℤ₃ suffices, order 3, the
smallest nontrivial case) already forces a canonical complex structure. U(1)
is required precisely when you additionally demand that the complex phases be
*physical dynamics* (D5) — which is the Alfsen–Shultz/orientation content, and
Proposition C exhibits an operational theory realizing D4 without D5.

## 3. Mini-theorem with dictionary (Task 3, reduces-to-FS branch)

**Statement.** For a finite-dimensional real GPT with compact normalized state
space, TFAE:
1. the observational quotient carries a complex structure canonical up to sign;
2. V̄₀ is Aut(K)-irreducible of complex Frobenius–Schur type;
3. (finite/compact Aut(K)) the associated complex irrep has ν(χ) = 0.
And separately: the canonical J generates *physical* U(1) dynamics iff
Aut(K) ⊇ U(1) acting single-weight — strictly stronger (Prop. C).

| Framework side | FS / representation side |
|---|---|
| observational quotient V̄ | minimal faithful real rep space |
| traceless part V̄₀ | the rep of G = Aut(K) |
| canonical ±J exists | real commutant ≅ ℂ (complex type, ν = 0) |
| no J at all | real type ν = +1, odd multiplicity (commutant ℝ) |
| many J's, none canonical | quaternionic ν = −1 (ℍ, S² of J's) or reducible |
| J is physical dynamics | U(1) ≤ Aut(K), single weight (A–S orientation) |
| local tomography selects ℂ (cross-ref "E7") | same ℝ/ℂ/ℍ axis, composite-system route [KNOWN, cited] |

## 4. Known-vs-conjectural ledger

- Real Schur lemma, commutant trichotomy ℝ/ℂ/ℍ, FS indicator ↔ type: **KNOWN**.
- Aut(K) compact; definable ⟹ invariant: **KNOWN** (standard arguments).
- D4/D5 as the two precise readings of "canonical/compatible": **CONJ (our
  formalization choice — the load-bearing move)**.
- Theorem A as stated (uniqueness-count argument over commutant algebras),
  Theorem B, Proposition C witness: **CONJ, proof-sketch grade**; no claim of
  novelty vs literature (Alfsen–Shultz and GPT-reconstruction literature not
  searched from this container — retrieval coverage: NOT QUERIED).
- Script results (Task 4): **exact finite computation**, output archived.

## 5. Artifacts

- `fs_indicator.py` — FS indicator + commutant + J-census, pure stdlib.
- `fs_table.txt` — verbatim output. Summary: Z₃/Z₄/Z₅ complex (ν=0, commutant
  ℂ, exactly ±J); D₄/D₅ real (ν=+1, commutant ℝ, no J); Q8 quaternionic
  (ν=−1, commutant ℍ, S² of J's — none canonical).
