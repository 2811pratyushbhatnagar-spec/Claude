# Representation-Invariance — definition (proposal, philosophy-free)   [non-canon · candidate]

*Read §1 with no knowledge of the project's history. §§2–4 are orientation and motivation, **explicitly not part
of the definition.** Warrant: candidate definition-proposal; **novelty UNDETERMINED** (to be located). Nothing
admitted or forced; adoption is Tier-3. Provenance: 2026-07-07 chat.*

## 1. Definition
**Data.**
- an object **O** in a fixed category **C**;
- a **specified** family **Rep(O)** of representations of O — morphisms `rᵢ : O → Rᵢ` in **C**. *(Rep(O) is part
  of the data, not secretly determined.)*
- a **notion of preservation** **P** — what "the same across representations" means. *(Primitive data, not
  derived: dependency (O,Rep) → P → I; without P there is no unique I. See the stress test — varying P over the
  same (O,Rep) yields different I: symmetric vs alternating vs coinvariant.)*

**Constructions.**
- **I(O)** — the **universal object (if it exists)** determined by `Rep(O)` and `P`: the representation-independent
  content. *(Not merely "the common part"; a universal property. Which construction realizes it is OPEN.)*
- **S(O)** — *optionally*, a chosen representative `rⱼ ∈ Rep(O)` for computation or communication.
- **G** — *optionally*, a procedure to construct or enumerate `Rep(O)`. *(Not required; many objects are defined
  without an effective generator.)*

**Principle.**
> **Conclusions intended to be representation-independent must be justified by `I(O)`, not by properties of any
> individual representation.**
> *(Corollary discipline: extract the invariant before quotienting by a representation.)*

**Research questions.**
1. How is **Rep(O)** specified?
2. What is the notion of **preservation P**?
3. Which **universal construction** realizes **I(O)** — and **when does I(O) exist**?
4. Under what conditions is **S** canonical?

**The one clean question:** *given a specified family of representations of an object, what universal
construction captures exactly the representation-independent information?*

## 2. Reading (orientation — NOT part of the definition): it is about INTERFACES
The object never appears directly; what appears is a family of ways of presenting it. **Rep(O)** = the
presentation layer · **I(O)** = what survives a change of presentation · **S(O)** = a chosen presentation. The
same shape recurs across **manifolds** (atlases), **algebra** (presentations), **logic** (models/theories),
**programming** (implementations of an interface), **physics** (coordinates / gauges). The proposal isolates the
common architecture behind these — which is why *locating* it (§4) is the right next act.

## 3. Instances (motivation — NOT the definition)
Fix `(C, Rep, P)` and the motivating stories reappear as **candidate realizations** (each admitted only by a
stated both-sides map, Tier-3): **Nothing** (self-negating O; Rep = readings) · **Identity** (I(O) = the
invariant across carriers) · **Physics** (Rep = coordinate/gauge choices; I(O) = the physical content).

## 4. Location checklist (comparison targets — targets, not verdicts)
institutions (Goguen–Burstall) · functorial semantics / sketches (Lawvere) · abstract interpretation (Cousot;
Galois connections) · descent / stacks / sheaves · invariant theory / GIT · model-theoretic definability &
imaginaries (Mᵉ𐞥) · (co)limits and ends. **Win either way:** *located* (named, connected) or *fruitful* (new).
A literature comparison is meaningful now that the object is precise.

## Register / holds
Definition-proposal · non-canon · candidate · novelty UNDETERMINED · nothing forced/admitted · Tier-3 to adopt.
*Distilled from GENERATION-SELECTION-ARCHITECTURE-2026-07-07.md (v1 generator/selector → v2 interpretation-invariant
→ v3 representation-invariance). Refinements applied 2026-07-07: "specified" not "admissible"; G optional; I = a
universal object (existence a question); principle reworded to representation-independence; interfaces reading;
all philosophical terms removed from §1.*
