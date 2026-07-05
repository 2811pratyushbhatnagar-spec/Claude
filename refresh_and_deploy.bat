@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo   Refresh the derived board, then deploy it (private)
echo ============================================================
echo.
echo Regenerating status.html from status.json + priorities.md ...
python "Scripts\status_page.py"
if errorlevel 1 ( echo status_page.py failed. Aborting. & goto end )
echo.
echo Deploying ONLY the status page (no ledger files) via Wrangler ...
call "deploy_status.bat"
:end
echo.
endlocal
