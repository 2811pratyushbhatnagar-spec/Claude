# framework — canonical repository (four ledgers + evidence log)

Composability without collapse: domains interact only through explicit, evidence-backed maps and never
collapse into one another. See `ARCHITECTURE.md` for the full statement; the two invariants that hold it
together: **never replace a map with an identification** · **the automation may produce, organize, and
challenge evidence; it never certifies evidence.**

## Layout
| Path | Content | Status |
|---|---|---|
| `LedgerA/ledger_A_canonical.md` | Mathematics (canonical; version lives in status.json; archive/ holds priors; audits/ holds independent-audit artifacts) | FROZEN |
| `LedgerB/` | Protocol v0.5 (`protocol_ledger.md`), kernel v0.3 (`kernel.md`), optional lens | FROZEN |
| `LedgerC/` | Correspondence | **EMPTY by design** |
| `LedgerD/` | Ontology / P1 | OPEN, allowed empty |
| `LedgerE/evidence_log.md` | append-only evidence log (the one ledger that logs negatives) | ACTIVE |
| `Journal/` | pointer — interpretive journal lives externally, labelled exploration | external |
| `Experiments/` | CM/MSF experiment notes + verify code (separate research track) | reference |
| `Scripts/` | Ledger-A computation harnesses (W-series, round-2/R-series) | frozen with Ledger A |
| `tests/` + `run_checks.py` | Tier-1 checks: regression (asserted counts) + consistency (cross-refs) | ACTIVE |
| `reconciliation/` | frozen dated snapshots — never edited; corrections are new dated notes | FROZEN |
| `handoffs/` | dated handoff notes | record |
| `questions.json` + `status.json` | Question Registry (lifecycle tracker; the "what next" driver) + machine status mirror | ACTIVE |
| `counts.json` | structured counts — source of truth for enumeration numbers; prose renders "N of M" from here | ACTIVE |
| `readiness.py` | generated Publication-Readiness view (`python readiness.py`) — view only, never canonical | view |
| `agenda.py` | registry query reads: affected-if-X-changes, next-agenda, not-externally-audited | view |
| `snapshot.py` → `SNAPSHOT.md`, `snapshot.json`, `DECISIONS.md` | project heartbeat (read SNAPSHOT.md first) + automation-vs-Tier-3 decision queues — generated, non-canonical | view |
| `WORKER-CONTRACT.md` + `Scripts/worker_guard.py` | stateless-worker contract (repo = only long-lived memory) + its mechanical boundary guard, wired into the automation commit path | IN FORCE |
| `Scripts/brute_force_step.py` | resumable brute-force chunk step inside the 5h cycle (queue BF-1..BF-5; negatives bank as findings; forced-bridge search held to forced-only, null certificate maintained) | IN FORCE |
| `DECISION-CLASSES.md` + `SUBSTANTIAL-RESULT-CHECKLIST-DRAFT.md` | decision classes A–D by irreversibility (A anchored to Tier-3; ambiguity classifies UP; evidence packets; artifact labeling) + the substantial-result bar (DRAFT — freezing is the steward's signature) | IN FORCE / DRAFT |
| `DECLASSIFICATIONS.md` + `protocols/` + `Scripts/review_metric.py` | v1.1 refinements: monotone classification (human-only de-escalation register), destroy-protocol infrastructure (none frozen; lifecycle order guarded), Class-A review instrumentation (built, not running) | IN FORCE / EMPTY / IDLE |
| `MANIFEST.sha256.json` + `GOVERNANCE-VERSION.json` + `DEPENDENCIES.json` | cryptographic freeze (constitutional core incl. the router AND the boundary list itself, verified FIRST — root of trust) + governance v2.0 machinery (freeze ratification queued Class-A; decision and enforcement recorded separately) + versioned dependency declarations | v2.0 (ratification pending) |
| `EVIDENCE-RIVER.md` + Mission Control strip in `status.html` | Ledger E as a chronological timeline + 3-line attention view (machine green/red, next Class-A decision, current open question) — Class-D generated views; the three-layer UI is DEFERRED until running shows these insufficient | views |

## One-command check
```
python run_checks.py
```
Runs validate.py (version drift vs status.json with historical-layer exemption; Ledger-C admitted=0
guard; Ledger-D-as-evidence guard), then consistency (cross-references, schema, versions), then
regression (re-executes the Ledger-A verification and asserts every reported count; fails loudly if
any number changed).

**Repo topology (2026-07-05):** THIS repo is canonical. The mounted folder
(`Desktop/New folder (2)/framework`) is a synced working mirror for the sandboxed agent and the
research-cycle skill; `.automation/` carries cross-agent records (see `cross-agent-protocol.md`).

## Governance firewall (in force)
Automation — including AI sessions operating this repo — **executes procedures only**. It may never:
1. admit a Ledger-C entry (candidates go to the queue; admission is Pratyush's),
2. change Ledger B (frozen; revisions require observed friction from real use, ratified),
3. promote conjecture → theorem (band upgrades are ratified, never automated),
4. touch Ledger D.
Reconciliation notes are frozen dated snapshots. Ledger E is append-only with fixed schema
`Date | Artifact | Action | Evidence | Disposition | Reason`.
