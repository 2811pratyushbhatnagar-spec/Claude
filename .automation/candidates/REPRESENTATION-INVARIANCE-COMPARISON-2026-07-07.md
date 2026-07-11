# Representation-Invariance — systematic comparison + placed verdict   [non-canon · candidate · cited]

*Compares the schema against existing frameworks to place it: reformulation / instance-collection / synthesis /
genuine generalization. Warrant: candidate; **cited**; reconstruct via a non-drafting stream. Nothing forced or
admitted; Tier-3. Provenance: 2026-07-07 chat + web sources (below).*

## The schema (refined per 2026-07-07)
Given **(C, O, Rep, P)** — C an ambient category; O an object; **Rep = a specified *diagram* attached to O**
(arrows: presentations / atlases / automorphisms / restrictions / interpretations); **P = a preservation
criterion** — construct **`I(C, O, Rep, P)`** = the universal object satisfying P w.r.t. Rep. *(Three orthogonal
parameters: C, Rep, P — so the invariant is `I(C,O,Rep,P)`, not `I(O)`.)*

## The comparison
| Framework | Its universal object | As an instance of `I(C,O,Rep,P)` | Verdict |
|---|---|---|---|
| **Weighted (co)limits / Kan extensions** | limit of a diagram `D:J→C` weighted by `W:J→Set`; "all concepts are Kan extensions" | Rep = the diagram, P = the weight, I = the weighted (co)limit / Kan extension | **the formal home** — the schema *is* this machinery |
| **GIT / invariant theory** | categorical quotient `X//G = Spec(k[X]^G)`, the **universal** G-invariant morphism | C = schemes, Rep = G-action, P = invariance, I = `k[X]^G` | **instance** |
| **Descent / sheaves** | global sections = equalizer over a cover | Rep = cover, P = compatible-on-overlaps, I = limit | **instance** |
| **Galois** | fixed field `ℚ̄^Gal = ℚ` | Rep = automorphisms, P = fixed, I = fixed field | **instance** |
| **Institutions (Goguen–Burstall)** | "truth invariant under change of notation" (satisfaction condition) | C = logics, Rep = signature morphisms, P = satisfaction-invariance | **instance (logic)** |
| **Abstract interpretation (Cousot)** | "best abstraction" `α∘f∘γ` via a Galois connection — **may fail to exist** (convex polyhedra) | Rep = abstractions, P = soundness, I = best abstraction | **instance; independently confirms "I need not exist"** |

## Placed verdict
- **Not a genuine generalization** (no new theorems). The schema = "the universal construction determined by a
  specified diagram + a preservation/weight," whose formal home is **weighted (co)limits / Kan extensions** —
  the most general universal-construction-from-a-diagram machinery.
- **It is a useful synthesis / reformulation.** It recognizes invariant theory, descent, Galois, institutions,
  and abstract interpretation as **instances of one template**, and — reached from an ontological start — it
  *rediscovers* that "representation-independent content" is a Kan-extension-flavored universal object. Added
  value over the bare category theory: the **interface/atlas reading** and the **orthogonal (C, Rep, P)**
  parametrization.
- **Confidence hedge (kept):** the home is "**Kan-extension-flavored universal constructions**," with weighted
  (co)limits the *core*; derived/homotopical invariants (cohomology) and non-GC abstractions (convex polyhedra)
  sit at the edge. Not collapsed to "weighted limits" alone.
- **Cross-check (notable):** the schema's Stage-2 prediction that **I need not exist** is independently realized
  by abstract interpretation's non-existent best abstraction for convex polyhedra — a different field exhibiting
  the same phenomenon.
- **The one genuine open problem it contributes** (a well-posed question, not a new object): **characterize the
  diagrams Rep (given C, P) for which `I` is nontrivial** — between the two degeneracies (|Rep| too small →
  tautology; Rep too large → trivial). Existing theories answer fragments (GIT stability; sheaf/descent
  conditions; existence-of-best-abstraction); the schema makes the **cross-domain** version askable.

## What the whole trajectory produced
`Nothing → self-reference → representations → interfaces → universal constructions.` Each step shed
interpretation-specific language; the endpoint is a **located** object (the Kan-extension pattern) with five
named instances. The durable output is the **separation** — motivation (Nothing / identity / physics) · schema
(representation-invariance) · formal realization (Kan-extension-flavored universal constructions) — and the
recognition that the ontology was, in disciplined form, a rediscovery of a central category-theoretic pattern.

## Register / holds
Candidate · non-canon · cited comparison verdict (reconstruct via a non-drafting stream) · "weighted (co)limits"
hedged to "Kan-extension-flavored universal constructions" · nothing forced/admitted · Tier-3 to adopt.

**Sources:** Kan extensions / weighted limits — https://ncatlab.org/nlab/show/Kan+extension ; "All Concepts are
Kan Extensions" — https://legacy-www.math.harvard.edu/theses/senior/lehner/lehner.pdf · Institutions —
https://en.wikipedia.org/wiki/Institution_(computer_science) , https://iep.utm.edu/insti-th/ · Abstract
interpretation (Cousot) — https://cs.nyu.edu/~pcousot/publications.www/CousotCousot-POPL14-ACM-p2-3-2014.pdf ·
GIT categorical quotient — https://userpage.fu-berlin.de/hoskins/GITnotes.pdf
