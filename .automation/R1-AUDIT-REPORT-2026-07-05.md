# R1 INDEPENDENT AUDIT REPORT — 2026-07-05

**NON-CANON. PROCEDURES ONLY.** This document records an automated independent audit of
Theorem R1 (Ledger A, reversible-contact, frozen v0.2). It is evidence, not governance.
It admits nothing to any ledger, promotes nothing, and alters no frozen text. All
Tier-3 decisions (conjecture -> theorem promotion, ledger admission, wording of
status.json) belong to the steward (Pratyush) alone.

**Inputs synthesized:** (a) harness reproduction of `ledger_A_witnesses.py` and
`ledger_A_round2.py` as-is (both exit 0, no assertion failures); (b) three blinded
step-by-step proof audits in relation algebra, run without sight of each other;
(c) two from-scratch enumerators (no harness code reuse) at
`C:\Users\Bhatnagar\Desktop\New folder (2)\framework\LedgerA\audit_enum_independent.py` and
`C:\Users\Bhatnagar\Desktop\New folder (2)\framework\LedgerA\audit_enum_n4.py`,
including an n=4 probe beyond all deposited data.

---

## 1. Verdict on the general proof

**VALID-WITH-GAPS (unanimous, 3/3 blinded audits).**

The theorem R1 is TRUE: under strict identities, the F-eq system forces
`R;S = Delta_dom` and `S;R = Delta_cod`, and any such pair (R,S) consists of the graph
of a bijection f and the graph of f^-1, with S = R^T, RET-existence and RET-uniqueness
both holding. Every auditor independently reconstructed a complete correct proof and
failed to break the theorem (attacks tried: branching return R={(a,b),(a,b2)},
S={(b,a)}; successor shift on N; doubling map; mixed inclusion weakenings; non-square
fibers; identity-vs-swap packaging counterexample). The RECORDED proof text, however,
is not yet a complete proof. Union of all gaps found, each with patchability:

| # | Gap (union across 3 audits) | Severity | Patchable? |
|---|---|---|---|
| G1 | Final sentence "Total + single-valued + injective both ways => bijection with S=R^T" is an **invalid inference form** standalone. Machine-checked counterexample: R = identity graph, S = swap graph on 2 points — all listed properties hold, S != R^T. Step only goes through by re-invoking R;S=Delta_dom, S;R=Delta_cod. | Highest (invalid form, true conclusion) | YES — ~3 lines |
| G2 | **Surjectivity of R never derived.** Needed for "bijection"; follows in one line from Delta_cod <= S;R (for each b, some a0 has (a0,b) in R). Absent from the text; smuggled inside G1's packaging. Repairing via finite counting instead would covertly import finiteness + equal fibers — must patch via the Delta_cod line. | High | YES — 1 line |
| G3 | **S = R^T asserted, not derived.** Both inclusions (S <= R^T via R-totality + S;R <= Delta_cod; R^T <= S via return witness + single-valuedness) missing from the text. | High | YES — 2 lines |
| G4 | Parenthetical "(totality of the return at a)" is a **mislabel**. The fact used is the RET-existence instance (a,a) in R;S supplied by Delta <= R;S — NOT totality of R,S. Machine-checked: totality alone admits round trips landing elsewhere (R={(a1,b1),(a2,b1)}, S={(b1,a1)}) and even nondeterministic R (R={(a,b1),(a,b2)}, S=empty passes R-total + S;R<=Delta). Step is justified only because Delta <= R;S was derived one sentence earlier. | Medium (wording; a reader could reconstruct an invalid argument) | YES — rewording |
| G5 | "Injectivity is symmetric via Delta_cod" **compressed to five words.** Symmetry is genuine (axiom pair invariant under (R,S,A,B)->(S,R,B,A) composed with transposition) but the mirror argument uses the OTHER two inclusions; all four inclusions of the two equations are individually load-bearing (ablation-verified at unequal fibers). The text also silently needs the same swap for single-valuedness of S. | Medium | YES — exhibit mirror step + one remark |
| G6 | **Implicit 8-to-2 reduction unstated.** The proof uses F-eq only at the inverse composites; the other six equations are tautologies under strict identities (Delta is a two-sided unit, idempotent). Machine-verified (identical survivor sets, 2 at n=2 / 6 at n=3, whether 8 or 2 equations imposed). Note: non-strict regimes do NOT permit this reduction — the FREE nondeterminism witness lives exactly there. | Low (true, trivial, but an auditor must check it) | YES — 1 remark |
| G7 | **EI-strong claimed without definition/discharge in the proof body.** Under the harness definition (`ledger_A_witnesses.py` line 74: step(c') = exact converse of step(c)) it coincides with S=R^T and follows from G3's patch, but the theorem lists it as a separate conclusion never discharged by name. | Low | YES — cite definition, note equivalence |
| G8 | **Hypothesis overstatement** (not a soundness gap): the theorem is local — any isomorphism pair in Rel (R;S=Delta_A, S;R=Delta_B) is a bijection pair. No groupoid transitivity, second object, or fibration structure is consumed. | Informational | Optional remark |
| G9 | **Edge cases unstated:** unequal fibers make the hypotheses unsatisfiable (0 survivors at all sizes <= 3, |A| != |B| — exhaustively verified); S0=S1=empty yields the empty bijection. Harmless because the proof is elementwise. | Low | YES — 1 remark |

**All gaps are patchable with ~8 lines total of added text; no gap threatens the
theorem's truth.** The correct patched proof was independently written out in full by
all three auditors and the reconstructions agree step for step.

---

## 2. Finiteness

**NOT NEEDED (unanimous: finiteness_needed = false in all three audits).**

Every step of the (patched) proof is a pointwise membership argument: no counting, no
"injective endo of a finite set is onto", no axiom of choice (f is defined by unique
existence, not selection). Therefore the audit supports the **strengthening**:

> **R1 holds for arbitrary state sets** (any cardinality, including infinite, and
> a priori different fibers). When the hypotheses hold, |States(I0)| = |States(I1)|
> is a *consequence* (the bijection), not a hypothesis.

Caveat tied to G2: this strengthening survives ONLY if surjectivity is patched via the
`Delta_cod <= S;R` line. A counting repair would silently confine R1 to finite equal
fibers. Infinite attacks (successor shift, doubling map) are each blocked pointwise by
the same two-move pincer: Delta <= composite manufactures a return witness; composite
<= Delta collapses it onto every competitor.

---

## 3. Enumeration concordance

Four independent sources: deposited v0.2 counts; harness re-run (as-is, exit 0);
from-scratch enumerator (bitmask encoding, no harness reuse); n=4 probe
(constraint-propagation enumerator, predictions made before running).

| Quantity | Deposited v0.2 | Harness re-run | From-scratch | Match |
|---|---|---|---|---|
| STRICT F-eq survivors, n=2 (of 256 (R,S) pairs) | 2 | 2 | 2 (both bijections, S=R^T: id, swap) | YES |
| STRICT F-eq survivors, n=3 (of 262,144) | 6 = 3! | 6 | 6 (all bijections, S=R^T) | YES |
| PARTIAL survivors, n=2 (full 4,096 space) | 7 | 7 (7/7 partial bij., 0 nondet, ids forced to dom/ran sub-diagonals) | 7 = sum C(2,k)^2 k! | YES |
| PARTIAL survivors, n=3 | 34 | 34 (34 partial bij., 0 nondet) | 34 = sum C(3,k)^2 k! | YES |
| FREE F-eq survivors, n=2 (65,536 space) | 56 | 56 | 56 | YES |
| FREE nondet survivors, n=2 | 37 | 37 | 37 (see definitional note below) | YES |
| FREE nondet witness | E0={(a,a)}, E1={(b,b),(b,b2)}, R={(a,b),(a,b2)}, S={(b,a)} | verbatim | in survivor list, all 8 eqs pass, nondet | YES |
| STRICT F-sup survivors, n=2 / n=3 | 49 / 1650 | 49 / 1650 | 49 / 1650 | YES |
| STRICT F-sub survivors, n=2 / n=3 | 31 / 25057 | 31 / 25057 | 31 / 25057 | YES |
| RET fractions, F-sup: n=2 RET-! / RET-E | 49/49, 2/49 | via supplementary ret_check.py (see sec. 5) | 49/49, 2/49 | YES |
| RET fractions, F-sup: n=3 | 1650/1650, 6/1650 | ret_check.py | 1650/1650, 6/1650 | YES |
| RET fractions, F-sub: n=2 RET-E / RET-! | 31/31, 2/31 | ret_check.py | 31/31, 2/31 | YES |
| RET fractions, F-sub: n=3 | 25057/25057, 6/25057 | ret_check.py | 25057/25057, 6/25057 | YES |
| F-eq RET (both), n=2 / n=3 | 2/2, 6/6 | confirmed | Delta exactly, trivial | YES |

**n=4 probe (beyond all deposited data — genuine prediction test):**

| Quantity | R1 prediction | n=4 result | Match |
|---|---|---|---|
| STRICT F-eq survivors | n! = 24, all bijections, S=R^T | 24, 0 structure violations | YES |
| PARTIAL F-eq survivors | sum C(4,k)^2 k! = 209, all partial bijections, S=R^T, 0 nondet | 209; per-k breakdown {0:1, 1:16, 2:72, 3:96, 4:24} termwise = C(4,k)^2 k!; ids forced to Delta_dom/Delta_ran | YES |

**Zero numerical discrepancies across all four sources.** Two definitional caveats
(neither a count mismatch):

- **Nondet-count reading:** deposited "37 nondeterministic" (FREE n=2) means "some
  effect among E0,E1,R,S not single-valued" (equivalently "R or S not single-valued"
  — also 37). Under the narrower "R alone not single-valued" reading the count is 25.
  Deposit wording could pin this down.
- **w1/w2 vs RET:** `ledger_A_round2.py` prints w1/w2 (converse-containment predicates:
  F-sup n=2 7/49, n=3 34/1650; F-sub n=2 7/31, n=3 265/25057), which are DIFFERENT
  predicates from the deposited RET fractions and must not be conflated. RET was
  verified by a supplementary read-only script (see sec. 5).
- Minor: the "256 (R,S) pairs" phrase for n=2 strict is implicit in the harness
  (16x16), not echoed as a printed `space=` line. Consistent.

---

## 4. RECOMMENDED confidence band for status.json

**Recommendation (wording only — adoption is Tier-3, the steward's alone):**

> R1: **proof-audited / theorem-grade evidence** — recorded proof VALID-WITH-GAPS
> (3/3 blinded audits; all gaps expositional and patchable, none touching truth);
> corroborated by independent exhaustive enumeration at n=2,3 (all counts concordant
> with deposit) and a successful blind n=4 prediction (24 = 4! strict, 209 =
> sum C(4,k)^2 k! partial); finiteness NOT required — holds for arbitrary state sets
> with |fibers| equal as a consequence. **Pending: patch of recorded proof text
> (gaps G1-G9) before any promotion.**

Suggested band: move from "conjecture (machine-checked small cases)" toward
"proved modulo recorded-text patch; enumeration-corroborated n<=4; cardinality-free".
Do NOT word it as "theorem" until the frozen text is patched in a new ledger version
(v0.2 is frozen; a patch means v0.3, a steward action).

**Explicitly: promotion conjecture -> theorem is a Tier-3 decision. This audit takes
no governance action. Ledger A remains frozen at v0.2. The call is Pratyush's alone.**

---

## 5. What remains open

1. **Proof-text patch (G1-G9)** in a steward-issued Ledger A v0.3: the ~8 missing
   lines (surjectivity via Delta_cod <= S;R; both S=R^T inclusions; reword the
   "(totality of the return at a)" parenthetical to cite Delta <= R;S / RET-existence;
   exhibit the mirrored injectivity step; state the 8-to-2 reduction; define and
   discharge EI-strong; optional locality and edge-case remarks).
2. **`ledger_a_verify.py` diff / harness RET printing:** `ledger_A_round2.py` as-is
   does not print RET-existence / RET-uniqueness — only the distinct w1/w2 predicates.
   The deposited RET fractions currently rest on a supplementary scratchpad script
   (`ret_check.py`, read-only, harness untouched) plus the from-scratch enumerators.
   Open item: fold RET printing into the canonical harness (or deposit ret_check.py
   alongside it) so the deposit is reproducible from canon scripts alone. Any change
   to canon harness files is itself a steward decision.
3. **Nondet-definition pin-down** in the deposit wording (37 = any-effect reading vs
   25 = R-only reading), so future audits cannot diverge on the predicate.
4. **Deposit the audit enumerators** (`audit_enum_independent.py`, `audit_enum_n4.py`,
   both under `framework\LedgerA\`) if the steward wants the n=4 evidence in canon;
   until then they are audit artifacts only.
5. **Optional hardening:** a machine-checked formalization (e.g. Lean/Coq) of the
   patched pointwise proof would close the gap class permanently; not required by
   this audit's verdict.
6. **Not open:** no numerical discrepancy anywhere; no counterexample candidate
   survived; no import/path fixes were needed to run the harness.

---

*Generated by the automated audit synthesis step, 2026-07-05. Non-canon.
No ledger entry, status.json field, or frozen text was modified.*

---

## Appendix (added same day): ChatGPT cross-agent pass — BLINDED, per cross-agent protocol

Conversation (steward's account): https://chatgpt.com/c/6a49f8d5-6224-83e8-948d-58734ebbb312
ChatGPT received ONLY the setting + theorem + verbatim proof (never this report or the auditors' output).
The platform's A/B test produced **two independent samples**; both returned:

> **VALID-WITH-GAPS. Theorem TRUE for arbitrary (including infinite) state sets; no finiteness or
> choice needed. Core reasoning and composition-order correct.**

Gap lists (union of both samples), mapped onto this report's numbering:
- totality witness arguments implicit (≈ G4's neighborhood);
- the b0 witness in single-valuedness should be explicitly justified from (a,a) ∈ R;S (= G4);
- "injectivity is symmetric" not actually proved — both samples wrote out the full mirror argument,
  matching the auditors' reconstruction step for step (= G5);
- **S = R^T asserted without proof; both inclusions supplied** (= G3, and the substance of G1).

Deltas: ChatGPT did not name G1's *invalid-inference-form* framing (it folded that defect into "S=R^T
unproved"), and did not flag G2 (surjectivity) as a separate textual gap — its own re-derivations derive
surjectivity from Delta_cod <= S;R exactly as G2's patch prescribes. No contradiction with any finding;
no gap found by ChatGPT that the auditors missed.

**Cross-agent status per the protocol ledger schema:** claim R1 — Claude: reconstructs YES, accepts YES ·
ChatGPT (2 samples): reconstructs YES, accepts YES → **promotion candidate** (Tier-3; the steward's call).
