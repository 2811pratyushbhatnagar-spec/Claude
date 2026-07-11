# Ledger-A R1 / |S|=3 / n=4 enumeration — BLOCKED (needs your input)   [non-canon]

The automation queue lists *"n=4 enumeration / convergence probe"* and priorities.md lists
*"R1 general proof beyond |S|=2"* and *"|S|=3 replication"*. I did **not** implement these, on purpose.

**Reason.** The Ledger-A objects — the reversible-contact signature, the exact R1 statement, and
the W-series witnesses (W1–W3) referenced in ARCHITECTURE.md — are not present in this repo
(`LedgerA/` is empty). Writing an enumerator would require inventing that signature, which would
violate the framework's own honesty register ("prove, don't define"; import no primitives).

**What is done instead.** The CSS convergence probe (`Experiments/enumerate.py`) extends the
*proven* carry-set check to higher bounds (ran clean to e≤400 on 2026-07-05; supports `--bound`
for overnight runs to e≤2000+). That is a real, reusable convergence probe for the carry-set line.

**To unblock the Ledger-A enumeration**, drop into `LedgerA/` (or point me at the private kernel
ledger) any of: the signature + axioms, the exact R1 statement, and the intended meaning of `|S|`
and `n`. Then I can write a finite-model enumerator that checks R1 as `|S|` grows — draft/evidence
only, with promotion staying Tier-3, yours.
