# Priority 1 — the distinguishability form (first cut) + the "nothing" tool, cross-checked   [non-canon · candidate]

*Proceeding on the priority order. Part I records the cross-model verdict on the "identify the nothing of the
situation" heuristic (Claude ∥ ChatGPT, live). Part II is the first cut at Priority 1 — the distinguishability
form `D` — with the tool used operationally (never as metaphysics). Research draft; nothing proved; Tier-3; canon
read-only. Source: ChatGPT "Research Program Assessment" — https://chatgpt.com/c/6a4ffe2d-aa78-83ee-b6b1-de0d8defb14a*

## Part I — the "nothing" tool: cross-model verdict (both models agree)
- **Bounded form = a legitimate research habit.** "Identify the nothing of the situation" is the *unification* of
  the standard mathematician's move — examine the trivial / terminal / initial / zero / empty / universal object.
  It reframes the question from "what is the answer?" to **"what exactly has become trivial / vanished here?"**,
  which reliably **exposes hidden assumptions**. It is *one strong heuristic among several* — "strong enough to be
  useful, weak enough to be true in many settings."
- **Universal form overclaims.** "The answer to *any* question comes from asking about nothing" does **not** survive
  contact with mathematics — much progress comes from *constructing richer examples / structure*, not from the null
  case. Keep the universal slogan out of the load-bearing layer.
- **Operational protocol (strip the "nothing" language).** For any proposed object `X`:
  1. **What is the object?** State it precisely enough that success and failure are recognizable.
  2. **When does it vanish?** Identify the smallest / trivial / degenerate / null instance — does it become empty,
     unique, constant, or undefined? *(There may be several distinct such poles; separating them is the payoff.)*
  3. **What does the vanishing expose?** Which assumption was doing the work; where the real (non-degenerate)
     regime is.
- **Register:** a *notebook compass / research protocol*, applied **after** the object is stated, never as
  motivation or metaphysics. This is the same discipline as the koan verdict — usable, bounded, non-mystical.

## Part II — Priority 1: the distinguishability form `D` (first cut)
**Setup.** Given `(S, F, O)` — states `S`, recursive update `F: S→S` (extend to histories `H` as needed),
observation map `O: S→Obs`. The **distinguishability form** `D(x,y)` measures how distinguishable two states are
under observation-along-`F`-trajectories.

**Candidate axioms (weakest object — to be tested, not asserted).**
- `D: S×S → V` for a value domain `V` — `{0,1}` (sharp/classical), `[0,∞)` (pseudometric), or a positive form (graded).
- `D(x,x) = 0` (a state is indistinguishable from itself).
- `D(x,y) = D(y,x)` (symmetry — *droppable* if observation is directional).
- **O-sensitivity:** `O(x) ≠ O(y) ⇒ D(x,y) > 0` (observations distinguish).
- **F-compatibility (the dynamic clause):** `D` is the least/greatest fixed point of *"distinguishable now via `O`,
  or after one `F`-step"* — i.e. `D(x,y)=0 ⟺ O(x)=O(y) ∧ D(Fx,Fy)=0` (observational bisimulation). The **sharp**
  version gives the minimal-realization partition `S/{D=0}`; the **graded** version replaces the boolean by a form.

**Run the tool — "when does `D` vanish?" — three *distinct* nothings (the productive result of the test):**
- **N1 — trivial observation (`O` constant):** `D ≡ 0`; every state observationally identical, **but `F` still
  exists.** So *dynamics and observation have already separated.* The cleanest "nothing" of the observation itself,
  and a genuine insight: it isolates pure dynamics with no observable, and shows a nontrivial `O` is required for
  content.
- **N2 — total discreteness (`D>0` for all `x≠y`):** the quotient is `S`; no reduction. The dual "everything" pole.
- **N3 — nonexistent quotient (structural obstruction):** *not* "all states identical," but **no minimal object
  satisfies the preservation requirements.** This is `non-existence-of-I is real`, and it is a *different* nothing
  from N1/N2.

**Payoff of the test.** The tool did *not* return one "nothing" — it returned **three structurally different ones**
(constant-`O` collapse · full discreteness · nonexistence-obstruction). Distinguishing them is exactly the honest
version of "failure modes" — concrete boundary cases surfaced by protocol, **not** the asserted "exactly three"
decomposition (which stays shelved per the register corrections). The **interior** between N1 and N2 — where `D`
takes intermediate values — is where the real object lives (matches "vacuous at the extremes, open in the interior").

**The crux (Priority 1's open question, = the physics seam).** In the interior, what axioms on `D` and `F`
(coherent recursive persistence + reversibility) — if any — **force** the graded `D` to be a **complex inner
product**, as opposed to real / quaternionic / a general convex effect algebra? That is the CDP/Hardy reconstruction
target, now posed concretely on `D`. **Drop "quantum" until this is a clean statement** — first characterize `D`
and its degenerate poles; the forcing question comes later (Priority 5).

**Immediate next steps (inside Priority 1).**
1. Pin the value domain `V` and whether the F-clause is lfp (inductive) or gfp (coinductive) — expect *both*
   readings (inductive = "distinguishable within finite horizon"; coinductive = "bisimilar forever").
2. Work one tiny concrete `(S,F,O)` end-to-end (Priority 4, brought forward as the test case): compute `D`, its
   partition, and which of N1/N2/N3 occur.
3. Only then ask the forcing question.

## Register / holds
Research draft · non-canon · the tool = bounded heuristic/protocol (cross-model), universal form overclaims · the
`D` axioms are *candidates to test*, nothing proved · "quantum" deferred to a clean statement · nothing
promoted/admitted · Tier-3 · canon read-only. Provenance: 2026-07-10 cross-model pass (Claude integrator ∥ ChatGPT
live in Chrome). Source: ChatGPT "Research Program Assessment" (URL above).
