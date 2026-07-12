# O-Conjecture v0.2 — Pointed Carrier Ledger

**Date:** 2026-07-03 · **Band:** STRUCTURED (Tier-1 identities EXACT, machine-checked) · **Status:** OPEN

## Question

Does there exist a single mathematical object **O**, with two canonical modes of
presentation — one intrinsic, one reconstructive — such that every FROZEN
kinematic deposit in the archive arises as a faithful image, quotient,
completion, or presentation of O, with all named selectors quarantined at the
*selection* of O and never appearing inside a construction?

## The object

**O = (ℤ[ω], ¯· , 𝔭)** — the Eisenstein order with its conjugation involution,
pointed at its unique ramified prime **𝔭 = (ω − 1) = (1 + 2ω)**, lying over 3.

## Tier-1 identities (EXACT — `verify_o_pointed_carrier.py`, exact integer arithmetic)

- **u = −ω·λ** where λ = ω − 1 (the non-return defect at h = 1) and u = 1 + 2ω
  (the orientability cycle element of the Chirality Price Gate). The defect and
  the orientation generator are **unit-associates**: same ideal 𝔭.
- **λ² = −3ω**, hence 𝔭² = (3). **u² = −3 = disc ℚ(ω).**
- **N(λ) = N(u) = 3**; residue weights x_h = N(ω^h − 1) = [0, 3, 3]; in
  particular **x₁ = N(𝔭)**, and the ⅓ in γ = ⅓ρ(u)ρ°(u) is 1/N(𝔭).
- **ℤ[ω]/𝔭 ≅ 𝔽₃** — the Z₃ carrier is the residue field of 𝔭.
- **ω ≡ 1 mod 𝔭** and conjugation acts trivially on 𝔽₃ — the two faces σ/σ̄
  fuse at 𝔭.
- **μ₆/{±1} ≅ Z₃** — the charge group of the Gauge/Charge Gate is the unit
  group of O modulo the invisible center.
- The shifted table x∗y = x + y + 1 is addition **transported along the root
  displacement** (φ(x) = x + 1 is an isomorphism onto (Z₃, +)); the identity
  e = 2 is derived, not stipulated — a torsor (affine) presentation of 𝔽₃.

**Upgrade of a logged loose residue:** the archive recorded "u² = −3 = disc"
as a rhyme. It is not a rhyme: (λ) = (u) = 𝔭. The seed defect, the Dirac
determinant's vanishing locus, the residue weight, the chirality grading's
integral representative, the discriminant, and the carrier are six
manifestations of one pointed prime. The frozen line "the Dirac operator is
the concrete instance of N(N) ≠ N" extends: **the chirality grading is the
concrete instance of the residue** — γ is represented by a unit multiple of
the defect.

## The two modes (fiber reading)

- **Intrinsic ι(O)** — reduction at 𝔭: the residue torsor. 𝔽₃ with affine
  structure, origin derived (e = −1), carrying the 0→1→2→0 recurrence.
  Here the defect **vanishes** (ω ≡ 1) and the two faces coincide.
- **Extrinsic ε(O)** — archimedean completion: ℂ_ℝ with σ ≠ σ̄ maximally
  separated. The separation **is** the bimodule room; the certified two-sector
  no-go says chirality needs exactly this.

**Consequence (theorem-shaped answer to the double-reading question):** the
Z₃ recurrence lives where the defect vanishes (char 3, faces fused);
chirality lives where the defect is visible (char 0, faces split). **No single
fiber of O supports both strata.** The explicit/implicit double reading is
forced, not optional — the frozen deposits sit at different places of the same
arithmetic object. This retro-explains the three independent detections of a
two-mode split in the record: N_i/N_o (source floor), Version A/B (DC-003
Stage 0), Route A/B (WU0 category audit).

## Conjecture statement (v0.2)

> Every FROZEN kinematic deposit factors through ι(O) or ε(O) using only the
> five-construction vocabulary **{reduction mod 𝔭, base change to ℂ, norm,
> unit action, one-form calculus}**, and the four named selectors (RSC, P1,
> P2, minimality) occur only in the selection of O — never inside a
> construction.

The selector-quarantine clause is what makes the test sharp: selectors may be
axioms (that is what selectors are), but if a construction *from* O needs a
new assumption mid-derivation, that row fails and O is not the generator.

## Factorization table

| Deposit | Construction (vocabulary item) | Verdict |
|---|---|---|
| Shifted ℤ₃ table | reduction mod 𝔭 + torsor transport by root | conditional on selection only ✓ |
| Residue weight x_h | norm of the defect: N(ω^h − 1) | native ✓ (x₁ = N(𝔭)) |
| Character lemma | characters of μ₃ = unit action | native ✓ |
| Factorization theorem det D̸ = (ω^h−1)·C_N | reduction + norm on the lattice | lattice scaffold paid, flagged |
| Orientability cycle u | unit action on the defect (u = −ωλ) | **native — upgraded from loose residue** ✓ |
| Chirality host (3-sector triple) | base change + bimodule of σ/σ̄ | NCG axiom package paid, flagged at selection of ε ✓ |
| Charge pattern (−1, 0, +1) | unit action: μ₆/{±1} on sectors | native ✓ |
| Higgs-like scalar φ | one-form calculus on the Dirac edge | calculus imported, flagged ✓ |
| Mode-locking (Beam 001) | norm (−log x_h) **+ stabilizer** | **fails the quarantine clause** — in-construction import; correctly outside the kinematic stratum |
| Dynamics · continuum · D1 / BD lanes | — | outside O's scope; already proven so (Source-F, six walls, imported lanes) |

## Tier-2 candidate lemma (localizes N-01)

Recast the source conditions arithmetically:

1. **Two faces, exactly** (the σ/σ̄ pair) ⇒ embedding set of size 2 ⇒
   φ(n) = 2 ⇒ candidates are only ℤ[i] and ℤ[ω] (n = 3, 4, 6; ℤ[ζ₆] = ℤ[ω]).
2. **Depth-2 non-return** (T²(n) ≠ n) ⇒ the Gaussian ramified residue field
   𝔽₂ = ℤ[i]/(1+i) has additive recurrence of period 2 — **excluded**. 𝔽₃
   has period 3 — the least that survives.

Within the two-embedding cyclotomic frame, ℤ[ω] is uniquely forced by the
source conditions; minimality is never invoked as a choice (C₄, C₅, … are not
residue fields of any two-face candidate). This does not close N-01; it
**localizes** it from "does P1 ∧ minimality force Z₃?" to "does the two-face
floor force the monogenic cyclotomic frame?" — the honest arithmetic content
of P2, and a strictly smaller open question.

## Tiered falsification

- **Tier 1** — arithmetic identities: verified exact (this deposit). Failure
  would be immediate refutation; they are theorems of ℤ[ω].
- **Tier 2** — (a) five-construction factorization of every frozen kinematic
  row (checkable row by row against the price ledgers); (b) the ℤ[i]-exclusion
  lemma (elementary; would move N-01). Either failing demotes O from
  *generator* to *minimal compression* — the demotion path the bootstrap's
  Type B classification already carries.
- **Tier 3** — scope boundary: settled negative by existing frozen deposits.
  O's earned role, if Tier 2 passes, is generator of the kinematic-arithmetic
  stratum at two places — no more, and provably no less.

## Does not claim

Does not claim O is Nothing, awareness, reality, or paradox. Does not claim
dynamics, continuum physics, gauge theory, the Standard Model, or the measured
universe. Does not claim the strong form (every successful structure from O
without additions) — that form is already falsified by the archive's own
frozen deposits. Claims only: the frozen kinematic deposits are fiber-images
of one pointed arithmetic object, with the selectors quarantined at selection;
and the Tier-1 identities, which are exact.

## Provenance

Assembled 2026-07-03 from: Research Index (frozen 8 June 2026) · Gate D
Dependency Ledger v0.1 · Source Axioms v0.1 · DC-003 · Chirality Price Gate
v0.1 (CERTIFIED) · Gauge/Charge Price Gate v0.1 WU1 · Physics Relevance &
Contact Audit v0.1 WU0 · Closed Routes · Open Gates. Conjecture reformulation
prompted by an external-chat proposal (intrinsic/reconstructive two-mode
test); pointing at 𝔭 and the fiber reading are new in this deposit.

**Reproduce:** `python3 verify_o_pointed_carrier.py` — exact integer
arithmetic in ℤ[ω] (no floats), exhaustive enumeration on finite windows;
exit 0 iff all 21 checks pass.
