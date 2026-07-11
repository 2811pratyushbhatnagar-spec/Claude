# Priority 5 — does compression supply information causality? A first conceptual pass   [non-canon · candidate · CONCEPTUAL, not computed]

*The frontier question: "can a compression-and-capacity `(S,F,O)` framework naturally generate an information-causality
(IC) constraint once composition and communication are added?" This is **sit-and-think** work, not a computation. This
note maps the logical structure precisely — what compression gives, what IC needs, the exact gap, and the specific
derivation target — and gives an honest **import-vs-derive** verdict. It is a map of the question, not a result.
Tier-3; canon read-only; nothing promoted.*

## The three-part structure IC lives in
IC is **not** a single-system statement. It involves three things: (i) Alice's data `D` (an `N`-bit database); (ii) a
bounded classical channel of capacity `m` (Alice → Bob); (iii) a shared correlated resource `ρ_AB`. The claim is
`Σ_k I(D_k : β | b=k) ≤ m` — Bob's *total* accessible information about `D` is bounded by the channel, **whatever the
shared correlations**.

## What the framework's compression gives
The minimal observation-preserving realization is a **single-system** statement: the smallest state reproducing a
system's observations is its observational quotient. It bounds the internal size of Alice's system and Bob's system
*separately*. It says nothing yet about (a) how a composite `ρ_AB` is structured, or (b) how a channel + shared
correlations combine.

## The exact gap
IC = *"shared correlations cannot boost the channel beyond `m` bits."* That is a property of the **composite + channel**,
not of either system alone — and it is **logically independent** of single-system compression. The decisive evidence is
already computed: the **PR box is built from two perfectly ordinary gbits**, each a fine 2-parameter minimal system
(compression is entirely satisfied locally), yet the composite **violates** `I ≤ m` (`ic_rac_game.py`: `I = 2 > 1`).
So **single-system compression does not imply IC.**

## What WOULD supply IC (the derivation target)
A **compositional** strengthening of compression:

> *The minimal joint realization of `(A, channel, B)` that reproduces Bob's observations must **factor through the
> channel** — so Bob's reconstruction of Alice's data is bounded by the channel's capacity, whatever the shared
> correlations.*

"Minimal joint realization factors through the interface" **is** an IC-type statement. The open question is whether this
compositional-compression principle is **forced** by the framework's existing commitments (single-system minimal
realization + the chosen tensor) or is an **extra axiom**.

## Honest verdict (register-careful)
1. Single-system compression **does not** supply IC (logically independent; PR-box counterexample, computed).
2. IC **would** follow from a compositional-compression axiom ("minimal joint realization factors through the interface").
3. Whether that axiom is **forced or imported is unknown** — and is the precise research question. **Current honest
   default: import**, because the framework defines compression per-system and has *no present principle* linking joint
   minimal realization to channel capacity. A derivation would require showing the framework's tensor + minimal
   realization *jointly force* factoring-through-the-interface; **no such argument exists yet.**
4. Even if achieved, this would **not** reconstruct quantum — IC is one discriminator, not the unique/final explanation
   of Tsirelson (recorded caution).

## The concrete thing to look for (if pursuing)
Whether, in the framework's composition, the observational quotient of the **joint** system `A ⊗ channel ⊗ B` necessarily
equals a quotient in which **Bob's marginal depends on Alice's data only through the `m`-bit channel image**. If the
minimal realization forces that factorization, IC follows; if not, it must be imposed. That is a precise, checkable
structural question about the (not-yet-chosen) tensor — and the honest place the program now sits.

## Register / holds
Conceptual analysis (not computed) · locates the logical structure of the frontier question precisely · **single-system
compression ≠ IC** (PR-box counterexample) · IC ⟸ a compositional-compression axiom whose forced-ness is the **open**
question · current default = **import** · nothing new proved · non-canon · Tier-3 · canon read-only. Provenance:
2026-07-10; builds on `PRIORITY-5-INFO-CAUSALITY-2026-07-10.md` and `ic_rac_game.py`.
