# Automation Audit — reversible-contact framework

**Third pass · 2026-07-05 (15:36 +0530) · procedures-only** (no governance action taken; nothing here promotes, admits, changes, adds, or publishes anything). Supersedes the second pass (`AUTOMATION-AUDIT-2026-07-05-b.md`, 13:17) — kept alongside it, not overwritten.

Canon at read time: `91ca5d6` (from the 15:03 heartbeat; **host-corroborated** — every manifest byte-size matches host `ls`, and `sha256sum ARCHITECTURE.md` = `aff6d79…` matches the manifest) · git `808393a` host-side (git is **unreadable from the sandbox** this run — see #1). Canon advanced `e222c8f → 91ca5d6` since the second pass via a steward/research-cycle content change (5 files: `ARCHITECTURE.md`, +`Journal/nothing-is-everything.md`, `LedgerE/ledger_E_evidence_log.md`, `priorities.md`, `status.json`) — observed only, not touched.

## What changed since the second pass (13:17 → now)

- **NEW (elevated from "watch"): the heartbeat is emitting *false* FLAGs under mount truncation.** The 15:03 cycle persisted `validate FLAGGED`, `git_head: null`, and `status.json unreadable` — **all three are phantoms.** `validate.py` is intact on the host (line 41 is a complete regex). Reproduced deterministically in *this* sandbox: `wc -c validate.py` = 2169 (full size) and `sha256sum` of the canon files match the manifest, yet Python's *source read* of `validate.py` truncates mid-string at line 41 ("unterminated string literal"), `compute_check.py` truncates the same way at line 45, and `git rev-parse HEAD` dies with "unknown error … reading the configuration files." So single-shot reads (wc, sha256sum) succeed while the interpreter's buffered reads truncate — the cycle can't tell a real validate failure from a mount phantom, and cries wolf every flaky run. This was "watch, don't act on a sandbox-only FLAG" in the second pass; there is now persisted proof it fired, so it becomes an actionable hardening item — **and a prerequisite for #2.**
- **Litter grew 5 → 7.** The 15:03 cycle wrote *two* state files at the same second (`…150359….10.json` with `material_change:false` and `…150359….7.json` with `material_change:true`) — two runners raced and recorded conflicting deltas. Prune (#4) still unwired.
- **No new runners; no new staleness.** No `*.bat`/`*.ps1` added since 13:17 (newest is `refresh_and_deploy.bat`, 11:24). `status.html` (10:11) is still one cycle newer than `site/index.html` (10:07) — same phone-board staleness, still gated on the one-time `wrangler login`. Nothing from the second pass **resolved** this run.

## Standing backlog (reprioritized)

The theme shifts: last pass it was "guards written but not wired"; this pass it's **"the wire is unreliable"** — the runtime the heartbeat executes in truncates its own source reads, so both the existing FLAG and any guard we wire in (#2) can misfire. Make the heartbeat honest first, then wire.

| # | Opportunity | How often it bites | Est. time saved | Effort |
|---|-------------|--------------------|-----------------|--------|
| 1 | Harden the heartbeat against mount truncation (stop false FLAGs) | Every flaky-mount run (≥2 today) | Kills false "validate FLAGGED"/null-git alarms + the host-side re-verification each one forces | Low–Med |
| 2 | Wire `compute_check.py` into the cycle heartbeat | Every cycle | Averts silent math rot — **but only after #1** (else it inherits false MISMATCH) | Low |
| 3 | Auto-publish the phone status board (still open) | ~5×/day | ~2–4 min × several/day + kills staleness | Low–Med |
| 4 | Wire `prune_state.ps1` in + dedupe concurrent runners | Every cycle | Caps state litter (now 7) + stops same-second double-writes | Low |
| 5 | Finish commit-on-clean cadence + delete dead `setup_git.ps1.ps1` | Every canon change | ~5–10 min/commit + removes a foot-gun | Low |
| 6 | Parametrize the enumerator for the \|S\|=3 replication | On demand | Closes the last piece of the R1 frontier probe | Med |

---

### 1 — Harden the heartbeat against mount truncation  ·  **top recommendation**
**What.** `cycle_check.py` runs `validate.py` (and would run `compute_check.py`) via the interpreter, whose buffered source read truncates on the flaky sandbox mount — producing a compile error on a file that is byte-for-byte intact on disk. The cycle then persists `validate FLAGGED` / `git_head: null` / `status.json unreadable`, none of which are real. Each occurrence costs a human the exact reverification the 13:05 TRACES CORRECTION already had to do once by hand.
**Approach.** Before trusting a validate failure, re-read the target and cross-check length/hash against the just-computed manifest (single-shot reads succeed here); on a compile/parse error whose file nonetheless hashes clean, **retry the read once, then degrade to a `MOUNT-SUSPECT — re-run` state instead of a hard `FLAGGED`.** Treat a git error the same way (emit `git: unreadable-in-sandbox`, not `null`). Never invert the safety default — a genuinely dirty validate must still FLAG; this only distinguishes "the checker couldn't read the file" from "the file is wrong."
**Why it's #1.** It's a standalone toil-reducer (stops recurring false alarms) *and* the precondition that makes #2 trustworthy. Wiring a compute guard into a cycle that can't reliably read its own source just multiplies the false-MISMATCH noise.

### 2 — Wire `compute_check.py` into the cycle heartbeat (carried from second-pass #1)
**What.** The compute-regression guard is built but still uncalled — `cycle_check.py` runs validate + fingerprint + delta only. Confirmed again this run.
**Approach.** One optional best-effort step: run `python Scripts/compute_check.py`, surface a MISMATCH into the heartbeat/delta, degrade a missing `sympy` to skip. **Gate on #1** so a truncated read of the harness degrades to `MOUNT-SUSPECT`, not a false MISMATCH. Non-zero exit → flag for a human; never auto-regenerate a reference baseline.

### 3 — Auto-publish the phone status board (carried, still open)
**What.** Unchanged in substance: the cycle neither regenerates (`status_page.py`) nor deploys the board. `status.html` (10:11) is still a cycle newer than `site/index.html` (10:07); `refresh_and_deploy.bat` exists but the deploy is gated behind a **one-time human `wrangler login`** (correctly human).
**Approach.** After that login, chain `status_page.py` → `wrangler pages deploy site` into the post-cycle step, gated on "content changed." Only `site/index.html` ships — no ledger leaves the machine.

### 4 — Wire `prune_state.ps1` in + dedupe concurrent runners
**What.** `Scripts/.cycle_state.<ts>.N.json` keeps accumulating (7 now, was 5) because the create-only design can't unlink on this mount; `prune_state.ps1` exists but isn't auto-invoked. Separately, the 15:03 cycle ran **twice in the same second** (PIDs …10 and …7) and wrote conflicting `material_change` — a mild race worth a lightweight guard.
**Approach.** Call `prune_state.ps1` (keep last ~10) as the final machine-side step. Optionally add a coarse same-timestamp lock/skip so two runners in one tick don't both write. Pure tidiness; touches no canon.

### 5 — Finish commit-on-clean + remove the dead runner (carried from second-pass #4)
**What.** Git history is real host-side (`808393a`) but `cycle_check.py` doesn't auto-commit after a clean validate — still the manual "Next" in `priorities.md` via `commit_if_clean.ps1`. `setup_git.ps1.ps1` (doubled extension) remains **dead** (superseded by `init_git.ps1` + `commit_if_clean.ps1`) and should be deleted. Note: git is unreadable from the sandbox, so this cadence must run where git works (host-side), not inside the truncated mount.
**Approach.** Run `commit_if_clean.ps1` only after validate passes clean **and** canon changed (commit derived history only — never force-push or rewrite). Delete the orphan `.ps1.ps1`.

### 6 — Parametrize the enumerator for |S|=3 replication (carried from second-pass #5)
**What.** n=4 is done and matched predictions; the |S|=3 replication isn't confirmed run. `Experiments/` already holds reproducible enumerators.
**Approach.** A bounds-as-args enumerator the cycle can run on demand, saving output + a "changed-vs-last" flag; any result lands as a **Ledger-E candidate draft** for the steward. Never auto-promotes (Tier-3).

---

## Already well-automated (leave alone)
- **The 5-hourly heartbeat** (`cycle_check.py`): validate + canon fingerprint + delta + one-line heartbeat. Minimal and correct in spirit — #1 only makes it honest about its own read failures, not bigger.
- **`compute_check.py`'s restraint**: references are baselines/drift-detectors, not authority claims; best-effort skips. Good design — needs to be *called* (#2) and *truncation-guarded* (#1).
- **Create-only timestamped state**: survives mounts that forbid unlink/rename — deliberate, not toil (the prune in #4 complements it).
- **Governance separation**: procedures-only cycle vs. Tier-3 human-only, consistently enforced. Don't dilute.

## Watch / revisit next cycle
- Once #1 lands, a `MOUNT-SUSPECT` verdict should trigger an automatic single re-run rather than waiting for the next 5-hour tick.
- The canon shorthash moved `e222c8f → 91ca5d6` (material 5-file steward change). Purely observed; record it in the next reconciliation snapshot.
- **Cross-system toil** (Notion mirror by hand; resonance/concurrence across Claude + ChatGPT + Dispatch with the D-0xx log maintained manually) — still a future orchestration pass, not yet in-repo toil.
- **Not automatable (by design):** independent verification of the k=3 selection proof is blocked on the private kernel ledger (Carrier Lemma) — a human/archive unlock, not toil.

## Guardrails
Every item above is **procedures-only**. Automation may compute, check, regenerate derived views, draft candidates, commit derived history, and summarize. It must never promote a conjecture to a theorem, admit or alter a ledger entry (A–E), change Ledger B, add to Ledger D, publish an interpretation, or merge a reconciliation. When in doubt, produce a draft and stop.
