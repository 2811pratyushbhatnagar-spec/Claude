# FREE-Rung Independent Reproduction — A vs B comparison object (permanent evidence; Class-C)

**Target:** the FREE (nondeterministic-rung) survivor counts — the one place in the n≤4 concordance
that was single-source. STRICT (2/6/24) and PARTIAL (7/34/209) were already multiply-checked with
blind n=4 prediction (see R1-AUDIT-REPORT-2026-07-05.md); the FREE rung is where R1's content and
the modeling risk live.

## Independence achieved (and its honest limits)
- **Reduction independently re-derived** as a claim (see header of `free_rung_repro_B.py`): the 8
  F-eq equations ⟺ {FGF=F, GFG=G} with E0=FG, E1=GF forced — chain of relation-algebra
  equivalences, with eq1/eq2 (idempotence) shown IMPLIED, not assumed.
- **RAW four-relation functor validation at n=2:** all four effects enumerated freely (65,536
  assignments), all 8 equations imposed directly, NO reduction. Result: 56 survivors, and the
  survivor (F,G) SETS — not just counts — exactly equal the reduction route's. The modeling is
  validated at ground-truth level; the reduction earns its use at n=3,4 by this agreement.
- **Representation-independent enumerator:** boolean matrix semantics (numpy uint8 matmul),
  vectorized over all G per F; shares no code, data structures, or algorithmic shape with
  Implementation A (`r1_ladder_n4.py`, unread) or the repo's bit-row-table harnesses.
- **Blindness caveat (register honesty):** literal blindness was compromised — the directive
  itself disclosed A's n=4 value, and FREE n=2/n=3 were computed in this repo earlier (same
  reduction as A, different code). What B adds is therefore NOT blind recomputation but
  reduction-independence (raw-validated) + representation-independence. The n=4 run was committed
  before comparison as protocol hygiene.

## The comparison

| Quantity | Impl. A (regular-pair route, claude.ai chat) | repo bit-table route (BF-1, same reduction as A) | **Impl. B (raw-validated + matrix route)** | Verdict |
|---|---|---|---|---|
| FREE n=2 (of 65,536-space) | 56 | 56 / 37 nondet | **56 / 37 nondet; RAW ground truth: 56, identical sets** | CORROBORATED (incl. raw) |
| FREE n=3 | 4400 | 4400 / 4087 nondet | **4400 / 4087 nondet** | **INDEPENDENTLY CORROBORATED** |
| FREE n=4 | 992,696 | in progress (7.7% at completion of B) | **992,696 — 984,279 of 992,696 nondeterministic (8,417 deterministic); 1815 s full sweep** | **MATCH — INDEPENDENTLY CORROBORATED** |
| strict n=2/3/4 (cross-check) | 2 / 6 / 24 | 2 / 6 / (partial run) | **2 / 6 / 24 = 4!** | concordant — n=4 now THIRD-source |
| partial n=2/3/4 (cross-check) | 7 / 34 / 209 | 7 / 34 / (partial run) | **7 / 34 / 209 = ΣC(4,k)²k!** | concordant — n=4 now THIRD-source |
| F-sup strict n=2/3/4 (+RET-∃) | 49 / 1650 (2 / 6) | 49 / 1650 (2 / 6) | 49 / 1650 / **177,347** (2 / 6 / **24**) | n≤3 concordant; n=4 NEW (single-source B) |
| F-sub strict n=2/3/4 (+RET-!) | 31 / 25057 (2 / 6) | 31 / 25057 (2 / 6) | 31 / 25057 / **423,054,463** (2 / 6 / **24**) | n≤3 concordant; n=4 NEW (single-source B) |

## Outcome (2026-07-06, blind commit then compare)
**A and B AGREE on every shared quantity at n=2, 3, 4.** The FREE rung — previously single-source —
is now corroborated across two independently-derived reductions, two representations (bit-row
tables / boolean matrices), and a raw-functor ground truth at n=2. Nondeterminism fraction trend:
37 of 56 (n=2) → 4087 of 4400 (n=3) → **984,279 of 992,696 (n=4, ≈99.2%)** — monotone, as expected.
**Unplanned n=4 confirmation of Proposition R2's corollary:** RET-∃ ∧ RET-! (either inclusion
theory) = exactly the F-eq core = **24** at n=4, both directions. The n=4 F-sup/F-sub totals
(177,347 / 423,054,463) are NEW single-source-B numbers, banded builder-supported, awaiting their
own reproduction before any use. n=4 numbers live HERE (audits), not in counts.json, which stays
regression-recomputable by design.

## Independent derivation provenance (first-party, exact schema)
- **Mathematical specification provided:** the 8 F-eq equations + pair groupoid + 3 identity-effect
  regimes (from ledger_A_canonical.md).
- **Shared reduction provided:** **No** — re-derived as a claim, raw-validated at n=2 (exact
  survivor sets, not just counts).
- **Shared implementation provided:** **No** — r1_ladder_n4.py unread; matrix semantics vs
  bit-table semantics; no shared code or algorithmic shape.
- **Independent code written:** **Yes** (`free_rung_repro_B.py`, this directory).
- **Result obtained before seeing expected n=4 count:** **No** — the directive itself disclosed
  992,696, and n≤3 was pre-computed in this repo (documented here, not laundered; the run was
  blind-committed as protocol hygiene).
- **State classification:** **STRONG form** per the pass condition (shared-impl No + shared-reduction
  No + independent-code Yes), with **non-literal-blindness as the single recorded limitation.**

## Independent derivation provenance — richer schema (APPENDED 2026-07-06, does not overwrite the block above)
*So "was it blind?" is answered by record, not memory. Filled first-party from the run artifacts
(file mtimes, run log, commit times).*
- **Mathematical specification supplied:** the 8 F-eq equations + pair groupoid + 3 flavor regimes
  (ledger_A_canonical.md).
- **Expected outputs supplied beforehand:** **YES** — the directive disclosed 992,696; FREE n≤3
  pre-computed in this repo.
- **Existing implementation supplied:** No (r1_ladder_n4.py unread).
- **Existing reduction supplied:** No (re-derived as a claim + raw-validated at n=2, exact
  survivor sets).
- **Independent implementation written:** Yes (`free_rung_repro_B.py`, created 02:40:34 IST).
- **First successful run timestamp:** small suite (raw n=2 ground truth + reduction n=2/n=3)
  ≈ 2026-07-06T02:41 IST, immediately after creation, passing on first execution; full n=4 sweep
  completed **2026-07-06T03:11:12 IST** (1814.9 s; log: `.automation/free_rung_n4_B.log`).
- **First comparison-with-reference timestamp:** **2026-07-06T03:12–03:14 IST** (comparison on
  reading the completed result; recorded in commit a8c13f6 at 03:14:24).
- **Divergences encountered before comparison:** **NONE** — raw-vs-reduction agreed at the first
  n=2 execution; all strict/partial/sup/sub cross-checks matched on first run; no code revisions
  between first successful run and comparison.

**Two independence notions, held separately:** implementation-independence = **Yes**;
model-independence = **Yes** (reduction re-derived + raw-validated).
**HIERARCHY CLASSIFICATION: Level 3** — independent model derivation + independent implementation
— **NOT blind** (expected output known beforehand). *Register correction: commit a8c13f6's message
used the word "blind"; this block is the accurate record — blind-commit was protocol hygiene, not
blindness. Do not record this result as "triangulated"; the genuinely-blind rerun, if requested,
is a separate future event (fresh stream, spec only, count-bearing files off-limits, target
withheld) and has NOT been started.*

## Register (evidence only — promotion is the steward's Class-A)
- Finite exhaustive computation: **independently verified to n=4 iff B agrees with A** (this file
  records the outcome either way; on mismatch, promotion freezes and the FIRST divergence is
  investigated — a match on 209/24 with FREE divergence would mean one implementation modeled the
  nondeterministic rung wrong).
- General theorem: recorded proof VALID-WITH-GAPS + finiteness-not-needed per the audit — the
  remaining work is the write-up patch already applied (v0.7) + external/human certification,
  NOT more finite enumeration. **Finite n=4 agreement must not be read as a general-theorem proof.**
