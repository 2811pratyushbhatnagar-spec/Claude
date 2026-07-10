# Enumeration Replication — Third Independent Environment (2026-07-09)

**Band:** EXACT (finite exhaustive computation) · **Status:** verification deposit, additive
**Source:** script transcribed verbatim from the 2026-07-03 session artifact
("Enumeration rerun — 2026-07-03"), relayed through conversation; executed in the
remote Claude Code container on 2026-07-09.

## What this is

An independent replication of the selection-theorem enumeration, in a third
environment:

1. April 2026 — original session "Axiom formulation audit and recovery"
   (primary deposit unlocated; provenance object).
2. 2026-07-03 — first independent rerun (session container, local lane).
3. 2026-07-09 — **this replication** (remote container, transcribed script).

The replication also passes through the lossy channel the project has been
auditing (conversation relay): the script survived relay byte-faithfully enough
to reproduce every recorded number, which is itself a data point for the
fact-decay ledger — code survives relay better than facts.

## Results — all recorded checkpoints reproduce

| Checkpoint | Recorded | This run |
|---|---|---|
| Tables with ν·ν = E pinned | 6561 | 6561 |
| Associativity survivors | 17 | 17 |
| After FGA (E·E ≠ E) | 2 | 2 |
| After AR (any of R₀/R₁/R₂) | 1 | 1 |
| Unique survivor | a·b = a+b+1 mod 3 | identical |
| Identity forced | I = 2, two-sided | [2] |
| ν↔E automorphism forced | yes | True |
| Group structure (Latin + assoc + id) | yes | True |
| E·E = ν and ν·E = E·ν = I forced | yes | True |
| FGA redundant given AR at n = 3 | claimed | AR alone: 17 → 1 (all three readings) |
| \|Ω\| = 2 exclusion | 0 survive | 0 under every FGA reading |
| Rival table (the "second survivor") | absorber | rows (1,2,2),(2,2,2),(2,2,2) — I an absorber |

Fingerprint scan: exactly three (FGA, AR) pairs reproduce the full recorded
cascade — FGA = E·E ≠ E with AR ∈ {E·E = ν; ν and E each generate; verbatim
non-idempotent-generation} — confirming the 2026-07-03 finding that the three
AR readings are extensionally equal on the operative domain (the 17
associative tables) while globally distinct. The stronger April-28 FGA
paraphrases give 1, not 2, from the 17 — confirming they are not the original
filter.

## Does not claim

- Does not replace the April 2026 primary deposit (still wanted as a citable
  provenance object).
- Does not verify that the hypothesis set (associativity + FGA + AR) follows
  from the source axiom — F1 remains open exactly as recorded ("one axiom +
  three structural principles").
- Does not touch the independence of the Gate-D conditional route to the same
  object.

**Reproduce:** `python3 enumeration_rerun.py` (stdlib only, seconds).
Output archived verbatim in `output.txt`.
