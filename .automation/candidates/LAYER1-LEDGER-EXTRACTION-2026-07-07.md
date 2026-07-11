# Layer-1 ledger — EXTRACTED from deposited results (not authored)   [non-canon · candidate · source-cited]

*The disciplined test of the Layer-1 proposal: for each already-deposited result, fill
`Introduces / Preserves-Exposes / Forgets / Depends-on / Provenance-Derivation` by **extraction from the repo**,
not from a blank page and not from memory. Done here against the actual files (Claude has repo read access; the
relaying ChatGPT instance did not). Sources: `[LA]` LedgerA/ledger_A_canonical.md (v0.7, FROZEN — read-only) ·
`[CL]` Experiments/carry_character_lemma.md · `[CSS]` Experiments/Carry-Set_Separation_note.md ·
`[FE]` Experiments/carryset_fixed_e_proof.md. Nothing edited in canon; candidate only; Tier-3.*

## Headline (two findings)
1. **The four info-flow columns extract cleanly for every real deposit** — the Layer-1 method *fits what is
   already proven*, no invented primitives needed.
2. **The Provenance/Derivation column is EMPTY for every deposit** — confirmed by reading, not assumed. That empty
   column is the genuine Layer-1 content still to write (the same Stage-0 "are two derivations of one value the
   same object?" question), and it is **absent from the deposits, not merely unformatted.**

## The extraction (each cell tagged with its source)

### R1 — the bijection theorem  `[LA]`
- **Introduces:** from a pair of relations with `R;S=Δ_A`, `S;R=Δ_B` (two-sided return identity), the conclusion
  "`R` is the graph of a bijection, `S=Rᵀ`."  `[LA §Theorem R1]`
- **Preserves/Exposes:** exactly the bijective content — totality, single-valuedness, injectivity, surjectivity
  (all four inclusions individually load-bearing); `|A|=|B|` is *exposed as a consequence*, cardinality-free.  `[LA]`
- **Forgets:** all quantitative/finite information (cardinality-free); the non-strict "free" structure lives
  outside its hypotheses.  `[LA]`
- **Depends-on:** the two inverse-composite identities (F-eq at strict identity effects); `Rel`. Nothing about
  finiteness, physics, or dynamics.  `[LA §Remarks]`
- **Provenance/Derivation:** **EMPTY** — R1 is about the *relations*, silent on whether two presentations yielding
  the same bijection `f` are one object or two.

### D5 determinism ladder  `[LA]`
- **Introduces:** three rungs set by the *identity-effect axiom* (free / sub-identity / strict).  `[LA §D5 ladder]`
- **Preserves/Exposes:** the determinism gradient — free = nondeterminism admitted (37 of 56 · 4087 of 4400);
  sub-identity = partial bijections `= |Iₙ|` (7 · 34); strict = total bijections `= |Sₙ|` (2 · 6).  `[LA]`
- **Forgets:** general-`n` structure (the `Iₙ`/`Sₙ` identification is FINITE-verified n=2,3; **GENERAL OPEN**).  `[LA]`
- **Depends-on:** the identity-effect rung (*not* functoriality); the tested encoding `ι: bᵢ↦aᵢ`.  `[LA]`
- **Provenance/Derivation:** **EMPTY.**

### The Character Lemma  `[CL]`  — *(this is what the relay calls "Θ / the reconstruction theorem"; see drift note)*
- **Introduces:** the classical sawtooth `((x)) = ⟨x⟩ − ½` on `(ℤ/e)^×`, summed over a 6-tuple `v`, expanded in
  **odd** Dirichlet characters.  `[CL Proof of the Character Lemma]`
- **Preserves/Exposes:** the **odd part `n⁻`** of the multiplicity function (the *antisymmetrization*) — the
  odd-character coefficients `Σᵢ χ(vᵢ)`. Conclusion: `n⁻ ≡ 0`, i.e. `v = −v` (negation-symmetry).  `[CL]`
- **Forgets:** the entire **even part `n⁺`** — annihilated by odd characters — **which includes the total mass
  (the trivial character).**  `[CL]`
- **Depends-on:** the finite prime field `(ℤ/e)^×`; the `T′` condition (`Σ⟨t vᵢ/e⟩ = 3 ∀ units t`); classical
  `B_{1,χ}≠0` for odd `χ`; the multiset `v`. Nothing physical.  `[CL]`
- **Provenance/Derivation:** **EMPTY.**

### Carry-Set Separation (CSS) + fixed-`e` `K(e)=D(e)`  `[CSS]` `[FE]`
- **Introduces:** the non-carry set `Φ_m = {t : (t mod e)+(mt mod e) < e}`; claim `m ↦ Φ_m` **injective on
  `G≅S₃` orbits up to scaling** ⇒ the `r(e)` orbit-traces + 1 are ℚ-independent (`K(e)=D(e)`), contingent on CSS.  `[FE Statement]`
- **Preserves/Exposes:** the **`G`-orbit of `m`** (the CM type up to Galois/scaling) — equivalently the
  j-invariant `I(m)=8(m²+m+1)³/(m²+m)²`, which separates orbits.  `[FE Appendix]`
- **Forgets:** everything below the *set* level — the carry **count** `|Φ_m|` (a single Dedekind sum / balanced-
  subgroup condition captures the count, not the set), so count-level invariants do not separate.  `[CSS §4.5]`
- **Depends-on:** a fixed odd prime `e`; the **CSS contingency** (open; verified computationally to `e ≤ 2000`);
  KR78 Thm 1 (primary-source read, *not reproduced*); CM theory (cited).  `[FE Register]`
- **Provenance/Derivation:** **EMPTY.**

### Prime-power fiber law  `[CSS §5]`
- **Introduces:** over `e = pᵏ`, the fiber of `Φ_m` over `s ∈ (ℤ/e₁)^×` has size `(d±1)/2` (`d=p^{k−1}`),
  exception exactly at `m ≡ −1 (mod p)`.
- **Preserves/Exposes:** the **count-level** (balanced-subgroup) structure of the fibers.
- **Forgets:** the **set-level** content — explicitly *does not* bear on set-level CSS.  `[CSS §4.5, §5]`
- **Depends-on:** prime-power modulus; the averaging identity `Σf=d(d−1)`, `Σ(f mod d)=d(d−1)/2`.
- **Provenance/Derivation:** **EMPTY.**

### N(N)≠N as a law  `[LA §signature D1–D6]`  — *(Ledger-A signature decision / ontology register, not a number-theory theorem)*
- **Introduces:** the **availability/execution split** — availability `= N(N)≠N` (a step is *possible*), execution
  `= N(N)=N` (it *happens*).  `[LA "availability/execution split"]`
- **Preserves/Exposes:** the distinction between a relation being *available* and being *realized*.
- **Forgets:** —
- **Depends-on:** the signature `Σ₀` decisions D1–D6.
- **Provenance/Derivation:** closest of all rows to a provenance statement (availability vs realization), but it
  **still does not** decide "two derivations of the same value = same or distinct object." **Effectively EMPTY on
  the Stage-0 question.**

## Drift-flags on the relayed example rows (the anti-drift payoff)
- **"Θ (sawtooth operator) / reconstruction theorem"** → the underlying object is **real** = the Character Lemma
  `[CL]`, but the *name* "Θ / reconstruction theorem" is **not in the deposits** (the sawtooth `((·))` is a
  classical device used *inside* the lemma's proof, not a named framework primitive). And one cell is **drift:**
  the relay's "**preserves total mass** + antisymmetrization" is half-wrong — the lemma **forgets** the total mass
  (it is the trivial character, part of the annihilated even part `n⁺`); only the **antisymmetrization `n⁻`** is
  exposed. *Corrected above.*
- **"σ — the compatibility map (integer-valued iff the multiset sums to zero)"** → **NOT LOCATED** in the deposits
  read `[CL][CSS][FE][LA]`. The "sums to zero" condition (`a+b+c ≡ 0`) is real and central, but a *named map σ*
  with that property is not on disk in what was read → **reconstructed-from-relay; needs a pointer or is absent.**
- **"carry-set fiber theorem — the 2-to-1 map `μ ↦ N_λ`"** → **NOT MATCHED.** The real neighbors are CSS
  (`m↦Φ_m` injective on `G`-orbits — orbit size up to 6, not 2) and the prime-power fiber law (`(d±1)/2`). A
  "2-to-1 `μ↦N_λ`" map is not in the deposits read → **reconstructed-from-relay; needs a pointer or is absent.**
- **"N(N)≠N as a law"** → **real**, but a Ledger-A *signature decision* (ontology register), not a number-theory
  deposit; filled above with that caveat.

## Verdict (what to actually do for Layer 1)
- **Build Layer 1 from the rows I could extract from source:** R1, the D5 ladder, the Character Lemma, CSS +
  fixed-`e` `K(e)=D(e)`, the prime-power fiber law, and the N(N)≠N split. Those are load-bearing and cited.
- **Do not carry the two unlocated rows** (σ "compatibility map"; the "2-to-1 `μ↦N_λ`" fiber theorem) into Layer 1
  until the steward points to where they are deposited — treating an unlocated relay-primitive as load-bearing is
  exactly the drift the proposal warns against.
- **The real Layer-1 content is the empty Provenance/Derivation column**, confirmed absent across every deposit:
  *nothing on disk decides whether two derivations of the same value are the same object.* That is the Stage-0
  question, and it is a genuine hole, not a hypothetical one.

## Provenance/Derivation — the empty cell, re-read (it is not a void)
The object-layer deposits carry no derivation-identity structure — confirmed above. But the framework *already
answers* the Stage-0 question at the **process layer**, and that answer is deposited:
- **Reconciliation rule** `[LA]` — two independent derivations of the same result (R-series vs W-series) are
  **reconciled, not identified**: kept as distinct *frozen dated snapshots*; "full agreement, no disagreements" is
  recorded as *agreeing evidence*; corrections are new dated notes, never edits. Deposited stance: **same value,
  different derivations = distinct objects that agree**, provenance preserved.
- **Evidence banding** — builder-supported / cross-confirmed / externally-audited counts *how many independent
  derivation paths* a claim survived; provenance *is* the confidence.
- **The convergence engine** (this session) — a working instance: it keeps derivations distinct, tracks
  independent `(model, evidence_path)` paths, and reconciles by invariant-extraction. The discipline is *running*.

**So the empty object-layer Provenance cell is not a void — it is a not-yet-internalized version of a process-layer
discipline the framework already runs.** The Layer-1 fill, in the framework's own terms: **lift the process
discipline into the object — a *derivation groupoid* (values as objects, provenance-equivalences as morphisms) /
a 2-categorical presentation where "how a value was reached" is first-class.** *[PROPOSAL — not extracted; the
shape of the fill, flagged hypothesis, for a specialist / cross-model to check. This also coincides with the R1
n=4 frontier and the `M(U)≅U` "precise M" gap — all three want the derivation made first-class.]*

## Register / holds
Extraction (not authorship) · non-canon · process-layer provenance **extracted+cited**, object-layer lift
(derivation groupoid) a **named proposal not extracted** · every cell tagged to a source file; two relay rows flagged
**unlocated/reconstructed**; one relay cell (**"preserves total mass"**) **corrected**; Provenance column
**empirically empty** across all deposits · canon read-only, nothing edited/promoted · Tier-3.
Provenance: 2026-07-07 chat; LedgerA/ledger_A_canonical.md; Experiments/{carry_character_lemma, Carry-Set_Separation_note, carryset_fixed_e_proof}.md.
