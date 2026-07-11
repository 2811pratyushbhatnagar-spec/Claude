# A universal construction from a specified diagram under a preservation criterion — where does it belong?

*A self-contained note for a category theorist. No motivation, no application — just the construction, worked
examples, degeneracies, and open questions. The single question is one of **placement**, not novelty.*

## 0. The one question
Given the data and construction below, **is this a standard categorical construction, and if so what is its
canonical name?** Candidate homes I can see — weighted (co)limits, Kan extensions, ends/coends, descent,
categorical Galois theory, closure operators / reflective localizations — are listed in §5 for you to confirm,
reject, or refine. I am **not** claiming novelty; I want the correct existing language, or a clear statement that
the construction is a union of several existing notions.

## 1. Primitive data `(C, O, Rep, P)`
- **C** — a category (the ambient setting).
- **O** — an object of `C` (the thing presented in many ways).
- **Rep** — a *specified diagram* `D : J → C` from a small index category `J`, whose vertices are presentations of
  `O` and whose arrows are the admissible change-of-presentation comparisons, together with a structural map tying
  the diagram to `O` (a cone `O → D` or a cocone `D → O`, per variance). `Rep` is **given data**, not "all
  presentations."
- **P** — a *preservation criterion*: what it means to respect `Rep`. Concretely `P` is either (i) a **weight**
  `W : J → Set` (or into an enriching base `V`), or (ii) a **property** (invariant under the arrows / fixed by them
  / compatible-on-overlaps / sound).

## 2. The construction
Define **`I(C, O, Rep, P)`** as the universal object satisfying `P` with respect to `Rep` — the terminal such
object (or initial, dually), when it exists:
- with `P` a property: `I` = the limit / equalizer / fixed-object cut out by "respects every arrow of `Rep`";
- with `P` a weight: `I` = the `P`-weighted (co)limit of `D`.

**Operational reading under test:** any property asserted to be independent of the choice of presentation must be a
property of `I`, not of an individual vertex `D(j)`.

## 3. Worked examples (all standard; the claim is only that one template covers them)
| # | `C` | `O` | `Rep` | `P` | `I` |
|---|-----|-----|-------|-----|-----|
| 1 | affine schemes | `X` with `G`-action | the `G`-action | invariance | `k[X]^G`, i.e. `X⫽G` (GIT quotient) |
| 2 | (pre)sheaves | space + open cover | Čech diagram of the cover | agree on overlaps | global sections (equalizer / limit) |
| 3 | fields | extension `L/k` | `Aut(L/k)` acting on `L` | fixed by all | fixed field `L^{Aut}` |
| 4 | signatures / logics | a presentation of a theory | signature morphisms | satisfaction-invariance | the invariant assertions (institutions) |
| 5 | a concrete domain | concrete semantics | a family of abstractions | soundness (Galois connection) | best abstraction (**may not exist**) |

## 4. Degeneracies (why the construction is not automatic)
- **Trivial-below (tautology).** If `Rep` has no nontrivial comparisons (`J` discrete, or `|J| = 1`), then
  `I ≅ O`: the construction returns its input and asserts nothing.
- **Trivial-above (collapse).** If `Rep` carries enough collapsing comparisons, `I ≅ 1` (terminal): everything is
  identified away.
- **Non-existence.** `I` is a **partial** operation. In `FinSet`, an infinite tower of proper injections has no
  finite universal vertex. Example 5 (convex polyhedra) has no best abstraction — a documented non-existence in a
  different field.
- **`P`-dependence.** Fixing `(C, O, Rep)` and varying `P` alone changes `I` (invariants vs. coinvariants;
  symmetric vs. alternating). `P` is not cosmetic.

The interesting regime is the proper one: **`1 ⊊ I ⊊ O`.**

## 5. Candidate placements (please adjudicate — §0, itemized)
1. **Weighted (co)limits / Kan extensions.** With `P` a weight, `I` is literally a weighted (co)limit of `D`;
   "all concepts are Kan extensions" suggests this is the general home. *Does the property-form of `P` also live
   here, or only the weighted form?*
2. **Ends / coends.** When `P` is "dinatural compatibility," `I` reads as an end. *Is the general construction an
   end over a suitable bifunctor?*
3. **Descent / stacks.** Examples 2 and 4 are descent. *Is `Rep` always a (co)descent diagram, or is descent a
   proper special case?*
4. **Categorical Galois theory (Janelidze–Tholen).** Examples 3–5 pair "presentations" with "invariants" via a
   Galois connection. *Is §6 exactly the theory of admissible reflections?*
5. **Closure operators / reflective localizations.** See §6.

I suspect (1) is the closest *general* answer, but I am explicitly **not settling** this: an earlier iteration
over-committed to "`I` is the limit" and had to retract. I would rather be told it is (1), or (1) ∪ (4), or
something I have miscategorised.

## 6. The question I believe is genuinely open (nontriviality / discrimination)
**Problem.** Fix `(C, O)`. Characterize the pairs `(Rep, P)` for which `1 ⊊ I(C,O,Rep,P) ⊊ O` — proper and
nontrivial.

**Per-domain answers already exist:**
- **GIT:** nontriviality ⟺ stability; Hilbert–Mumford criterion via one-parameter subgroups; the null cone.
- **Galois:** proper intermediate invariants ⟺ proper nontrivial subgroups; a simple group ⟹ only trivial
  invariants.
- **Descent:** nonconstant global sections; obstruction classes in `H^{≥1}`.
- **Abstract interpretation:** existence of a best abstraction (the Galois-connection condition).

**Conjectural uniform form.** `Rep + P` induce a **closure operator** (equivalently a Galois connection) on the
subobject (or congruence) lattice of `O`; **`I` is nontrivial iff that closure has a proper fixed point** strictly
between `⊥` and `⊤`. The four per-domain criteria would then be shadows of one lattice-theoretic statement.

**Question:** is this uniform statement already a theorem (and if so, where), false as stated, or open but
well-posed and worth pursuing?

## 7. What I am asking
Not "is this new." Rather: **name the construction** (§5), and say whether **§6 is known, false, or open**. Any of
"it's weighted limits," "it's categorical Galois theory," "it's half descent and half invariant theory," or "your
§6 is Theorem X in [ref]" is a fully satisfying answer and improves the work.

---
*Repo metadata (not part of the note): non-canon · candidate · register-stamped · nothing forced/admitted · Tier-3.
Content assembled from REPRESENTATION-INVARIANCE-{MINIMAL-DEF,STRESS-TEST,COMPARISON}-2026-07-07.md; all framework,
ontology, and physics language deliberately stripped for specialist review. Provenance: 2026-07-07 chat.*
