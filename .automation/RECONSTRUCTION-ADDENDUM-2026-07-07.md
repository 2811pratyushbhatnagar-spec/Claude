# Reconstruction Addendum — three verification axes, held disjoint (2026-07-07)   [non-canon · Class-D · warrant CANDIDATE]

*Corrects and tightens STATE-RECONSTRUCTION-2026-07-07.md after a steward/cross-agent review. Each fix
severs a spot where success on a weaker claim was reading as success on a stronger one — the same operation
the framework runs, applied to the reconstruction itself. Read-only on all governed/canon paths; promotes
nothing. Provenance `FILE §sec`.*

## Correction 1 — the worker contract is PARTIALLY operationalized (not "philosophy became code")
`worker_guard.py` mechanizes the **write-authority** boundary: it git-diffs the tree vs HEAD and refuses a
commit if any governed path changed, if an append-only file lost lines, or if a decision-class de-escalated
without a `DECLASSIFICATIONS.md` row (`WORKER-CONTRACT.md §Enforcement`; `worker_guard.py`). It does **not**
enforce the **semantic** boundary — "produce evidence, never conclusions-as-facts" is still worker
*discipline*, not a guard that can stop it. So the mechanizable half (who may write where) is mechanized; the
irreducibly-semantic half (warrant-writing) stays policy. That asymmetry *is* the confidence/warrant line.
**Nuance:** the guard is **live now** while `Q-GOV-V2-FREEZE` is **unsigned** (`GOVERNANCE-VERSION.json`
`frozen:false`) — worker-boundary *enforcement* runs ahead of the formal constitutional *freeze*. Decision ≠
enforcement; only the second is the steward's signature. Honest claim: **a design constraint is partially
operationalized through enforcement.**

## Correction 2 — internal consistency ≠ historical correctness
Three-file version check, performed: `status.json` → Ledger A `"0.7"`; `LedgerA/ledger_A_canonical.md` header
→ "v0.7 · CANONICAL · FROZEN"; `SNAPSHOT.md` → "Ledger A frozen v0.7 canonical". **All three agree on 0.7**
⇒ this is the repository's *internally-consistent reported state* (rules out a bookkeeping / version-drift
defect). Whether v0.7's **content** is correct relative to the framework's history is a **separate** question
the version fields cannot answer. My prior phrase "agreement means advancement" collapsed the two: agreement =
self-consistency; advancement-being-*correct* is a further check version fields can't provide. (The context
map's "v0.3" vs repo "v0.7" is the **map being stale, not failing** — reconstruction override working as
designed; the map lowered reconstruction cost without reducing the requirement.)

## Correction 3 — the free-rung reproduction, graded by provenance (not filename)
**Identity check (warrant-relevant):** Impl A (regular-pair route, chat) FREE n=4 = **992,696**; Impl B
(`free_rung_repro_B.py`, boolean-matrix route) = **992,696** (984,279 nondet / 8,417 det; 1815 s)
(`FREE-RUNG-REPRODUCTION-2026-07-06.md §comparison`). **Match** at n=2/3/4; strict 2/6/**24**, partial
7/34/**209** concordant, n=4 now third-source.

**Independence grade (primary first-party schema, same file §provenance):** independent code = **Yes**;
shared implementation = **No** (`r1_ladder_n4.py` unread); shared reduction = **No** — re-derived from the 8
F-eq equations *and* raw-validated at n=2 (exact survivor **sets**, not just counts); derived-from-spec =
**Yes**; **result-before-seeing-target = No** (the directive disclosed 992,696; FREE n≤3 pre-computed
in-repo). Self-verdict: **Level 3 — model- + implementation-independent, NOT blind; "do not record as
triangulated."** On the independence *spectrum* this is high — past "shared reduction, different arithmetic,"
short of "raw functor, no reduction, blind." Residual: the raw-functor ground truth is exhaustive only at
**n=2**; at n≥3 modeling-correctness rests on the reduction-equivalence claim (mechanically shown, n=2-validated).

**Blind cross-check (this session, orchestrated):** a fresh stream given **spec only** (the 8 equations +
setup; no counts, no reduction) independently wrote a raw four-relation enumerator and returned **56 survivors
/ 37 nondet** at n=2 — **match**, genuinely blind at the ground-truth level (the "regular-pair" lens re-earned,
not inherited). Extends the blind bar exactly as far as compute allows.

**Net banding:** FREE n=4 = **cross-confirmed** (two independent implementations + a blind n=2 ground truth) —
**not externally-audited.** The genuinely-blind n=4 (fresh stream, spec only, target withheld, count-bearing
files off-limits) remains the open, **steward-commissioned** bar; the repo specs it and records it **not
started** (`FREE-RUNG-REPRODUCTION §hierarchy`).

**Comparison semantics, held to the confidence/warrant line:** *Match* increases confidence that both
implementations compute the same mathematical object; it does **not** prove either correct (a shared error is
logically possible — though the blind + raw n=2 ground truth excludes a shared *modeling* error at n=2).
*Divergence* would establish only that **at least one** of {implementation, interpretation, specification}
differs, and would **trigger reconstruction** — a trigger, not a verdict, and not even a localizer of which.

## The structure this surfaces — three orthogonal verification axes
1. **Policy** — does the worker obey the contract? *Enforced by `worker_guard.py` (partial: write-authority only).*
2. **Repository** — does the repo agree with its primary artifacts? *Three-file v0.7 consistency: PASS; historical-correctness: separate, open.*
3. **Mathematics** — does an independently-derived implementation reach the same result? *992,696 match; Level-3 not-blind + a blind n=2 ground truth; blind n=4 open.*

The failure mode is **diagonal leakage** — letting a green light on a cheap axis illuminate an expensive one.
The worker obeying its contract (1) says nothing about whether the math is right (3); the repo being internally
consistent (2) says nothing about whether the worker is bounded (1) or the reproduction independent (3). Each
axis certifies only itself; the integrity of the whole is precisely the refusal to let one axis vouch for
another — the confidence/warrant discipline, and the three-way gap taxonomy, one level up.

## Holds (unchanged)
Read-only on canon; reconstruction overrides the map where they conflict; the v2 **freeze is the steward's
signature**; the **blind-n4 bar is the steward's call** — this addendum is what lets it be made. Evidence only;
promotion / admission / freeze remain Tier-3.

*Provenance: WORKER-CONTRACT.md; Scripts/worker_guard.py; GOVERNANCE-VERSION.json; status.json; LedgerA/ledger_A_canonical.md; SNAPSHOT.md; LedgerA/audits/FREE-RUNG-REPRODUCTION-2026-07-06.md; packages/staging/free-rung-n4-repro/{free_rung_repro_B.py, package_manifest.json}; plus this session's blind raw-n2 stream (56/37).*
