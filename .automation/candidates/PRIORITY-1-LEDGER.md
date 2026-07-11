# Priority 1 — living taxonomy ledger   [non-canon · candidate · auto-appended]

*The "keep going" document for Priority 1 (the distinguishability form `D` / minimal observation-preserving
quotient). Computed examples (Claude-side, reproducible), the cross-model ladder, a QUEUE the automation works
through one item/cycle, and a ChatGPT-ASK-QUEUE (human-gated). Nothing promoted; Tier-3; canon read-only.*

## Cross-model frame (Claude ∥ ChatGPT, 2026-07-10)
The classical→quantum gap is a **LADDER, not a jump**:
`sharp partition → behavioural ultrametric → general pseudometric → convex/probabilistic (simplex) → linear →
positive (sesqui)linear form → complex Hilbert.` Computed examples have now **walked it to the frontier**:
- E1 gives the ultrametric; E3 breaks it into the **classical simplex (L1/TV)**; E4 shows the **quantum** step is
  the move to a **non-simplex complex body (Bloch ball, trace distance)**.
- E5 fills the **general/normed rung**: continuous (real) observation yields a genuinely continuous **weighted-L1**
  metric (additive, has midpoints, **not** an ultrametric) that is still **not Hilbert** (parallelogram law fails) —
  pinning that the jump to Hilbert needs a **positive quadratic form**, not merely a norm. The **Gramian half**
  then REACHES that rung classically: L2 read-out ⇒ `D²=(x−y)ᵀW(x−y)` (observability Gramian), parallelogram
  **holds**, ker `W` = unobservable subspace ⇒ **Kalman quotient** — a positive **real** form; only ℂ + the
  non-simplex body remain (= E4 frontier).
- **Frontier — now sharply located (E7):** the ℝ-vs-ℂ discriminator is **local tomography**, with a verified bounded
  witness (`ρ±`, Wootters count real 9<10 vs ℂ 16=16). What remains is the **full reconstruction** — the *minimal
  axiom set* forcing complex QM (local tomography **and** purification / continuous reversibility, per Hardy / CDP):
  a derivation / literature job, **not** a toy-example gap. (Local tomography rules out real-QM but is not, alone, all of it.)

## Examples computed (reproducible — `.automation/priority1/`)
| # | object | reading | verified result | rung / pole |
|---|---|---|---|---|
| **E1** | 5-state Moore machine | sharp + graded `D` | `5→3` minimal realization; graded `D` = **ultrametric** `{0,½,1}` | INTERIOR (N1/N2) |
| **E2** | 3-elt abstraction family | best-abstraction | best exists+unique **iff meet-closed**; else no best | **N3** (non-existence) |
| **E3** | 5-state labelled Markov chain | Kantorovich pseudometric | `½,½,1`; **not ultrametric**; `y`=convex midpoint; simplex `Δ({A,B})`, **L1/TV** | off-ultrametric → CONVEX (simplex) |
| **E4** | qubit vs classical bit | trace distance / decomposition | `I/2` has **two** pure decompositions (z vs x) ⇒ **not a simplex**; `T=1, 1/√2, 1/√2` (a sphere) | CRUX: **simplex → complex body** |
| **E5** | linear system `F=diag(λ)`, real read `O(s)=s`; + LTI `A=diag(.8,.5,.9,.3)`, `C=[1 1 0 0]` | discounted L1 metric + L2 observability-Gramian `D` | weighted **L1** on `R^n` (`w_i=1/(1−γλ_i)`); **continuum** of values, **additive** (midpoints), not ultrametric; parallelogram **fails** ⇒ not Hilbert. **Gramian half:** `W=[[25/9,5/3],[5/3,4/3]]⊕0` exact (Lyapunov + scipy + T=600 trajectory ≤1e-12); `D(αe₁,0)=5α/3`; ker `W`=unobservable subspace ⇒ minimal quotient `4→2` (Kalman); parallelogram **holds** (=74/9) ⇒ positive **real** bilinear form | continuous → **normed** (L1) → **positive REAL form** (L2; last rung before ℂ) |
| **E7** | two-rebit pair `ρ±=(I⊗I±σy⊗σy)/4` | local tomography (real-QM observables `{I,σx,σz}`) | valid real states (eig `{0,0,½,½}`); equal local marginals; **identical** under every real-local product (max diff `0`); globally distinct (`⟨σyσy⟩=±1`, `T=1`); Wootters count **real 9<10** (gap = σyσy dir) vs **ℂ 16=16** | **ℝ→ℂ step**: local tomography (standard discriminator) |
| **E8 (N3b)** | finite unary language `L={a,aa}` | minimal trace-equivalent realization, nondeterministic | minimal NFA size **3** (all 196 smaller NFAs exhausted, incl. multi-initial: 0 accept); of 4096 3-state NFAs exactly **6** accept `L`, in **3 non-isomorphic classes** (all trim) ⇒ minimal realization **NOT unique**. Witnesses: `A` = det chain `0→1→2, F={1,2}` vs `B` = nondet fork `0→{1,2}, 2→1, F={1}` — trace-equal, non-isomorphic, **not bisimilar**; determinize+minimize ⇒ **isomorphic** minimal DFAs (4-state) = Myhill–Nerode uniqueness restored. *Independently corroborated by a 2-symbol random search (`nfa_nonunique_min.py`): another certified pair of non-isomorphic 3-state minimal NFAs.* | **N3** (uniqueness half): canonical minimal quotient = property of the **equivalence** (bisim/determinism restore it; linear-time loses it) |

Scripts: `D_worked_example.py`, `N3_best_abstraction.py`, `LMC_behavioural_metric.py`, `qubit_vs_bit.py`, `continuous_observation_metric.py`, `continuous_graded_D_gramian.py`, `aggregation_L2_vs_L1.py`, `rebit_local_tomography.py`, `N3b_nonunique_minimal_nfa.py`, `nfa_nonunique_min.py`, `worked_example_pipeline.py`, `monoidal_composition_sketch.py`, `gbit_composite.py`, `chsh_tiers.py`, `ic_rac_game.py`.
**E4 exhibits the classical↔quantum contrast; it does NOT derive quantum** (that is the open reconstruction question).

**L2→inner-product rung — triple-corroborated (2026-07-10):** (i) observability-Gramian/Lyapunov (`continuous_graded_D_gramian.py`); (ii) diagonal closed-form + polarization recovering `⟨u,v⟩_Q` (`aggregation_L2_vs_L1.py`: L2 ⇒ parallelogram **holds** 5.6471=5.6471; L1 ⇒ **fails** 19.86≠10.17); (iii) a **live ChatGPT round** that independently proposed the same L1→L2 experiment and named **Jordan–von Neumann** (a norm is inner-product iff the parallelogram law holds). Decomposition `behavior→metric→norm→inner-product(J–vN)→complex-Hilbert→quantum`; the reconstruction gap begins **after** the inner-product step.

## QUEUE — Claude-side, one item/cycle (BOUNDED; do not invent endless items)
✔ **DONE Priority-2 write-up** (2026-07-10) — `candidates/PRIORITY-2-EXISTENCE-PROBLEM-2026-07-10.md`: existence = meet-closure (E2); uniqueness = the *equivalence*, not the size (E8); degeneracy = N1/N2 (E1); geometry = the aggregation ladder (E1→E7, E4). Anchored to E1–E8; nothing proved beyond the computed witnesses.

**QUEUE EMPTY → TAXONOMY COMPLETE (2026-07-10).** Per the agreed cap the auto-loop **PAUSES generation** — no new toy examples. Open frontier = quantum reconstruction (Hardy/CDP): the full complex-QM axiom set, human/literature work.
✔ **DONE E8/N3b** (2026-07-10) — non-uniqueness computed exhaustively: `L={a,aa}` minimal NFA size 3 (196 smaller exhausted); 3 non-isomorphic minimal classes; det-chain vs nondet-fork trace-equal but not bisimilar; minimal DFA unique ⇒ uniqueness lives in the equivalence, not the size. *(Independently corroborated by a 2-symbol random-search script `nfa_nonunique_min.py`.)*
✔ **DONE E5** (2026-07-10, BOTH halves) — continuous-observation variant: weighted-L1 (normed, not Hilbert) + Gramian L2 (positive real form, Kalman quotient `4→2`).
✔ **DONE E7** (2026-07-10) — rebit local-tomography witness `ρ±`: real-local statistics identical, globally distinct (`T=1`); Wootters count real 9<10 vs ℂ 16=16. Local tomography = the standard ℝ-vs-ℂ discriminator (E4-support; does NOT alone derive ℂ).
**When this QUEUE is empty → TAXONOMY COMPLETE.** The auto-loop then **PAUSES generation** and records:
"open frontier = quantum r
## ChatGPT-ASK-QUEUE (human-gated; one per cycle)
- ✔ **POSTED + ANSWERED 2026-07-11** (steward Chrome was live): positivity-substitutes-for-compactness (a)(b)(c) — **confirmed, attack surface 1 CLOSED**; + literature kill-list for novelty candidates (i)–(iv). Integrated → `PRIORITY-5-COMPLEXIFICATION-STEP1-CLOSURE-2026-07-11.md`.
- **STAGED (next cycle):** "Confirm the full form-count trichotomy under hypothesis X: (sym,antisym)-dims (1,0)/(1,1)/(1,3) ⟺ FS real/complex/quaternionic — so 'antisym-dim=1' is exactly the complex-case selector. Subtlety check: when D is used to identify V≅V*, do antisym form-counts translate correctly into the commutant's unitary structure (ℂ vs ℍ), and is (1,3) the right quaternionic count in the *bare-GPT* reading? Ultracode Round-4 census will run the same claim numerically — flag any group where the census could mislead."

## NEXT-PRIORITIES (ranked discussion for the steward — DECIDES NOTHING)
1. **Full-text literature audit vs the kill-list** (Moretti–Oppio; Alfsen–Shultz; Müller SciPost; + the mandated contact: Hardy, Masanes–Müller, Barnum–Wilce) — *lead: steward (full-text reading) + ChatGPT (audit runner)*. Both models: highest expected value; MANDATORY before any novelty claim or write-up.
2. **Trichotomy completion + two-layer write-up skeleton** (algebraic theorem: forms ⟺ ±J; then quantum interpretation: geometric phase, λω measurability hierarchy) — *lead: Cowork + ultracode (Round-4 census)*. Ready once 1 clears; skeleton can be drafted register-honestly in parallel.
3. **Composition/tensor extension** — does local tomography force one GLOBAL consistent J across composites (±J ambiguity under ⊗)? — *lead: ultracode + Cowork*. Untouched; natural successor theorem.
4. **Bare-GPT static loop observable for ω** — *PARKED* (cross-model verdict: statically impossible — prepare–measure data has no antisymmetric part; the dynamical Hessian under continuous reversibility IS the answer). Revisit only if the audit surfaces a static route.
orces ℂ over ℝ?
  → **ChatGPT verdict (live, 2026-07-10):** correct + correctly located; L1 = a *choice of aggregation*
  ("distinguishability inherits the aggregation's geometry"); "normed → inner product" is a **separate** rung
  (**Jordan–von Neumann**), **below** reconstruction; next layer = **real-vs-ℂ / local tomography / purification**
  ⇒ cross-model backing for the **rebit witness** (QUEUE #2). Still open: is L2 aggregation *principled* (Fisher / capacity)?
  → **ChatGPT verdict on principled-L2 + rebit (live, 2026-07-10):** L2 is *principled but NOT uniquely forced by the
  dynamics* — the recursion doesn't force Euclidean, the **aggregation** does; strongest **internal** justification =
  the **observability Gramian** (quadratic form = the energy to distinguish trajectories); otherwise quadratic is
  canonical only once you accept a quadratic-energy / Gaussian-noise principle (no general theorem forces it). Rebit:
  **confirmed the correct bounded witness**, with narrower wording — "local tomography is the standard axiom separating
  ℂ- from ℝ-Hilbert QM in **many** reconstruction frameworks" (not "exactly forces ℂ"; also purification / continuous
  reversibility). Its proposed next step (K(AB) vs K(A)·K(B) count) = **already computed as E7**. ASK now closed.
- **PENDING (E8/N3b, 2026-07-10):** verified: `{a,aa}` has 3 non-isomorphic 3-state minimal NFAs (det chain vs
  proper-nondet fork), trace-equal yet **not bisimilar**; minimal DFA unique. Is the sharp standard statement
  "a canonical minimal realization exists iff one quotients by a bisimulation-type congruence (deterministic ⇒
  trace = bisim)" — with Kameda–Weiner / Arnold–Dicky–Nivat as the anchors for NFA minimal non-uniqueness — and
  should the Priority-2 write-up therefore cast **N3** as: *existence* generally OK, *uniqueness* = a property of
  the OBSERVATION equivalence (linear-time loses it, branching-time restores it)? *(human-gated)*

## Automation
Scheduled task **`priority-1-taxonomy`** (cron `0 */8 * * *`): each cycle takes the TOP QUEUE item, does the
Claude-side computation (reproducible), appends the result + a TRACES line, updates both queues, and stages the
next ChatGPT-ASK. **ChatGPT leg is human-gated.** When the QUEUE empties, it pauses generation (cap above). Every
result is a candidate; nothing promoted.

## Register / holds
Living taxonomy · non-canon · E1–E8 computed + reproducible; E4 reaches the **known frontier** (simplex vs
non-simplex complex body = quantum reconstruction, open); cross-model verdict = correct + known + the ladder
framing; nothing promoted/admitted · Tier-3 · canon read-only. Provenance: 2026-07-10; ChatGPT "Research Program
Assessment" https://chatgpt.com/c/6a4ffe2d-aa78-83ee-b6b1-de0d8defb14a.

**Status (2026-07-10): bounded example-taxonomy COMPLETE (E1–E8) + Priority-2 write-up filed. Auto-loop PAUSED at the
agreed cap; open frontier = quantum reconstruction (human/literature). Remaining ChatGPT-ASKs are cross-checks only
(human-gated), not new generation.**

**Priority-4 (ChatGPT-recommended) DONE (2026-07-10):** one LTI system carried end-to-end
(`candidates/PRIORITY-4-WORKED-EXAMPLE-2026-07-10.md`, `worked_example_pipeline.py`) — ties `I(C,O,Rep,P)` (Markov
invariant) to the `(S,F,O)` Kalman quotient and to `D` (observability Gramian; ker = unobservable subspace). Next per
ChatGPT = **Priority 5 (quantum reconstruction): literature / derivation**, scoped in `candidates/PRIORITY-5-RECONSTRUCTION-SCOPE-2026-07-10.md`.
