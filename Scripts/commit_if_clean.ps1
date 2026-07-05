# commit_if_clean.ps1 -- run on your machine to snapshot canon whenever it changed AND
# validate passes clean. Procedures-only: committing derived history is not a governance
# decision; this never force-pushes or rewrites history. Wire it after a cycle, or schedule it.
Set-Location "C:\Users\Bhatnagar\Desktop\New folder (2)\framework"
python validate.py
if ($LASTEXITCODE -ne 0) { Write-Host "validate FLAGGED -- not committing. Resolve flags first."; exit 1 }
$changes = git status --porcelain
if (-not $changes) { Write-Host "No changes to commit."; exit 0 }
git add -A
git commit -m ("cycle snapshot {0} (validate clean)" -f (Get-Date -Format 'yyyy-MM-dd HH:mm'))
git log --oneline -1
