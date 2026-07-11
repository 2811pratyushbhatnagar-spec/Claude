# Destroy-Protocols — infrastructure, NOT evidence (none frozen yet)

*A destroy-protocol is versioned and frozen INDEPENDENTLY of any result it tests. It is
infrastructure: the pre-registered, per-result-type standard that destroy-attempts must exhaust
(substantial-result checklist criterion 3). It is never evidence about the result.*

**Strict lifecycle (timestamp/hash-enforced by test_consistency):**
```
protocol.frozen_at  <  run.started_at  <  evidence.collected_at  <  promotion.proposed_at
```
A promotion proposal violating this order is **INADMISSIBLE as a substantial-result candidate** —
the guard fails it mechanically. Retroactive protocols cannot bless already-run attempts.

**Freezing a destroy-protocol is a Class-A (human) act** — it is the per-result-type instance of
the checklist bar and belongs to Pratyush's freeze signature. **No protocol is frozen yet.**

## Protocol object (one json per result-type, in this directory)
```json
{
  "result_type": "enumeration | proof | null-result | ...",
  "version": "0.1",
  "standard": ["list of destroy-attempts that MUST be exhausted"],
  "frozen_at": null,
  "frozen_by": null
}
```
`frozen_at`/`frozen_by` are set ONLY by the steward. Automation may DRAFT protocol files
(frozen_at = null) as Class-B proposals; it may never set the freeze fields.

## Promotion proposal object (`.automation/promotion_proposals/*.json`)
```json
{
  "item": "Q-...", "protocol": "protocols/<type>.json",
  "run_started_at": "...", "evidence_collected_at": "...", "proposed_at": "...",
  "packet": { "produced_at": "...", "producer": "...", "repo_head": "...", "dep_hashes": {} }
}
```
