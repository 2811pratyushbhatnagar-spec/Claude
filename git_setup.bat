@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo   reversible-contact  -  git setup + cleanup
echo ============================================================
echo.
echo Cleaning broken/partial git state and scratch files...
if exist ".git" rmdir /s /q ".git"
for /d %%D in (.git_broken_*) do rmdir /s /q "%%D"
del /q err.txt initerr.txt "setup_git.ps1.ps1" "setup_git.ps1" 2>nul
echo.
where git >nul 2>nul
if errorlevel 1 (
  echo ERROR: git is not installed / not on PATH.
  echo Install "Git for Windows" from https://git-scm.com/download/win , then run this again.
  goto end
)
echo Initializing a real repo and committing the current canon...
git init
git symbolic-ref HEAD refs/heads/master
git config user.email "2811pratyushbhatnagar@gmail.com"
git config user.name  "Pratyush Bhatnagar"
git add -A
git commit -m "Initial snapshot: reversible-contact canon + cycle machinery (validate clean)"
echo.
echo === Result ===
git log --oneline
git status -s
echo.
echo Done.  cycle_check.py will now report the git short-hash.
:end
echo.
pause
endlocal
