# Priority 4 — one completely worked example: the whole pipeline on a single LTI system   [non-canon · candidate]

*ChatGPT's Priority 4: "find one completely worked example… one convincing example will teach you more than twenty
abstractions." Carry ONE system through every stage of the pipeline, tying the two framework objects — the
representation-invariance object `I(C,O,Rep,P)` and the `(S,F,O)` minimal quotient — into a single thread that ends in
the distinguishability form `D`. Computed + reproducible (`.automation/priority1/worked_example_pipeline.py`).
Standard linear-systems theory, reorganized under the schema; nothing new proved. Tier-3; canon read-only.*

## The system
Discrete-time LTI `x_{k+1}=A x_k + B u_k`, `y_k = C x_k`, with
`A = diag(0.5, 0.8, 0.3)`, `B = [1,1,0]ᵀ`, `C = [1,1,0]`.
The third mode (eigenvalue `0.3`) has `C₃=0` (**unobservable**) and `B₃=0` (**uncontrollable**) — so it should drop out.

## The pipeline, stage by stage (all verified)
1. **Representation family `Rep`.** Similarity `x ↦ Tx` sends `(A,B,C) ↦ (TAT⁻¹, TB, CT⁻¹)` — a genuinely different
   representation (a random invertible `T` changes both `A` and `C`).
2. **Preservation criterion `P`.** Preserve the input–output map: the Markov parameters `g_k = C Aᵏ B`
   (equivalently the transfer function `H(z)=1/(z−0.5)+1/(z−0.8)`).
3. **The invariant `I(C,O,Rep,P)`.** `g_k = 0.5ᵏ + 0.8ᵏ = [2, 1.3, 0.89, 0.637, …]`, and `C'A'ᵏB' = C Aᵏ B` for
   **every** invertible `T` (verified, `max|g'−g| = 2·10⁻¹⁶`). The Markov sequence **is** the representation-independent
   observable — the concrete `I`.
4. **Minimal quotient (Kalman).** Observability rank `2` (unobservable dim `1`); controllability rank `2`; Hankel-matrix
   rank `2`. So the minimal realization has dimension **2** — a genuine reduction `3→2`. **Existence holds.**
5. **Uniqueness.** The minimal realization is **unique up to similarity** (the `Rep` group): two minimal 2-D realizations
   related by an invertible `S` produce identical Markov parameters (verified), both equal to the 3-D system's. This is
   the linear-systems form of **E8's thesis** — *uniqueness is a property of the equivalence (here the representation
   group), not an absolute property of the object.*
6. **Distinguishability form `D`.** The observability Gramian `W` solves `AᵀW A − W + CᵀC = 0`:
   `W = [[4/3, 5/3, 0], [5/3, 25/9, 0], [0, 0, 0]]`, and `D(x,y)² = (x−y)ᵀ W (x−y)`.
   `ker W = span{e₃}` = the unobservable subspace = **exactly the states the quotient identifies** (`D=0` for states
   differing only in `e₃`). On the quotient `ℝ³/ker ≅ ℝ²`, `W` is positive-definite → a **Euclidean** distinguishability
   geometry (the E6 rung), `D(e₁,e₂)² = 7/9 > 0`.

## Why this is the consolidation
The two framework objects turn out to be **two faces of one construction**. The I/O invariant (Markov parameters,
`I(C,O,Rep,P)`) and the state quotient (Kalman / observability, the `(S,F,O)` minimal realization) are dual views of the
same move — *keep what observation preserves, remove what observation cannot see* — and the graded distinguishability
form `D` (the Gramian) is the refinement whose **kernel is precisely the quotient**. Existence holds; uniqueness holds
**modulo `Rep`**. The thread also ties the taxonomy together: same Gramian family as **E5/E6**, the uniqueness-modulo-
equivalence of **E8**, and the closed (invariant) observable subspace echoing **E2's** existence-via-closure.

## What it does / does not establish
Establishes: a single, concrete, end-to-end instance of the whole schema — one can point at every arrow
(`Rep → P → I → minimal quotient → existence/uniqueness → D`) in one worked system. Does not: prove anything new;
Kalman decomposition and observability Gramians are standard. The contribution is the *single coherent thread* that
makes the abstract schema legible — which is exactly what Priority 4 was for.

## Next (per ChatGPT's order)
Priority 5 — return to quantum reconstruction — is the only step left, and it is **literature/derivation work** (the
full complex-QM axiom set: local tomography + purification / continuous reversibility, per Hardy / CDP), not a toy
example. The bounded computational program (E1–E8 + this worked example) is complete.

## Register / holds
Computed + reproducible · non-canon · candidate · standard linear-systems theory reorganized under the schema · ties
`I(C,O,Rep,P)` ↔ `(S,F,O)` quotient ↔ `D` in one example · nothing promoted/admitted · Tier-3 · canon read-only.
Provenance: 2026-07-10; script `.automation/priority1/worked_example_pipeline.py`; ChatGPT "Research Program
Assessment" https://chatgpt.com/c/6a4ffe2d-aa78-83ee-b6b1-de0d8defb14a.
