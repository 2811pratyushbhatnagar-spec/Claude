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

---

# Round 2 addendum — broadened R4b-S + process-level R4b-P (2026-07-12)

**Input status:** Round-2 spec received in relay OUTLINE only (queue file
`ULTRACODE-QUEUE-MON-PHASE-A-2026-07-11.md` not yet on the shared branch);
the broadened readings below are ultracode's DECLARED stand-in mechanizations
— diff against the §-exact text on push. D_arrow/D_SQDB machinery (§13–16)
likewise unpushed; R4b-P handled by a dilation argument instead, flagged.
Artifacts: `round2_r4b_broadened.py`, `round2_output.txt` (verbatim).

## Results

1. **Subsystem reading** (record = free tensor factor; compatibility =
   P_act = P_c⊗I): passes exactly where a compatible basis-aligned
   factorization exists — M1 D=4 and M2b D=4 pass **by becoming** 2⊗2 with
   content-only activeness (structurally identical to M3-content); M1 D=2,3
   fail for dimension reasons (no factorization); **M3's own §7 orientation
   predicate (P⊗Q) is INCOMPATIBLE with the subsystem reading** — it ties the
   record factor, so even the doubled carrier passes only after relaxing its
   predicate to content-only (P_act = P_c⊗I). Round-1 conjecture confirmed
   and sharpened: single carriers pass only by covertly being M3, and M3
   itself needs a predicate revision for its doubling to do the work.
2. **Write-protection: 0 survivors under every reading.** The subsystem
   record stays forgeable — I⊗X writes the flag without any rejection
   (machine-confirmed). Room and write-protection are independent.
3. **Multiplicity reading ≡ Round-1 R4b-weak** (structural identity; spot
   check consistent). Dimension artifact, unchanged.
4. **Superselection reading: structurally impossible** — R5 forces W and W₊
   into the same (active) sector; a sector label can never fire on one and
   not the other. One-line proof, no enumeration needed.
5. **R4b-P via dilation (machine demo):** a retained instrument outcome is
   storage; storage is an ancilla; the dilated M1 (system⊗record-qubit) is
   *verbatim* M3-with-content-predicate — R3, renewal, record-set all pass,
   and the forgery (I⊗X) comes along too. **Process-level recording is not a
   third way: it IS doubling, by Stinespring.** Caveat: if the queue file's
   R4b-P (D_arrow/D_SQDB-based) differs from record-retention, rerun needed.

## Answer to Round 2's decisive question

Does M3 ever pass on process-level grounds where no generalized state-level
record can? **No — because the two routes coincide.** Every reading sorts
into exactly two independent requirements:
- **ROOM:** a record needs a free tensor factor with content-only activeness.
  This forces M3-structure — natively, by reinterpretation (composite dims),
  or by dilation (process retention). Prime-dimension single carriers are
  excluded outright. *The Register-Doubling Gap's positive half lives here.*
- **WRITE-PROTECTION:** no state, subsystem, sector, or dilated record
  certifies that rejection *occurred* while the record factor is freely
  writable. This is not a carrier property at all — it requires an
  admissibility constraint (record-factor write access coupled to rejection
  events). *Phase-B's real target: an Adm-structure axiom, e.g. "the only
  admissible operations touching H_record are those induced by R3-passing
  events on H_content" — under which the forgery census should collapse.*

Register note: nothing here promotes anything; MoN lane, non-canon;
predicate-revision suggestion for M3 (P_act = P_c⊗I) is a proposal for the
Journal, steward's call.
