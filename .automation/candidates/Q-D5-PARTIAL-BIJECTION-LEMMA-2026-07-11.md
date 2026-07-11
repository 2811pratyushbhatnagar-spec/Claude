# Candidate proof: Q-D5-STRUCTURE-GENERAL (sub-identity rung, general cardinality)

**Status:** PROMOTED. Pratyush ratified this proof 2026-07-11 ("promote and proceed+", Tier-3, direct
decision). Now **Theorem D5G** in `LedgerA/ledger_A_canonical.md` (v0.9). This document is retained as the
historical derivation trail (Round 1 failed lemma → Round 2 fix → proof → cross-checks); the canonical
statement lives in Ledger A, not here.
**Origin:** Steward's own intuition (paired vs. unpaired doors) → ChatGPT reframe → ChatGPT-proposed lemma
falsified by Cowork → Cowork located the missing axiom already in Ledger A → corrected proof, cross-checked
with ChatGPT again. Full trail: chatgpt.com/c/6a4ffe2d, 2026-07-11.
**Relation to canon:** Ledger A (`LedgerA/ledger_A_canonical.md`), the D5 ladder, sub-identity ("⊆ Id") row.
`status.json` Ledger A `open`: `"Q-D5-STRUCTURE-GENERAL (arbitrary finite state sets)"`.

## The question

D5 ladder, sub-identity rung: identity effects are only forced to *partial* bijections. Verified by hand at
n=2,3 (counts 7, 34) that the survivor set is isomorphic to the symmetric inverse monoid I_n. General n
(or arbitrary infinite X): open.

## Round 1 — a proposed lemma, and why it failed

First pass (ChatGPT) proposed: "R admits *some* S with R;S⊆Δ_A, S;R⊆Δ_B" characterizes partial bijections,
for any X. **False as stated** — counterexample X={1,2,3}, R={(1,2),(1,3)} (not even functional), S=∅:
both inclusions hold vacuously for literally any R, since the empty relation trivializes them. Verified by
brute enumeration (`lemma_check.py`). ChatGPT confirmed the hole and pointed to the fix: don't patch with a
maximality condition (itself nontrivial); instead check whether the *framework's actual construction*
already pins S to something less degenerate than "any relation."

## Round 2 — the fix was already in Ledger A

Re-read `LedgerA/ledger_A_canonical.md` (the D5 ladder table + Theorem R1's own proof). Two facts already
on record there:

1. The ladder table states, for the sub-identity rung: **`step(c′) = Rᵀ`** — i.e. S is not free, it is
   *defined* as the relational converse of R, by harness construction. (Same move already used and
   discharged in Theorem R1, step 7: "EI-strong is by definition step(c′) = converse(step(c))
   (harness definition, `ledger_A_witnesses.py`)".)
2. So the real sub-identity axiom set is **`R;Rᵀ ⊆ Δ_A` and `Rᵀ;R ⊆ Δ_B`, with S := Rᵀ pinned** — not
   "there exists some S." The degenerate S=∅ witness from Round 1 is no longer available except when R
   itself is empty, since S is derived from R, not chosen independently.

## Theorem (partial-inverse characterization) — proof

**Claim.** Let X be any set (no cardinality restriction) and R ⊆ X×X. Then
`R;Rᵀ ⊆ Δ_X` and `Rᵀ;R ⊆ Δ_X` **iff** R is the graph of a partial bijection on X (an injective partial
function D → X, D ⊆ X).

**Proof.**
- (⇒) `R;Rᵀ ⊆ Δ`: if (a,b)∈R and (a′,b)∈R, then (a,a′) ∈ R;Rᵀ, so a=a′ — i.e. R is **injective**
  (at most one input maps to each output).
  `Rᵀ;R ⊆ Δ`: if (a,b)∈R and (a,b′)∈R, then (b,b′) ∈ Rᵀ;R, so b=b′ — i.e. R is **functional**
  (single-valued). Functional + injective = exactly an injective partial function, i.e. a partial
  bijection.
- (⇐) If R is the graph of a partial bijection, both inclusions follow immediately from injectivity and
  functionality directly.

No finiteness is used anywhere — same style as Theorem R1's cardinality-free proof (whose own S:=Rᵀ move
this reuses). ∎

**Corollary.** When the two sides coincide (A=B=X), the survivors of the sub-identity rung are precisely
the elements of the symmetric inverse monoid I_X — not merely isomorphic to it, but its standard
realization: multiplication = relational composition, inverse = relational converse (Rᵀ), identity = Δ
restricted to a subset. This identification is definitional once the structural theorem above is in hand,
not a separate combinatorial fact to re-verify at each n.

## Computational cross-check

`d5_general_check.py` (Cowork sandbox, brute enumeration over all relations on X, n=2,3,4): the R's
satisfying `R;Rᵀ⊆Δ` and `Rᵀ;R⊆Δ` exactly coincide with the partial bijections of X, in all three cases,
zero mismatches:

| n | axiom-satisfying | partial bijections | \|I_n\| = Σ C(n,k)²k! |
|---|---|---|---|
| 2 | 7 | 7 | 7 |
| 3 | 34 | 34 | 34 |
| 4 | 209 | 209 | 209 |

(n=2,3 were already known from the hand-verification on record; n=4 is new confirmation, matching the
general proof rather than requiring separate combinatorics.)

## ChatGPT cross-check (Round 2)

Confirmed the proof: "Provisionally, yes... nothing in that argument depends on finiteness... the theorem
is genuinely cardinality-free." On the I_X identification: "essentially yes... they're not merely
isomorphic to the symmetric inverse monoid — they are its standard realization." One stylistic note (no
mathematical gap): state it as two separate claims — (1) the structural theorem (R admits this pair of
inclusions with S:=Rᵀ iff R is a partial bijection), then (2) the corollary identifying the survivor set
with I_X — rather than conflating them. Also flagged as good practice, not a defect: check whether this
characterization already has a standard citation in inverse-semigroup / relation-algebra literature before
treating it as novel; even if it's standard, it doesn't weaken the result for this framework's purposes —
it only affects the citation, not the correctness.

## What this resolves and what it doesn't

- **Resolves** (candidate-grade, pending Pratyush's review): the general-cardinality structural content of
  Q-D5-STRUCTURE-GENERAL — "the sub-identity-rung survivors are exactly the partial bijections of X, for
  any X" is now a short, elementary, cardinality-free proof, matching R1's style and reusing R1's S:=Rᵀ
  harness-definition move. The I_X identification follows as a near-immediate corollary.
- **Does not resolve**: whether an equivalent characterization is already standard in the literature
  (ChatGPT's suggested due-diligence check, not yet done this session). This affects citation/novelty
  framing only, not correctness.
- **Not done**: promoting Q-D5-STRUCTURE-GENERAL, editing its confidence band in Ledger A, or updating
  `status.json`'s open-items list. That is a Tier-3 act (promotion, per the governance list) and is
  Pratyush's decision alone, same as R1's promotion was.

## Disposition

Read-only on all canon/governed paths this session; only `.automation/candidates/` written. `status.json`
Ledger A `open` list unchanged. If Pratyush wants to close Q-D5-STRUCTURE-GENERAL on the strength of this
proof, that requires his explicit Tier-3 decision, the same pattern used for R1.
