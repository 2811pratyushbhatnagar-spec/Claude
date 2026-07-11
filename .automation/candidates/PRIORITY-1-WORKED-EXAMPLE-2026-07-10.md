# Priority 1 — first worked example (verified): `D` on a tiny `(S,F,O)`   [non-canon · candidate · computed]

*The next move on Priority 1: carry ONE concrete `(S,F,O)` end-to-end. Computed + reproducible
(`.automation/priority1/D_worked_example.py`). Sharp `D` (minimal realization) and graded `D` (behavioural metric)
both computed; the degenerate poles exercised; one honest new finding. Research draft; nothing proved beyond the
finite computation; Tier-3; canon read-only.*

## The example
`S = {0,1,2,3,4}`; `F: 0→1, 1→4, 2→3, 3→4, 4→4` (`4` a sink); `O: 0,1,2 ↦ x` and `3,4 ↦ y`.
Observation streams: `0 ↦ x x y^∞`; `1,2 ↦ x y^∞`; `3,4 ↦ y^∞`.

## Sharp `D` (observational equivalence = minimal realization) — computed
Classes **`{0}, {1,2}, {3,4}` — 5 states → 3**, a genuine, unique reduction (Myhill–Nerode). Minimal machine
`C0(x) → C1(x) → C2(y) → C2` (F respects the classes; quotient well-defined). This is the **interior** pole
(proper reduction, neither trivial nor discrete).

## Graded `D` (behavioural pseudometric `d(x,y)=2^{-first-differing-step}`) — computed
`d(0,1)=d(0,2)=0.5` (agree at step 0, differ at step 1); `d(0,3)=d(0,4)=d(1,3)=… =1.0` (differ at step 0);
`d=0` within classes. The **interior is populated**: states carry *intermediate* distinguishability = *how long
until they diverge.*

## The three degenerate poles — exercised by tuning `O`
- **N1 (`O ≡ y`):** one class; `D` trivial; but `F` still runs → *dynamics and observation separated.* ✓ computed.
- **N2 (`O` all distinct):** all singletons; no reduction. ✓ computed.
- **N3 (nonexistent quotient):** does **not** occur here — finite deterministic Moore machines always have a
  unique minimal realization. **N3 needs leaving this setting:** nondeterministic minimization (not unique),
  infinite state, or continuous observation. (Confirms the draft: non-existence lives *outside* finite-determinism.)

## The honest new finding (why computing this was worth it)
The graded `D` that falls out of bisimulation is an **ULTRAMETRIC** (values `2^{-k}`, strong triangle inequality) —
**not** an inner-product / positive form, and certainly not a *complex* one. So the classical→quantum
"distinguishability form" jump is **not** "sharp partition → graded form" (that step is automatic and yields an
ultrametric); it is the **further, non-automatic** jump **ultrametric → (complex) inner-product geometry.**
That sharpens Priority 1's crux: the forcing question isn't "why graded?" (graded is free) but **"what forces the
graded geometry to be Hilbertian / complex rather than ultrametric?"** — exactly the CDP/Hardy reconstruction
content, now pinned to a concrete gap this example makes visible.

## Immediate next steps (still inside Priority 1)
1. Add a **nondeterministic** or **infinite-state** variant to actually exhibit **N3** (non-existence /
   non-unique minimization) — the one pole not yet realized.
2. Add a **continuous observation** variant to get a genuinely continuous graded `D` (not the discrete ultrametric)
   and see what geometry it wants.
3. State the crux cleanly: **ultrametric → inner-product** — which axioms on `(F, O, D)` force it, if any.

## Register / holds
Computed (finite, reproducible) · non-canon · sharp + graded `D` and N1/N2 exercised; N3 flagged as out-of-setting;
the **ultrametric-vs-inner-product** finding is the sharpened crux (a located gap, not proved) · nothing
promoted/admitted · Tier-3 · canon read-only. Provenance: 2026-07-10; script `.automation/priority1/D_worked_example.py`.
