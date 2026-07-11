# Stability-convergence engine   [non-canon · candidate · procedures-only]

The multi-agent engine as a **feedback loop**: promote a conclusion only when the
**invariant across independent representations stops moving** — not after a fixed
number of stages. Design source:
`../candidates/ENGINE-STABILITY-CONVERGENCE-DESIGN-2026-07-07.md`.

## Two layers (why it does not echo)
- **Layer 1 — parallel blind round (anti-echo).** Every leg answers the same
  question **concurrently, blind to the others**. Independence lives here. The
  invariant = claims surviving **≥ N independent `(model, evidence_path)` paths**;
  two agents on the same path collapse to one (echo, enforced in code).
- **Layer 2 — self-driving adaptivity.** Between rounds the transition rule reads
  **only** the synthesised invariant + open disagreements (never the raw
  transcripts) and sets the next round's mandate (Refutation → Integration →
  Diversity). *The last round decides the next.* Stops on **stability**, not stages.

Sequential peeking (agent B reads agent A before answering) would create echo — so
adaptivity is confined to Layer 2, operating on de-echoed summaries only.

## Topology (the mediator design)
```
                         question
                            |
        +-------------------+-------------------+
        |                   |                   |
    claude_A            claude_B               gpt
   (mediator)          (Claude,             (ChatGPT,
   Claude,             counter-             literature)
   first-principles    example)                 ^
        |                                        | driven THROUGH
        |  holds Chrome  --> opens/relays ChatGPT +  claude_A's Chrome
        +--> Consensus Synthesizer  (rotates)  -->  Stability Monitor
```
**Refined triad (2026-07-07 — see `../candidates/ENGINE-TRIAD-TOPOLOGY-2026-07-07.md`):**
the blind independence unit is a **cross-model pair — one Claude builder ∥ one
ChatGPT builder** — built in parallel, blind. The **second Claude is the
integrator node**: Consensus Synthesizer + orientation-holder (next mandate) +
chat-manager (drives ChatGPT in Chrome). It does not build blindly and gets no
vote in the invariant; it acts only on the summaries, so it never contaminates the
pair. Under high complexity a triad may **recurse into a triad-of-triads** joined
by a shared integrator node or a shared Claude/ChatGPT pair (the cross-model split
preserved at every level); when the logic goes linear or the register shifts, it
**absorbs back** into the simple triad.

## The math
Representation = `(agent, model, evidence_path, mandate, claims)`. Independence is
counted over `(model, evidence_path)`. Invariant = claims asserted by ≥ N
independent paths, minus any contested claim (`X` and `not X` both present).
Stability = Jaccard distance between successive invariants; the loop stops when it
holds at ≤ τ and the invariant has ≥ N independent paths. **Confidence = survival
across independent representations** — not a scalar, not a stage count.

## Files
| file | role |
|---|---|
| `invariant.py` | Representation model · `extract_invariant` (N-path gate) · `stability` |
| `scheduler.py` | the transition rule: `next_mandate` (round-level) · `next_directive` |
| `orchestrator.py` | `run_convergence` — parallel-blind rounds + adaptive mandates |
| `agents.py` | `MockWorker` (offline) · `MailboxWorker` (live filesystem handoff) |
| `cycle.py` | one persisted cycle (a round) so the loop KEEPS RUNNING across firings |
| `run_demo.py` | offline proof: convergence + the anti-echo demonstration |
| `run_live.py` | live wiring of the mediator topology (needs Chrome) |
| `QUESTION.txt` | the question the running loop is currently chewing on |
| `runs/loop_state.json` | accumulated blind rounds (seeded from the live 2-Claude round) |
| `runs/LOOP-STATUS.md` | human-readable current invariant + open disagreements |

## Run
- **Offline (no models):** `python run_demo.py`.
- **The running loop (per cycle):**
  `python cycle.py --peek` → the mandate for the next round; gather that round's
  Claude legs **in one batch (blind, parallel)**; write `round.json`; then
  `python cycle.py --new round.json` recomputes the invariant + stability and
  reports the next mandate. State persists in `runs/loop_state.json`.

## Cross-model honesty
The two **Claude legs run unattended** → a provisional invariant (2 independent
paths, but **1 model**). The **ChatGPT leg adds the second model** and needs a
live logged-in Chrome, so `cross_model_ok` stays **false** until the steward runs
it. A scheduled cycle therefore produces a provisional invariant and **queues the
ChatGPT cross-model confirmation** for when you are present.

## Governance boundary
Procedures-only. Emits a **candidate** invariant + a trace. Never promotes to
canon, never edits Ledgers A–E, never adds ontology. `worker_guard.py` /
`WORKER-CONTRACT.md` still apply. **Adoption or wiring into the heartbeat is a
Tier-3 decision — the steward's alone.**

*Register: non-canon · candidate · nothing forced/admitted · Tier-3 to adopt.
Provenance: 2026-07-07 chat.*
