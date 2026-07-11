# Priority 5 — reading the primary sources + supply-vs-import analysis (cross-checked)   [non-canon · candidate]

*Read Hardy 2001 (quant-ph/0101012) and CDP 2011 (PRA 84 012311; arXiv:1011.6451) in the primary sources, extracted
the axioms, asked the disciplined question — does the `(S,F,O)`/recursive-persistence framework **supply** each axiom
or **import** it — and ran the whole analysis past ChatGPT (skeptical register). This note records the axioms, the
verdict, and the one concrete next structure that came out of it. Tier-3; canon read-only; nothing promoted.*

## The axioms (from the sources)
**Hardy (2001).** Two integers: `N` = max states reliably distinguished in one shot; `K` = min number of probability
measurements to determine a state. `K = N^r`. Five axioms — 1 Probabilities, 2 Simplicity (`K=K(N)`, minimal),
3 Subspaces (an `M`-dim subspace behaves like an `M`-dim system), 4 Composite systems (`N=N_A N_B`, **`K=K_A K_B`** =
local tomography), 5 **Continuity** (*there exists a continuous reversible transformation between any two pure states*).
Axiom 5 forces `r=2` and **rules out classical** (`r=1`, `K=N`); local tomography (Axiom 4) selects **complex** over
real/quaternionic.
**CDP (2011).** Five informational axioms — causality, perfect distinguishability, ideal compression, local
distinguishability (= local tomography), pure conditioning — define a broad class; one postulate, **purification**
(every mixed state is the marginal of a pure state, essentially unique up to reversible transformations on the
environment), singles out quantum.

## Supply-vs-import — my analysis + ChatGPT's scorecard
The disciplined question: for each axiom, does the framework's own structure *supply* it, or must it be *imported*?

| Candidate supply | My claim | ChatGPT's verdict (skeptical) |
|---|---|---|
| **Ideal compression = minimal realization** | the CORE (minimal observation-preserving quotient / Kalman) | **Strong** — substantive, *not merely verbal*, if stated operationally ("given `O`, replace the system by the smallest state space preserving all observable behaviour" = DFA minimization etc.). But **not the same object** (CDP's is informational, ours behavioural/dynamical): say *"same abstract optimization pattern — minimal faithful representation — in different operational settings."* Do **not** claim "our theorem proves ideal compression." |
| **Observable subspace = subspaces axiom** | Kalman observable subspace (P4) | **Strong** — "real mathematics, no issue." |
| **Causality = the arrow of `F`** | directed persistence dynamics | **Moderate** — supplies *directed dynamics*, but that is **not** CDP's causality (an operational *no-signalling-from-the-future* statement). Related, not the same theorem. |
| **Continuity via reversibility of `F`** | reversibility supplies Hardy's continuity | **Not yet / weak** — *reversibility does not imply continuity.* Finite groups, discrete automata, permutations are all reversible yet **none** satisfy Hardy's continuity axiom. (Direct pushback — my hopeful lead was wrong.) |
| **Purification via observable/unobservable = system/environment** | the quotiented states look like a purifying environment | **Mostly analogy** — structural resemblance only; purification's *uniqueness up to reversible transformation on the environment* is **not** established. Weakest claim. |

## The verdict (ChatGPT: "the part I find most convincing")
My diagnosis — *the framework robustly supplies the compression / minimal-realization skeleton, and every specifically
**quantum**-injecting axiom (continuity, purification, and the ℂ-forcing local tomography) is weak or imported* — was
called **accurate**, with one important **register correction**:

> **Do not call the framework "classical" — it has not proved that.** Say instead: *the framework is presently a theory
> of **minimal observable dynamics**, and quantum reconstruction begins when one asks **how independently specified
> observable systems compose**.*

So the honest boundary is not classical-vs-quantum; it is **single-system vs composite**. The framework lives entirely
on the single-system side; every reconstruction axiom that injects quantum structure lives on the composition side.

## The one concrete next structure (the genuinely useful output)
ChatGPT's answer to "what is the smallest addition that would let the framework even *pose* local tomography" is **not
local tomography itself** but, more primitively:

> **A symmetric monoidal (tensor) composition law on observable systems** — a rule taking `(S₁,F₁,O₁)`, `(S₂,F₂,O₂)`
> to a joint `(S₁₂,F₁₂,O₁₂)`.

Only then can one ask the real questions: *What are the admissible composite observations? Does every global observable
factor through local ones? Is the induced observation functor faithful on composites? Does minimal realization commute
with composition? When does `Obs(A⊗B) ≅ Obs(A)⊗Obs(B)`?* **Local tomography becomes a property of that composition**
(does the tensor of observables recover all joint observables), not an imported statement. That is the concrete,
bounded, mathematical next direction — and it connects straight back to the framework's own "plurality / n-copies"
thread.

## Register / holds
Literature read in primary sources · axioms extracted (Hardy verbatim; CDP from the published record) · supply/import
analysis cross-checked with ChatGPT (skeptical) · **corrections absorbed**: compression/subspaces = strong (pattern-
level, not identity); causality = only directedness; continuity-via-reversibility = **wrong** (reversibility ≠
continuity); purification = analogy only · framework is *minimal observable dynamics*, **not** proved classical ·
reconstruction boundary = **composition** · concrete next step = a symmetric monoidal law on observable systems, with
local tomography as a property of it · nothing promoted/admitted · Tier-3 · canon read-only. Provenance: 2026-07-10;
Hardy quant-ph/0101012; CDP arXiv:1011.6451; ChatGPT https://chatgpt.com/c/6a4ffe2d-aa78-83ee-b6b1-de0d8defb14a.
