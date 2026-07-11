# Priority 5.5 — CHSH tiers: quantum sits strictly between classical and boxworld   [non-canon · candidate · computed]

*The frontier question — "what selects quantum inside the locally-tomographic-with-entanglement class?" — has a clean
computable discriminator: the CHSH correlation strength. (`.automation/priority1/chsh_tiers.py`, numpy, exact.)
Tier-3; canon read-only; nothing promoted.*

## Computed (exact)
| theory | `max |CHSH|` | meaning |
|---|---|---|
| classical / local | **2** | deterministic (local-hidden-variable) strategies |
| **quantum** (singlet, optimal settings) | **2√2 ≈ 2.8284** | Tsirelson bound |
| boxworld / PR box | **4** | algebraic maximum |

Strict tiering **`2 < 2√2 < 4`** (verified).

## Reading
Quantum is the sub-theory that **beats classical** (entanglement: `CHSH > 2`) yet **obeys Tsirelson** (`CHSH ≤ 2√2`,
which **forbids PR boxes**). So inside the locally-tomographic-with-entanglement class where the gbit lives, quantum is
pinned **strictly between** the classical simplex (`CHSH = 2`, no entanglement) and boxworld (`CHSH = 4`, PR boxes).

The reconstruction question is now precise: **what caps correlations at `2√2` (rules out PR boxes)?** Tsirelson's bound
is a *consequence* of the complex inner-product (Hilbert) structure — i.e. it is downstream of the very thing we are
trying to reconstruct. The candidate **principles** that single out `2√2` from *outside* quantum are **information
causality** (Pawłowski et al. 2009), **macroscopic locality** (Navascués–Wunderlich), and relatives. Whether the
`(S,F,O)` / recursive-persistence structure **supplies** any such principle is the open supply-vs-import question at
this rung (parallel to the Hardy/CDP axiom analysis in `PRIORITY-5-READING`).

## The map, now complete through the CHSH tier
`deterministic (S,F,O)` → **+ convexity `[0,1]`** → `classical simplex` (CHSH 2, separable) → **+ tensor** →
`gbit / boxworld` (CHSH ≤ 4, entangled, locally tomographic) → **quantum = the Tsirelson-bounded (`≤ 2√2`) sub-theory.**
Every arrow is now instantiated by a computed example (E1–E8, gbit, this).

## Register / holds
Computed + reproducible · standard Bell / Tsirelson / PR-box facts, placed as the framework's **frontier waypoint** ·
quantum located strictly between classical and boxworld · the open question (which *principle* caps at `2√2`, and
whether the framework supplies it) is honestly flagged as **open, no current evidence** · non-canon · Tier-3 · canon
read-only.
**ChatGPT-ASK (staged):** is **information causality** the honest candidate principle a recursive-persistence/`(S,F,O)`
structure might supply to cap correlations at Tsirelson — or is that firmly *imported*? Provenance: 2026-07-10;
`chsh_tiers.py`; builds on `PRIORITY-5-GBIT-COMPOSITE-2026-07-10.md`.
