@echo off
rem Stage-0 gate: deterministic, zero model tokens on no-op (the common case).
C:\Windows\py.exe -3 "C:\Users\Bhatnagar\Desktop\code\framework\Scripts\stage0_gate.py" >> "C:\Users\Bhatnagar\Desktop\code\framework\.automation\gate_log.txt" 2>&1
set GATE_RC=%ERRORLEVEL%

rem Refresh the phone board (also deterministic - pure python view over status.json/priorities).
C:\Windows\py.exe -3 "C:\Users\Bhatnagar\Desktop\code\framework\Scripts\status_page.py" --out "C:\Users\Bhatnagar\Desktop\code\framework\status.html" >> "C:\Users\Bhatnagar\Desktop\code\framework\.automation\gate_log.txt" 2>&1
copy /Y "C:\Users\Bhatnagar\Desktop\code\framework\status.html" "C:\Users\Bhatnagar\Desktop\New folder (2)\framework\status.html" >nul 2>&1

rem Commit-on-clean cadence (audit 2026-07-05-b item 4): commit_if_clean.ps1 self-guards
rem (worker_guard -> validate -> changed-check), so this call commits ONLY when validate
rem passes clean AND canon changed; commits derived history only, never force-pushes.
rem Wired here (unpinned wrapper) rather than in cycle_check.py, which is hash-pinned
rem constitutional core post-freeze (editing it = Class-A + human re-pin).
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\Bhatnagar\Desktop\code\framework\Scripts\commit_if_clean.ps1" >> "C:\Users\Bhatnagar\Desktop\code\framework\.automation\gate_log.txt" 2>&1

rem OPTIONAL escalation auto-spawn (disabled by default; enable only if the steward wants
rem unattended model reasoning when the gate OPENS - it seeds the session with the brief ONLY):
rem if %GATE_RC%==10 claude -p "Read C:\Users\Bhatnagar\Desktop\code\framework\.automation\escalation_brief.md and act on the delta only, honoring WORKER-CONTRACT.md."
exit /b %GATE_RC%
