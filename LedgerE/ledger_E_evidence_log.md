# Ledger E — Evidence Log

**Purpose:** the historical trace of the project. Records only — never argues. What was attempted, what
survived, what failed, what was withdrawn or corrected, and why. It is the one ledger that logs *negatives*,
which is what keeps the framework from quietly rewriting its own history to look inevitable. Entries are dated
and append-only; nothing here is edited after the fact — later corrections are new entries, not overwrites.

**Register:** record. No advocacy, no conclusions. Distinguishes the *current state* of the framework (the
other ledgers) from the *path* that produced it (here).

---

## 2026-07-04 — snapshot

| Item | Outcome | Why / note |
|---|---|---|
| MSF side-problem: K(e)=D(e) at odd primes | **Established** (KR 1978 Thm 1 + independently-proved character lemma) | one open verification: the KR Thm 1 read is relayed (kr.txt), not first-party; a human read closes it |
| O-conjecture ("one object generates all recovered results") | **Withdrawn** | failed three checks — vacuity, class-collapse, detachability; residue reframed as a dependency-graph question |
| Object-search: does a structure's navigability *equal* reversible contact? | **Partial** | a thin discriminating class exists (connected groupoid-navigable + stack-like locality); but the full hope fails — an object can forbid traps, cannot confer freedom; the must/may remainder is un-absorbable |
| Enrichment-attack: can finite enrichment absorb the selection remainder? | **Strong hypothesis falsified** | selection-*as-structure* absorbs completely; minimal survivor = a structureless indexical |
| "Deflation is entailed / nothing there" (from the above) | **Corrected** | over-reached ontologically; honest form is *loss of structural jurisdiction* — the mathematics is silent there, licensing neither "nothing" nor "something ineffable" |
| capture = attractor (dynamical reading) | **Corrected** | conservative dynamics is a false friend (Poincaré recurrence = forced return); right category is choice-time / groupoid, not measure-preserving flow |
| Semantic-closure ↔ Tarski undefinability | **Walked back** to analogy | promising correspondence, not an established equivalence; held as a research direction |
| "Universe as a must/may object" (physics) | **Not admitted; held at register 2** | generic to all physics, interpretation-relative (no truth-maker; Bohm/Copenhagen/Everett disagree on the split), inherits the selection remainder = measurement problem. Nothing forced; physics ledger stays empty |
| Ledger A | **Frozen v0.1** (2026-07-04) | six signature decisions settled by finite models; results R1–R8 / W1–W12; centerpiece: return-existence is the irreducible reversibility axiom (return-exclusivity derivable from oplax, return-existence from nothing); strict functoriality collapses nondeterminism; invertible algebra ≠ undoable dynamics (W3). Built twice independently; the two constructions agree on the core |
| Ledger A — open | R1 general proof **hand-stated**; results on one small algebra | routed to round-2: prove/refute R1 beyond \|S\|=2; partial-identity variant (could overturn R1); \|S\|=3 replication; local states |
| "stack-like locality" in the class statement | **Removed** until formally defined | motivated in conversation, never formalized in-ledger; register kept clean |
| Ledger B | **Frozen v0.5** | v0.1→v0.4 added the self-application clauses; v0.5 applied ultracode's audit — Non-conversion asymmetry-inversion corrected (it had graded the participant, not the artifact), Transparency self-instantiated, smuggled A-parallel demoted to Ledger-C business, person≠picture assumption labelled. Closed under its purpose |
| Symmetry Condition + six-condition Self-Application variant | **Demoted to testing hypotheses** | not admitted as clauses; they reopen Ledger B only if testing shows they cover a failure mode none of the existing clauses addresses |
| Ledger C | **Empty** (a success, not a gap) | candidate queue holds one entry, *unadmitted*: return-existence ↔ always-available exit, awaiting a stated map |
| Ledger D | **Held open** | P1 = question schema, two readings sorted (structural → a Ledger-A question; ground → the frozen boundary). Allowed empty indefinitely |
| Reconciliation of the two parallel Ledger-A efforts | **In progress** (round-2) | records which version won and why; will be frozen as a dated snapshot, not edited |

---

## 2026-07-05 — snapshot

| Item | Outcome | Why / note |
|---|---|---|
| Ledger A canonicalized at v0.2 | **Adopted into repo** (`LedgerA/ledger_A_math_v0.2_canonical.md` + harnesses), steward-authorized ("yes, fix that move") | v0.2 (frozen 2026-07-04) supersedes v0.1; carries the round-2 results — R1 candidate general proof (conjecture-grade pending independent audit), determinism boundary (strict → bijections; ⊆Δ → partial bijections 7/34; free → 56 F-eq survivors, 37 nondet), R2 + dual, \|S\|=3 replication (6 = 3!), local-states by construction, two adversarial flags (comp-uniqueness a choice; inv redundant at max point) |
| Round-2 reconciliation | **Frozen 2026-07-04, imported** to `reconciliation/` | full agreement, no disagreements; complementary methods (R-series enumeration / W-series witnesses); notation map adopted (F-eq/F-sup/F-sub, RET-∃/RET-!, EI-w1/w2). Caveat stands: exact-number diff pending — `ledger_a_verify.py` still not on disk |
| validate.py: historical-layer exemption | **Tooling change** (procedures-only, non-canon) | version-drift check now skips `LedgerE/` + `reconciliation/` — append-only history legitimately names superseded versions; drift-checking is for current-state docs. Without this, bumping canon would force editing frozen history |

---

*Governance: append-only; dated snapshots; corrections are new rows, never edits. New concepts do not enter
here — only records of what happened to them.*
