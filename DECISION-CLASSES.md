# Decision Classes — v1.0 (Class-B governance change, 2026-07-05; queued for steward batch review)

> **The portable methodological statement (recorded 2026-07-06, beside the warrant-boundary
> invariant):** *"Design the research process so that integrity is enforced by architecture
> wherever architecture can enforce it, and make explicit the points where architecture must stop
> because only independent reconstruction can increase warrant."*

*Replaces the flat FIFO decision queue with classes by IRREVERSIBILITY. Rationale: review effort
should scale with what cannot be undone; a flat queue buries irreversible scientific claims among
regenerable artifacts. Endorsed by both AI reviewers and Pratyush's directive; implementation logged
in Ledger E.*

## The classes

| Class | Content | Review |
|---|---|---|
| **A — Irreversible scientific claims** | EXACTLY the Tier-3 set in `status.json → governance.tier3_human_only`: promote conjecture→theorem, admit Ledger C entry, modify Ledger B, ontology/Ledger D, publish | **Individual review, never batched.** |
| **B — Interpretive / governance changes** | architecture revisions, validator policy, dashboard criteria, this document | Small batched review with written rationale |
| **C — Evidence records** | Ledger E entries, regenerated dashboards, manifests, successful recomputations, brute-force bank entries | Bulk review; spot-check samples |
| **D — Purely generated artifacts** | counts renderings, dependency views, manifests, summaries (SNAPSHOT, DECISIONS, readiness, agenda) | **No approval needed if validators pass**; regenerate on demand |

## Anchors and rules
- **Class A is anchored to the Tier-3 firewall, not to automation discretion.** Membership is *derived
  from* `status.json governance.tier3_human_only`; automation MAY NOT declassify an A-item, ever.
  Changing the Tier-3 list is itself Tier-3.
- **Tie-break: ambiguous items classify UP** (stricter class). Asymmetric caution — the cost of
  over-reviewing a Class-C item is minutes; the cost of under-reviewing a Class-A item is a false
  scientific claim.
- **Evidence packet required on every queue item** (rendered in DECISIONS.md): what changed · why ·
  which scripts produced it · validator status · dependencies · whether independent reproduction
  exists · recommended action · decision class — and, for Class A, the substantial-result-checklist
  status.
- **Artifact labeling:** every artifact carries its class at point of display. A Class-D count is
  never presentable as a Class-A result — register discipline enforced on the dashboard, not just
  at review.

## Top invariant (paired with "Never replace a map with an identification")
> **The automation may produce, organize, and challenge evidence; it never certifies evidence.**
Content-firewall (what may be claimed) + process-firewall (who may certify it).

## v1.1 refinements (2026-07-05, Class-B change, queued for batch review)
1. **Monotonic classification.** Automation may only ESCALATE (D→C→B→A); no automated de-escalation,
   ever. De-escalation requires a human-authored row in `DECLASSIFICATIONS.md` (governed). Authority is
   tiered: lowering a Class-A item is itself a Class-A act; lowering C→D is Class-B. Mechanically
   enforced in `Scripts/worker_guard.py` (conservative-static-analysis property: uncertainty moves up).
2. **Result / Destroy-protocol / Promotion are three independent objects.** The destroy-protocol is
   infrastructure, not evidence; versioned and frozen independently (`protocols/`); freezing one is a
   Class-A act (the per-type instance of checklist criterion 3 — the steward's bar-freeze signature).
   Order enforced by timestamp: frozen_at < run.started_at < evidence.collected_at < proposed_at;
   violations are INADMISSIBLE as substantial-result candidates (test_consistency guards the chain).
3. **Event-time evidence packets.** A packet is an atomic OUTPUT of the producing step
   (event → packet → validators → queue item), never reconstructed from history. No packet → not
   reviewable. Wired into WORKER-CONTRACT.md and the producers (e.g. the brute-force bank).
4. **Dependency-scoped staleness.** Packets carry repo-head + dependency hashes; a packet is STALE iff
   its OWN dependency-closure changed before review — no whole-queue invalidation on unrelated
   commits. Stale ⇒ "regenerate before review"; on regeneration, class re-derives monotonically.
5. **Review instrumentation (pilot; built, NOT running — running is the steward's call).** Per
   Class-A review: time required, additional-context-requested, confidence-after
   (`Scripts/review_metric.py` → `.automation/review_metrics.jsonl`). **Diagnostic of PACKET
   QUALITY, never a target, never approval pressure** — a slow review with many context-requests is
   a good finding (the packet was thin), not a failure.

## v1.2 mechanizations (2026-07-06, Class-B, queued)
1. **Escalation feedback.** Every auto-escalation logs provenance (which rule fired) to
   `.automation/escalations.jsonl`; `Scripts/governance_metrics.py report` computes escalation
   rate, human de-escalation rate, and **precision BY RULE** (localizes a too-broad rule).
   **GUARD:** metrics only FLAG a rule for HUMAN breadth-review; automation may NEVER auto-tighten
   or auto-relax an escalation rule (the machine making itself more permissive is forbidden by the
   conservative-static-analysis property). Governance instrumentation stays out of research views.
2. **STALE is purely mechanical** — a packet is STALE iff any declared-dependency hash differs
   from the hash recorded at emission; no judgment. **SUPERSEDED** = a newer packet exists for the
   same decision. Invariant: each decision has exactly ONE live (non-stale, non-superseded) packet
   = the review target; all priors retained append-only.
3. **Cryptographic freeze.** `MANIFEST.sha256.json` pins every governance-critical immutable;
   `validate.py` fails on any byte change without a human-authorized re-pin
   (`Scripts/pin_manifest.py --authorize`). Dependency declarations are versioned + pinned
   (`DEPENDENCIES.json`); packets record the declaration version/hash they consumed.
4. **Two-object separation, enforced.** Packet-quality metrics (time, context-requests,
   confidence) and scientific status — the ONE canonical evidence-band vocabulary:
   **builder-supported / independently-reproduced / finite-verified / general-conjecture /
   promoted** — never appear in the same table; the dashboard generator asserts it (existing
   count-vocabulary maps: builder-only→builder-supported, cross-confirmed→independently-reproduced,
   externally-audited→independently-reproduced+external).

## v2.0 — CONSTITUTIONAL FREEZE (machinery in force 2026-07-06; **the FREEZE ACT is queued Class-A**)
- **The freeze itself is Pratyush's signature** (registry Q-GOV-V2-FREEZE): a system must not
  self-execute its own constitutional freeze. All machinery below is implemented as Class-B and in
  force; "FROZEN" becomes binding on ratification.
- **Constitutional core — EXPLICIT and CLOSED** (list in `GOVERNANCE-VERSION.json`, enforced ==
  manifest core by test_consistency): class rules, validator definitions, freeze/hash mechanism,
  dependency schema, packet schema (worker contract), governance versioning, **and the
  gate/router (`Scripts/cycle_check.py`)** — scripts decide whether models run, so unpinned wake
  logic would be a hole in the freeze. Hash-verified by `validate.py` BEFORE any other check; core
  compromised ⇒ nothing downstream runs. Core changes: Class-A only. **The constitutional surface
  must not creep** — everything outside the list evolves under normal governance.
- **Pre-registered observation schema** (the ONLY signals that admit a governance proposal):
  queue-scaling · packet-sufficiency · validator-effectiveness · dependency-declaration-accuracy ·
  automation-time-savings · token-resource-efficiency.
- **Observation ≠ ratification:** a red-team run / failure / near-miss TRIGGERS REVIEW — it admits
  a proposal; the change still passes normal Class-A process. A failure never auto-rewrites rules.
- **Triangulation trigger = expected value of error detection**, not strictly Class A: independent
  reproduction is required when EV(catching an error) > cost of another run. Usually coincides
  with Class A; grounded in error-detection either way.
- **Retrospective labeling:** pre-v2 artifacts are "governance v1 (retrospective)" — never
  rewritten, never upgraded-by-declaration; regenerate from logs where feasible.
- **THE STOPPING RULE** (binding on ratification): *no further governance proposals unless
  triggered by a pre-registered observation signal from execution*
  (`.automation/execution_evidence.jsonl`; the run ledger and guard violations feed it — the
  sensor and the reopening condition are the same stream). Deployment note: pausing/slowing the
  expensive schedule while the deterministic gate is built is a deployment choice, not a weakening.
  After ratification: the layer is frozen like the ledger architecture; the automation re-aims at
  the mathematics (n=4 completion, null packaging, R1 decision).
- **Register on completeness (correction adopted 2026-07-06, replacing any "the design is
  finished" phrasing — itself a warrant-like claim):** *the v2 core architecture appears
  internally coherent; future changes are driven by implementation experience and independent
  review, not by searching for another foundational principle.*
