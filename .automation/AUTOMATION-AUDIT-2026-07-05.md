# Automation Audit — reversible-contact framework

**First pass · 2026-07-05 · procedures-only** (no governance action taken; nothing here promotes, admits, changes, adds, or publishes anything)

Scope: the local `framework` canon repo and its cycle machinery (`status.json`, `validate.py`, `Scripts/cycle_check.py`, `Scripts/status_page.py`, the `.bat`/`.ps1` runners), cross-referenced with two recent Cowork sessions ("Framework context", "Work reflection and priorities"). The philosophy throughout: **expand the operation space while keeping representation minimal** — favor one more composable primitive or check that "earns its place," never new canon.

## Standing backlog (prioritized)

| # | Opportunity | How often it bites | Est. time saved | Effort |
|---|-------------|--------------------|-----------------|--------|
| 1 | Wire up real version history (commit-on-clean) | Every canon change | Unblocks correctness + ~5–10 min/manual commit | Low |
| 2 | Auto-publish the phone status board after each cycle | ~5×/day | ~10–20 min/day + kills staleness | Low–Med |
| 3 | Automate the queued n=4 / \|S\|=3 enumeration probe | On demand / per frontier push | Converts a manual research chore into repeatable compute (high leverage) | Med |
| 4 | Add a compute-regression guard to the heartbeat | Every cycle (cheap) | Averts silent math rot (a class `validate.py` can't see) | Low |
| 5 | Draft reconciliation/Ledger-E scaffolds + prune runner litter | Per milestone / every cycle | ~10–15 min/snapshot + ongoing tidiness | Low |

---

### 1 — Wire up real version history (commit-on-clean)
**What.** This local repo has no working commit history. The heartbeat records `git_head: null` and falls back to a content hash; in-repo `git` currently errors; the initial-snapshot commit in `git_setup.bat` / `setup_git.ps1.ps1` hasn't run here. Two concrete bugs block it: `setup_git.ps1.ps1` has a **doubled `.ps1.ps1` extension** (double-click opens an editor, doesn't run), and `.gitignore` ignores `Scripts/.cycle_state.json` (singular) while the real runner litter is `Scripts/.cycle_state.<timestamp>.N.json` — so state files would be committed as canon noise.
**Why it matters.** The framework's own *historical layer* — Ledger E append-only, dated reconciliation snapshots, "inspectable rather than rewritten" — is aspirational without real git underneath it. This is the substrate the append-only discipline sits on.
**Approach (procedures-only).** Rename to `setup_git.ps1`; fix the ignore pattern to `Scripts/.cycle_state.*.json`; run the one-time snapshot; then let the cycle `git commit -am` **only after `validate` passes clean and canon changed**. Commit-only — never force-push or rewrite history (committing derived history is not a governance decision; rewriting it would be).
**Est. savings.** Mostly correctness (a real `git_head` in every heartbeat) plus ~5–10 min per manual commit attempt.

### 2 — Auto-publish the phone status board after each cycle
**What.** `cycle_check.py` validates + fingerprints but does **not** regenerate the dashboard or deploy (confirmed: no `status_page`/`wrangler`/`.html` references in it). Dashboard regen (`status_page.py`) is *optional* in the cycle; the deploy (`deploy_status.bat` → `npx wrangler pages deploy`) is a **fully manual double-click**. Evidence of the resulting drift right now: `status.html` was regenerated at 10:11 but `site/index.html` (what the phone actually serves) is from 10:07 — **the phone board is a cycle stale**.
**Why it matters.** You set this up to glance at on your phone; a board that silently lags every cycle defeats the point.
**Approach.** Chain `python Scripts/status_page.py` → `wrangler pages deploy site` into the post-cycle step, **gated on "content changed"** (skip deploy when the heartbeat says no material change). `deploy_status.bat` already stages only `site/index.html`, so no ledger ever leaves the machine. One-time `wrangler login` remains manual (unavoidable, correctly so).
**Est. savings.** ~2–4 min × several/day of manual babysitting, plus eliminated staleness.

### 3 — Automate the queued n=4 / |S|=3 enumeration & convergence probe
**What.** `priorities.md` explicitly queues **"n=4 enumeration / convergence probe (automation queue)"** and **"|S|=3 replication"** as work that "could overturn R1." `Experiments/verify.py` already runs finite, reproducible checks (carry-set injectivity over odd primes ≤250; a `K_P(e)=D(e)` space-certificate for small e). Extending it to the queued probes is the natural next primitive.
**Why it matters.** Highest scientific leverage in the backlog — it directly manufactures Ledger-A evidence (witnesses) and is the cleanest example of "expand operations, minimal representation": a reproducible computation that yields evidence, not a new axiom.
**Approach.** A parametrized `Experiments/enumerate.py` (bounds as args) the cycle can run on demand, saving outputs alongside a "changed-vs-last" flag; any positive/negative result lands as a **Ledger-E candidate draft** for your admission. Never auto-promotes to a theorem (Tier-3).
**Est. savings.** Turns an open, manual, easy-to-defer research chore into a repeatable (even overnight) compute.

### 4 — Add a compute-regression guard to the heartbeat
**What.** `validate.py` checks document/version drift and governance only — it does **not** check that the mathematics still computes. `verify.py` + `verify_output.txt` exist, but nothing re-runs `verify.py` and diffs the result, so a broken proof script or a changed constant would pass every cycle unnoticed.
**Why it matters.** It closes a whole failure class the current checker structurally cannot see — exactly the bar `validate.py`'s own header sets ("a new check earns its place only by catching a failure nothing else catches").
**Approach.** One optional cycle step: re-run `Experiments/verify.py`, normalize, diff against `verify_output.txt`, flag on mismatch. Guard: `verify.py` needs `sympy` while the heartbeat is stdlib-only — run it **best-effort** so a missing dependency degrades to a skip, not a failure.
**Est. savings.** Prevents silent compute rot; minutes-to-hours per averted regression.

### 5 — Draft reconciliation/Ledger-E scaffolds + prune runner litter
**What.** Two low-effort items. (a) `priorities.md` "in progress" has *Round-2 reconciliation … to be frozen as a dated snapshot*; `reconciliation/` is empty and producing snapshots + Ledger-E appends is manual. (b) `Scripts/.cycle_state.<ts>.N.json` files accumulate (4 in one day) because the append-only mount can't prune them, and they aren't `.gitignore`d.
**Approach.** The cycle **drafts** a dated reconciliation template pre-filled with current status + canon hash and a Ledger-E candidate row, leaving the decision to you (admitting = Tier-3). A machine-side prune keeps the last N state files. Draft + tidy only; never admit.
**Est. savings.** ~10–15 min per templated snapshot, plus ongoing cleanliness.

---

## Already well-automated (leave alone)
- **The 5-hourly heartbeat** (`research-cycle-5h` → `cycle_check.py`): validate + canon fingerprint + delta detection + one-line heartbeat. Solid and appropriately minimal.
- **Create-only timestamped state**: the runner persists state as create-only files so it survives mounts that forbid unlink/rename — a genuinely thoughtful design, not toil.
- **Governance separation**: procedures-only cycle vs. Tier-3 human-only decisions is clean and consistently enforced (`status.json` + the task prompt). Don't dilute it.
- **`validate.py`'s restraint**: deliberately small, drift + governance only. Keep resisting growth.

## Watch / revisit next cycle
- Once #1 lands, add commit-hash provenance to the heartbeat and to reconciliation snapshots.
- **Cross-system toil seen in sessions** (beyond this repo): decisions are mirrored to **Notion** by hand, and math is cross-checked across **Claude + ChatGPT + Dispatch** ("resonance/concurrence") with the decision log (D-0xx) maintained manually. Candidates for a future orchestration pass — see the companion multi-agent brief.
- **Not automatable (by design):** independent verification of the k=3 selection proof / exact-insensitivity lemma is blocked on the **private kernel ledger** (Carrier Lemma v0.8). That's a human/archive unlock, not toil.

## Guardrails
Every item above is **procedures-only**. Automation may compute, check, regenerate derived views, draft candidates, commit derived history, and summarize. It must never promote a conjecture to a theorem, admit or alter a ledger entry (A–E), change Ledger B, add to Ledger D, publish an interpretation, or merge a reconciliation. When in doubt, produce a draft and stop.
