@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo   Deploy status board to Cloudflare Pages (private)
echo ============================================================
echo.
echo Staging site\ (ONLY the status page is uploaded - no ledger files)...
if not exist site mkdir site
copy /y status.html site\index.html >nul
if errorlevel 1 (
  echo ERROR: status.html not found next to this file. Aborting.
  goto end
)
echo.
echo Deploying with Wrangler (first run downloads it via npx)...
call npx --yes wrangler pages deploy site --project-name reversible-contact-status
echo.
echo If a https://...pages.dev URL printed above, that is your phone link.
echo First time here? Open PHONE-SETUP.md for login + making it private.
:end
echo.
pause
endlocal
