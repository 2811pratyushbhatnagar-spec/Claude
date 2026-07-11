# Ledger A — Mathematics of Reversible-Contact Structures, v0.1 · FROZEN
> **SUPERSEDED by `ledger_A_math_v0.2_canonical.md`** (round-2: R-series reconciliation, R1 general proof,
> partial-identity gradient, |S|=3 replication). Witness/independence content below remains valid and is
> carried forward unchanged.

**Register: internal computation (finite-model checked), not refereed theorems.** All independence and
decision results are witnessed by explicit finite models in `ledger_A_witnesses.py` (reproduce:
`python3 ledger_A_witnesses.py`). Architecture: this is Ledger A only. No interpretation, no protocol
reading, no physics — **Ledger C stays empty**; nothing here depends on or supports Ledgers B/D.

## Signature Σ₀ (all decisions settled by finite models as arbiter)

Sorts: `I` (interfaces), `C` (contacts), `S` (states).
Maps/relations: `dom, cod : C → I` · `at : S → I` · `comp ⊆ C×C×C` (**partial**, functional table)
· `inv ⊆ C×C` (**relational** is-inverse-of) · `en ⊆ C×S` (availability) · `step ⊆ C×S×S` (**relation**, licensed effect).

**Settled decisions (each with its computed arbiter result):**
- **D1 — composition PARTIAL.** Total composition + typing coherence (A1) is UNSAT in any model with a
  type-mismatched pair (8 such pairs already in W1). Not a taste choice; a satisfiability fact.
- **D2 — inverse RELATIONAL.** A total inverse operation excludes W2p (contacts `f`,`g` admit no coherent
  inverse candidate) — i.e. totality bakes the groupoid answer into the vocabulary. Relational `inv` defers
  reversibility to axiom A4, which finite models can violate. (Confirms the pre-freeze refinement.)
- **D3 — step is a RELATION.** W4 (two licensed outcomes from one state) is core-consistent; a functional
  `result` would exclude it — determinism must not be baked in.
- **D4 — undo quantifier: adopt EI-strong at the maximal point; register EI-bisim as the named variant.**
  W6 (return-to-an-equivalent-copy) separates bisim from strong/w1. Choice among variants inside Ledger A is
  by mathematics only (derivability, see Theorem); any preference for bisim on protocol-semantic grounds
  would be a Ledger-C act and is NOT made here.
- **D5 — effect-composition EQUALITY (F-eq).** Inclusion ⊆ admits decorative composites (W7a: composite
  licenses nothing); inclusion ⊇ admits magic composites (W7b: composite invents a transition its parts
  cannot perform). Equality = no junk, no magic.
- **D6 — availability/execution split CONFIRMED.** W8 (idle availability: enabled with no licensed effect)
  is core-consistent and inexpressible if `en := dom(step)`; the split also makes A5 a genuine axiom.

## Axioms

**Core (asserted):**
- **A1** typing coherence of composition · **A2** relational associativity · **A5** effect soundness
  (`step(c,s,s′) → en(c,s)` + endpoint typing).

**Test lattice (each admitted only WITH an independence witness):**
- **A3** identities exist, STRICT form: identity effects are exactly the diagonal (`step(e_i) = Δ_{S_i}`),
  enabled everywhere on their interface. *Register note: A3 is the exit-affordance — "a meeting that changes
  nothing is always available."* (Stated here as mathematics; the gloss is bracketed, not load-bearing.)
- **A4** invertibility: every contact has an inv-partner, coherent with composition via identities.
  (Dependency edge: coherent A4 presupposes A3.)
- **F** effect-functoriality (equality form, per D5): composite step = composed steps.
- **EI** effect-inversion: inverse contacts undo each other (strong = relational converse; variants w1/w2/bisim registered).
- **T** transitivity: every interface reachable from every interface.
- (**R** return-possible is a *property*, not an axiom — see Findings.)

## Theorem (internal, computation-checked + relation-algebra argument)

**Core + A3(strict) + A4 + F(eq) ⊢ EI(strong).**
*Argument:* coherence gives `comp(c,c′)=e_dom`, `comp(c′,c)=e_cod`; F-eq + strict A3 give
`step(c);step(c′) = Δ` and `step(c′);step(c) = Δ`; relations composing to identities both ways are inverse
bijections, so `step(c′) = converse(step(c))`. Verified on every in-harness model satisfying the hypotheses
(W1, W12).
**Strictness is necessary:** W11 satisfies core + A3(loose) + A4 + F(eq) with EI(strong) FALSE — a loose
identity's extra effect propagates through absorption composites and breaks the converse. So EI is **derived**
at the maximal point and **independent** only below F (witness W3).

## Independence matrix (witnessed)

| Witness | Violates exactly | Everything else | Role |
|---|---|---|---|
| W1 | — | all pass | maximal class inhabited (consistency) |
| W9 | A3 | rest pass | identities independent |
| W2p | A4 | rest pass (incl. T, R) | invertibility independent |
| W10 | F | rest pass (incl. EI) | functoriality independent of effect-undo |
| W3 | F, EI | rest pass | EI independent below F |
| W12 | T | rest pass | transitivity independent |
| W11 | A3(strict) | F-eq, A4 pass; EI fails | strictness-necessity for the Theorem |
| W4, W6, W7a/b, W8 | (decision witnesses) | | D3, D4, D5, D6 arbiters |

## Findings deposited

1. **Two reversibilities, provably independent.** Algebraic invertibility (A4) and dynamical undo (EI) come
   apart: W3 is a perfect groupoid whose effects do not undo. The axioms binding algebra to dynamics (F, EI)
   are where the structure's content lives; at the maximal point EI collapses into A3+A4+F (Theorem).
2. **Return is strictly weaker than invertibility.** W2p: no inverses (A4 false) yet every step reversible by
   *reachability* (R true, via other contacts). R is a property implied by the maximal point but obtainable
   without it.
3. **Maximal point of the lattice** = Σ₀ + A3 + A4 + T (+F, with EI derived) = transitive groupoid with
   coherent, effect-undoing dynamics — the earlier object-search class, now refined by (1): "transitive
   groupoid" alone was necessary-not-sufficient.
4. Inverse uniqueness at the maximal point follows classically from A2+A3 (not separately deposited).

## Open (round 2, NOT frozen)

Locality/gluing (restriction structure on interfaces; stack-style up-to-iso gluing) — requires signature
extension; deferred until a use-case demands it. Multi-party joint enablement typing — same status.

*v0.1 frozen 2026-07-04. Revisions require either a computed counterexample to something asserted here or a
new witnessed independence result — not conceptual refinement.*
