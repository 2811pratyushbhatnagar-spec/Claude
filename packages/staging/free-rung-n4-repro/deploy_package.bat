@echo off
rem PRIVATE VERIFY deploy - one command, run by the steward only. Not publication.
rem Prereq (one-time): wrangler login   (same as the phone board)
cd /d "%~dp0"
wrangler pages deploy . --project-name reversible-contact-private-verify --branch main
echo.
echo Now LOCK it (one-time, same pattern as PHONE-SETUP.md): Cloudflare dashboard ^> Zero Trust ^> Access
echo   ^> Applications ^> Add ^> the reversible-contact-private-verify.pages.dev domain ^> policy: only your email.
