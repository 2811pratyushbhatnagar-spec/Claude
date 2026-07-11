# Read-Model & Packaging Principles — recorded 2026-07-06 (Class-D documentation; invariants at the public edge)

## 1. READ-MODEL INVARIANT
**The repository is authoritative; the interface AND any package are read-only PROJECTIONS of it.**
- Test (mechanical): deleting the UI or a package must leave governance unchanged. If any UI or
  package action changes governance state, the architecture has leaked — forbidden.
- Consequence: a package is a GENERATED, HASH-SIGNED rendering of a result's ACTUAL ratified
  status. It can only DISPLAY status — *proven finite n=2,3 · general open · Ledger C candidate ·
  verification pending · governance frozen* — never confer it. **"Clearly presented" is not a
  status; "ratified" is.** This extends the never-certify invariant to the public edge.
- Enforced: projections (SNAPSHOT, DECISIONS, EVIDENCE-RIVER, status.html, packages) are never
  manifest-pinned as governance and never appear in dependency declarations (test_consistency).

## 2. PACKAGING PRINCIPLE — activates ONLY when the mathematics produces a result (no empty shell)
The first package is **Result Package #001**, grounded in a RESULT (ideally the honest n=4 null):
*result + supporting computation + provenance + current framework state + reproduction instructions.*
The framework appears because it explains the result — not vice versa.
**First page answers exactly four questions** (the public analogue of the register discipline):
1. What is claimed?
2. What is NOT claimed?
3. What evidence supports it?
4. How to reproduce or challenge it?
A stranger meets the research artifact first, then discovers it is unusually reproducible because
of the governance underneath.

## 3. READER COMPREHENSION, NOT READER ENDORSEMENT — accepted design principle (2026-07-06)
*Forward writing guidance for future artifacts and packages. NOT retroactive — existing docs are
not rewritten to it (that would be deferred elaboration). Projection-layer guidance only; not
constitutional, not manifest-pinned.*

**Four disjoint objects; none ever substitutes for another:**
- **(a) Class-A signatures** change project state — the steward only (promote → theorem, admit
  Ledger C, freeze). These three stay explicit *named endorsements*: they genuinely certify.
- **(b) Evidence** changes what is known — computation, audits, reproductions.
- **(c) Registers** describe current status — machine-readable: proved / verified_finite / open /
  interpretation / …
- **(d) Reader receipts** touch only the reader — local, optional, never written back,
  navigation-only ("resume where I left off"); **never epistemology, never counted, never
  aggregated, never read as approval.**

**Stranger test:** the one durable outcome of reading is *"I understand what is claimed, what is
not, what supports it, and what would change its status."* If a reader leaves believing
*"I helped certify this,"* the artifact failed.

**Attached sharpening (carried from the original candidate):** understanding-states are for
READING; dissolving the three Class-A ratifications into "understood enough to continue" would
blur never-certify in the other direction. Comprehension everywhere, endorsement only at the
irreversible acts.

## 4. TWO-COORDINATE STATUS PAIR — adopted labeling guidance (2026-07-06; no new infrastructure)
Artifacts are written with status as a PAIR: **(confidence, warrant)**.
- **Confidence** — pipeline-writable: computation, reproduction counts, audit outcomes may move it.
- **Warrant** — **NOT pipeline-writable**: only world-events move it (a steward signature, an
  external referee, an independent human reconstruction). No script, model, or pipeline output
  ever writes warrant.
This is the confidence/warrant setter-split as *writing guidance*, effective immediately; the
propagation MECHANISM over the dependency graph stays a deferred candidate (see
`.automation/deferred_candidates.md`) until observed need.

## 5. EVIDENCE-RIVER DIAGNOSTIC (self-check, generated with the river)
If the timeline is dominated by infrastructure events (validator passed, hash updated, dashboard
regenerated), **the machinery has become the primary activity — flag it.** A healthy river reads
as research (n=4 completed, counterexample not found, destroy attempt failed, null packaged).
Infra events stay present but backgrounded. The river generator computes and prints this
diagnostic; a FLAG here is itself a valid observation-signal input (automation-time-savings /
queue-scaling) for the governance sensor stream.
