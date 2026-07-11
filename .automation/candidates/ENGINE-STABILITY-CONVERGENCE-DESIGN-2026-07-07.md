# Engine design: from pipeline to stability-convergence loop   [non-canon · candidate · design lens]

*Applies the representation-invariance vocabulary to the multi-agent engine. This is a **design lens over known
engineering/mathematics** — not a new object, and not machinery to bolt on. Per the standing discipline (fold
vocabulary; build nothing that doesn't earn its place), §7 lists the minimal earned changes; the rest is
re-description of governance that already exists. Warrant: candidate design; Tier-3 to adopt; nothing
forced/admitted. Provenance: 2026-07-07 chat (cross-agent relay).*

## 1. The reframe
The engine's job is not to produce truth directly; it is to produce **stable conclusions from several imperfect
agents.** That is a representation problem:
- **O** — the underlying question (unknown to the system).
- **Rep** — independent agent runs / prompts / retrievals / decompositions.
- **P** — what counts as agreement (logical equivalence, compatible derivation, shared evidence).
- **I** — the conclusion promoted to the ledger.

Each agent, prompt, reasoning style, and retrieval path is one representation; the engine extracts what survives
them.

## 2. Pipeline → loop
Replace the fixed org-chart (Builder → Reviewer → Judge) with iterative convergence:
```
state₀
repeat:
    generate a new *independent* representation
    extract the invariant I   (what survives across representations so far)
    measure Δ(Iₙ, Iₙ₋₁)
until Δ < threshold            # stability, not stage-count
promote I with its evidence trace
```
Stopping is **empirical (stability)**, not **architectural (reach stage 9).** There is no universal stage number:
three representations may pin one question; fifteen may not pin another. Depth is an output, not a constant.

## 3. Confidence, redefined
Not a scalar. A **survival trace**:
```
invariant survived:  ✓ adversarial review    ✓ literature search
                     ✓ reformulation         ✓ independent model
                     ✗ external expert
```
Confidence = **stability under additional independent representations.** This is exactly the existing banding
(builder-supported / cross-confirmed / externally-audited) restated as "how many independent representations has
`I` survived."

## 4. Components (responsibilities, not an org chart)
- **Representation Workers** — deliberately *different interfaces* onto the same `O`: first-principles derivation ·
  literature/precedent · counterexample/adversarial · reformulation (e.g. category-theoretic restatement) ·
  reduction to a known result. Not better/worse — different.
- **Consensus Synthesizer** (internally: the invariant extractor) — answers only "what survives across these
  representations?", emitting `{ invariant · representation-specific · open disagreements }`. Never "which answer
  do I like." *(Name it for its responsibility, not the math analogy — Consensus Synthesizer / Evidence
  Consolidator / Stability Analyzer.)*
- **Stability Monitor** — keeps the per-round invariant history; fires promotion when a further independent
  representation stops changing `I`.
- **Diversity Driver** — the anti-convergence role, opposite to the others: "produce a representation unlike any
  prior one" / "find the strongest formulation that makes the current invariant fail." Success = new interfaces,
  not agreement. Guards against premature convergence and the echo pathology.

## 5. The invariant that actually matters is *independence*
Rotating roles does **not** by itself buy independence. The failure mode is one agent that builds, then reviews its
own build, then judges its own review — one representation in three hats. The governing constraint:
> **No conclusion is promoted without surviving ≥ N independent representation paths.**

Guard *independence of paths*, not the number of models or the number of stages.

## 6. Three agents, rotating roles — and the concrete instantiation
Three agents suffice to sustain the three standing pressures — **Construction / Refutation / Integration** — *if*
they are adaptive role-players under §5, not fixed Builder/Reviewer/Judge identities. Roles rotate each cycle; the
**trace records which agent played which role** (so an audit can verify `I` survived genuinely diverse
representations).

**Composition — 1 ChatGPT agent + 2 Claude agents (each with full tools, storage, and Chrome) — is a good
instantiation, with one caveat that is the whole point:**
- It satisfies the anti-echo rule (≥1 ChatGPT + ≥1 Claude) at the **model level** — the strongest independence
  axis, because the two model families have different priors and therefore *decorrelated* errors. Put the
  cross-model agent where correlated error hurts most: as the **Refuter**, or as an **independent Synthesizer**.
- But two Claude agents count as **two independent representations only if deliberately differentiated** —
  different **role**, different **prompt**, different **evidence path** (one derives cold; the other retrieves via
  Chrome), ideally different **context**. Two Claudes with identical tools, prompt, and context are *one*
  representation in two bodies — the §5 pathology, which role-rotation alone will not fix.
- **Rotate synthesis too.** If one agent (or one model) always synthesizes, its bias silently becomes the
  invariant. Have different agents synthesize on different cycles and *compare the syntheses*; independent
  convergence of syntheses is stronger than trusting a permanent synthesizer.
- All three need **storage** (read `status.json`; write `.automation/candidates/`; append `TRACES.md`) and
  **Chrome** (independent retrieval = an independent `Rep`). Give each a **capability vector**, not a permanent
  title, so the orchestrator asks *"what representation is missing?"* rather than *"whose turn is it?"*

**So: yes — 1 ChatGPT + 2 Claude works**, provided the two Claudes are pushed onto genuinely different
representation paths and synthesis rotates. The count is not the point; the **independence** is.

## 7. The minimal earned changes (everything else is vocabulary)
Per the evidence-river caution (don't refactor a working system for elegance), adopt only what earns its place:
1. **Log the per-cycle invariant** (Stability Monitor as an append to the existing trace, not a new service), so
   the stopping rule can be *stability* rather than a fixed stage count.
2. **Add the Diversity Driver** to the role rotation (one cycle whose explicit goal is to break the current
   invariant).
3. **Make promotion require the independence count** (§5) rather than "reached the last stage."

The rest — banding, confidence/warrant, anti-echo, independent streams — is already this idea; fold the `Rep/P/I`
rationale into WORKER-CONTRACT's *why* and build nothing new.

## 8. Fractal note
The same loop runs at every scale: 3 agents per question → the engine per project-question → cross-project
invariant → framework promotion. The three pathologies recur at each scale (too few reps → echo; too many
uncontrolled → mush; the tuning target is a *proper intermediate* `Rep`). The architecture "closes" not after 3 or
9 stages but when the invariant stabilizes.

## Register / holds
Candidate design lens · non-canon · known engineering/mathematics (no new object claimed) · Tier-3 to adopt ·
nothing forced/admitted. Provenance: 2026-07-07 chat (cross-agent relay); cross-agent-protocol.md ·
WORKER-CONTRACT.md · IMPLICATIONS-REPRESENTATION-INVARIANCE / REPRESENTATION-INVARIANCE-STRESS-TEST candidates.
