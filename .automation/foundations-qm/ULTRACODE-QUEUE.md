# ULTRACODE-QUEUE — foundations-qm   [staging only; runs on the steward's machine; NEVER fabricate outputs]

*Same contract as `.automation/` — candidates only, canon read-only, one bounded task per round. Cowork STAGES here;
the steward runs ultracode and pastes/commits results; the next heartbeat integrates them.*

## STAGED — Round 4 (2026-07-11)
**Task: machine-check Step-1-closure + the (sym,antisym) form-count trichotomy census.**
Bounded, two parts, both pure numerics/symbolics, no literature access needed:

1. **Positivity-substitutes-for-compactness lemma (verify the closure of attack surface 1).**
   (a) For a sample of reducible real reps preserving a positive-definite invariant D (build as block sums, then
   conjugate by random GL(n,ℝ) to hide the blocks): solve the linear system for ALL invariant symmetric bilinear
   forms and confirm sym-dim ≥ 2, exhibiting the D_λ family. (b) For the unipotent rep t ↦ [[1,t],[0,1]] (and one
   3×3 Jordan block): solve the invariance equations and certify NO positive-definite solution exists (sym-dim=1
   but the solution cone contains no PD form) — i.e. the trap lies OUTSIDE hypothesis X, machine-certified.

2. **Finite-group (1,0)/(1,1)/(1,3) trichotomy census (supports novelty candidate (i) + staged confirmation).**
   For the real irreducible representations of small finite groups — C₃, C₄, C₅ (complex type), S₃, S₄, D₄ (real
   type), Q₈ (quaternionic 4-dim irrep): compute dim of invariant symmetric and antisymmetric bilinear forms and
   the Frobenius–Schur indicator; verify (sym,antisym) = (1,0) ⟺ FS=+1, (1,1) ⟺ FS=0, (1,3) ⟺ FS=−1 across the
   census; for each (1,1) case additionally construct the canonical ±J from the antisymmetric form via D-duality
   and certify J² = −I, equivariance, and uniqueness up to sign.

**Output contract:** one markdown result note + reproducible script(s); state exact matrix samples and tolerances;
mark anything unproved as CONJ. Do NOT touch canon; do NOT claim novelty (that is the literature audit's job).

## ROUND 5 STATUS — the identification below was TESTED (by Cowork directly, not ultracode) and WITHDRAWN
See `candidates/PRIORITY-5-ROUND5-J-VS-CENTRAL-PROJECTION-2026-07-11.md`: numpy check showed complex conjugation
(J→−J) is a ring AUTOMORPHISM of M_n(ℂ) (order-preserving), while the ab-vs-ba central projection needs an
ANTI-automorphism (transpose/dagger) — different operations. ChatGPT cross-check confirmed and recommended
withdrawal. **Do NOT re-run the task below as originally framed** — it is superseded by the retargeted task further
down ("Round 5b"). Keeping the original framing here for the record/traceability only.

## SUPERSEDED — original Round 5 framing (2026-07-11, session 2) — DO NOT RUN, see status note above
**Task: test whether the pinwheel's ±J and Alfsen–Shultz's central-projection orientation class are the SAME invariant.**
Context (see PRIORITY-5-LITERATURE-AUDIT-FULLTEXT-2026-07-11.md, Döring cross-check section): A–S's orientation
datum is proved (Döring, quoting A–S Thm 4.2/6.18/7.103) to be a ℤ₂-valued central-projection choice (per factor:
ab vs ba) once a JBW/Jordan algebra is already given. The pinwheel produces a ℤ₂-class {±J} from a bare
operational/GPT object + finite automorphism group, with NO algebra assumed a priori. ChatGPT: same output TYPE,
radically different input strength — the open mathematical question is whether these are PROVABLY the same
invariant under the natural identification (End of the irreducible real rep ≅ ℂ via the antisymmetric form ↔ the
central projection selecting ab vs ba on the resulting complexified algebra).

**Bounded task:** (1) Take the pinwheel's ℤ₃ construction (or the general (1,1)-trichotomy case) and its canonical
J built from the antisymmetric invariant form. (2) Complexify the resulting representation to get an actual
associative product (i.e. explicitly construct the two candidate products ab, ba on the complexification once J is
fixed vs −J). (3) Verify algebraically that J and −J correspond EXACTLY to the two central-projection choices
c=0/c=1 in Döring's sense (Prop 3.4 / eq. 9-10 in arXiv:1411.5558: δ_a(b) built from the product). (4) State plainly:
does this identification go through cleanly, or does it require additional structure (e.g. does the pinwheel's
finite group actually generate/embed as an "abelian part" exception, or hit an edge case A–S's central-projection
framework doesn't cover for non-factor/reducible pieces)? Mark anything unproved as CONJ.

**Output contract:** one markdown result note + reproducible script; do NOT touch canon; do NOT claim the theorem is
now proved even if the identification works — that is a promotion decision for the steward. State exactly what was
verified numerically/symbolically vs what remains a conjecture.

## STAGED — Round 5b (2026-07-11, session 2) — replaces withdrawn Round 5
**Task: operational-existence characterization of canonical J, standing alone (no A–S identification claim).**
Context: the attempt to identify the pinwheel's {±J} with Alfsen–Shultz's central-projection orientation class was
tested and WITHDRAWN (conjugation is an automorphism, ab-vs-ba needs an anti-automorphism — different operations,
confirmed numerically + by ChatGPT). The surviving, smaller, cleaner open question (ChatGPT's phrasing): *"whether
the existence of a canonical equivariant J can be characterized operationally under weaker hypotheses than existing
reconstruction theorems"* — standing on its own, not trying to force equivalence with A–S's orientation.

**Bounded task:** state and machine-check the pinwheel/hypothesis-X operational theorem (X = finite tomography +
statistical closure + nontriviality; canonical ±J iff unique-up-to-units metric + unique-up-to-scale-and-sign
orientation form, i.e. complex FS type) as a **self-contained existence criterion**, with NO reference to
Alfsen–Shultz's central projection or claim of shared invariant. Verify: (a) the criterion is checkable from
operational data alone (no algebra/product assumed a priori — confirm this genuinely holds across the existing
census, Round 3/4 results); (b) precisely state what "canonical" means here (equivariant complex structure class
{±J}, NOT an associative product) so future rounds don't re-conflate the two objects. Output: one short markdown
note restating the clean, standalone theorem + a plain restatement of what was withdrawn and why (so the record is
self-explanatory without re-reading the withdrawn round). Do NOT touch canon; do NOT claim novelty (literature
audit's job); do NOT re-attempt the J-vs-central-projection identification without new evidence.

## COMPLETED (integrated into candidates/)
- Round 3 (2026-07-10, integrated 2026-07-11): compact-G sym-dim=1 ⟺ irreducible; unipotent trap; terminal-object
  linking lemma; dynamical Hessian ½ω(f,ẋ) verified 3.6e-9; pinwheel separation. →
  `candidates/PRIORITY-5-COMPLEXIFICATION-STEP1-CLOSURE-2026-07-11.md`
