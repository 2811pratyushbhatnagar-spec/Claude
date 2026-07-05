# setup_git.ps1 — run once on your machine (Windows PowerShell) to give the
# reversible-contact repo a real git history and clean up sandbox litter.
# The Cowork sandbox mounts this folder create/append-only, so it cannot run git
# or delete these leftovers itself — this has to run where the filesystem is normal.
$ErrorActionPreference = 'SilentlyContinue'
Set-Location "C:\Users\Bhatnagar\Desktop\New folder (2)\framework"

# 1) remove the broken .git skeleton + the moved-aside copy + scratch files
Remove-Item -Recurse -Force .git
Get-ChildItem -Directory -Filter '.git_broken_*' | Remove-Item -Recurse -Force
Remove-Item -Force err.txt, initerr.txt

# 2) initialize a real repo and snapshot current canon + the cycle machinery
$ErrorActionPreference = 'Stop'
git init
git symbolic-ref HEAD refs/heads/master 2>$null
git config user.email "2811pratyushbhatnagar@gmail.com"
git config user.name  "Pratyush Bhatnagar"
git add -A   # .gitignore already excludes status.html and Scripts/.cycle_state.*.json
git commit -m "Initial snapshot: reversible-contact canon + cycle machinery (validate clean)"
git log --oneline
Write-Host "`nDone. From now on cycle_check.py will report the git short-hash instead of the content hash."
