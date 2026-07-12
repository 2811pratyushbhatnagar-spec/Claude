# Q-DIFF Closure — `ledger_a_verify.py` does not exist anywhere reachable

**Date:** 2026-07-12T15:09Z · **Agent:** ultracode (remote container) · **Register:** non-canon worker note
**Verdict: CLOSED NEGATIVE (references-only).** The file was never delivered; every record
consistently describes it as external pending material (EXT-ledger_a_verify).

## Three-channel exhaustive hunt (all read-only)

1. **Full git history** (all refs incl. main / governance-repin /
   claude-understand-3yr-work-hvqr9n; 19 commits): no file ever added, no object path,
   no reflog/stash entry, no dangling blob (`git fsck`), no filesystem match. The string
   is referenced on ~100 lines across 23 files (reconciliation notes, brute_force_step.py
   BF-2 probe, bf_state.json, DECISIONS.md, questions.json, snapshot, priorities,
   status.json, test_consistency.py KNOWN_PENDING, Ledger A canonical + archives, Ledger E,
   handoffs, audits, state reconstructions) — all as "not on disk / never arrived."
2. **GitHub code search**, both owner-case variants: 0 hits; exactly three branches exist.
3. **Notion workspace**, four query formulations: 0 hits.

## What this closes and what it leaves

- BF-2's four-path probe can stop expecting the file to "appear": it never existed in any
  reachable store. The absence is now a verified fact, not an open watch.
- The steward's fork (Tier-3-adjacent, his call): (a) relay `ledger_a_verify.py` + R3–R8
  statements from wherever they live natively, reopening the exact-number diff; or
  (b) declare EXT-ledger_a_verify permanently unavailable and re-scope Q-DIFF to the
  independent counts already frozen in `reconciliation/reconciliation_2026-07-04.md`
  (free-identity n=2: 37/56; n=3: 4087/4400 — agreeing across constructions), with
  strict/sup/sub cross-checks as a fresh worker task if wanted.
- `status.json`'s open[] wording and `questions.json`'s Q-DIFF disposition are canon-state
  edits — left untouched here; this note is the evidence they would cite.
