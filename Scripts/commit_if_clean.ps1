# commit_if_clean.ps1 -- run on your machine to snapshot canon whenever it changed AND
# validate passes clean. Procedures-only: committing derived history is not a governance
# decision; this never force-pushes or rewrites history. Wire it after a cycle, or schedule it.
# 2026-07 (audit 2026-07-05-b item 4): repo path parametrized. Default = CANON
# (Desktop\code\framework, per the 2026-07-05 two-repo unification row); the previous
# hardcoded path pointed at the mounted MIRROR, so the cadence would have snapshotted
# the wrong repo. Pass -RepoPath to override (e.g. for the mirror).
param([string]$RepoPath = "C:\Users\Bhatnagar\Desktop\code\framework")
Set-Location $RepoPath
python Scripts/worker_guard.py
if ($LASTEXITCODE -ne 0) { Write-Host "worker_guard VIOLATION (WORKER-CONTRACT.md) -- not committing. Report instead."; exit 1 }
python validate.py
if ($LASTEXITCODE -ne 0) { Write-Host "validate FLAGGED -- not committing. Resolve flags first."; exit 1 }
$changes = git status --porcelain
if (-not $changes) { Write-Host "No changes to commit."; exit 0 }
git add -A
git commit -m ("cycle snapshot {0} (validate clean)" -f (Get-Date -Format 'yyyy-MM-dd HH:mm'))
git log --oneline -1
