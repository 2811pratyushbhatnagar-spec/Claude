# Ledger A Reconciliation — 2026-07-04 · FROZEN SNAPSHOT

**Governance (rule in force from this date):** reconciliation notes are frozen, dated snapshots. Any later
correction is a NEW dated note; this file is never edited.

## Scope
Reconciles my frozen Ledger A (W-series, `ledger_A_math_v0.1_frozen.md` → `ledger_A_math_v0.2_canonical.md`)
against Pratyush's parallel construction (R-series, `ledger_a_verify.py`, exhaustive over all 65,536
step-dynamics on the minimal transitive groupoid).

## Caveat (load-bearing)
`ledger_a_verify.py` was **not on disk** at snapshot time (Desktop-wide search). All numbers below are my
**independent reproduction** of the specified experiment (`ledger_A_round2.py`), not a code diff. The
exact-number diff against his output is **pending** and will be a new dated note.

## Findings — full agreement, no disagreements found

1. **Strict functoriality ⇒ deterministic/bijective dynamics + both undos.** My counts: |S|=2 strict
   identities: 2 survivors (the 2 bijections with inverse transposes); full 65,536 space restricted to
   strict ids agrees; |S|=3 (262,144 pruned pairs): 6 = 3! survivors, all total bijections, EI-strong,
   RET-∃, RET-! all hold.
2. **Oplax (composed ⊆ composite, canonical F-sup): return-exclusivity free, return-existence underivable.**
   |S|=2: exclusivity 49/49, existence 2/49. |S|=3: 1650/1650 vs 6/1650. Also deposited: the unstated dual —
   F-sub gives existence free (31/31; 25057/25057), exclusivity underivable (2/31; 6/25057).
3. **Invertible algebra ≠ undoable dynamics.** Same groupoid algebra across the whole space; with identities
   free, F-eq has 56 survivors of which 37 nondeterministic (witness: E0={(a,a)}, E1={(b,b),(b,b2)},
   F={(a,b),(a,b2)}, G={(b,a)}).

## Notation reconciliation (adopted into the canonical ledger)
- His *existence/exclusivity* = state-level Δ-inclusions (canonical **RET-∃**, **RET-!**) — distinct from my
  relation-level converse-inclusions (**EI-w1**, **EI-w2**); both pairs retained.
- His *oplax* = **F-sup** (composed ⊆ composite); dual **F-sub**; frozen choice **F-eq**.
- His R-series (enumeration findings) and my W-series (independence witnesses) are complementary methods
  over the same object; both carried in the canonical ledger.

*Snapshot frozen 2026-07-04. Register: internal computation, not refereed.*
