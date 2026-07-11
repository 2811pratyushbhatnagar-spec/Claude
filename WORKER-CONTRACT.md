# Stateless-Worker Contract — v1.0 (band-1 operational governance)

*Binding on every automated agent (Claude session, subagent, cycle skill, ChatGPT-relayed procedure)
operating on this repository. The repo is the ONLY long-lived memory; workers are stateless.*

## The cycle (every worker, every run)
1. **PULL** the current repo state (canon: `Desktop/code/framework`; mirror: the mounted folder).
2. **EXECUTE** assigned procedures only (Automation Queue in `DECISIONS.md`; `questions.json`
   entries with `owner: auto`; standing checks/regenerations).
3. **PRODUCE** evidence and candidate changes — never conclusions-as-facts. Every produced evidence
   artifact is emitted **with its evidence packet at production** (event-time provenance: producer
   script, repo head, dependency hashes). **No packet → the item is not reviewable**; provenance is
   never reconstructed retroactively — regenerate the artifact to get a real packet. A packet is
   STALE iff anything in ITS dependency-closure changed before review (dependency-scoped — unrelated
   commits do not invalidate the queue); stale ⇒ regenerate before review, and on regeneration the
   class is re-derived monotonically (it may only rise automatically; see DECLASSIFICATIONS.md).
4. **RETURN** machine-readable outputs (json/counts/exit codes) plus human-facing recommendations
   into the Decision Queue; append evidence rows to Ledger E; append candidates to queues.
5. **EXIT.** Retain nothing. Anything worth keeping goes into the repo before exit as evidence,
   a candidate row, or a generated artifact.

## What a worker MAY touch
- **Generated artifacts** (regenerable, non-canonical): `SNAPSHOT.md`, `snapshot.json`,
  `DECISIONS.md`, dashboards (`status.html`, `site/`), manifests, `counts.json` values *with
  regression backing*, registry `evidence`/`next_action` fields.
- **Append-only records** (add rows, never edit or delete existing ones): `LedgerE/evidence_log.md`,
  the Ledger C candidate queue (`LedgerC/README.md`), `.automation/TRACES.md` (claim/done lines
  per the cross-agent protocol), `.automation/` reports.

## What a worker may NEVER touch (ratified / governed state)
- `LedgerB/` (protocol) · `LedgerD/` (ontology) · `LedgerA/ledger_A_canonical.md` and
  `LedgerA/archive/` (frozen mathematics) · `reconciliation/` (frozen snapshots) · `status.json`
  (versions + governance) · this contract.
- No promotion conjecture→theorem, no Ledger C admission, no registry `state` flips upward, no
  publishing, no history rewriting (never `git init` over an existing repo, never force-push).
- Changes to governed state happen only via the steward (Tier-3) or an explicitly logged
  dual-agreement instruction — and then by the instructed session, with a Ledger E final remark.

## Resource rules (governance v2)
- **Deterministic software decides whether AI is needed; AI never decides whether deterministic
  software should have run.** Scripts are the gatekeepers (cycle_check prints the GATE verdict);
  models are specialists invoked only when the gate says reasoning — not computation — is required.
  A healthy idle repo spends ~no tokens. Adversarial/destroy passes are *scheduled* reasoning,
  exempt from the change-gate by design.
- **Budget exhaustion halts automation; it never relaxes validation.** Scarce resources make the
  system slower, never less trustworthy.
- Context is computed, not chosen: load changed objects + their dependency closure, not the repo.
- Per-run usage is recorded in `.automation/run_ledger.jsonl` (deterministic side written by the
  cycle; the wrapper session appends model-token counts). Optimization is evidence-driven.

## Enforcement
`Scripts/worker_guard.py` checks the working tree against this boundary (governed paths unchanged;
append-only files gained lines only). The automation commit path (`Scripts/commit_if_clean.ps1`)
runs it before every commit and refuses to commit on a violation. Guard failure = stop and report,
never override.
