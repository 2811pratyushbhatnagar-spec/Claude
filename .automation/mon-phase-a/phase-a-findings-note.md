# Phase A — Rejection Predicate R1–R5: Harness Findings

**Register:** non-canon, Tier-3 worker computation, MoN lane (separate framework;
no reversible-contact canon touched). **Frozen input:** R1–R5 + determinacy +
M1/M2a/M2b/M3 as relayed verbatim from `Journal/mon-two-nothing-kernel-2026-07-11.md`
§7–§8 (2026-07-12). **Artifacts:** `phase_a_harness.py`, `phase_a_output.txt`
(verbatim). All checks exact (1e-9), ray-deduplicated, exhaustive over the
declared candidate families (a stated discretization of U(D): signed
permutations + DFT ± named candidates; M3 adds A⊗B, S·(A⊗B), S). No silent
caps: the D=3 doubled-carrier family drops per-entry signs (declared in-code).

## Headline answer to the frozen open question

> "Does R3 alone (or R3+R4b together) discriminate M2 from M3, or does the
> discrimination require something the exhaustive sweep hasn't been asked to check?"

**Neither R3 nor R3+R4b discriminates M2 from M3. Every discrimination the
sweep found is a predicate-shape or dimension artifact, orthogonal to
single-vs-doubled carrier topology. The discrimination requires a condition
R1–R5 does not contain.** Specifically:

1. **R3 discriminates predicate symmetry, not models.** Swap fails R3 under the
   swap-invariant predicate (confirmed: A(SW)=1) and passes under the
   orientation predicate (confirmed) — but M1, M2b, and M3 all pass R3 with a
   suitable disjoint active/inactive designation. R3 is a property of the
   (predicate, candidate) pair; every model can be given a predicate that
   makes it pass.
2. **R4b-weak (state-record reading) tracks rank(P_act) ≥ 2, nothing else.**
   Survivors: M1 D=3 |act|=2 → 1; M1 D=4 |act|=2 → 2; M2b D=4 (2/2 split) → 2;
   M3 D=3 orientation rank-2 → 2. Zero survivors at every rank-1 active
   designation (M1 D=2, M2b D=2, M3 D=2 orientation) — including the doubled
   carrier. Reason: the successor must return to A=1 while a fixed flag
   distinguishes it from W; that needs ≥ 2 orthogonal rays inside the active
   region — recycling room, not register doubling.
3. **R4b-strong (history-record / unforgeability reading) annihilates every
   model: 0 survivors everywhere.** With the full declared family admissible,
   every successor reachable via a rejection is also reachable by a
   rejection-free candidate, so no state-borne flag can certify that rejection
   *occurred*. Records-as-states are forgeable in all four models alike.
4. **Determinacy, where it holds, is also a dimension artifact:** |J|/~op = 1
   exactly when the inactive region has dimension 1 (M1 D=3), and > 1
   otherwise. It measures the size of the target region, not the model's
   structure.
5. **M2a fails R4b-weak at both sizes tested** — its frame-ray-set predicate is
   non-projective (flagged in the model definition itself) and too rigid for
   any renewal+flag pair in the declared family. This is the one genuine
   per-model separation the sweep produced, and it separates M2a from
   *everything*, in the failing direction.

## What the missing condition is (Phase-B candidate, stated precisely)

R1–R5 never asks the record to be a **subsystem**. R4b as frozen accepts any
flag observable; the sweep shows that reading collapses into either
active-region dimension (weak) or universal forgery (strong). The natural
repair: require the trace to live on a tensor factor **commuting with the
renewed active content** — record readable without disturbing the new whole.
Under that condition the doubled carrier is no longer optional decoration:
a record-subsystem + active-subsystem decomposition *is* carrier doubling,
demanded intrinsically. Conjecture for Phase B (unproved here): with
R4b′ := "∃ tensor factorization H ≅ H_content ⊗ H_record, compatible with the
active designation, flag supported on H_record," M3 passes and M1/M2 pass only
by covertly *becoming* M3 (choosing a factorization is choosing a second
register). If so, the Register-Doubling Gap lives in R4b′, and the
graph-projection negative result is untouched (uniqueness still doesn't
produce the gap; the record requirement does).

**Register-2 resonance, logged not claimed:** this is the dynamical twin of
the banked Tower-page line "points cost summands — spatial multiplicity is
literally the composition import." Phase A's version: **records cost
registers.** Same shape, different carrier; identity refused without a
construction, per house rule.

## Constraint honesty

- The candidate family is a finite discretization of a continuous group;
  passing/failing here is exhaustive over the family, indicative for U(D).
  Conditions R2/R3/R5 are ray-conditions where this is harmless; R4b-strong's
  forgery check can only get *harder* with more admissible candidates, so its
  universal failure is robust under enlargement. R4b-weak existence results
  could in principle gain witnesses in the continuum — the rank-1 failures are
  proved by dimension counting, not by family limits, so they stand.
- CP-but-non-unitary candidates were not enumerated (R4a restricts to
  invertible-admissible anyway; noted).
- Determinacy used ~op = ray equality on the fixed W (declared); coarser
  operational equivalences would only merge classes, never split them.
