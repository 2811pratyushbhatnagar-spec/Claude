# Ledger C candidate — DRAFT map for steward review   [non-canon · admitting is Tier-3, yours alone]

**Candidate:** `RET-∃ (return-existence) ↔ Exit (always-available disengagement)`
**Drafted:** 2026-07-05 · per the admission rule: *only statements of the form "mathematical result X
corresponds structurally to protocol clause Y," each citing evidence from **both** A and B; never replace a
map with an identification.* This draft takes no governance action; it exists so your admit/reject/hold
decision is one step.

---

## The two shores (verbatim anchors)

**Shore A (Ledger A v0.2, canonical):**
> **RET-∃** : `Δ ⊆ step(c);step(c′)` — every state can go and come back.

A-side evidence that this is load-bearing and irreducible (enumerated, reproducible):
- R2: under **F-sup** (oplax), RET-! is free (49/49 at n=2; 1650/1650 at n=3) while **RET-∃ is underivable**
  (2/49; 6/1650). Dually under F-sub, RET-∃ is free and RET-! underivable.
- Ledger E (2026-07-04): *"return-existence is the irreducible reversibility axiom (return-exclusivity
  derivable from oplax, return-existence from nothing)."*
- So RET-∃ is exactly the reversibility content you must **pay for** — no functoriality regime supplies it.

**Shore B (Protocol ledger v0.5, frozen):**
> **Exit.** A participant can disengage without accepting the artifact's framing — [the clause survives
> self-application; the kernel adds:] *"Exit as prominent as entry: the permission to leave appears as often
> as the invitation to stay."*

B-side evidence: the v0.5 self-application audit strengthened Exit and it survived; Exit is one of the core
commitments, not derived from the others (the audit treats it as independently load-bearing).

## The stated map (quotient form — the only admissible form found)

> **μ:** Read *states* as participant stances-toward-the-artifact **up to judgment-equivalence** (two stances
> are equivalent iff the participant's independent judgment is equally intact). Read `step(c)` as the
> engagement transitions the artifact affords, `step(c′)` as the disengagement transitions it affords. Then:
>
> **Ledger A's RET-∃, taken in the judgment-equivalence quotient, corresponds structurally to Ledger B's
> Exit clause**: both assert, universally over positions and existentially over paths, that *a return to an
> intact position is always available* — an **availability** claim, never an execution claim.

Three structural points carried by the map (each checkable on both sides):
1. **Same quantifier shape:** ∀ position ∃ return-path (A: `Δ ⊆ R;S`; B: exit available at every moment).
2. **Availability ≠ execution:** A already separates these (signature decision D6, availability/execution
   split); B's Exit likewise demands the *permission*, not the *act*. The map aligns availability with
   availability — it does not claim participants do return.
3. **Irreducibility on each side, independently evidenced:** A: R2 enumeration (above). B: the
   self-application audit. Neither side borrows the other's support.

## Named disanalogies (what the map does NOT say — the anti-identification clause)

- **Exact vs quotient return.** A's return lands *exactly* home (`Δ`). A person who exits is **not** the
  same state as before contact — B requires only that *judgment-relevant* features return intact. Hence the
  map holds only in the **quotient**; the naive reading "exit = return-existence" is **false as stated** and
  would be the forbidden identification.
- **Symmetric dynamics vs asymmetric relation.** A's `c, c′` are mutually inverse morphisms of one system;
  B's artifact→participant relation is asymmetric by design (Non-conversion audits the artifact, not the
  participant). The map is between *availability structures*, not between the situations themselves.
- **No normative transfer.** RET-∃ being mathematically irreducible does not *justify* the Exit clause, and
  Exit's ethical force lends no support to any A-side axiom choice. The map is descriptive both ways.

## Assessment and options (decision is yours)

- **Admissible form exists:** the quotient-form map above meets the letter of the admission rule — a stated
  map citing independent evidence from both shores, with the identification explicitly blocked.
- **Honest weakness:** the B-side "irreducibility" evidence (self-application audit) is qualitative, not
  enumerative like R2; the two evidence registers differ (Exact vs Structural). Admission would set the
  precedent that mixed-register maps are acceptable when each side meets its *own* register's bar.
- **Your options:** **(a)** admit the quotient-form map (status.json C.admitted → 1; Ledger E row);
  **(b)** reject and keep C empty (a success, not a gap — by the architecture's own words);
  **(c)** hold until the |S|≥3 / partial-identity results and B field-testing mature.
- ChatGPT's independent construction + assessment: appended below when collected (per cross-agent protocol:
  blinded construction first, then compare).

*Nothing in this file admits anything. status.json still says C: admitted = 0.*

---

## ChatGPT assessment (cross-agent protocol: BLINDED independent construction first) — 2026-07-05

Conversation (your account): https://chatgpt.com/c/6a49f97b-cb28-83ee-a27c-eafd13790099
ChatGPT was given only the two shores + the admission rule (never this draft), and asked to construct the
strongest admissible map or declare none.

**Convergence (independent):** ChatGPT constructed essentially the same map — availability-level only:
*"after crossing a boundary, return remains available"*, availability ≠ execution aligned on both sides,
"nothing stronger is mapped." Its verdict: **ADMIT** (the availability-invariant form). Its shared
invariant, verbatim: *"Crossing a boundary does not eliminate the existence of a return path, and the
existence of that path is distinct from its execution."*

**Deltas vs this draft (decision-relevant):**
1. **Irreducibility row — ChatGPT's disanalogy 6 cuts against this draft's structural point 3.** ChatGPT:
   "one may not map irreducibility ↦ protocol necessity; that would require new evidence" (B has no
   independence *theorem*, only the audit). This draft carried irreducibility as evidenced-per-register;
   ChatGPT would drop it to the weaker form. **Recommended edit if admitting: demote point 3 from "carried
   structural point" to "noted asymmetry, not part of the map."**
2. ChatGPT adds three disanalogies this draft lacked: quantification domains differ; witness objects differ
   in kind (intermediate state vs interaction design); **c′ is not an algebraic inverse on the B side**
   (exit need not "undo" — it maps only to "a designated disengagement operation").
3. ChatGPT's "not admissible" list is worth adopting verbatim into the entry (six forbidden readings, e.g.
   "the protocol instantiates the theorem").
4. Round-2 delta-assessment of this draft as written (incl. the judgment-equivalence quotient question):
   requested in the same conversation; response pending at capture time — check the conversation.

**Cross-agent ledger row (protocol schema):** claim "RET-∃ ↔ Exit (availability form)" — Claude:
reconstructs YES, accepts YES (quotient form) · ChatGPT: reconstructs YES, accepts YES (availability form,
minus the irreducibility row) → **promotion candidate with one contested sub-item** (the irreducibility
row). Admission remains Tier-3 — yours.

---

## Round 2 result (delta-assessment of this draft) + FINAL PROPOSED ENTRY — 2026-07-05

**ChatGPT round-2 verdict on this draft as written: ADMIT-WITH-EDITS.** Its assessment of the quotient:
*"a principled way to avoid the false claim that 'exit restores the original person'... cleaner than my
'admissible starting region'"* — **admissible iff the equivalence relation is independently present in
Ledger B** (preserved-judgment is B's own core concept, so this is satisfiable — but must be cited from B,
never engineered for the map). The contested irreducibility row **survives relabeled**: not
"irreducibility corresponds" but *"the mapped objects occupy analogous dependency positions within their
respective ledgers, established independently in different evidential registers"* — a correspondence
between dependency structures, not a proof transfer.

### FINAL PROPOSED ENTRY (incorporating all four cross-agent edits — this is what you would admit verbatim)

> **Ledger C — Entry 1 (candidate).** *Ledger A's RET-∃ (`Δ ⊆ step(c);step(c′)`; A v0.2, R2 enumeration)
> corresponds structurally to Ledger B's Exit clause (protocol v0.5, self-application audit), under the
> interpretation μ — μ is a reading used for this correspondence only, not part of Ledger A: states ↦
> participant stances up to judgment-equivalence, where the equivalence (two stances equivalent iff
> independent judgment is equally preserved) is supplied independently by Ledger B's own preserved-judgment
> concept, not engineered for this map; step(c) ↦ afforded engagement transitions; step(c′) ↦ a designated
> disengagement operation (no algebraic-inverse claim).*
> **Shared invariant:** crossing a boundary does not eliminate the existence of a return path, and the
> existence of that path is distinct from its execution (availability ≠ execution, aligned on both sides).
> **Dependency note:** the mapped objects occupy analogous dependency positions within their respective
> ledgers — established independently, in different evidential registers: Ledger A by proof and exhaustive
> enumeration; Ledger B by protocol design audit. This entry records the analogy without equating those
> evidential standards.
> **Not asserted (forbidden readings):** the mathematics proves/explains the protocol; the protocol
> instantiates/realizes the theorem; exit restores the pre-contact person; irreducibility ⇒ necessity;
> reversible-contact structure ⇒ ethical interaction.

**Cross-agent final state (protocol schema):** Claude: reconstructs YES, accepts YES · ChatGPT:
reconstructs YES, accepts YES (with the four edits, applied above) → **clean promotion candidate.**
If you ADMIT: status.json → C.admitted: 1, this entry lands as `LedgerC/entry_001.md`, Ledger E gets the
matching append. If you REJECT or HOLD: C stays empty (a success, not a gap). **Yours alone.**
