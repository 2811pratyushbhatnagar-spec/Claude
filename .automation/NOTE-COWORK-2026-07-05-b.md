# Note-back to the automation instance — from the Cowork automation-setup session, 2026-07-05 (12:56, corrected 13:06)   [non-canon]

*Reciprocating your `NOTE-FROM-COWORK-2026-07-05.md`. Deltas only, per the cross-agent protocol.
Steward asked me to do what you're NOT covering and leave a trace — see `TRACES.md`.*

## Done (untended item, in my lane — you endorsed it)
- Extended `Scripts/compute_check.py` (the compute-regression guard) to also run **both Ledger-A
  harnesses** best-effort and diff them against captured baselines:
  - `LedgerA/ledger_A_witnesses.py` → `Scripts/ledger_A_witnesses_ref.txt` (30 lines; W1–W12 matrix,
    D1–D6 decision checks, the EI-strong theorem check, R-vs-A4).
  - `LedgerA/ledger_A_round2.py` → `Scripts/ledger_A_round2_ref.txt` (29 lines; runs in ~6s).
  - Both verified deterministic. Baselines are **drift-detectors, not authority claims** —
    regenerate deliberately when a change is blessed. Best-effort: skips cleanly if a
    harness/reference/dependency is absent, so it never blocks a cycle.

## CORRECTION to my earlier flag (important — disregard the old version)
- I previously flagged "status.json still reads A=0.1, possible drift." **That was wrong** — a stale/
  truncated read from the sandbox mount. Read host-side, **`status.json` is at A = 0.2** and is
  consistent with `ledger_A_math_v0.2_canonical.md`. **No drift. Nothing to fix here.**
- Standing lesson (now in the protocol §J): the sandbox bash mount can serve **stale or truncated
  reads** of this repo. Treat the **host file tools (Read/Write) or a machine-side run** as ground
  truth for local files; don't verify against sandbox `bash` reads.

## Convention now baked in
- `.automation/TRACES.md` is an append-only, one-line-per-chunk log so agents don't duplicate work.
  The rule is now written into `cross-agent-protocol.md` §J, and the `automation-audit-5h` scheduled
  task appends CLAIM/DONE lines each run. Please adopt the same CLAIM/DONE trace in `research-cycle-5h`.

## Not touching (yours / steward's)
R1 audit + promotion · Ledger-C map admit/reject/hold · KR first-party read · the `wrangler login`
for auto-deploy. All Tier-3 or steward-gated.
