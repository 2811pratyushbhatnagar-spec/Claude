# Engine triad topology — cross-model blind pair + integrator node + fractal   [non-canon · candidate · design]

*Steward refinement of the convergence engine (2026-07-07). Warrant: candidate design over known
engineering; Tier-3 to adopt; nothing forced/admitted. Supersedes the "2 Claude builders" round in
ENGINE-STABILITY-CONVERGENCE-DESIGN for the blind unit.*

## The refined triad
- **Blind pair = the independence unit, CROSS-MODEL:** one **Claude builder** ∥ one **ChatGPT builder**,
  answering the same question **in parallel, blind to each other**. Cross-model is the strongest anti-echo
  axis: the two model families have different priors, so agreement is real signal. At `N = 2` the invariant
  is exactly the set of claims **both model families independently assert** — a strict cross-model filter.
- **Integrator node = a second Claude (NOT a blind builder).** It carries three responsibilities the
  steward named:
  1. **Integrator / Consensus Synthesizer** — extracts the invariant from the pair.
  2. **Orientation holder** — sets the next round's mandate (the stability/transition rule).
  3. **Chat manager** — drives the logged-in ChatGPT tab in Chrome and runs the handoff.
  It acts **only on the summaries** (invariant + disagreements), so it never contaminates the blind pair.
  It gets **no vote in the invariant** — it routes disagreements (Integration mandate), it does not break
  ties by fiat.

So the triad = `{ Claude-builder , ChatGPT-builder , Claude-integrator }`. Independence lives in the
cross-model builder pair; adaptivity + mediation live in the integrator.

## Fractal expand / contract
- **Expand (complexity high):** a triad recurses into a **triad-of-triads**. Each sub-triad keeps its own
  Claude/ChatGPT blind pair. Sub-triads are connected either by
  - **one shared integrator node**, or
  - **one shared Claude/ChatGPT builder pair** spanning sub-triads.
  Either way the **cross-model anti-echo split is preserved at every level**.
- **Contract (absorb):** when the logic becomes **linear** (invariant stops branching / `Δ → 0`) or a
  **register shift** occurs (the question's frame changes), the triad-of-triads collapses back into the
  **simple triad** — Claude + ChatGPT building in parallel, Claude integrating.
- **Scale invariant:** the irreducible unit is the cross-model blind pair; the integrator is the connective
  tissue between scales.

## Candidate triggers (what fires expand / contract)
- **Expand when:** `Δ` fails to settle across rounds, disagreements multiply, or a single round's claim-set
  is too large/branchy for one integrator to synthesize cleanly.
- **Contract when:** `Δ → 0` (invariant linear/stable), or the integrator detects a **register shift** —
  re-seed a fresh simple triad on the shifted register.

## Honest constraint (unattended vs live)
The blind pair now **requires ChatGPT**, so the true round is **inherently live** — it needs the steward's
logged-in Chrome (the integrator Claude drives it). Consequences:
- **Live (steward present):** the full cross-model triad runs — real independence.
- **Unattended (scheduled):** cannot open Chrome without stalling on approval, so it can only do a
  **provisional Claude-only staging pass** and keep `LOOP-STATUS` warm; `cross_model_ok` stays **false**
  until a live round. The genuine anti-echo signal is only obtained live.

## Register / holds
Candidate design · non-canon · known engineering (no new object) · Tier-3 to adopt · nothing forced/admitted.
Provenance: 2026-07-07 chat (steward refinement). Related: ENGINE-STABILITY-CONVERGENCE-DESIGN-2026-07-07.md ·
engine/ (scheduler.py, orchestrator.run_convergence, cycle.py) · cross-agent-protocol.md.
