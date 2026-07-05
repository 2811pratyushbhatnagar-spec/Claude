# init_git.ps1 -- run ONCE on your machine (Windows PowerShell) from anywhere.
# Supersedes the mis-named root script setup_git.ps1.ps1. The Cowork sandbox mounts this
# folder create/append-only and cannot run git or delete the broken .git skeleton, so this
# has to run where the filesystem is normal.
$ErrorActionPreference = 'SilentlyContinue'
Set-Location "C:\Users\Bhatnagar\Desktop\New folder (2)\framework"

# 1) clear the broken git skeleton + sandbox litter + the mis-named script
Remove-Item -Recurse -Force .git
Get-ChildItem -Directory -Filter '.git_broken_*' | Remove-Item -Recurse -Force
Remove-Item -Force err.txt, initerr.txt, 'setup_git.ps1.ps1'

# 2) ensure .gitignore catches timestamped runner state + the non-canon audit dir
@'
# Derived views and runner state -- regenerated, not canon
status.html
Scripts/.cycle_state.json
Scripts/.cycle_state.*.json
.automation/
**/__pycache__/
*.pyc
'@ | Set-Content -Path .gitignore -Encoding utf8

# 3) initialize a real repo and snapshot canon + cycle machinery
$ErrorActionPreference = 'Stop'
git init
git symbolic-ref HEAD refs/heads/master 2>$null
git config user.email "2811pratyushbhatnagar@gmail.com"
git config user.name  "Pratyush Bhatnagar"
git add -A
git commit -m "Initial snapshot: reversible-contact canon + cycle machinery (validate clean)"
git log --oneline
Write-Host "`nDone. cycle_check.py will now report the git short-hash instead of the content hash."
