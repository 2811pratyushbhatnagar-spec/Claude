# Ledger A — Mathematics of Reversible-Contact Structures · v1.0 · CANONICAL · FROZEN

**Register: internal computation (exhaustively enumerated + hand-proved where stated), not refereed
theorems.** Repo-canonical location of Ledger A; filenames are de-versioned in-repo (version lives in this
header). Supersedes `archive/ledger_A_math_v0.2_canonical.md` and `archive/ledger_A_math_v0.1_frozen.md`
(witness/independence content carried forward unchanged). Reproduce: `python ../Scripts/ledger_A_witnesses.py`
(W-series) and `python ../Scripts/ledger_A_round2.py` (R-series reproduction + variants); regression-guarded
by `../tests/test_regression.py`. Ledgers B/C/D untouched; **Ledger C stays empty** — the
return-existence↔exit candidate remains unadmitted (no stated map).

**Changelog.** v1.0 (2026-07-11, Pratyush's Tier-3 ratification — "promote", direct decision):
**Q-R2-BAND RATIFIED — the "free" halves of Proposition R2 upgraded from searched-universe grade to
proved-internal, at any cardinality.** Grounds: the free halves were already noted (v0.3) to admit a
one-line argument — at the specific inverse-composite pair used in R2's fixed algebra, F-sup's inequality
`step(a);step(b) ⊆ step(ab)` instantiated at `ab=e` with strict identities (`step(e)=Δ`) gives
`step(f);step(g) ⊆ Δ` directly, i.e. RET-! along that composite; F-sub gives the dual `Δ ⊆ step(f);step(g)`,
i.e. RET-∃. Cross-checked with ChatGPT, which confirmed the argument is a direct substitution (no
enumeration, no finiteness, no use of the fixed algebra's specific size or the second object) and
generalizes to any category/groupoid containing one inverse-composite pair under strict identities — not
limited to the n=2/n=3 searched universes. ChatGPT's one precision note (adopted below): state the claims
as holding *along the inverse composite*, not as a blanket property of "every solution" in prose, to keep
the logical dependence transparent. The "bijection core" halves (RET-∃ under F-sup, RET-! under F-sub) are
UNTOUCHED — those remain searched-universe grade (a countermodel already shows non-derivability in
general, which needs no further proof, but the *positive* claim that only the core satisfies them stays
empirical). Decision given directly by Pratyush, 2026-07-11 (Cowork session).
v0.9 (2026-07-11, Pratyush's Tier-3 promotion — "promote and proceed", direct decision):
**Q-D5-STRUCTURE-GENERAL PROMOTED — the sub-identity-rung survivors are proved, for arbitrary state sets
(any cardinality, not just n=2,3,4), to be exactly the partial bijections of the underlying set, hence the
symmetric inverse monoid I_X.** Grounds: the D5 ladder's own harness definition for the sub-identity rung,
`step(c′) = Rᵀ` (S is not free — it is the relational converse of R, the same definitional move Theorem R1
already discharges), reduces the two sub-identity inclusions to elementary unfoldings — `R;Rᵀ⊆Δ` is exactly
injectivity of R, `Rᵀ;R⊆Δ` is exactly functionality of R — giving "R is a partial bijection on X" for any
X, no finiteness needed. Computationally cross-checked by brute enumeration at n=2,3,4 (7/34/209, zero
mismatches — n=4 new, beyond the prior hand-verified n=2,3); cross-checked with ChatGPT, confirmed sound
and cardinality-free. See `.automation/candidates/Q-D5-PARTIAL-BIJECTION-LEMMA-2026-07-11.md` for the full
derivation trail (including a first-pass lemma that was falsified and corrected before this one). Decision
given directly by Pratyush, 2026-07-11 (Cowork session).
v0.8 (2026-07-11, Pratyush's Tier-3 ratification — governance act, no mathematical change):
**Theorem R1 PROMOTED from conjecture to theorem.** Grounds: recorded proof VALID-WITH-GAPS by 3 blinded
audits + 2 blinded ChatGPT samples (unanimous), all 9 gaps expositional and patched into the v0.7 text
(no gap touched the theorem's truth); enumeration-corroborated at n=2,3 with zero discrepancies across
four independent sources, including a successful blind n=4 prediction (24 = 4! strict, 209 = ΣC(4,k)²k!
partial); finiteness not required (holds for arbitrary state sets, |A|=|B| a consequence not a hypothesis).
Decision given directly by Pratyush, 2026-07-11 (Cowork session). See `audits/R1-AUDIT-REPORT-2026-07-05.md`
§4 for the recommended band this promotion adopts.
v0.7 (2026-07-05, audit-driven patch under the dual-agreement rule; NO promotion taken):
Theorem R1 proof text patched per the unanimous independent audit (3 blinded audits + 2 blinded ChatGPT
samples, VALID-WITH-GAPS — gaps G1–G9 all expositional, patches prescribed and agreed; see
`audits/R1-AUDIT-REPORT-2026-07-05.md`); statement strengthened to arbitrary state sets (cardinality-free —
|fibers| equal is a consequence, not a hypothesis); n=4 blind-prediction evidence recorded (24 = 4! strict,
209 = ΣC(4,k)²k! partial); nondeterminism definition pinned in counts.json; validate.py adopted (historical
exemption + Ledger-C/D guards, from the mounted repo); unified status.json schema. Promotion remains Tier-3.
v0.6 (2026-07-04, new witnessed result): structure-map check executed at n=2,3 for both
rungs (completeness / converse=inversion / closure — ALL PASS); structure identifications two-banded:
FINITE (n=2,3) VERIFIED under the tested encoding, GENERAL stays OPEN (registry split:
Q-D5-STRUCTURE-FINITE theorem-grade finite-exhaustive, Q-D5-STRUCTURE-GENERAL open).
v0.5 (2026-07-04, governance edit only — no mathematical change): structured counts
(`../counts.json`) become the source of truth for enumeration numbers; all ratio prose renders as explicit
"N of M" (checked against counts.json by test_consistency).
v0.4 (2026-07-04, owner instruction + new witnessed result): the D5 ladder recorded as the
sharpened characterization (determinism carried by the identity-effect axiom, not functoriality); free-rung
n=3 counts (4400/4087) computed and cross-confirmed with the R-series; structure identifications (I_n, S_n)
banded TO-VERIFY, not asserted; no promotions.
v0.3 (2026-07-04, governance edits only — no mathematical change): R2 promoted to a numbered
Proposition with explicit assumptions and precise bands; repo canonicalization; de-versioned filename.
v0.2 (2026-07-04): round-2 — reconciliation, R1 candidate general proof, partial-identity gradient, |S|=3
replication, R1 confidence band per governance. v0.1 (2026-07-04): signature decisions D1–D6, W-series
witnesses, independence matrix.

## Reconciliation with the parallel construction (R-series)

**Frozen dated snapshot: `../reconciliation/reconciliation_2026-07-04.md`** (governance rule: reconciliations
are frozen snapshots; corrections are new dated notes, never edits). Summary: independent reproduction of the
full 2¹⁶ = 65,536-assignment experiment; **full agreement on all three shared findings, no disagreements**;
exact-number diff pending `ledger_a_verify.py` (not on disk at snapshot time; his R3–R8 statements likewise
not yet on disk — reconciliation of those is pending material).

**Notation map (canonical henceforth):**
| His | Mine (v0.1) | Canonical name | Definition |
|---|---|---|---|
| strict functoriality | F-eq (D5) | **F-eq** | composite effect = composed effects |
| oplax | F-sup / "magic" direction (W7b) | **F-sup** | composed ⊆ composite |
| (dual, unnamed) | F-sub / "decorative" direction (W7a) | **F-sub** | composite ⊆ composed |
| return-existence | — (state-level; ≠ my w1) | **RET-∃** | Δ ⊆ step(c);step(c′) — every state can go and come back |
| return-exclusivity | — (state-level; ≠ my w2) | **RET-!** | step(c);step(c′) ⊆ Δ — any actual return lands exactly home |
| — | EI-w1 / EI-w2 (relation-level converse-inclusions) | **EI-w1 / EI-w2** | kept as the finer, relation-level pair; distinct from RET-∃/RET-! |

## Theorem R1 — PROMOTED (2026-07-11, Tier-3, Pratyush)

*Let R = step(c), S = step(c′) satisfy R;S = Δ_A and S;R = Δ_B (as forced by F-eq at the inverse
composites under strict identity effects). Then R is the graph of a bijection f: A → B, S = Rᵀ (the graph
of f⁻¹), and EI-strong, RET-∃, RET-! all hold. **No finiteness is used: the theorem holds for arbitrary
state sets, and |A| = |B| is a consequence, not a hypothesis.***

**Proof** (pointwise; each of the four inclusions Δ_A⊆R;S, R;S⊆Δ_A, Δ_B⊆S;R, S;R⊆Δ_B is individually
load-bearing — ablation-verified at unequal fibers):
1. *(Totality.)* For a∈A, Δ_A ⊆ R;S gives (a,a) ∈ R;S: a **return witness** b₀ with (a,b₀)∈R, (b₀,a)∈S.
   So R is total; symmetrically (Δ_B ⊆ S;R) S is total.
2. *(Single-valuedness of R.)* If (a,b),(a,b′)∈R, take the return witness b₀ of step 1 — the fact used is
   the RET-existence instance (a,a)∈R;S, **not** mere totality (totality alone admits round trips landing
   elsewhere). From (b₀,a)∈S, (a,b)∈R and S;R ⊆ Δ_B: b₀=b; likewise b₀=b′; so b=b′.
   *(Mirror — single-valuedness of S, using the OTHER two inclusions:)* if (b,a),(b,a′)∈S, Δ_B ⊆ S;R gives
   a₀ with (b,a₀)∈S, (a₀,b)∈R; from (a₀,b)∈R, (b,a)∈S and R;S ⊆ Δ_A: a₀=a; likewise a₀=a′; so a=a′.
3. *(Injectivity of R.)* If (a,b),(a′,b)∈R, Δ_B ⊆ S;R gives a₀ with (b,a₀)∈S, (a₀,b)∈R; from (a,b)∈R,
   (b,a₀)∈S and R;S ⊆ Δ_A: a₀=a; likewise a₀=a′; so a=a′. (Injectivity of S mirrors.)
4. *(Surjectivity of R.)* For b∈B, Δ_B ⊆ S;R gives (b,b)∈S;R: some a₀ with (b,a₀)∈S, (a₀,b)∈R, so
   b ∈ ran(R). **This line — not counting — is what makes the theorem cardinality-free.**
5. *(Bijection.)* Total + single-valued = a function f; injective (3) + surjective (4) ⇒ f is a bijection.
6. *(S = Rᵀ, both inclusions.)* **S ⊆ Rᵀ:** let (b,a)∈S; totality gives (a,b′)∈R; then (b,a),(a,b′) put
   (b,b′)∈S;R ⊆ Δ_B, so b′=b, i.e. (a,b)∈R. **Rᵀ ⊆ S:** let (a,b)∈R; step 1's witness at a gives
   (a,b₀)∈R, (b₀,a)∈S; single-valuedness of R gives b₀=b, so (b,a)∈S. Hence S = Rᵀ = graph(f⁻¹).
7. *(Conclusions discharged.)* **EI-strong** is by definition step(c′) = converse(step(c)) (harness
   definition, `ledger_A_witnesses.py`), i.e. S = Rᵀ: discharged by step 6. **RET-∃** (Δ ⊆ R;S) and
   **RET-!** (R;S ⊆ Δ) are the hypotheses themselves. ∎

**Remarks (per audit).** *(8-to-2 reduction:)* under strict identities the other six F-eq equations are
tautologies (Δ is a two-sided unit and idempotent); the proof consumes F-eq only at the two inverse
composites — machine-verified (identical survivor sets under 2 vs 8 equations). This reduction is NOT
valid in non-strict regimes; the free-rung nondeterminism witness lives exactly there. *(Locality:)* the
theorem is local — any pair R,S in Rel with R;S=Δ_A, S;R=Δ_B is a bijection pair; no groupoid
transitivity or second-object structure is consumed. *(Edge cases:)* |A|≠|B| makes the hypotheses
unsatisfiable (verified exhaustively at sizes ≤3); empty fibers yield the empty bijection.

**Enumeration confirmation:** |S|=2 strict: 2 survivors = the 2 bijections; |S|=3 strict: 6 = 3!.
**Blind n=4 prediction (audit, 2026-07-05):** predicted 24 = 4! strict and 209 = ΣC(4,k)²k! partial before
running; both matched, zero structure violations (audit enumerators in `audits/`).

**Confidence band (updated 2026-07-11): THEOREM (promoted).** Recorded proof found VALID-WITH-GAPS by
3 blinded audits + 2 blinded ChatGPT samples (unanimous: theorem TRUE, cardinality-free); all 9 gaps
expositional, patched above per the auditors' agreed reconstructions; enumeration-corroborated n ≤ 4
including the blind n=4 prediction; finiteness not required. **Promoted conjecture → theorem 2026-07-11,
Pratyush (Tier-3, direct decision).**

## The D5 ladder (sharpened characterization): determinism is carried by the identity-effect axiom

**Reframing of R1:** functoriality (F-eq) supplies coherence; **determinism enters exactly through the
identity-effect rung**, not through functoriality. Under F-eq throughout (identity effects are *forced* to
E0 = step(f);step(g), E1 = step(g);step(f) by the inverse composites), the ladder:

| identity effects | survivor dynamics | counts (n=2 · n=3) | structure reading | band |
|---|---|---|---|---|
| **free** | nondeterminism admitted, via non-diagonal idempotent identities | **37 of 56** nondeterministic · **4087 of 4400** nondeterministic (counts.json: feq-free-n2, feq-free-n3) | none claimed | **builder-supported** (reproducible via run_checks; n=3 counts agree across both independent constructions; NOT yet externally audited) |
| **⊆ Id** (sub-identity) | **partial bijections**, step(c′)=Rᵀ; identities pinned to exact dom/ran sub-diagonals | **7** · **34** (· **209** at n=4), 0 nondeterministic in all three — = Σₖ C(n,k)²k! = **\|I_n\|** exactly (feq-subid-n2/-n3/-n4) | symmetric inverse monoid I_n — **FINITE (n=2,3,4): VERIFIED · GENERAL: PROVED (Theorem D5G, 2026-07-11)** | counts builder-supported; finite structure map VERIFIED (regression-guarded); general identification PROMOTED — Q-D5-STRUCTURE-GENERAL closed |
| **= Id** (strict) | **total bijections**, both undos (Theorem R1, band above) | **2** · **6**, all deterministic — = **\|S_n\|** exactly (feq-strict-n2/-n3) | symmetric group S_n — **FINITE (n=2,3): VERIFIED · GENERAL: OPEN** | bijection fact = R1 (**PROMOTED to theorem 2026-07-11**); finite structure map VERIFIED; general open |

Nondeterminism witness (free rung, n=2): E0={(a,a)}, E1={(b,b),(b,b2)}, F={(a,b),(a,b2)}, G={(b,a)}.
**Two-band reading of the structure identifications (structure-map check, 2026-07-04):**
- **FINITE, VERIFIED:** for n=2, 3 (and now 4, see Theorem D5G below) the surviving effect structures are
  isomorphic to I_n (sub-identity rung) and S_n (strict rung) **under the tested encoding** (ι: bᵢ↦aᵢ) —
  every partial bijection / permutation appears exactly once, relational converse matches monoid/group
  inversion, and the encoded set is closed under composition. All three sub-checks pass at every scale
  checked; regression-guarded.
- **GENERAL, sub-identity rung: PROVED (Theorem D5G, 2026-07-11).** The strict rung's general case was
  already Theorem R1; the sub-identity rung's general case (Q-D5-STRUCTURE-GENERAL) is now closed by
  Theorem D5G immediately below — arbitrary state sets, no finiteness required.

## Theorem D5G — Partial-Inverse Characterization (Q-D5-STRUCTURE-GENERAL) — PROMOTED (2026-07-11, Tier-3, Pratyush)

*Let X be any set (no cardinality restriction) and R ⊆ X×X, with S := Rᵀ pinned by the sub-identity rung's
own harness definition (`step(c′) = Rᵀ`, same definitional move Theorem R1 already discharges). Then
`R;Rᵀ ⊆ Δ_X` and `Rᵀ;R ⊆ Δ_X` hold **iff** R is the graph of a partial bijection on X (an injective partial
function D → X, D ⊆ X). Consequently, when A = B = X, the sub-identity-rung survivors are exactly the
elements of the symmetric inverse monoid I_X — not merely isomorphic to it, but its standard realization
(multiplication = relational composition, inverse = relational converse, identity = Δ restricted to a
subset).*

**Proof.**
1. *(⇒, injectivity.)* If (a,b)∈R and (a′,b)∈R, then (a,a′) ∈ R;Rᵀ, so `R;Rᵀ⊆Δ` gives a=a′ — at most one
   input maps to each output, i.e. R is injective.
2. *(⇒, functionality.)* If (a,b)∈R and (a,b′)∈R, then (b,b′) ∈ Rᵀ;R, so `Rᵀ;R⊆Δ` gives b=b′ — at most one
   output per input, i.e. R is single-valued.
3. Functional + injective = exactly an injective partial function, i.e. a partial bijection on X.
4. *(⇐)* If R is the graph of a partial bijection, both inclusions follow immediately from injectivity and
   functionality directly. ∎

No finiteness is used anywhere — same style as Theorem R1's cardinality-free proof, and the same S:=Rᵀ
harness move. The I_X identification is the standard realization, not a separate combinatorial fact
needing re-verification at each n, once the structural claim above is fixed.

**Enumeration confirmation:** brute enumeration over all relations on X (`d5_general_check.py`): the R's
satisfying `R;Rᵀ⊆Δ` and `Rᵀ;R⊆Δ` exactly coincide with the partial bijections at n=2 (7), n=3 (34), and
n=4 (209) — zero mismatches, matching Σₖ C(n,k)²k! = \|I_n\| in every case. n=4 is new confirmation beyond
the prior hand-verified n=2,3.

**Confidence band: THEOREM (promoted).** Elementary proof, cardinality-free by construction (no
finite-case argument to generalize — the proof never mentions |X|); cross-checked with ChatGPT (confirmed
sound: "nothing in that argument depends on finiteness... genuinely cardinality-free"; I_X identification
confirmed as the standard realization, not mere isomorphism); computationally cross-checked n=2,3,4 with
zero discrepancies. One open due-diligence item, non-blocking: whether this characterization already has a
standard citation in inverse-semigroup / relation-algebra literature (affects citation only, not
correctness — noted by ChatGPT as good practice before any external claim of novelty).
**Promoted open question → theorem 2026-07-11, Pratyush (Tier-3, direct decision, "promote and proceed").**

## Proposition R2 — return-halves under the two functoriality inclusions

**Assumptions (explicit).** (i) Algebra fixed: the minimal transitive groupoid — I={0,1};
C={e0,e1,f,g}; f;g=e0, g;f=e1; identities absorb; inv={(f,g),(g,f)}. (ii) Identity effects strict:
step(e)=Δ. (iii) Non-identity effects arbitrary relations (no determinism, totality, or undo assumed).
(iv) Enumeration scope: |S₀|=|S₁|=2 exhaustive; |S₀|=|S₁|=3 exhaustive with identities pinned
(262,144 pairs).

**Statement.**
(a) Under **F-sup** (composed ⊆ composite): **RET-! holds along the inverse composite for every
solution — PROVED, any cardinality (2026-07-11)**, while **RET-∃ is underivable in general** — it holds
only on the F-eq bijection core (searched-universe grade). Counts: n=2 exclusivity 49 of 49, existence
2 of 49; n=3: exclusivity 1650 of 1650, existence 6 of 1650.
(b) Dually, under **F-sub** (composite ⊆ composed): **RET-∃ along the inverse composite — PROVED, any
cardinality (2026-07-11)**, **RET-! underivable in general** (searched-universe grade). Counts: n=2
existence 31 of 31, exclusivity 2 of 31; n=3: existence 25057 of 25057, exclusivity 6 of 25057.
(c) **Corollary:** RET-∃ ∧ RET-! ∧ (either inclusion) ⟺ the F-eq maximal point (searched-universe grade,
untouched by this ratification).

**General proof of the free halves (PROVED, 2026-07-11).** Let a,b be any composable pair with ab=e in a
category (or groupoid) where identity effects are strict (step(e)=Δ) — the specific two-object algebra
above supplies one instance (a,b)=(f,g), but nothing below uses its size or its second object.
*F-sup half:* the inequality `step(a);step(b) ⊆ step(ab)` instantiated at ab=e gives
`step(a);step(b) ⊆ step(e) = Δ` directly — this is exactly RET-! along that composite. *F-sub half:*
dually, `step(ab) ⊆ step(a);step(b)` at ab=e gives `Δ = step(e) ⊆ step(a);step(b)` — exactly RET-∃ along
that composite. Neither step uses enumeration, finiteness, or any property of the relations beyond the
inclusion axiom itself and strict identities. **Precision note (per cross-check):** these are proved *along
the inverse composite*, not as a blanket property independent of which pair is examined — the phrasing
above reflects that.

**Band.** *Free halves: PROVED-INTERNAL, any cardinality* (ratified 2026-07-11, Pratyush, "promote" —
Tier-3 direct decision; grounds and cross-check recorded in the v1.0 changelog entry above). *Underivability
halves and the corollary (c): unchanged, searched-universe grade* — the non-derivability claims are
already settled in general by the explicit finite countermodels (one countermodel suffices to show
non-derivability), but the *positive* "only the bijection core satisfies both" claim remains empirical,
established exhaustively for the searched universes (iv) only.

## Carried forward from v0.1 (unchanged)

Signature Σ₀ and decisions D1–D6 (partial compose; relational inverse; step a relation; EI variants
registered; F-eq frozen; availability/execution split). Independence matrix W1–W12 (A3, A4, F, T each
witnessed exactly-one-violation; EI derived at the maximal point, independent below F; strictness-necessity
witness W11). Findings: invertible algebra ≠ undoable dynamics (56−2 of the F-eq survivors on the SAME
groupoid algebra fail bijectivity when identities are free); return strictly weaker than invertibility (W2p).

## Round-2 verdicts

1. **R1 — PROMOTED to theorem 2026-07-11** (round-2 status superseded 2026-07-05 by the independent audit —
   proof VALID-WITH-GAPS, text patched, cardinality-free — then superseded again 2026-07-11 by Pratyush's
   Tier-3 promotion decision; see the Theorem R1 band above).
2. **Partial-identity variant — GENERAL CASE PROMOTED to theorem 2026-07-11** (Theorem D5G: partial
   bijections, identities forced, exact counts 7 / 34 / 209 at n=2,3,4, general X proved cardinality-free).
3. **|S|=3 replication — VERIFIED** (262,144-pair space; 6 = 3! survivors; R1/R2 patterns exact).
4. **Local-states variant — VERIFIED by construction:** the encoding already fibers states over interfaces
   (`at : S → I`); per-interface containers with a project map are a re-presentation, all counts unchanged.
5. **Adversarial pass — two flags deposited:** (i) `comp` is a partial *function* — uniqueness of composites
   is a (standard, now explicit) choice, an axiom candidate if ever relaxed; (ii) `inv` is redundant at the
   maximal point (definable from comp via A2+A3) — kept as primitive only for sub-maximal theories.
   **Tightened class statement:** the maximal point is a **transitive groupoid acting on its state fibers**
   (effects = a functor into finite sets and bijections) — *established at the searched scales; the general
   form inherits R1's confidence band.* "Stack-like locality" stays dropped (never formalized in-ledger).
   No other hidden bake-ins found.

*v0.4 frozen 2026-07-04. Revision requires a computed counterexample, a new witnessed result, or a recorded
governance instruction — not conceptual refinement. Governance: reconciliations are frozen dated snapshots;
corrections are new dated notes. Ledger E (append-only Evidence Log, `../LedgerE/evidence_log.md`) may be
referenced by deposits; this ledger does not write to it. Pending: exact-number diff vs `ledger_a_verify.py`;
independent audit of the R1 proof; R3–R8 statements not yet on disk.*
