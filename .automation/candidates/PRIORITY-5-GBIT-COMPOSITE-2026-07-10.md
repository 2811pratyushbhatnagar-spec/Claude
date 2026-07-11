# Priority 5.5 — the gbit composite: local tomography HOLDS, entanglement PRESENT   [non-canon · candidate · computed]

*Executed ChatGPT's calibrated target — add the `[0,1]` convex structure (probability = nothing..everything) via the
square bit ("gbit"), then compute the one number it named: the affine dimension of the composite state space.
(`.automation/priority1/gbit_composite.py`, numpy + scipy, exact.) Tier-3; canon read-only; nothing promoted.*

## The model
A single **gbit** has two fiducial binary measurements `X, Z`; a normalized state is `(P(X=0), P(Z=0))` in the unit
**square** `[0,1]²` — convex but **not a simplex**. GPT state vector `v = (1, x, z)`; the 4 pure states are the corners;
`K = 3`, `dim Ω_A = 2`. This is the smallest model where local state space is convex-non-simplex and composition is
nontrivial.

## Computed (exact)
- **`dim(Ω_AB)` = affine rank of the 16 product states = 8 = `(2+1)(2+1) − 1`  ⇒  LOCAL TOMOGRAPHY HOLDS.** The composite
  gains dimension the way **classical** *and* **complex QM** do — *unlike* real QM, where E7's Wootters count was `9 < 10`.
- A **PR box** (the no-signalling correlations `P(ab|xy) = ½` iff `a⊕b = x·y`) is **not** a convex combination of product
  states (LP infeasible) ⇒ a genuine **non-product extreme point** ⇒ **entanglement is present** in the (max) tensor.

## Reading
The gbit is a **locally-tomographic theory that nonetheless has entanglement**, sitting **strictly between** the
classical simplex (no entanglement) and quantum. This closes the subtlety cleanly:

> **Local tomography is not classicality.** It is E7's ℝ-vs-ℂ test (holds for classical, complex QM, *and* the gbit;
> fails for real QM). And it is reached only **after** adding the `[0,1]` convex structure — the simplex first, then a
> non-Cartesian tensor that admits entangled extreme points like the PR box.

## Where it sits in the map (now computed end-to-end)
`deterministic (S,F,O)`  →  **+ convexity**  →  `classical simplex` (correlated but separable)  →  **+ non-Cartesian
tensor**  →  `gbit` (locally tomographic, entangled)  →  … → `quantum`. The gbit is the smallest calibrated waypoint
*past* the simplex; **quantum is a further restriction** — the sub-theory of the max/boxworld tensor that forbids PR
boxes while keeping local tomography. That "what selects quantum inside the locally-tomographic-with-entanglement class"
is the next reconstruction question (Hardy's continuity / CDP's purification live here).

## Register / holds
Computed + reproducible · standard boxworld/GPT facts, reorganized as the framework's **calibrated waypoint** past the
simplex · the `[0,1] = nothing..everything` convex step is now concretely instantiated · nothing new proved · non-canon
· Tier-3 · canon read-only.
**ChatGPT-ASK (staged):** confirm the gbit affine-dimension count and the placement — *quantum = the sub-polytope of the
max tensor that forbids PR boxes and keeps local tomography; what axiom (continuity? purification?) selects it?*
Provenance: 2026-07-10; `gbit_composite.py`; builds on `PRIORITY-5-COMPOSITION-SKETCH-2026-07-10.md`.
