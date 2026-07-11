# Round 5 — does J vs −J realize A–S's central projection? [non-canon · candidate]

*Two independent passes converged on the same negative result. First, Cowork ran a quick numerical falsification
in-session. Then ultracode (steward's machine, three-agent adversarial workflow: construction + Döring-fetch +
two refutation passes) ran the full staged task and went much further: not just "J-flip ≠ central-projection" but
"the pinwheel doesn't even land inside Alfsen–Shultz's domain." Recording both, ultracode's as the fuller result.*

## Pass 1 — Cowork numerical falsification (in-session, numpy, M₂(ℂ))
Naive hypothesis under test: **J ↔ pick "ab"**, **−J ↔ pick "ba"** (A–S's central projection c=0/1).
Checked exactly (seed-reproducible, `round5_check.py`): ψ_⋆ = −ψ confirmed (matches Döring's formula); complex
conjugation (J→−J relabeling) is a ring **automorphism** of Mₙ(ℂ) — order-preserving, does NOT swap ab/ba; transpose
and dagger/adjoint ARE anti-automorphisms (that's what actually reverses order); for self-adjoint a,b, (ab)\*=ba is
a *forced* identity, not a free choice. **Verdict: FALSIFIED** — {J,−J} is automorphism-level, {ab,ba} is
anti-automorphism-level; different structural levels. ChatGPT cross-check confirmed and recommended explicit
withdrawal (archived below).

## Pass 2 — ultracode Round 5 (steward's machine, three-agent adversarial workflow) — the fuller result
Commit `da0ad33` on `claude/understand-3yr-work-hvqr9n` (PR #1). Artifacts:
`.automation/foundations-qm/{round5-orientation-note.md, round5_orientation.py, round5_dyncorr_check.py,
round5_output.txt}`. Canon untouched. Workflow: three parallel verification agents (fetch Döring's actual text;
adversarially attack the rebit-obstruction proof; attack the state-space-classification/qubit-mismatch claims)
alongside a construction script in the main loop.

**VERDICT: the identification does NOT go through — same output TYPE (ℤ₂ conjugation torsor), provably NOT the
same invariant. The failure is structural: the pinwheel never enters Alfsen–Shultz's domain, and where A–S's ℤ₂ IS
nontrivial (the qubit), the pinwheel's form-criterion ℤ₂ is EMPTY. Disjoint supports in every case examined.**

**Task-by-task:**
1. **Construct + complexify.** Pinwheel Aut(K)=ℤ₃ confirmed by exhaustive sampling (720 candidate isometries; only
   0°/120°/240° survive); (sym,antisym)=(1,1); J=rot 90°, J²=−I, [J, rot 120°]=0, all exact. Complexifying (V̄₀,±J)≅ℂ±
   is fine.
2. **"Two candidate associative products" cannot even be constructed**, because Döring's machinery needs a Jordan
   algebra of observables first, and: (a) **the pinwheel body is not a JB state space** (Jordan/von-Neumann-Wigner
   classification: finitely many pure states forces a simplex; 6 extreme points would need Δ⁵, dimension 5≠2) —
   adversarially confirmed, no hole found; (b) the minimal Jordan completion via the canonical metric is the
   **rebit V₂** (real qubit).
3. **The c=0/1 test, on V₂: the A–S/Döring product set is EMPTY, not two-element** — proved two independent ways:
   (i) V₂ is not the self-adjoint part of any complex \*-algebra (semisimplicity via a Jacobson-radical/simple-
   Jordan-ideal argument, no positivity needed; ruled out an exotic-swap-involution loophole on ℂ³) → A–S's own
   characterization (sa-of-vN ⟺ dynamical correspondence exists) gives emptiness; (ii) a direct, A–S-free,
   machine-checked proof: der(V₂)=so(2) is 1-dimensional abelian (kernel dim 1, computed) while
   [L_{e₁},L_{e₂}] = the rotation generator ≠ 0 (computed exactly), so [ψ_a,ψ_b] = −[L_a,L_b] is **unsatisfiable** —
   a genuine Lie-algebraic obstruction, so(2) is too small. Real-algebra loophole also closed: V₂=Sym(M₂(ℝ)), but
   transpose is an isomorphism M₂(ℝ)→M₂(ℝ)^op fixing every observable (ab-vs-ba is pure gauge over ℝ); in M₂(ℂ)
   transpose acts on Hermitians as conjugation (σ_y↦−σ_y) — nontrivial — which is exactly why the *qubit's* ℤ₂ is
   real. Control verified on M₂(ℂ): shared Jordan part, product-swap ⟺ ψ↦−ψ ⟺ i↔−i, c∈{0,1} associative, c=½ is
   NOT (deviation 1.42).
4. **Where it breaks + the sharpening.** (i) the pinwheel misses A–S's framework entirely (not a Jordan state
   space); (ii) even the Jordan completion (rebit) has an EMPTY orientation set — a case Döring's classification
   never parametrizes (his theorem also explicitly excludes ℂ⊕ℂ and type I₂ on the vN side); (iii) **converse
   mismatch**: Bloch-ball automorphisms = O(3) exactly, invariant antisymmetric forms on ℝ³ have dimension 0
   (machine + parity) — yet the *qubit's* A–S ℤ₂ IS nontrivial, carried by the invariant antisymmetric product
   (cross product / su(2) bracket), unique up to scale under SO(3), sign-flipped by transpose.

**The corrected picture (the real payoff).** Our invariant is a **form-level ℤ₂** (lives on pinwheel-type,
non-Jordan theories). A–S's is a **bracket-level ℤ₂** (lives on Jordan/vN theories). Both instantiate one pattern —
"residual freedom = conjugation ℤ₂ on a 1-dimensional antisymmetric invariant" — on **different carriers**, with
**disjoint supports** in every case examined so far. Whether a common generalization exists (one invariant
restricting to ω here and the bracket there), and whether disjoint-supports is a theorem, are the **two genuinely
new open questions** — CONJ, not attempted.

**Coverage honesty (ultracode's own flag):** arXiv is 403-blocked from ultracode's container; Döring 1411.5558 was
reached at snippet level only — Def 3.2/Prop 3.4 wording and the A–S citation keys (4.2/6.18/7.103/7.100) are
UNVERIFIED at that level (the dynamical-correspondence definition and central-projection formula were
snippet-confirmed, matching what Cowork read at full-text level in the parallel pass above — cross-consistent).
Script's first draft over-attributed the emptiness claim to Döring; audited and corrected in-place by the adversarial
pass. Nothing promoted.

## ChatGPT cross-check (Cowork's numerical pass, 2026-07-11, live)
Confirmed the falsification sound: conjugation (automorphism) vs. transpose/dagger (anti-automorphisms) are
genuinely different operations; recommended explicit withdrawal. Archived: *"Withdrawn: canonical J and the
Alfsen–Shultz orientation are the same invariant."* Surviving question (before ultracode's deeper pass):
*"whether the existence of a canonical equivariant J can be characterized operationally under weaker hypotheses
than existing reconstruction theorems."* ChatGPT's meta-observation: third round in this program where a stronger
identification (compression↔local-tomography; J↔orientation; J↔central-projection) was proposed then deliberately
falsified under stress-test, each time leaving a smaller, cleaner residual — "exactly how a serious mathematical
program should evolve."

**Steward's question for ChatGPT on ultracode's fuller result (staged, not yet posted this round):** is there any
theory where the form-ℤ₂ and the bracket-ℤ₂ are simultaneously defined and nontrivial — or is disjointness a
theorem?

## ChatGPT cross-check on ultracode's fuller result (2026-07-11, live)
**Do not infer a theorem from the current evidence yet.** What's established: pinwheel lies outside A–S's hypotheses
(not a JB state space); the Jordan completion (rebit) doesn't recover A–S structure (empty orientation set); the two
carriers are different (form-data vs. bracket/associative-product data). What's NOT yet established: that the
supports are disjoint *in general* — three examples (non-Jordan pinwheel, its Jordan completion, the qubit) is an
informative sample, not a theorem. Four live possibilities going forward: (1) disjoint support (never simultaneously
nontrivial), (2) coincidence on overlap (agree when both exist), (3) independent invariants (vary independently),
(4) one refines the other. Recommended reframing: *"current evidence indicates the form-ℤ₂ and the A–S bracket-ℤ₂
are structurally distinct invariants with different domains of definition; whether they ever coexist nontrivially
remains an open classification problem"* — not "disjointness is the theorem." **Suggested next bounded computation**
(Round 6 candidate, not yet staged): take a theory KNOWN to satisfy A–S's hypotheses (finite-dim complex matrix
algebra / other simple Euclidean Jordan algebras / spin factors / quaternionic examples) and explicitly compute the
form-ℤ₂ invariant there. If nontrivial → disjointness is false. If forced to vanish for structural reasons → that's
the mechanism a real disjointness theorem would need.

## Status
Identification hypothesis **WITHDRAWN**, now on stronger footing (structural non-membership + Lie-algebraic
obstruction, not just a labeling mismatch). Two new open questions staged (common generalization; disjointness as
theorem) — CONJ, untouched, canon untouched, nothing promoted. Non-canon; Tier-3; canon read-only. Sources:
`round5_check.py` (Cowork, this session); ultracode commit `da0ad33` (PR#1,
`.automation/foundations-qm/round5-orientation-note.md`); Döring arXiv:1411.5558; chatgpt.com/c/6a4ffe2d.
