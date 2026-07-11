# Priorities — reversible-contact

*Edit this file freely, then refresh status.html. Recognized sections: "Needs your attention", "In progress", "Next", "Recently done".*
*Updated: 2026-07-05 (post-unification — canon at Desktop/code/framework; this file mirrors in both repos)*

## Needs your attention
- **Commit the manifest re-pin** — you've run `pin_manifest.py` and I've drafted the Ledger E row + `GOVERNANCE-VERSION.json` enforcement_status update to match; review `git diff` on all three files (`MANIFEST.sha256.json`, `GOVERNANCE-VERSION.json`, `LedgerE/evidence_log.md`) and commit when satisfied
- **Optional: independent hash cross-check** — my own sandbox couldn't verify the manifest's SHA-256 hashes byte-for-byte (mount reliability issue, not a sign of a real problem — see the Ledger E row); ultracode offered to do this independently in its own environment if given repo access — worth doing before calling enforcement fully verified, not urgent
- **Manifest guard enforcement test** — separate, later milestone: a fresh guarded-validator run rejecting an unauthorized post-repin core edit; do not run yet

## Closed 2026-07-11 (this session)
- **Governance manifest re-pin** — RE-PINNED (Pratyush, run natively on his machine); `GOVERNANCE-VERSION.json` freeze_status + enforcement_status updated to reflect it; Ledger E row added
- **Q-R2-BAND** — RATIFIED (Pratyush, "promote", direct decision); the "free" halves of Proposition R2 (RET-! under F-sup, RET-exists under F-sub) upgraded to proved-internal at any cardinality; Ledger A now v1.0. Bijection-core halves untouched, still searched-universe grade only
- **Q-D5-STRUCTURE-GENERAL** — PROMOTED open question → theorem (Pratyush, "promote and proceed", direct decision); Theorem D5G in Ledger A — sub-identity rung survivors = partial bijections of X = I_X, any cardinality, cardinality-free proof
- **Governance v2 FREEZE** — RATIFIED (Pratyush, direct decision)
- **R1 promotion** — PROMOTED conjecture → theorem (Pratyush, direct decision); Ledger A now v0.8
- **Ledger C candidate: RET-∃ ↔ Exit** — ADMITTED as proposed (Pratyush, direct decision); `LedgerC/entry_001.md`
- **KR Thm 1 read (K(e)=D(e))** — guided reading package ready: `.automation/KR-READ-PACKAGE.md`
- **`ledger_a_verify.py`** — your R-series script is still not on disk anywhere; drop it in for the exact-number diff (note: the audit's from-scratch enumerators already reproduced every deposited count with zero discrepancies)
- **Batch review (dual-agreement rule)** — final remarks queued in the evidence log: R1 proof-text patch, two-repo unification, validate.py adoption, schema unification
- **One-time `wrangler login`** — unlocks phone-board auto-deploy

## In progress
- **Stage-0 deterministic gate LIVE** (native Task Scheduler, 5h, zero-token no-ops) — old two Dispatch tasks superseded, safe to delete; n=4 progresses via direct manual chunks
- ChatGPT round-2 delta-assessment of the C-map draft (queued, free-tier throttled)

## Next
- Free-rung n=4 (constraint-propagation route per audit enumerator), if wanted
- Q-CONVERGE: composition/iteration semantics on the frozen signature, then a finite-model probe
- Commit-on-clean cadence via `Scripts/commit_if_clean.ps1`; phone-board auto-deploy

## Recently done
- **Two-repo unification (2026-07-05)** — canon = Desktop/code/framework (now at the version stated in status.json); mounted folder = synced mirror; staleness resolved (mounted copy had been seeded from the then-current canon, byte-identical, four versions behind); audit artifacts, validate.py (historical exemption + C/D guards), cross-agent protocol, and cycle machinery folded into canon
- **R1 independent audit complete** (2026-07-05) — valid-with-gaps; n=4 blind probe matched predictions (24 = 4! strict, 209 = ΣC(4,k)²k! partial); zero enumeration discrepancies across four sources; proof text patched per the auditors' agreed reconstructions
- **Cross-agent protocol v0.1 draft** converged with ChatGPT (2026-07-05, non-canon)
