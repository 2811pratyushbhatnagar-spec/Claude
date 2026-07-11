# Priority 2 — the existence & uniqueness problem for the minimal observation-preserving quotient   [non-canon · candidate]

*Consolidates the Priority-1 taxonomy (E1–E8) into a clean statement of the central problem — ChatGPT's
"Priority 2: state the existence problem cleanly." Not a proof; a **map of the question**, with every cell
anchored to a computed, reproducible example under `.automation/priority1/`. Nothing promoted; Tier-3; canon read-only.*

## The object
Given a system `(S, F, O)` — states `S`, one-step dynamics `F: S→S` (a *relation* in the nondeterministic case),
observation `O: S→Obs` — form the observation stream `obs(x) = (O(x), O(Fx), O(F²x), …)`. Two readings of
"distinguishability" sit on top of this:

- **Sharp `D`** — the observational-equivalence relation `x ∼ y  ⟺  obs(x)=obs(y)`. Its quotient is the
  **minimal observation-preserving realization**.
- **Graded `D`** — a behavioural (pseudo)metric `D(x,y)` measuring *how far* two states are from observationally equal.

Priority 2 asks, for this minimal quotient / this form `D`: when does it **exist**, when is it **unique**, when is it
**empty/trivial**, and what **geometry** does the graded interior take (its "representability")?

## The four questions, each anchored to a computed example

| Question | Answer (register-careful) | Anchor |
|---|---|---|
| **Existence** | A best (most-abstract *sound*) quotient exists **and** is unique **iff the family of admissible abstractions is meet-closed** (a Moore family / a Galois connection). A non-meet-closed family gives a target with **incomparable** minimal sound quotients ⇒ **no best** = pole **N3 (non-existence)**. | **E2** |
| **Uniqueness** | Even when a minimal realization exists, **uniqueness is a property of the observation *equivalence*, not of the system**: **branching-time / deterministic** (bisimulation) ⇒ **unique** (Myhill–Nerode); **linear-time / nondeterministic** (trace) ⇒ **not unique** (non-isomorphic minimal NFAs). | **E8 (N3b)** |
| **Emptiness / degeneracy** | Two trivial poles bound the interior: **N1** — `O` constant ⇒ `D≡0`, dynamics and observation *separate*; **N2** — `O` behaviourally injective ⇒ all states distinct, *no* reduction. The useful content lives strictly between them. | **E1** (by tuning `O`) |
| **Geometry / representability** | The graded interior's geometry is **inherited from the observation aggregation**, climbing a ladder: symbolic ⇒ **ultrametric** (E1); probabilistic ⇒ **simplex / L1–TV** (E3); real + **L1** aggregation ⇒ **normed** (E5); real + **L2** aggregation ⇒ **Euclidean / inner-product** (E6, *Jordan–von Neumann*); the **ℝ→ℂ** step is **local tomography** (E7); the full **non-simplex complex body** is the reconstruction frontier (E4). | **E1,E3,E4,E5,E6,E7** |

## Three structural theses (candidate · non-canon)

**1. Existence = closure.** A canonical *best* abstraction exists exactly when the admissible-abstraction family is
closed under meets (Moore/Galois). This is the precise content of pole **N3**: drop meet-closure and the best
abstraction genuinely fails to exist (E2). *(Standard order theory; the contribution is only its placement in the schema.)*

**2. Uniqueness = the equivalence, not the size.** The minimal *size* can be pinned while the minimal *object* stays
non-unique. For `L={a,aa}` the minimal NFA has size 3 yet comes in **three non-isomorphic** classes (det-chain vs
proper-nondet fork — trace-equal but **not bisimilar**); determinizing collapses them to **one** canonical minimal DFA
(Myhill–Nerode). So a canonical minimal realization is recovered exactly by quotienting under a **branching-time /
bisimulation** congruence — **linear-time (trace) equivalence loses canonicity** (E8). Independently corroborated by a
second search over a 2-symbol alphabet.

**3. Geometry = aggregation.** Distinguishability has **no single canonical geometry**; it inherits the geometry of how
observation error is aggregated over time. The classical→quantum "ladder" is this inheritance made explicit —
`ultrametric → simplex → normed → inner-product → complex Hilbert` — and the aggregation choice (symbolic / probabilistic
/ L1 / L2) selects the rung. The only genuinely hard rung is the last: *why a complex inner product with a non-simplex
state space*, which is **local tomography + purification / continuous reversibility** — the standard reconstruction
frontier (E1→E7, E4). Quadratic (L2) aggregation is *principled but not uniquely forced by dynamics*; its strongest
internal justification is the **observability Gramian**.

## What this buys — and what it does not

**Buys:** one uniform schema — *existence* (closure), *uniqueness* (equivalence), *degeneracy* (N1/N2), *geometry*
(aggregation ladder) — under which automata minimization, abstract interpretation, behavioural metrics, and
GPT/quantum reconstruction all appear as instances of a single question about the minimal observation-preserving quotient.

**Does not:** prove any new theorem. Each anchor is a known result or a computed witness; the contribution (if any) is
the *uniform organization*, and the one honest open problem is the full complex-QM reconstruction — literature-level,
**not** a toy-example gap.

## Register / holds
Consolidation of E1–E8 · non-canon · candidate · every cell anchored to a reproducible computation · nothing
promoted/admitted · Tier-3 · canon read-only. With this write-up the **bounded example-taxonomy is COMPLETE** and the
auto-loop **pauses generation** (the agreed cap). Open frontier = quantum reconstruction (Hardy / Chiribella–D'Ariano–
Perinotti) — human / literature work, not a toy-example loop. Provenance: 2026-07-10; ChatGPT "Research Program
Assessment" https://chatgpt.com/c/6a4ffe2d-aa78-83ee-b6b1-de0d8defb14a.
