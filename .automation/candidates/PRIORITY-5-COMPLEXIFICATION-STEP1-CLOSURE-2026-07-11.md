# Priority 5 — operational complexification theorem: Step-1 CLOSED (positivity ⇒ complete reducibility) + the literature kill-list   [non-canon · candidate]

*Heartbeat cycle 2026-07-11. Integrates the un-transcribed tail of the live ChatGPT thread (three exchanges from
2026-07-10 that post-date the last TRACES entry) + this cycle's POSTED-AND-ANSWERED confirmation. Three-leg status:
Cowork (this note) ∥ ChatGPT (live, confirmed) ∥ ultracode (Round 3 integrated; Round 4 staged). Nothing promoted;
Tier-3; canon read-only. Thread: chatgpt.com/c/6a4ffe2d-aa78-83ee-b6b1-de0d8defb14a.*

## Current theorem shape (cross-model agreed, 2026-07-10/11)
Operational hypotheses (hypothesis X) → **unique invariant distinguishability metric** (up to units) + **unique
invariant orientation form** (up to scale & sign) → **canonical complex structure ±J** (canonical up to complex
conjugation; J↔−J *is* i↔−i) → **Frobenius–Schur complex type** — with FS appearing as the *classification at the
end, not an assumption* (ChatGPT: "exactly the shape reconstruction theorems usually have"). Irreducibility is
**DERIVED**, not assumed; the linking lemma runs through the minimal realization as the **terminal object** in the
category of state-generated realizations of a fixed behaviour (universal property ⇒ Aut/commutant/form-counts/
FS-type/J-census are invariants of observable behaviour).

## Newly integrated from the thread (was NOT yet in the repo)
1. **ChatGPT two-pressure-point audit** (2026-07-10): (P1) sym-dim=1 ⇒ irreducible+multiplicity-one needed a real
   theorem, with reducible-indecomposable / non-semisimple reps the counterexample hunting ground; (P2) the
   orientation form ω was operationally unclosed. Linking-lemma repair (compute on the universal minimal quotient)
   endorsed; "canonical up to conjugation" endorsed as clean. **KNOWN-framing; P1 now closed (below); P2 resolved
   into a measurability hierarchy (below).**
2. **Geometric-phase round** (integrator ∥ ChatGPT): ω's quantum handle = the **Bargmann invariant / Pancharatnam
   geometric phase of three-state loops** (pairwise probs are symmetric, cannot see ω; the three-vertex loop phase =
   symplectic area; real QM has trivial Bargmann invariant). ChatGPT verdict: **correct inside complex QM; NOT a
   GPT operationalization** — the Bargmann invariant needs amplitudes, which bare GPTs lack; circularity threatens.
   Redirect adopted: **two-layer theorem** — algebraic core (forms ⟺ ±J), then geometric phase as the *quantum
   interpretation/application*, never a hypothesis. **KNOWN (in-QM part); the GPT loop-observable question stays open.**
3. **Ultracode Round 3** (integrated; converges with ChatGPT): (a) compact-G proof of sym-dim=1 ⟺ irreducible, with
   the **unipotent [[1,t],[0,1]] trap** showing compactness was load-bearing; (b) terminal-object linking lemma;
   (c) **dynamical answer to ω-measurability**: the mixed Hessian ∂²P/∂t∂θ of P(t,θ)=p(g_t s(θ), e_f) tabulates
   ½ω(f,ẋ) (verified 3.6e-9) — ω is always *definable* (Haar average), **not statically measurable** (prepare–measure
   data has no antisymmetric part; QM itself the witness), **dynamically measurable** under continuous reversibility;
   the pinwheel (canonical ω, no flow) separates invariance from dynamics *at the measurability level*. ChatGPT:
   provisional YES — a three-level split (existence of J / physical e^{tJ} / measurability of ω). **KNOWN vs CONJ:
   the Hessian identity is verified numerics + proof sketch (KNOWN-leaning, pending write-up); "= the standard GPT
   route to ℂ" is placement, not novelty.**
4. **Cross-model verdict on status**: the mathematical core (canonical J from commutant + orientation) **likely
   intersects Moretti–Oppio and Alfsen–Shultz** (titles/abstracts only — full texts NOT read). Residual novelty
   candidates: **(i)** bare-GPT (1,1) form-count criterion with irreducibility *derived*; **(ii)** finite-group
   sufficiency + pinwheel separation (literature emphasizes continuous groups); **(iii)** the explicit traps/failure
   taxonomy; **(iv)** the λω measurability quantification (QM-as-λ=0). One-sentence status (ChatGPT): *plausible
   operational reconstruction criterion whose mathematical core appears to intersect established representation
   theory; the remaining question is attribution, not correctness.* Next step (both models): **full-text literature
   audit before any write-up.** Side note, register-checked: complex structure = the *dimensionless/angle* sector
   (J = quarter-turn, phase mod 2π), metric = the *magnitude* sector — accurate as interpretive summary, NOT a
   foundational principle.

## THIS CYCLE'S CONFIRMATION — posted live and ANSWERED (2026-07-11)
**Ask:** does positivity substitute for compactness, closing Step-1's remaining hole with no added axiom?
**ChatGPT: YES — attack surface 1 essentially CLOSED**, with one wording fix:
- **(a) confirmed.** The compact proof only ever needed **complete reducibility**. Invariant positive-definite D ⇒
  every invariant subspace has an invariant D-orthogonal complement ⇒ completely reducible; then D_λ = D|W₁ ⊕ λD|W₂
  (λ>0) gives sym-dim ≥ 2 for any reducible rep. Hence under hypothesis X: **sym-dim = 1 ⟺ irreducible, no
  compactness assumption.**
- **(b) confirmed.** The unipotent trap is auto-excluded: every isometry of a positive-definite form is
  ℂ-diagonalizable with unit-circle eigenvalues; a nontrivial unipotent is not.
- **(c) wording tightened (adopt for write-up):** *"Because the representation preserves D, its image is already a
  subgroup of O(D). Since O(D) is compact, the representation is completely reducible."* (No closure talk unless
  averaging over the closure is later invoked.)
**Consequence:** the theorem's hypotheses as already stated (invariant distinguishability metric) supply the
semisimplicity; correctness risk has shifted **almost entirely to literature overlap**. — Marked **KNOWN**
(elementary, standard ingredients; cross-model confirmed; ultracode Round-4 machine-check staged).

## The literature KILL-LIST (audit protocol — falsifiable per candidate; ChatGPT, 2026-07-11)
| candidate | defeated IF full text contains | check first |
|---|---|---|
| (i) (1,1) form-count criterion | "canonical complex structure iff exactly one invariant symmetric + one invariant alternating form" | Moretti–Oppio uniqueness theorems; commutant=ℂ characterizations via invariant bilinear forms |
| (ii) finite-group sufficiency + pinwheel | "a finite automorphism group of complex type suffices for canonical J" / continuous one-parameter symmetry proved unnecessary | reconstruction papers' symmetry hypotheses — **most likely novel** (lit emphasizes continuous reversibility) |
| (iii) the traps taxonomy | explicit counterexamples: non-equivariant canonical J; J without uniqueness; multiplicity/reducibility failures | whether papers isolate failure modes or only prove the positive theorem |
| (iv) λω measurability hierarchy | "ω exists abstractly + static tomography cannot recover it + continuous reversible dynamics recover it infinitesimally" | orientation observability; Berry-curvature reconstruction; operational symplectic-form recovery — **easiest to accidentally rediscover** |

## KNOWN vs CONJ ledger (current)
- KNOWN: positivity ⇒ complete reducibility ⇒ (sym-dim=1 ⟺ irreducible) under hypothesis X; unipotent excluded;
  ±J ⟺ i↔−i; Bargmann/Pancharatnam = ω's in-QM handle; static non-measurability of ω; dynamical Hessian recovery
  under reversibility (numerics 3.6e-9 + sketch).
- CONJ / OPEN: novelty of (i)–(iv) (pending full-text audit); bare-GPT static loop observable for ω (cross-model:
  likely none — parked); composition/tensor extension (global J consistency, untouched); full trichotomy statement
  (1,0)/(1,1)/(1,3) ⟺ real/complex/quaternionic as the *operational* FS trichotomy (next confirmation staged).

## Register / holds
One confirmation posted + answered live (steward's Chrome was open) · Step-1 hole closed with hypotheses as stated ·
kill-list = the audit protocol; **full-text reading is steward work (human-gated)** · nothing promoted · Tier-3 ·
canon read-only. Provenance: 2026-07-11 heartbeat; ChatGPT thread above; ultracode Rounds 1–3 (as relayed in-thread);
Moretti–Oppio; Alfsen–Shultz; Stueckelberg; Müller (SciPost); Pancharatnam/Bargmann/Berry.
