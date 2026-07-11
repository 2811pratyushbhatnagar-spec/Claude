# Representation-Invariance — stress test (does it define something?)   [non-canon · candidate · worked examples]

*Tests the minimal definition against the four-stage protocol (coherence / existence / reduction / usefulness).
Warrant: candidate; the constructions are **standard and reviewer-checkable**; the unifying claim is a
**hypothesis from examples, not a theorem** — reconstruct via a non-drafting stream. Nothing admitted or forced;
Tier-3 to adopt. Provenance: 2026-07-07 chat.*

## Data, restated (structural change accepted): (O, Rep, P)
Primitive data is **(O, Rep, P)** with dependency **(O, Rep) → P → I**: (O,Rep) fixes the presentations; **P**
(the notion of preservation) fixes what "invariant" *means*; **I** is determined by all three. **P is primitive,
not derived** — without P there is no unique I (§ P-dependence).

## Stage 1 — Internal coherence
Coherent **as a schema, once P is typed.** "The universal object determined by Rep and P" is well-posed iff P is
given a type — operationally, **P selects a universal construction over the diagram Rep** (a weight/direction).
No hidden circularity; the single requirement is that **P be specified, with a type**, or I is underdetermined.

## Stage 2 — Existence: three genuinely different examples (I exists, nontrivial)
| # | C | O | Rep(O) | P | **I(O)** | construction |
|---|---|---|--------|---|----------|--------------|
| E1 | comm. k-algebras | k[x,y] | the S₂ swap-presentation | invariant under S₂ | **k[x,y]^{S₂}=k[x+y, xy]** | ring of invariants O^G (a limit) |
| E2 | (pre)sheaves on X | a presheaf F | restrictions F→F(Uᵢ), a cover {Uᵢ} | compatible on overlaps | **F(X)=eq(∏F(Uᵢ)⇉∏F(Uᵢ∩Uⱼ))** | equalizer / limit over the cover |
| E3 | fields | ℚ̄ | Gal(ℚ̄/ℚ) | fixed by all σ | **ℚ̄^{Gal}=ℚ** | fixed field (limit over the group) |
Existence holds; the three are realized by *different* constructions — **yet all three are limits over their
Rep-diagram** (the first clue toward the verdict).

## Stage 3 — Reduction + emergent structure
Each reduces to a known construction. They unify: E1–E3 are all **limits over the representation diagram**; the
P-dependence test reaches the *dual* direction. **Leading hypothesis (from examples, not a theorem):**
> *I(O) is a **weighted (co)limit / (co)end over the diagram Rep, with P the weight/direction*** — limit under
> "fixed/compatible" P, colimit under "identified/quotient" P.
If so the object **locates** to standard category theory (weighted (co)limits, ends, Kan extensions), with
invariant theory / descent / Galois as instances. *Caveat:* not every invariant is a plain (co)limit
(cohomology, derived invariants, definability), so the full object may be "the universal/**derived** construction
over the diagram"; "always a plain (co)limit" is **not** claimed.

## Pathologies (2) — where the content lives
- **|Rep| = 1** (single r: O→R): "representation-independent" is vacuous; I = the content of r; **S trivial**;
  the **principle becomes a tautology.** ⇒ the content lives in the *multiplicity* of Rep.
- **Rep = every morphism out of O** (incl. the collapse O→1): under limit-type P, invariance under the collapse
  forces **I = terminal (trivial).** ⇒ too-large Rep also trivializes.
**Finding:** I is nontrivial only for a **proper, intermediate** Rep (an atlas) — the real admissibility
condition (nontriviality/faithfulness, *not* closure).

## Non-existence (1) — existence is conditional on C
In **C = FinSet**, let Rep be an infinite tower of surjections `… ↠ [3] ↠ [2] ↠ [1]`. The compatible object is
the **inverse limit**, which is infinite — **not in FinSet**. ⇒ **I does not exist in C.** Existence ⇔ C has the
(co)limit P selects (C complete/cocomplete enough). Answers "for which C, Rep does I exist?".

## P-dependence (1) — same (O, Rep), different P → different I
On (O, Rep) = (k[x,y], S₂):
- P = **trivial** character ("fixed") → **symmetric** polynomials k[x,y]^{S₂} (a **limit**, O^G).
- P = **sign** character (semi-invariant) → **alternating** polynomials, the (x−y)-multiples (a different subobject).
- P = **coinvariant** ("identified across the action") → **O_G = O/(σx−x)** (a **colimit**, generally ≠ O^G).
Same (O, Rep); three P's → three I's spanning **limit → subobject → colimit**. ⇒ **P primitive**; vindicates
withdrawing "I = limit."

## Stage 4 — Usefulness (preliminary)
As tested, it proves nothing new; candidate value is **organizational** — one schema under which group-invariants,
sheaf descent, Galois fixed fields, semi-invariants, and coinvariants are the *same move* ((co)limit over the
Rep-diagram, P = direction). A clarifying re-description, likely **locating** to weighted (co)limits / ends —
not new mathematics — pending the (now well-set-up) literature pass.

## Verdict (honest, preliminary)
1. **Coherent** — as a schema, once P is typed. 2. **Exists** — nontrivial examples, conditional on C's
(co)completeness. 3. **Reduces** — per-instance to known constructions; *hypothesis:* unifies as **(co)limit/end
over the diagram, P = weight**. 4. **Useful** — organizing vocabulary, not (yet) new. **Net:** the test points to
*"essentially X"*, **X = weighted (co)limits / ends over a specified representation-diagram** — with real structure
learned (P must be typed; Rep proper/intermediate; C complete enough). The postponed literature pass is now
maximally informative: compare THIS schema against weighted (co)limits, ends, Kan extensions, institutions,
descent, invariant theory.

## Register / holds
Candidate · non-canon · standard constructions (reconstruct via a non-drafting stream) · the unification is a
**hypothesis from examples, not a theorem** · nothing forced/admitted · Tier-3 to adopt.
*Provenance: 2026-07-07 chat; REPRESENTATION-INVARIANCE-MINIMAL-DEF-2026-07-07.md.*
