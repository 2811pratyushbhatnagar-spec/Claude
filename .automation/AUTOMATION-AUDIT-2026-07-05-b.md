# Automation Audit — reversible-contact framework

**Second pass · 2026-07-05 (13:17 +0530) · procedures-only** (no governance action taken; nothing here promotes, admits, changes, adds, or publishes anything). Supersedes the first pass (`AUTOMATION-AUDIT-2026-07-05.md`, 10:32) — kept alongside it, not overwritten.

Canon at read time: `e222c8f` (from the 11:54 heartbeat, host-read) · git `808393a`. **Mount caveat this run:** sandbox bash served *truncated* reads (validate.py / compute_check.py showed phantom mid-line syntax errors; in-repo git errored) — consistent with the standing TRACES note. All findings below rest on **host file tools**, not sandbox bash.

## What resolved since the first pass (10:32 → now)

The hard part — *building* the tools — largely landed. Three of the five original items are effectively closed:

- **#1 Version history** — `git_head` now populates (`808393a`) where the first pass saw `null`; `.gitignore` fixed to the real litter glob `Scripts/.cycle_state.*.json` (+ excludes `.automation/`); real commits exist (`priorities.md`: "commit 808393a"). Helpers `init_git.ps1` and `commit_if_clean.ps1` are on disk. *Residual → new #4 below.*
- **#3 n=4 / |S|=3 enumeration probe** — the n=4 blind probe **ran** and matched predictions (24 = 4! strict, 209 = ΣC(4,k)²·k! partial); audit enumerators deposited in `LedgerA/`. *Residual: |S|=3 replication → new #5.*
- **#4 Compute-regression guard** — `Scripts/compute_check.py` is **built** (re-runs `verify.py` + the two Ledger-A harnesses, diffs captured refs, best-effort skips). *But it is not yet invoked by the cycle → new #1 below.*

Partially advanced: **#5 reconciliation/litter** — `draft_reconciliation.py` and `prune_state.ps1` now exist and `reconciliation/` is populated (2026-07-04 snapshot), but the prune isn't auto-run (litter grew 4 → 5).

## Standing backlog (reprioritized — the "last mile")

The theme this pass: the guards were **written but not wired**. `cycle_check.py` still runs validate + fingerprint + delta only — it calls neither `compute_check.py`, `status_page.py`, `prune_state.ps1`, nor any deploy/commit. So the leverage now is connecting built tools to the heartbeat, not building new ones.

| # | Opportunity | How often it bites | Est. time saved | Effort |
|---|-------------|--------------------|-----------------|--------|
| 1 | Wire `compute_check.py` into the cycle heartbeat | Every cycle | Averts silent math rot (the guard exists but never runs) | Low |
| 2 | Auto-publish the phone status board (still open) | ~5×/day | ~2–4 min × several/day + kills staleness | Low–Med |
| 3 | Wire `prune_state.ps1` into the cycle | Every cycle | Caps runner-state litter (now 5 files) | Low |
| 4 | Finish commit-on-clean cadence + delete the dead `setup_git.ps1.ps1` | Every canon change | ~5–10 min/commit + removes a foot-gun | Low |
| 5 | Parametrize the enumerator for the \|S\|=3 replication | On demand | Closes the last piece of the R1 frontier probe | Med |

---

### 1 — Wire `compute_check.py` into the cycle heartbeat  ·  **top recommendation**
**What.** The compute-regression guard from the first pass is now a real script, but `cycle_check.py` (confirmed by host read) never calls it — it runs `validate.py`, fingerprints canon, and diffs the manifest, nothing more. So the guard that catches silent math rot is sitting idle: a broken proof harness or a changed constant would still pass every cycle unnoticed, exactly the failure class item #4 was meant to close.
**Approach.** One optional, best-effort step in the cycle (or in the `refresh_and_deploy` chain): run `python Scripts/compute_check.py`, surface a MISMATCH into the heartbeat/delta summary, and let a missing dependency (sympy) degrade to a skip. Non-zero exit → flag for a human; never auto-"fix" a reference baseline (regenerating a ref is a blessed, deliberate act).
**Why it's #1.** The expensive part is done. Not wiring it means all of item #4's value is unrealized while looking finished.

### 2 — Auto-publish the phone status board (carried, still open)
**What.** Unchanged from the first pass in substance: the cycle neither regenerates (`status_page.py`) nor deploys the board. Evidence persists — `status.html` (10:11) is newer than `site/index.html` (10:07), so the served board is a cycle stale, and `priorities.md` says so outright. A chained runner `refresh_and_deploy.bat` now exists, but the deploy is gated behind a **one-time human `wrangler login`** (correctly human).
**Approach.** After that login, chain `status_page.py` → `wrangler pages deploy site` into the post-cycle step, gated on "content changed." Only `site/index.html` ships — no ledger leaves the machine.

### 3 — Wire `prune_state.ps1` into the cycle
**What.** `Scripts/.cycle_state.<ts>.N.json` files keep accumulating (5 now, was 4) because the create-only design can't unlink on this mount. `prune_state.ps1` exists to cap them but isn't auto-invoked.
**Approach.** Call it (keep last N, e.g. 10) as the final machine-side step of the cycle. Pure tidiness; touches no canon.

### 4 — Finish commit-on-clean + remove the dead runner
**What.** Git history is real now, but `cycle_check.py` doesn't auto-commit after a clean validate — it's still the manual "Next" in `priorities.md` via `commit_if_clean.ps1`. Separately, `setup_git.ps1.ps1` (doubled extension, double-click opens an editor) is now **dead** — superseded by `init_git.ps1` + `commit_if_clean.ps1` — and should be deleted to avoid confusion.
**Approach.** Have the cycle run `commit_if_clean.ps1` only after validate passes clean **and** canon changed (commit derived history only — never force-push or rewrite). Delete the orphan `.ps1.ps1`.

### 5 — Parametrize the enumerator for |S|=3 replication
**What.** n=4 is done and matched predictions; the |S|=3 replication (the other half of first-pass item #3) isn't confirmed run. `Experiments/` already holds reproducible enumerators.
**Approach.** A bounds-as-args enumerator the cycle can run on demand, saving output + a "changed-vs-last" flag; any result lands as a **Ledger-E candidate draft** for the steward. Never auto-promotes (Tier-3).

---

## Already well-automated (leave alone)
- **The 5-hourly heartbeat** (`cycle_check.py`): validate + canon fingerprint + delta + one-line heartbeat. Still solid and minimal.
- **compute_check.py's restraint**: references are explicitly baselines/drift-detectors, not authority claims; best-effort skips. Good design — it just needs to be *called* (#1).
- **Create-only timestamped state**: survives mounts that forbid unlink/rename — deliberate, not toil (the prune in #3 complements it, doesn't replace it).
- **Governance separation**: procedures-only cycle vs. Tier-3 human-only, consistently enforced. Don't dilute.

## Watch / revisit next cycle
- Once #1 lands, record the compute_check verdict in each heartbeat and in reconciliation snapshots.
- The sandbox **mount is again serving truncated reads** this run (bash saw phantom syntax errors; git errored). Not a repo defect — the files are intact on disk (host reads clean). Keep treating host file tools as ground truth; don't act on a sandbox-only "FLAG."
- **Cross-system toil** (Notion mirror by hand; resonance/concurrence across Claude + ChatGPT + Dispatch with the D-0xx log maintained manually) — still a future orchestration pass, not yet toil worth automating in-repo.
- **Not automatable (by design):** independent verification of the k=3 selection proof is blocked on the private kernel ledger (Carrier Lemma) — a human/archive unlock, not toil.

## Guardrails
Every item above is **procedures-only**. Automation may compute, check, regenerate derived views, draft candidates, commit derived history, and summarize. It must never promote a conjecture to a theorem, admit or alter a ledger entry (A–E), change Ledger B, add to Ledger D, publish an interpretation, or merge a reconciliation. When in doubt, produce a draft and stop.
