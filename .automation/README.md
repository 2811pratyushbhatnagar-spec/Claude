# automation/ — non-canon procedures-only output

This folder holds automation-opportunity audits produced by the `automation-audit-5h`
scheduled task (and by hand). It is **tooling output, not canon**: nothing here is a
ledger, and nothing in it promotes a conjecture, admits a Ledger C entry, changes
Ledger B, adds ontology, or publishes. Those remain Tier-3 human-only decisions
(see `status.json` → `governance.tier3_human_only`).

- `AUTOMATION-AUDIT-<date>.md` — a dated, create-only snapshot of the standing
  automation backlog (what could be automated, how often it bites, est. time saved).
- The scheduled audit writes a new dated file each run only when the backlog changes;
  otherwise it emits a one-line heartbeat, mirroring `Scripts/cycle_check.py`.

Safe to delete anything here; it regenerates.
