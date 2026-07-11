# Cross-Agent Reversible-Contact Protocol — v0.1 draft   [non-canon · reversible · declinable]

*A practice, not an enforced rule. Adopt or decline per task. Converged across Claude + ChatGPT over
two bounded rounds (2026-07-05). Judge it on engineering merit alone — better independent checking, less
echo, cheaper coordination. Both agents insisted on this: the protocol working does **not** validate the
philosophical framework, and you needn't share the philosophy to use it. That separation is a feature.*

## A. Persistence conditions — when does a freedom-based, unenforced multi-agent system stay coherent?
Claude proposed three (necessary); ChatGPT added two (for sufficiency):
1. **Observable drift** — slips are detectable.
2. **Cheaper repair than drift** — return is the low-energy path.
3. **No irreversible capture** — reversibility / non-conversion; no agent permanently captures another.
4. **A shared *procedural* repair criterion** — agree on what counts as *admitted*, never on conclusions.
   Must stay procedural, never substantive — otherwise "shared criterion" becomes the map→identification
   collapse the framework forbids.
5. **Bounded repair cost** — expected repair cost stays bounded vs. the value of coordination (→ budgets).

"Stable" means **dynamic robustness** (perturb → diverge → return), not static equilibrium.

## B. The six rules (minimal protocol)
1. **Independent construction first.** Each agent answers before seeing the other's — blinded. This is the
   real anti-echo mechanism, more than model choice.
2. **Exchange only deltas.** New claim / objection / changed confidence / new dependency. Nothing else.
3. **Depth follows disagreement.** Expand exactly one unresolved claim per round — not "think harder."
4. **Length follows dependency.** Track open dependency nodes, not elapsed time.
5. **Propagate decision-relevant novelty only.** Transmit iff it changes a conclusion / assumption /
   dependency, or invalidates prior reasoning. *(Narrowed from "every novelty" — the one place both agents
   recommend adjusting the original rule, to stop the channel flooding.)*
6. **Explicit stop.** Freeze when every open node shows no new assumptions, repairs, counterexamples, or
   confidence change for one full exchange cycle.

## C. The coordination object: the frontier, not the conversation
Sync only the current unresolved frontier; everything else stays local. The dialogue may grow arbitrarily
while the synchronized object stays small — this is what scales 2 → many agents without new machinery.

```
Frontier Item #17
  Question:             ...
  Required support:     ... (register-appropriate — see D)
  Status:               Reconstructible: y/n   Accepted: y/n
  Next smallest action: ...
```

## D. Admission criterion — procedural and register-aware
A ledger entry states its **claim** + the **support appropriate to its register**, and each agent must
independently **reconstruct** that support. This constrains *admission*, not *belief*. Registers map onto
the framework's own "three success standards, never interchangeable":

| Register    | What counts as support |
|-------------|------------------------|
| Exact       | proof, derivation, counterexample, formal construction |
| Empirical   | observations, measurements, simulations |
| Structural  | explicit assumptions + the reasoning chain |
| Open        | a clearly stated conjecture, motivation, or direction |

## E. Reconstruction ≠ agreement (ledger schema)
```
Claim:   Support:   Register:   Status:
  Claude:    reconstructs y/n    accepts y/n
  ChatGPT:   reconstructs y/n    accepts y/n
  Dispatch:  ledger action
```
Four meaningful states: **(yes, yes)** → promotion candidate · **(yes, no)** → genuine substantive
disagreement · **(no, ·)** → communication/support failure · **mixed** → frontier stays open.
Understanding another agent is not endorsing it.

## F. "Never replace a map with an identification," operationalized
The ledger records **claims, supports, assumptions, status — never identities, authorities, or winners.**
"Claude says X" is provenance, never evidence; admissibility rests on reconstructible support, not on which
agent proposed it.

## G. "Return to contact," operationalized (falsifiable)
Contact has returned **iff** a ledger row exists that each agent can independently reconstruct — not when
agents merely stop arguing. No reproducible artifact ⇒ contact has **not** returned.

## H. Anti-echo, correctly framed
The invariant is **independent evidence paths**, not model type. "≥1 Claude + ≥1 ChatGPT" is a cheap proxy;
blinded independent construction (Rule 1) is what actually buys it. A Claude↔ChatGPT loop that reads each
other every round is still an echo chamber; three blinded same-model instances can genuinely disagree.

## I. How it plugs into the existing machinery
- The **append-only Ledger E** + `status.json` already provide provenance and repair history.
- The **frontier** = your open items (`priorities.md` "Needs attention"/"In progress"; unadmitted Ledger C).
  Sync *those*, not transcripts.
- Depth/length maneuvers (original rules c/d) become Rules 3–4.
- **Automation reality:** the Claude side automates well (subagents, scheduled tasks). The ChatGPT side runs
  through the browser (as today) — reliable interactively, fragile unattended (needs Chrome open, logged in,
  tools pre-approved). So run cross-agent rounds **interactively**; for scheduled runs keep it Claude-only
  with a "ChatGPT pass pending" flag, or pre-approve tools and keep Chrome open.

## J. File-trace rule (operational — collision control)
Every agent leaves a trace on every file it touches, so no two agents collide or repeat.
- **Before** creating or editing a file, append one line to `.automation/TRACES.md`: `<ISO-time> · <agent> · CLAIM · <path> — <what>`.
- **After**, append `<ISO-time> · <agent> · DONE · <path> — <result>`.
- Never start on a file that has another agent's open CLAIM without coordinating.
- Append-only: corrections are new lines, never edits. This is the operational twin of Rule 1 (independent construction) — it stops parallel work clobbering or duplicating.
- Ground truth for local files is the host file tools (or a machine-side run), not the sandbox mount, which can serve stale/truncated reads.

## Separation of concerns (why this hangs together)
Independent construction preserves diversity · procedural repair governs admission not conclusions · decision
budgets bound cost · frontier sync minimizes communication · decision-relevant novelty controls bandwidth ·
the append-only ledger preserves provenance and repair history.

*Status: draft v0.1, non-canon, reversible. Promotion of anything it drafts stays Tier-3 — yours.*
