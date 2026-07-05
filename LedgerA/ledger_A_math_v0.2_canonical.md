# Ledger A — Mathematics of Reversible-Contact Structures, v0.2 · CANONICAL · FROZEN

**Register: internal computation (exhaustively enumerated + hand-proved where stated), not refereed
theorems.** Supersedes `ledger_A_math_v0.1_frozen.md` (whose witness/independence content is carried
forward unchanged). Reproduce: `python3 ledger_A_witnesses.py` (W-series) and `python3 ledger_A_round2.py`
(R-series reproduction + variants). Ledgers B/C/D untouched; **Ledger C stays empty** — the
return-existence↔exit candidate remains unadmitted (no stated map).

## Reconciliation with the parallel construction (R-series)

**Frozen dated snapshot: `ledger_A_reconciliation_2026-07-04.md`** (governance rule: reconciliations are
frozen snapshots; corrections are new dated notes, never edits). Summary: independent reproduction of the
full 2¹⁶ = 65,536-assignment experiment; **full agreement on all three shared findings, no disagreements**;
exact-number diff pending `ledger_a_verify.py` (not on disk at snapshot time).

**Notation map (canonical henceforth):**
| His | Mine (v0.1) | Canonical name | Definition |
|---|---|---|---|
| strict functoriality | F-eq (D5) | **F-eq** | composite effect = composed effects |
| oplax | F-sup / "magic" direction (W7b) | **F-sup** | composed ⊆ composite |
| (dual, unnamed) | F-sub / "decorative" direction (W7a) | **F-sub** | composite ⊆ composed |
| return-existence | — (state-level; ≠ my w1) | **RET-∃** | Δ ⊆ step(c);step(c′) — every state can go and come back |
| return-exclusivity | — (state-level; ≠ my w2) | **RET-!** | step(c);step(c′) ⊆ Δ — any actual return lands exactly home |
| — | EI-w1 / EI-w2 (relation-level converse-inclusions) | **EI-w1 / EI-w2** | kept as the finer, relation-level pair; distinct from RET-∃/RET-! |
| R1 | Theorem (v0.1) | **Theorem R1** | see below |

## Theorem R1 — candidate general proof (recorded 2026-07-04, pending independent audit)

*Groupoid algebra, strict identity effects (step(e)=Δ), F-eq. Then for every inverse pair (c,c′):
R=step(c) is the graph of a bijection and step(c′)=Rᵀ — dynamics is deterministic, total, injective, and
both undos (EI-strong, RET-∃, RET-!) hold.*
**Proof.** F-eq at the inverse composites gives R;S=Δ_dom, S;R=Δ_cod. Δ⊆R;S makes R total; Δ⊆S;R makes S
total. Single-valuedness: if (a,b),(a,b′)∈R, pick b₀ with (a,b₀)∈R,(b₀,a)∈S (totality of the return at a);
S;R⊆Δ forces b₀=b and b₀=b′, so b=b′. Injectivity is symmetric via Δ_cod. Total + single-valued + injective
both ways ⇒ bijection with S=Rᵀ. ∎
**Enumeration confirmation:** |S|=2 strict: 2 survivors of 65,536-space restriction = the 2 bijections;
|S|=3 strict (identities pinned, 262,144 pairs): 6 survivors = 3! bijections. All det+total+inj, both undos.

**Confidence band (governance, 2026-07-04):** *established exhaustively for the searched finite universes*
(|S|=2 minimal groupoid; |S|=3 pruned); *in general: candidate proof recorded above, held at
conjecture-grade until independently audited.* External-facing wording until then: "established for the
searched finite universe, conjectured in general (proof recorded, pending audit)."

## The determinism boundary (round-2 headline)

The collapse is governed by **sub-diagonality of identity effects, not strictness per se**:
- **step(e) = Δ (strict):** effects are total bijections (Theorem R1).
- **step(e) ⊆ Δ (partial identities, D5-variant):** collapse SURVIVES weakened — every F-eq solution is a
  **partial bijection** with step(c′)=Rᵀ, and the identity effects are *forced* to be exactly the dom/ran
  sub-diagonals. Counts match the partial-injection formula Σₖ C(n,k)²k! exactly: **7** at n=2 (7/7 partial
  bijections, 0 nondet), **34** at n=3 (34/34, 0 nondet).
- **step(e) free:** collapse FAILS — nondeterminism enters precisely through non-diagonal idempotent
  identity effects. Full 65,536 enumeration: F-eq survivors **56**, of which **37 nondeterministic**; witness:
  E0={(a,a)}, E1={(b,b),(b,b2)}, F={(a,b),(a,b2)}, G={(b,a)}.

## R2 and its dual (both scales, exhaustive)

- **F-sup (his oplax): RET-! free, RET-∃ underivable.** n=2: exclusivity 49/49, existence 2/49.
  n=3: 1650/1650 vs 6/1650. CONFIRMED.
- **Dual (F-sub): RET-∃ free, RET-! underivable.** n=2: 31/31 vs 2/31. n=3: 25057/25057 vs 6/25057.
- **Corollary:** RET-∃ ∧ RET-! ∧ (either inclusion) ⟺ the F-eq maximal point. The two inclusion directions
  are exactly the two return-halves.

## Carried forward from v0.1 (unchanged)

Signature Σ₀ and decisions D1–D6 (partial compose; relational inverse; step a relation; EI variants
registered; F-eq frozen; availability/execution split). Independence matrix W1–W12 (A3, A4, F, T each
witnessed exactly-one-violation; EI derived at the maximal point, independent below F; strictness-necessity
witness W11). Findings: invertible algebra ≠ undoable dynamics (now also: 56−2 of the F-eq survivors on the
SAME groupoid algebra fail bijectivity when identities are free); return strictly weaker than invertibility
(W2p).

## Round-2 verdicts (as tasked)

1. **R1 — searched-universe VERIFIED; candidate general proof recorded** (band above: conjecture-grade in
   general until the proof passes independent audit; if it stands, no nondeterministic counterexample can
   exist under strict identities).
2. **Partial-identity variant — VERIFIED, headline survives weakened** (partial bijections; identities
   forced; exact counts 7 / 34).
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

*v0.2 frozen 2026-07-04. Revision requires a computed counterexample or a new witnessed result — not
conceptual refinement. Governance: reconciliations are frozen dated snapshots (see
`ledger_A_reconciliation_2026-07-04.md`); corrections are new dated notes. Ledger E (Evidence Log,
chat-side, append-only) exists and may be referenced by deposits; this ledger does not write to it.
Pending items: exact-number diff against `ledger_a_verify.py`; independent audit of the R1 general proof.*
