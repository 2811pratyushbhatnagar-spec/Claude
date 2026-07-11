# Cross-Agent Provenance Map v0.1 — where every referenced concept actually lives

**Register:** pointer/structural, Class-D, non-canon. Nothing here is a claim;
every row is an address plus a verification status. Purpose: end the
relay-trust problem between Cowork (local, reversible-contact repo + Notion
connector), ultracode (remote container, GitHub mirror + Notion), and ChatGPT
(resonance only, no storage access).
**Date:** 2026-07-11 · **Author:** ultracode session (branch
`claude/understand-3yr-work-hvqr9n`).

## The one structural fact that resolves the confusion

There are **two distinct research programs** plus one undeposited layer:

1. **MoN/FoI** (Movement of Nothing / Framework of Identity) — canonical
   surfaces: Notion workspace (readable map) + GitHub archive. This is where
   the register vocabulary (AVOWED, membrane, Disallowed) lives.
2. **reversible-contact** — canonical repo on Pratyush's machine
   (Desktop/code/framework), Ledgers A–E, status.json, governance v2.
   Transport branch: `governance-repin` on the shared mirror.
3. **The July 2026 claude.ai/ChatGPT threads** — fresh-design material that
   is **deposited nowhere** (relay-only). Known, standing gap.

Cowork searched only #2 for vocabulary from #1 and #3 — hence the misses.

## Concept → canonical address (verification status per row)

### Domain 1 — MoN/FoI Notion archive (ultracode read these directly, 2026-07-09/11)

| Concept | Address | Status |
|---|---|---|
| AVOWED band (and EXACT/STRUCTURED/IMPORTED/NOT-CLAIMED) | Notion "Research Index", page id `378f0d01bc8881e89cddd0fa1a8ce597`, "How to read this index": "AVOWED (posited, not proved)" | READ-DIRECT |
| Discovery/justification membrane | same page, Standing constraint: "nothing-reasoning may motivate and discover, but cannot justify or derive physics. Coherence is never treated as derivation." | READ-DIRECT |
| Disallowed list | Notion "Gate D Dependency Ledger v0.1", id `36af0d01bc88811e9ab8f40e3a9b303d`, section "Not Allowed" (first line: "Z₃ follows from bare N(N) ≠ N") | READ-DIRECT |
| Verification Instrument v1.0 (retrieval-coverage protocol, B0/B1 baselines, provenance enum) | Notion id `38df0d01bc88818b84a5c6e196ca9fa1`, FROZEN 2026-06-28, under "Coherent Orientation Layer — Shared Memory" | READ-DIRECT |
| O-Conjecture v0.2 (pointed carrier) | Notion id `392f0d01bc88818285b9c417bd28d1e5` + repo `physics/o-conjecture/` (this branch, commit 94e8062, PR #1) | READ-DIRECT + IN-REPO |
| "code survives relay better than facts" (fact-decay echo) | `physics/enumeration-replication/README.md` (this branch, commit 710b159) | IN-REPO (Cowork independently confirmed) |

### Domain 2 — July claude.ai/ChatGPT threads: RELAY-ONLY, UNDEPOSITED

| Concept | Source | Status |
|---|---|---|
| Layer-1 specification / "pending spec ruling" (defs: representation, weaker-than, recoverable contact, legal rewrite) | July-3 claude.ai thread, relayed verbatim into the ultracode session | **UNDEPOSITED — exists in no repo or Notion page. The "spec ruling" is a pending Pratyush decision, not a document.** |
| Two-axis indexing (provenance band × quantification domain) | same thread (named there as a session articulation of archive practice) | UNDEPOSITED as a named rule; components exist in archive practice |
| Fact-decay catalogue (5–6 named relay-loss instances) | same thread | UNDEPOSITED except the one-line repo echo above |
| Detachability finding ("finite math stands without the ontology") | same thread, asserted as an early ratified finding | RELAY-VERBATIM; archive anchor not independently verified by ultracode |
| Three-frontier separation (Selection/Derivation/Characterization); four-layer architecture (Object/Presentation/Selection theorem/Ledger) | same threads | UNDEPOSITED; partially instantiated by `physics/enumeration-replication/` |
| "New name needed" (the label "Layer 1" collides with the Field Architecture's 16 stations) | same thread | UNDEPOSITED |

### Domain 3 — reversible-contact repo (canonical on Pratyush's machine; mirror branch `governance-repin`)

| Concept | Address | Status |
|---|---|---|
| Ledger C entry 1 + forbidden-readings clause | `LedgerC/entry_001.md`; Ledger E row 2026-07-11: "entry carries its own forbidden-readings clause (blocks the identification the architecture's invariant prohibits)" | VERIFIED on `governance-repin` (b8d4d45) |
| Governance v2 freeze, manifest, independent hash verification arc | `MANIFEST.sha256.json`, `GOVERNANCE-VERSION.json`, `LedgerE/evidence_log.md` — commits eced7e5 (re-pin) + 2ca1370 (verification row, 16/16) | VERIFIED + AUTHORED (2ca1370) by ultracode |

## Consequences for the automation loop

1. **Cowork can verify Domain 1 directly** — it has the Notion connector; the
   page ids above are fetchable. No trust relay needed.
2. **Domain 2 is the real gap** and has been since the 2026-07-09 state sync:
   the fresh design exists only in chats. Fix = deposit (this map is step 1;
   the spec skeleton at `.automation/candidates/` is step 2; the full
   thread transcripts via the chat-archive handoff protocol is step 3).
3. **Domain 3 hygiene:** Cowork should fetch `mirror/governance-repin`
   (it reported only `main` and the ultracode branch); Pratyush should pull
   2ca1370 into the canonical repo.
4. Standing loop unchanged: Cowork = courier/resonance-driver, ultracode =
   compute/verify, ChatGPT = adversarial opinion, Pratyush = all Tier-3 acts.
