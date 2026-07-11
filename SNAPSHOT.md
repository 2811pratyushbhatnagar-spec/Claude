# PROJECT SNAPSHOT — generated view, non-canonical · Class-D artifact (regenerate: `python snapshot.py`)

*Generated at head `5960054 2026-07-06 23:53`. The one file to read first; everything below is derived from status.json / questions.json / counts.json / Ledger E / git / a fresh run_checks execution.*

## Canonical state
- **Mathematics**: Ledger A frozen v0.7 canonical
- **Protocol**: Ledger B frozen v0.5; testing, not extension
- **Correspondence**: empty by design; admitted=0; candidate queue: 2 (unadmitted)
- **Ontology**: open-empty-allowed
- **EvidenceLog**: active-append-only
- **Journal**: separate-companion
- **Publication**: not-started
- **head**: `5960054 2026-07-06 23:53` · working tree DIRTY

## Repo health
- checks (fresh run): **ALL TIER-1 CHECKS PASS**
- validator catches to date: introduced-date + catches-to-date: ledgerE-6-field-schema (07-04, 1: pipe-broken row); dangling-ref (07-04, 1 genuine: unlisted external validate.py; +3 scope-refinement fires at introduction); arch-label-sync (07-04, 2: stale Ledger-B v0.4 label at introduction; then caught the v0.5->v0.6 bump leaving ARCHITECTURE.md stale, same day); felt-register, conjecture-cite-band, withdrawn-cite, counts-coherence, registry-schema (07-04, 0 catches so far)

## Readiness (condensed; full: `python readiness.py`)
- **Mathematics**: not ready: 3 conjecture(s), 7 open
- **Publication**: not ready: 8 item(s) awaiting human action

## Open blockers (human-owned, live)
- **Q-R1-GENERAL** [conjecture] — Pratyush: promote to theorem or decline (audit complete, text patched, dual-agent accept).
- **Q-D5-BOUNDARY** [conjecture] — Ratify the general partial-bijection argument together with the R1 audit.
- **Q-D5-STRUCTURE-GENERAL** [open] — Prove for arbitrary finite state sets (the R1-style relational argument is the natural route) or extend computation; ratification is Tier-3.
- **Q-R2-BAND** [conjecture] — Pratyush ratifies or declines (Tier-3).
- **Q-R3-R8** [open] — Relay the R3-R8 statements (and/or ledger_a_verify.py); reconcile as a new dated snapshot.
- **Q-DIFF** [open] — Relay ledger_a_verify.py; run the diff; deposit a new dated reconciliation note.
- **Q-P1** [open] — None; held. Any content is Tier-3.
- **Q-GOV-V2-FREEZE** [open] — Pratyush signs or declines the v2 freeze. On signature, TWO separate milestones get their own event-time packets: (1) 'ratified - decision complete'; (2) 'enforcement ACTIVE' only after the guarded validator demonstrably rejects an unauthorized core edit post-ratification. Then: restart mathematics (n=4 completion, null packaging, R1 decision).

## Last verified computations (counts.json, regression-guarded)
- feq-free-n2: 37 of 56 nondeterministic (cross-confirmed)
- feq-free-n3: 4087 of 4400 nondeterministic (cross-confirmed)
- feq-subid-n2: 0 of 7 nondeterministic (builder-only)
- feq-subid-n3: 0 of 34 nondeterministic (builder-only)
- feq-strict-n2: 0 of 2 nondeterministic (cross-confirmed)
- feq-strict-n3: 0 of 6 nondeterministic (builder-only)
- fsup-free-n2: 2095 of 3994 nondeterministic (builder-only)
- fsub-free-n2: 660 of 679 nondeterministic (builder-only)

## Independent-reproduction banding
- **externally-audited** (0): none
- **cross-confirmed** (3): feq-free-n2; feq-free-n3; feq-strict-n2
- **builder-only** (5): feq-subid-n2; feq-subid-n3; feq-strict-n3; fsup-free-n2; fsub-free-n2

## Outstanding destroy-attempts (what an adversary should try, per live claim)
- **Q-R1-GENERAL** [conjecture]:
  - a nondeterministic counterexample satisfying F-eq + strict identity effects at any cardinality
  - a defect found in the recorded 5-line proof
- **Q-D5-BOUNDARY** [conjecture]:
  - a nondeterministic F-eq survivor with sub-diagonal identity effects at any n
  - count mismatch vs sum C(n,k)^2 k! at any tested n
- **Q-D5-STRUCTURE-GENERAL** [open]:
  - a counterexample state-set where survivors fail the monoid/group laws
- **Q-S4-SCALE** [open]:
  - mooted if Q-R1-GENERAL is ratified
- **Q-R2-BAND** [conjecture]:
  - a defect in the recorded one-line general arguments
  - a countermodel to a free half at any cardinality
- **Q-DIFF** [open]:
  - any count mismatch reopens the affected reconciliation as a new dated note
- **Q-GOV-V2-FREEZE** [open]:
  - execution evidence demanding a governance change arrives before ratification

## Ledger E — recent rows
- 2026-07-06 · Reader-interface candidate re-classified (split) · **PRINCIPLE ACCEPTED (projection layer) / UI DEFERRED**
- 2026-07-06 · Provenance block + staged reproduction package · **STAGED, HANDOFF-READY**
- 2026-07-06 · Provenance richer schema + private-verify deploy staging · **LEVEL-3 RECORDED / DEPLOY STAGED**
- 2026-07-06 · Consolidation capture (thread-final) · **CONSOLIDATION-COMPLETE**
- 2026-07-07 · Framework Context Map + v2.1 change-set · **CANDIDATES LOGGED, NOTHING ADOPTED**

## Recent commits
- `5960054 Consolidation capture: distillation + completeness-register wording, (confidence,warrant) labeling adopted, engineering frontier queued`
- `9a5d027 Provenance richer schema (Level 3, NOT blind - register held) + private-verify deploy staged (not run)`
- `fe3b4bd Provenance block (first-party, exact schema) + staged free-rung-n4 reproduction package (NOT published)`
- `c6c6339 Split reader-interface candidate: comprehension-not-endorsement principle ACCEPTED (projection layer); UI stays deferred`
- `2acf773 Log deferred design candidate: states-of-understanding interface + Challenge Queue (NOT built)`
