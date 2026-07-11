# Automation Audit — reversible-contact framework

**Fourth pass · 2026-07-06 (00:36 +0530) · procedures-only** (no governance action taken; nothing here promotes, admits, changes, adds, or publishes anything). Supersedes the third pass (`AUTOMATION-AUDIT-2026-07-05-c.md`, 15:36) — kept alongside it, not overwritten. The 20:36 run was a no-change (6 open, canon `91ca5d6`); this pass records the first material delta since.

Canon at read time: `728e1ce` (12-char `728e1ce00628`, from the 00:13 heartbeat; **host-corroborated** — host `status.json` reads A 0.7/frozen · B 0.5/frozen · C 0.1/open(0) · D 0.1 · E 0.1, matching the cycle's ledger line, and validate is clean at **31 docs**). Git: **unreadable-in-sandbox** this run (not `null` — same read failure as prior passes; host-side git is real but advanced past `808393a` with the restructure). Canon advanced `91ca5d6 → 728e1ce` via a large steward/native-Claude restructure (see TRACES 21:48→00:21) — observed only, not touched.

## What changed since the third pass (15:36 → now)

- **MAJOR: the decision-class / governance restructure landed.** Doc count `27 → 31`; **Ledger A promoted `0.2 → 0.7` and frozen; Ledger B `→ 0.5` and frozen**; new governance layer added (`DECISION-CLASSES.md`, `DECISIONS.md`, `DECLASSIFICATIONS.md`, `WORKER-CONTRACT.md`, `SUBSTANTIAL-RESULT-CHECKLIST-DRAFT.md`); ledgers reorganized (per-ledger `README.md`, `LedgerA/archive/`, `LedgerA/audits/`, canonical filenames replacing `*_v0.x` variants). Purely observed; all of it is GOVERNED and Tier-3.
- **ESCALATED — the published phone board is now a whole restructure stale (item #3).** `status.html` (10:11) and `site/index.html` (10:07) are byte-unchanged since the third pass, but canon has since leapt from the pre-restructure world to `728e1ce`. The board therefore still shows the **old ledger states** (pre-0.7 A, 27-doc count) to anyone reading it. Last pass this was "one cycle behind"; it is now materially wrong. The regen half (`status_page.py`) is **ungated** and overdue; only the `wrangler` deploy is (correctly) gated on the one-time human login.
- **NEW harnesses appeared (21:48–23:55), none wired into `cycle_check.py`.** `Scripts/brute_force_step.py` (BF runner, carries its own reduction self-test), `Scripts/worker_guard.py` (**GOVERNED — never edit**), `Scripts/review_metric.py` (new; **not** covered by `compute_check.py`), plus `ledger_A_round2.py` / `ledger_A_witnesses.py` (these two **are** guarded by `compute_check`). New surface area, but the heartbeat still runs only validate + git.
- **Litter grew `8 → 9`.** A ninth `Scripts/.cycle_state.*.json` (`…001305….6.json`) landed; `prune_state.ps1` still unwired (item #4). Single runner this tick — no 15:03-style same-second race.
- **Standing #1 fired again.** `compute_check.py` truncated in *this* sandbox at line 45 (`unterminated string literal`) though it is byte-intact host-side (70 lines, line 45 complete) — a mount phantom, **not** compute drift. Fresh corroboration: the sandbox `ls` served a **stale** `status.json` (2253 B / Jul-4) while the host file is the restructured 3787 B version. The runtime still can't reliably read its own sources.
- **Nothing from the third pass resolved.** `cycle_check.py` still invokes only `validate.py` (+ git); items #1, #2, #4, #5 remain unwired and #3's regen is overdue.

## Standing backlog (reprioritized)

The theme this pass: **a big canon restructure landed and the derived/published layer didn't follow.** The heartbeat is still honest-but-blind (validate + git only), and its runtime still truncates its own reads. The freshest, highest-visibility, and *ungated* action is regenerating the stale board; the standing correctness fix (#2, truncation-hardening) is unchanged and still fires.

| # | Opportunity | How often it bites | Est. time saved | Effort |
|---|-------------|--------------------|-----------------|--------|
| 1 | **Regenerate the phone board against `728e1ce` (ungated `status_page.py`)** — it publicly shows pre-restructure ledger states | Every canon change (just bit, hard) | Kills a wrong-state public board; ~2–4 min manual regen each restructure | Low |
| 2 | Harden the heartbeat against mount truncation (stop false FLAGs / `git_head:null`) | Every flaky-mount run (fired again this run) | Kills false "validate FLAGGED"/null-git alarms + the host re-verification each forces | Low–Med |
| 3 | Wire `compute_check.py` into the cycle heartbeat (+ extend to cover new `review_metric.py`) | Every cycle | Averts silent math rot — **but only after #2** (else false MISMATCH under truncation) | Low |
| 4 | Wire `prune_state.ps1` in + dedupe concurrent runners | Every cycle | Caps state litter (now 9) + stops same-second double-writes | Low |
| 5 | Finish commit-on-clean cadence + delete dead `setup_git.ps1.ps1` | Every canon change | ~5–10 min/commit + removes a foot-gun | Low |
| 6 | Parametrize the enumerator for the \|S\|=3 replication | On demand | Closes the last piece of the R1 frontier probe | Med |

---

### 1 — Regenerate the stale phone board  ·  **top recommendation (new this pass)**
**What.** The restructure moved canon `91ca5d6 → 728e1ce` (A `0.2→0.7/frozen`, 27→31 docs) but `status.html`/`site/index.html` are frozen at 10:07–10:11 — i.e. they render the *pre-restructure* ledger states. Anyone glancing at the phone board sees stale governance.
**Approach.** Run `Scripts/status_page.py` against current canon to refresh `status.html` (and the `site/` artifact). This half needs **no login** and should run now; the `wrangler pages deploy site` publish stays (correctly) gated on the one-time human `wrangler login`. Only derived views change — no ledger leaves the machine. *(Procedures-only: this audit does not itself regenerate — it flags; the research-cycle or steward runs the regen.)*
**Why it's #1.** It is the concrete new harm this run, it is ungated, and it is the cheapest high-visibility fix on the board.

### 2 — Harden the heartbeat against mount truncation (carried from third-pass #1)
**What.** `cycle_check.py` runs `validate.py` (and would run `compute_check.py`) through the interpreter, whose buffered source read truncates on the flaky mount — a compile error on a file byte-for-byte intact on disk. Reproduced again this run: `compute_check.py` dies at line 45; the sandbox even served a stale `status.json`. The cycle then persists `validate FLAGGED` / `git_head:null` / `status.json unreadable`, none real.
**Approach.** Before trusting a validate failure, re-read the target and cross-check length/hash against the just-computed manifest (single-shot reads succeed here); on a parse error whose file nonetheless hashes clean, retry once, then degrade to `MOUNT-SUSPECT — re-run` instead of a hard `FLAGGED`. Treat a git error the same way (`git: unreadable-in-sandbox`, not `null`). Never invert the safety default — a genuinely dirty validate must still FLAG.
**Why it matters.** Standalone toil-reducer *and* the precondition that makes #3 trustworthy.

### 3 — Wire `compute_check.py` into the cycle heartbeat (carried from third-pass #2)
**What.** The compute-regression guard is built but still uncalled — `cycle_check.py` runs validate + fingerprint + delta only (confirmed again). It guards `verify.py` + the two `ledger_A_*` harnesses but **not** the new `review_metric.py`.
**Approach.** One optional best-effort step: `python Scripts/compute_check.py`, surface a MISMATCH into the heartbeat/delta, degrade a missing `sympy` to skip. Gate on #2 so a truncated read degrades to `MOUNT-SUSPECT`, not a false MISMATCH. Optionally add `review_metric.py` (with a captured baseline) to its CHECKS list. Non-zero exit → flag for a human; never auto-regenerate a baseline.

### 4 — Wire `prune_state.ps1` in + dedupe concurrent runners (carried from third-pass #4)
**What.** `Scripts/.cycle_state.<ts>.N.json` keeps accumulating (9 now, was 7→8) because the create-only design can't unlink on this mount; `prune_state.ps1` exists but isn't auto-invoked.
**Approach.** Call `prune_state.ps1` (keep last ~10) as the final machine-side step. Optionally a coarse same-timestamp lock/skip so two runners in one tick don't both write. Pure tidiness; touches no canon.

### 5 — Finish commit-on-clean + remove the dead runner (carried from third-pass #5)
**What.** Git history is real host-side but `cycle_check.py` doesn't auto-commit after a clean validate — still the manual "Next" in `priorities.md` via `commit_if_clean.ps1`. `setup_git.ps1.ps1` (doubled extension) remains **dead** (superseded by `init_git.ps1` + `commit_if_clean.ps1`) and should be deleted. Git is unreadable from the sandbox, so this cadence must run host-side, not inside the truncated mount.
**Approach.** Run `commit_if_clean.ps1` only after validate passes clean **and** canon changed (commit derived history only — never force-push or rewrite). Delete the orphan `.ps1.ps1`.

### 6 — Parametrize the enumerator for |S|=3 replication (carried from third-pass #6)
**What.** n=4 is done and matched predictions; the |S|=3 replication isn't confirmed run. `Experiments/` already holds reproducible enumerators; the BF queue (`BF-1`) is advancing normally (F=485/65536, ~0.7%, ~5 F/s — not stalled).
**Approach.** A bounds-as-args enumerator the cycle can run on demand, saving output + a "changed-vs-last" flag; any result lands as a **Ledger-E candidate draft** for the steward. Never auto-promotes (Tier-3).

---

## Already well-automated (leave alone)
- **The 5-hourly heartbeat** (`cycle_check.py`): validate + canon fingerprint + delta + one-line heartbeat. Minimal and correct in spirit — #2 only makes it honest about its own read failures.
- **`compute_check.py`'s restraint**: references are baselines/drift-detectors, not authority claims; best-effort skips. Needs to be *called* (#3) and *truncation-guarded* (#2).
- **The brute-force queue** (`brute_force_step.py` + `bf_state.json`): create-only state, append-only findings bank, self-tested reduction, chunked with CPU-time estimates. Progressing (`BF-1` 202→351→485 across three chunks). Healthy — leave it.
- **Create-only timestamped state**: survives mounts that forbid unlink/rename — deliberate (the prune in #4 complements it).
- **Governance separation**: procedures-only cycle vs. Tier-3 human-only, now formalized in `DECISION-CLASSES.md`. Don't dilute.

## Watch / revisit next cycle
- Record the canon move `91ca5d6 → 728e1ce` (major restructure: A `0.7/frozen`, B `0.5/frozen`, decision-class layer) in the next reconciliation snapshot. Purely observed.
- `review_metric.py` (new, 23:55) is an unguarded compute surface — fold into `compute_check.py`'s CHECKS when #3 is wired (needs a blessed baseline first).
- Once #2 lands, a `MOUNT-SUSPECT` verdict should trigger an automatic single re-run rather than waiting for the next 5-hour tick.
- `BF-2` (exact-number diff) stays blocked on `ledger_a_verify.py`, still absent (probed 4 paths) — a human drop-in, not toil.
- **Cross-system toil** (Notion mirror by hand; resonance/concurrence across Claude + ChatGPT with the D-0xx log maintained manually) — still a future orchestration pass, not yet in-repo toil.
- **Not automatable (by design):** independent verification of the k=3 selection proof is blocked on the private kernel ledger (Carrier Lemma) — a human/archive unlock.

## Guardrails
Every item above is **procedures-only**. Automation may compute, check, regenerate derived views, draft candidates, commit derived history, and summarize. It must never promote a conjecture to a theorem, admit or alter a ledger entry (A–E), change Ledger B, add to Ledger D, publish an interpretation, merge a reconciliation, or lower any item's classification (monotonic, escalate-only). When in doubt, produce a draft and stop.
