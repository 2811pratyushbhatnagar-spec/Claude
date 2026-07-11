# Priority 5 — forcing the compositional-compression axiom: the attempt and its precise outcome   [non-canon · candidate]

*We really tried to **force** the compositional-compression axiom (= information causality) from the framework's
compression core, cross-checked live with ChatGPT. Outcome: it does **not** force from compression-as-counting — for a
precise and correct reason — and the honest result is a **sharply-posed, genuinely-open research problem**, not another
example. Tier-3; canon read-only; nothing promoted.*

## The attempt (four steps)
1. **No-signalling as a compression fact.** Bob's local minimal realization can't distinguish Alice's data `D` (his
   marginal is `D`-independent). ✓ genuine.
2. **Tempting move.** "info available `=` local `(0)` + message `(≤m)` `= ≤m`" ⇒ IC.
3. **Why it fails.** The additivity is wrong: the PR box is no-signalling **and** uses a 1-bit message yet yields 2 bits
   (van Dam). The shared correlation carries no `D`-info alone but produces a **decoding advantage in combination with
   the message** — *control of **synergistic information*** (structurally a "key," but the precise notion is synergy).
   So no-signalling + message-counting does **not** give IC. *(ChatGPT: "essentially the correct diagnosis.")*
4. **Reduction.** IC (Pawłowski) is built from **mutual information** `I(X:Y) = H(X)+H(Y)−H(X,Y)` — i.e. **Shannon**
   entropy — and its proof uses Shannon / von-Neumann **chain-rule** identities. The framework's minimal realization is
   state-**counting** → **Hartley / Rényi-0** entropy (`H₀` = log of the minimal-realization dimension), which "says
   nothing about probabilities."

## ChatGPT's verdict (skeptical cross-check)
- **"Rényi-0 is not enough" — confirmed.** Counting gives Hartley `H₀`; IC needs Shannon `H₁` (mutual information).
- **But "compression can NEVER force IC" is too strong.** What is actually shown: Shannon `H₁` requires a **probability
  distribution over the minimal realization**, and *at present nothing in `(S,F,O)` selects one* — so without
  probabilities, `H₁` is simply **undefined**. If the framework acquires probability measures, updating, coding
  theorems, asymptotic typicality, then Shannon **could** emerge.
- **On boxworld (safe historical claim):** *"boxworld exposes that convex state spaces + dimension + no-signalling are
  insufficient; its entropy proposals fail enough of the Shannon-like identities the IC proof needs"* — not "boxworld
  has no entropy, therefore violates IC."

## The precise outcome — a reframed, genuinely-open research problem
The question is **no longer** "can counting prove IC?" (answer: **no** — Rényi-0 ≠ Shannon). It becomes:

> **Can structural compression be extended into a probabilistic coding theory whose canonical entropy is Shannon rather
> than Hartley?**

*(ChatGPT: "That is a precise research problem. It is also where the current framework is genuinely incomplete, rather
than merely awaiting another example.")*

## Why this closes the loop cleanly
The upgrade this demands — **a probability distribution over the minimal realization** — is the *same* `[0,1]`
convex/probabilistic upgrade that earlier produced the gbit and entanglement (the "probability = nothing..everything"
step). So the framework's own next structural move (**become probabilistic**) is the **shared prerequisite** for *both*
entanglement *and* a Shannon-capable compression. Until then, compression = Hartley `H₀` (counting), which provably
**cannot** force IC; after it, the compression → IC derivation becomes a live, well-posed question — still gated on the
Shannon chain-rule identities that boxworld fails.

## Register / holds
Genuine forcing attempt + live cross-check · the naive forcing (no-signalling + counting) provably **fails** (van Dam /
synergistic information) · IC needs Shannon `H₁`; counting gives Hartley `H₀`; `H₁` is undefined without a probability
distribution the framework doesn't yet select · honest verdict: **not forced by compression-as-counting; not proven
impossible; the real gap is a probabilistic coding theory (Shannon) the framework lacks** · this is genuine
*incompleteness*, not a missing example · nothing promoted · Tier-3 · canon read-only. Provenance: 2026-07-10; ChatGPT
https://chatgpt.com/c/6a4ffe2d-aa78-83ee-b6b1-de0d8defb14a; Pawłowski et al. 2009 (information causality);
Barnum–Barrett–Leifer–Wilce (entropy in GPTs); van Dam (nonlocality & communication complexity).
