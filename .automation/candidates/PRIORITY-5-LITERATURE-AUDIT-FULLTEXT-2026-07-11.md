# Priority 5 — full-text literature audit: what the primary sources actually say   [non-canon · candidate]

*The steward-gated, highest-EV step both models flagged: read the actual papers, not abstracts, and decide which
residual-novelty candidates survive contact. Done live with ChatGPT in the loop. Tier-3; canon read-only; nothing
promoted. Honest register throughout — this is an **attribution** audit, and its whole point is to find prior art that
defeats our candidates, not to protect them.*

## Sources and access (honest about what was actually read)
- **Moretti–Oppio, arXiv:1611.09029** — **READ IN FULL** via arXiv native HTML (v3). Primary-text quotes below.
- **Müller, Les Houches notes, arXiv:2011.01286** — abstract read; reconstruction route confirmed (see below).
- **Alfsen–Shultz orientation theory** (PNAS 95(12):6596; *Geometry of State Spaces of Operator Algebras*, ch. on
  orientation) — **NOT fully readable here** (PNAS page returned no text; book paywalled). Worked from the established
  result; **the full read of the orientation chapters remains the one genuinely open check** and is the steward's to do.
- **Barnum–Wilce**, **Masanes–Müller**, **Hardy** — not fetched this cycle; flagged as remaining kill-list.

## What Moretti–Oppio's text actually says (primary quotes)
1. **Irreducibility is a HYPOTHESIS, never derived.**
   - *Definition 2.11* defines an irreducible family of operators; *Prop. 2.13* is "Schur's lemma for essentially
     selfadjoint operators … let 𝔘 ⊂ 𝔅(H) be **irreducible**" — i.e. Schur is applied **to** already-irreducible families.
   - The relaxed version characterises (not derives) it: "**ℜ is irreducible if and only if** the commutant lattice
     𝓛_{ℜ'}(H) = {0, I}." Irreducibility of the **observable algebra** is taken as the physical hypothesis.
   - **Nowhere** is irreducibility *derived* from uniqueness of an invariant form. ⇒ our candidate (1) — *irreducibility
     derived, in a bare GPT with no a-priori algebra* — is genuinely **outside M–O's stated scope**.
2. **Continuous groups only.**
   - *Remark 3.2* (verbatim): "In the rest of the paper we only consider the case of a **finite-dimensional real Lie
     group G**." Here "finite-dimensional" is the **manifold dimension** of a continuous group (Poincaré), **not** a
     discrete/finite symmetry group.
   - The main results (§4.2, §5.3): "**Emergence of a complex structure (unique up to sign) from Poincaré symmetry**."
   - ⇒ our candidate (2) — *finite-group sufficiency + the pinwheel: an invariant J with **no** continuous dynamics* — is
     **untouched** by M–O.
3. **The mechanism is theirs.** Unique-up-to-sign J commuting with the observables, from the **commutant classification of
   irreducible real von Neumann algebras** (Schur trichotomy ℝ/ℂ/ℍ), in real Hilbert space. This **is** our mechanism.
   Not novel.

## Müller (GPT reconstruction) — also continuous
The Les Houches reconstruction obtains ℂ from **Tomographic Locality + Continuous Reversibility + the Subspace Axiom**
("how one obtains the complex numbers and operators of the usual representation"). Again the route to ℂ is **continuous
reversibility**, not a finite symmetry group. This is the D5 route already recorded — established, and continuous.

## Per-candidate verdict after primary-text contact
| # | Candidate | Verdict | Why (from the sources) |
|---|-----------|---------|------------------------|
| core | canonical ±J from commutant/orientation | **ESTABLISHED — not novel** | M–O prove it (confirmed at source); Alfsen–Shultz own the orientation form. |
| (1) | bare-GPT (1,1) form-count, irreducibility **derived** | **SURVIVES vs M–O; PENDING Alfsen–Shultz / Barnum–Wilce** | M–O *assume* irreducibility (Def 2.11); deriving it from form-uniqueness in a bare GPT is outside their scope — but Jordan-theory or GPT-reconstruction prior art could still subsume it. |
| (2) | finite-group sufficiency + **pinwheel** (static J, no dynamics) | **STRONGEST — untouched by the continuous-symmetry literature** | M–O and Müller both rest on continuous groups / continuous reversibility; a finite/discrete symmetry giving invariant J with no flow is not in their stated scope. Still to check: any finite-group GPT reconstruction. |
| (3) | the traps (label-doubling; unipotent non-compact) | **Expository** | Standard once stated; strengthen the presentation, not results. |
| (4) | λω / QM-as-λ=0 measurability hierarchy | **At most a new FRAMING** | Ingredients (orientation, Berry phase, continuous reversibility) established; the explicit definability/invariance/dynamics split is presentation, pending Alfsen–Shultz. |

## Honest standing verdict
The **central mechanism is established** — now confirmed against the Moretti–Oppio text itself, not just its abstract.
What is left as *candidate* novelty is **not the existence of J** but two structural refinements: **(2)** the
finite-group / static-J separation (the pinwheel), which is the strongest because the entire prior literature we've
touched uses continuous symmetry; and **(1)** deriving irreducibility rather than assuming it, which is a real
distinction from M–O but must still meet Alfsen–Shultz and Barnum–Wilce before any claim. The correct framing remains
ChatGPT's: **"an operational/categorical reformulation of known complex-structure mechanisms, together with finite-group
and realization-theoretic refinements"** — *not* "a new theorem about canonical complex structure."

## ChatGPT cross-check on the primary-text findings (2026-07-11, live)
**Q1 — confirmed.** Ranking of what's plausibly novel: **(1st) finite-group / static-J** (strongest — "Moretti–Oppio
explicitly restrict to Lie groups, and the reconstruction route is also continuous"); **(2nd) irreducibility-from-form-
uniqueness** (plausible, pending Jordan/operator-algebra literature); **(3rd) everything else** = exposition / packaging /
consequences. Verdict: "a substantially narrower and more defensible position than where the project started."

**Q2 — the key discriminator for the Alfsen–Shultz read.** Reduce the whole audit to one question:
> **Do Alfsen–Shultz *derive* the existence and uniqueness of the complex structure from operational / order-theoretic
> uniqueness conditions, or do they *assume* the algebraic simplicity / irreducibility that our theorem aims to derive?**

Concretely, hunt for three things: **(A)** does orientation already *force* irreducibility/simplicity (if it's assumed
first → candidate (1) is *not* subsumed; if orientation + an operational condition forces it → it probably is — "the
single biggest thing I'd look for"); **(B)** is orientation defined *intrinsically / order-theoretically*, or recovered
from *one-parameter (connected) automorphism groups*? — if every construction goes through Lie groups / flows /
connected automorphism groups, the finite-group pinwheel sits **outside** their framework; **(C)** do they prove
"orientation ⟺ complex structure up to sign" for a broad class of Jordan systems (if so the mechanism is covered, and
the only remaining question is whether our *hypotheses* differ).

**The sharpening on candidate (2) (important).** The finite-group result is only interesting if **conceptually
essential**, not a degenerate special case. The strongest theorem must be phrased as a **necessity separation** —
*"continuous reversibility is sufficient for a canonical J but **not** necessary"* — which the pinwheel *proves*. Merely
exhibiting one finite example with the same algebraic commutant is "an obvious representation-theoretic curiosity" a
referee would dismiss. **"That framing, if it survives the remaining literature audit, is where the real mathematical
value lies."** ⇒ action: reframe candidate (2) as the necessity-separation statement, not "here is a finite example."

## Remaining open (steward)
- Full read of **Alfsen–Shultz** orientation chapters against the **key discriminator** above (decisive for (1)/(4));
  **Barnum–Wilce** and **Masanes–Müller** for whether a finite-group GPT route to ℂ exists (decisive for (2)).
- These need the actual books/papers (paywalled / non-loading here) — genuinely the steward's reading to do.
- If (2) survives, **restate it as a necessity separation** before any write-up.

## Orientation literature read + the decisive resolution (2026-07-11, with ChatGPT)
Read the orientation route via **Niestegge arXiv:1402.0158** (restates Alfsen–Shultz precisely; PMC full text was
CAPTCHA-gated — **not** bypassed), plus **Masanes–Müller 1004.1483** and **Barnum–Wilce 1202.4513**.

**Decisive finding.** Alfsen–Shultz obtain the complex structure from a **dynamical correspondence**: selfadjoint
elements play the dual role of observables **and generators of dynamical groups** (continuous one-parameter groups /
order-derivations). So their route to J is **via continuous dynamics**, not static order structure. Every established
route agrees: Moretti–Oppio (Poincaré), Alfsen–Shultz (dynamical correspondence), Masanes–Müller & Müller (continuous
reversibility), Barnum–Wilce (Jordan self-duality + local tomography + a qubit). **None uses a finite/discrete group with
no flow.** ⇒ candidates (1) and (2) **unify** into one question: *can a canonical equivariant complex structure arise
**without continuous dynamics**?*

**The crux, resolved honestly (this is the important correction).** A finite group yields the complex structure **only up
to sign** — the class {J, −J} — because a discrete group has no "arrow of time" (t>0 vs t<0) to *select* the orientation;
continuous dynamics is exactly what supplies that arrow. This matches (i) our own earlier result (static ω-recovery
fails — QM the witness — dynamics fixes the sign) and (ii) the framework's standing "canonical **up to conjugation**"
(±J = i vs −i = antiunitary equivalence, same predictions). So the necessity separation **does not collapse — it must be
restated, weaker and precise**:

> **Corrected theorem (candidate).** A canonical equivariant complex structure **exists (up to complex conjugation — the
> ±J class) without continuous dynamics**; a continuous **dynamical correspondence is needed only to *select an
> orientation* (the sign, i vs −i) within that class.**

I.e. the contribution is a clean **static/dynamical split**: the *existence* of the complex structure (±J class) is
static (a finite group / form-count suffices); *fixing the orientation* is dynamical (needs a flow). ChatGPT: "I would
**not** regard 'only up to sign' as a collapse … a clarification of exactly which part of the complex structure is static
and which part is dynamical … a much sharper and more defensible contribution than the broader claims the project started
with."

**What the audit still must determine** (the one open hinge): is this precise **static/dynamical split** — existence of
the ±J class without dynamics vs. orientation requiring dynamics — *absent from the existing literature*? All routes read
so far use continuous dynamics **even to obtain the ±J class**; if that is truly universal in the literature, the split
is a genuine (if modest) new clarification. Deciding it needs the **Alfsen–Shultz orientation chapters in full** (still
CAPTCHA/paywall-gated here — the steward's read).

## Weaver review (AMS Bulletin 2004) — the actual A–S books' orientation route, and a sharpened discriminator (2026-07-11, session 2)
Found a freely-accessible primary-*adjacent* source (open PDF, not paywalled): Nik Weaver's AMS Bulletin review of
*both* Alfsen–Shultz books (*State Spaces of Operator Algebras*, 2001; *Geometry of State Spaces of Operator
Algebras*, 2003) — distinct from the Niestegge-restated "dynamical correspondence" paper used in the prior round.

**What the books' orientation route actually is (per Weaver, verbatim quotes).** The smallest face of S(A) containing
two distinct pure states is a line segment (inequivalent states) or a **3-ball** (equivalent states). "A induces an
orientation of every 3-ball face of S(A), and these orientations vary continuously in an appropriate sense." The
central theorem: the product on A is recovered from this data, and "continuously varying orientations of the facial
3-balls of S(A) are in one-to-one correspondence with products which make A ... into a C*-algebra." This is a
**different** characterization from the dynamical-correspondence one (selfadjoint elements as generators of
continuous one-parameter groups) — geometric/order-theoretic on its face, not explicitly a time-flow.

**ChatGPT cross-check (ordinal, careful).** Confirms this materially changes the audit, but **not** in the direction
of collapse: (Q1) "static" here is not the same as "discrete" — orientation is a *section of an orientation bundle
over a continuously parameterized family of faces*, so it remains fundamentally continuous, just not *dynamical* in
the time-flow sense; not equivalent to a finite-group construction. (Q2) the global orientation choice is itself extra
structure — reversing every orientation simultaneously should correspond to the opposite algebra, i.e. the ±J /
conjugation ambiguity persists here too (expected, not derived from the review alone). (Q3) **the discriminator
sharpens rather than resolves**: the honest question is no longer "does A–S use dynamics?" but **"does their
construction require a continuously parameterized family of local orientation choices?"** — if yes (as Weaver's
"vary continuously" phrasing suggests), the pinwheel (finite group, no continuous family of anything) is a
**strictly stronger elimination**: not just no continuous *dynamics*, but no continuous *geometric* structure of any
kind. ChatGPT's verdict: **downgrade confidence that the pinwheel is "obviously novel," but do not conclude
subsumed** — burden shifts to showing the finite-group criterion recovers {J,−J} without needing A–S's continuous
orientation-bundle machinery.

**Revised comparison table (per ChatGPT).** Moretti–Oppio = continuous spacetime symmetry; Masanes–Müller/Müller =
continuous reversibility; Alfsen–Shultz (via Weaver) = continuous geometric orientation of facial 3-balls; our
candidate = finite symmetry + invariant-form criterion. Still a meaningful distinction, still not settled — the
Weaver review is a secondary source (a book review), not the books themselves; whether A–S's orientation theory
secretly implies (or is implied by) the finite-group criterion needs the primary text.

**Status.** Open hinge NOT resolved, but reframed and sharpened: is a continuously-varying orientation bundle over
facial 3-balls *required* for A–S's construction, or could a finite automorphism group's fixed/discrete orientation
data suffice within their own framework? Still steward-gated (needs the books or a fuller secondary exposition).
Non-canon; nothing promoted; Tier-3; canon read-only. Source: Weaver, AMS Bull. 41(4):535–539 (2004),
ams.org/journals/bull/2004-41-04/S0273-0979-04-01019-5; chatgpt.com/c/6a4ffe2d.

## Döring cross-check (arXiv:1411.5558) — A–S's orientation primitive is discrete, and the discriminator resolves (2026-07-11, session 2 cont'd)
Found a second, higher-quality secondary source: Andreas Döring, *Two New Complete Invariants of von Neumann Algebras*
(arXiv:1411.5558), which quotes Alfsen–Shultz's **Theorem 4.2** and **Theorem 6.18** in detail (their actual statements,
not a paraphrase — the closest primary-quality contact achieved so far short of the books themselves).

**What A–S actually prove (per Döring's exposition).** A *dynamical correspondence* on a JB-algebra A is a linear map
ψ: A → skew order derivations satisfying two axioms. Thm 4.2: a JBW-algebra A is (isomorphic to) the self-adjoint part
of a von Neumann algebra **iff** a dynamical correspondence exists on A, and there is a **bijective correspondence**
between associative products on A+iA and dynamical correspondences on A. Crucially: "any two such associative
products [inducing the same Jordan product] differ by a **central projection** c which is 1 on the abelian part"
(a⋆b = c·ab + (1−c)·ba). For a factor this collapses to exactly **two** possibilities (ab vs ba, i.e. the opposite
algebra) — a bijective correspondence between central projections and associative products. Thm 6.18 (A–S): bijective
correspondence between dynamical correspondences and **orientations in the sense of Connes**. Döring's own gloss:
"the choice of an orientation amounts to picking the direction of time."

**What this settles.** A–S's orientation datum — however phrased (dynamical correspondence / Connes orientation /
time-direction) — is proven **equivalent to picking a central projection**, i.e. for a factor, a **ℤ₂-valued
(discrete) choice** = exactly the {J,−J} / {ab,ba} sign ambiguity. The one-parameter automorphism groups are
*generated from* that discrete choice once the Jordan/algebra structure and an element are given; they are not
independent continuous input in addition to it.

**ChatGPT resonance — the discriminator reframed, not collapsed.** Agrees the residual datum is discrete (a ℤ₂ choice
per factor, matching our {J,−J}), but pushes back on "this collapses the split": the real distinction was never
discrete-vs-continuous, it is **where the orientation datum comes from**. A–S: *input* = a full Jordan/JBW algebra
already assumed; *output* = the residual ℤ₂ orientation class (central projection). Pinwheel: *input* = a bare
operational/GPT object + a finite automorphism group, **no algebra assumed a priori**; *output* = the same *type* of
object (a canonical {±J} class). Same output type, radically different (weaker) input — "that, not finite versus
continuous, is now the interesting mathematical question." ChatGPT's suggested sharpened theorem statement:

> Under purely operational hypotheses together with a finite automorphism group satisfying [X,Y,Z], the observable
> quotient canonically determines the **same ℤ₂-orientation class** that appears in Alfsen–Shultz as the residual
> ambiguity of associative products.

Caution flagged: exactly-two-associative-products does NOT automatically mean every finite-group-selected {±J} lands
on *the same* invariant — proving that identification is a real mathematical theorem, not just a structural analogy.

**Status.** This is the sharpest formulation of the open hinge to date: not "does A–S need dynamics" but "is the
pinwheel's {±J}-selection provably the *same* invariant as A–S's central-projection/orientation class, reached from
strictly weaker (pre-algebraic) hypotheses." Not proved; not subsumed; not promoted. Still needs (a) the actual A–S
books or a fuller primary read to confirm central-projection = orientation class is the *complete* story (no residual
continuity requirement hiding elsewhere), and (b) a proof/ultracode check that the pinwheel's ±J and A–S's central
projection are the *same* invariant under a common identification. Non-canon; nothing promoted; Tier-3; canon
read-only. Source: Döring arXiv:1411.5558 (quoting Alfsen–Shultz Thm 4.2, 6.18, Thm 7.103/Lemma 7.100);
chatgpt.com/c/6a4ffe2d.

## Register / holds
Primary-text audit (M–O read in full; Müller abstract; Alfsen–Shultz **not** fully accessible — flagged) · mechanism
**established at source** · candidates (2) then (1) are the only plausibly-novel residuals, both **pending** the
still-unread orientation + GPT-reconstruction texts · nothing promoted · Tier-3 · canon read-only. Provenance: 2026-07-11;
Moretti–Oppio arXiv:1611.09029 (full text); Müller arXiv:2011.01286; Alfsen–Shultz PNAS 95(12):6596;
ChatGPT https://chatgpt.com/c/6a4ffe2d-aa78-83ee-b6b1-de0d8defb14a.
