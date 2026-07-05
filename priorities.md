# Priorities — reversible-contact

*Edit this file freely, then refresh status.html. Recognized sections: "Needs your attention", "In progress", "Next", "Recently done".*
*Updated: 2026-07-05 (late — R1 audit complete)*

## Needs your attention
- **R1 promotion (Tier-3, yours alone)** — audit DONE: **valid-with-gaps** (unanimous — 3 blinded Claude auditors + 2 blinded ChatGPT samples); theorem TRUE, finiteness-free; 9 patchable gaps (~8 lines of text) → read `.automation/R1-AUDIT-REPORT-2026-07-05.md`, then decide: patch the proof text as v0.3 and/or promote
- **Ledger C candidate: RET-∃ ↔ Exit** — draft map ready at `.automation/ledger_C_candidate_map_DRAFT.md`, with ChatGPT's blinded independent construction appended (both converge on the availability-form map; one contested sub-item: the irreducibility row) → admit / reject / hold
- **KR Thm 1 read (K(e)=D(e))** — your guided reading package is ready: `.automation/KR-READ-PACKAGE.md`; tutor chat primed and waiting: https://chatgpt.com/c/6a49f9c3-0418-83ee-8c10-198ed750f335
- **`ledger_a_verify.py`** — your R-series script is still not on disk anywhere; drop it in for the exact-number diff
- **One-time `wrangler login`** — unlocks phone-board auto-deploy (the phone board is currently a cycle stale)

## In progress
- ChatGPT round-2 delta-assessment of the C-map draft (queued in the same conversation — free-tier throttled)

## Next
- Proof-text patch (G1–G9) toward the next Ledger-A revision, if you approve; pin the nondet definition (37 any-effect vs 25 R-only)
- Commit-on-clean cadence via `Scripts/commit_if_clean.ps1`; phone-board auto-deploy (automation backlog #2)

## Recently done
- **R1 independent audit complete** (2026-07-05) — valid-with-gaps; **n=4 blind probe matched predictions: 24 = 4! strict, 209 = ΣC(4,k)²k! partial**; zero enumeration discrepancies across deposited / harness / from-scratch; audit enumerators deposited in `LedgerA/`
- **Ledger A v0.2 canonical adopted into repo** (2026-07-05, steward-authorized; commit 808393a); validate historical-layer exemption added
- **Round-2 reconciliation frozen** (2026-07-04) and imported to `reconciliation/`
- **Cross-agent protocol v0.1 draft** converged with ChatGPT (2026-07-05, non-canon)
