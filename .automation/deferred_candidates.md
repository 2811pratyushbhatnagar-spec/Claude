# Deferred design candidates — LOGGED, NOT BUILT (append-only)

*The stopping rule forbids admitting a UI/design change without an observed execution signal from
the pre-registered schema. Candidates here wait for their named reopen signal to land in
`.automation/execution_evidence.jsonl`. Recording is Class-D documentation; building is not.*

- CANDIDATE 2026-07-06 · **States-of-understanding interface + Challenge Queue** (ChatGPT/Pratyush) · status: DEFERRED, awaiting evidence

## States-of-understanding interface (full record)
Shift the human interface from "signatures" to STATES OF UNDERSTANDING — per object the reader
marks one of: **not-read · read · can-explain-in-own-words · understand-the-evidence ·
understand-what's-open · disagree-have-challenge · want-to-investigate.**
**NO "approve / believe / certify" among them.**

**Challenge Queue** beside the Question Board: each object shows open-questions / active-challenges /
successful-reproductions — shows where the pressure is; doesn't decide truth.

**Portable AI handoff** = {state graph, question graph, evidence graph, register/status metadata,
dependency graph}.

**One-liner:** "a research OS organized around questions, evidence, and understanding — not tasks,
opinions, or approvals."

## Sharpening (recorded with the candidate)
States-of-understanding applies to **READING**. The three Class-A ratifications — promote→theorem,
admit Ledger C, freeze — **STAY explicit named endorsements**. Dissolving them into "understand
enough to continue" would blur never-certify in the OTHER direction. Honest interface =
understanding-states everywhere, **endorsement only at the irreversible acts.**

## Reopen signals (what moves this candidate → build; nothing else does)
1. A **logged instance of signature→endorsement drift** in execution_evidence, OR
2. The minimal Mission-Control board **proving insufficient in real use** (logged, with the
   pre-registered observation-schema signal it instantiates — e.g. packet-sufficiency).
Until such a signal lands, this stays a deferred candidate — not built.
- CANDIDATE 2026-07-06 (re-classified) · **SPLIT by ChatGPT/Pratyush**: the DESIGN PRINCIPLE ("reader comprehension, not reader endorsement"; four disjoint objects; stranger test) is ACCEPTED as forward writing guidance -> READ-MODEL-AND-PACKAGING.md §3 (projection layer, not pinned, not retroactive). The UI IMPLEMENTATION (comprehension-checkpoint widgets, persistent receipts, challenge-queue counts as actual UI) REMAINS DEFERRED with the unchanged reopen signal (signature->endorsement drift instance OR Mission Control insufficient in real use).

- CANDIDATE 2026-07-06 · **Engineering frontier (ChatGPT's four + the three-service split)** · status: DEFERRED, awaiting observed need · reopen signal: RUNNING the system reveals which is needed first (logged in execution_evidence with its observation-schema signal)
  - (a) per-artifact fingerprinting + derivation caching / incremental compilation — refinement of the Stage-0 gate
  - (b) confidence-transition field in traces — small; follows the (confidence, warrant) pair
  - (c) structured disagreement objects / Challenge Queue as actual infrastructure — new infra
  - (d) epistemic-status propagation on the dependency graph — extends invalidation; the MECHANISM for the adopted (confidence, warrant) labeling
  - (e) THREE-SERVICE split: Evidence / Reasoning / Governance with mechanically-distinct write-authority — maps to the confidence/warrant setter-split
