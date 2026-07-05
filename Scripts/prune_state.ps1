# prune_state.ps1 -- keep only the newest N runner-state files (machine-side; the sandbox
# mount is create/append-only and cannot delete). Safe: touches only Scripts/.cycle_state.*.json.
param([int]$Keep = 12)
Set-Location "C:\Users\Bhatnagar\Desktop\New folder (2)\framework\Scripts"
$state = Get-ChildItem -File -Filter '.cycle_state.*.json' | Sort-Object LastWriteTime -Descending
if ($state.Count -le $Keep) { Write-Host "$($state.Count) state files; nothing to prune (keep $Keep)."; exit 0 }
$state | Select-Object -Skip $Keep | ForEach-Object { Remove-Item -Force $_.FullName; Write-Host "pruned $($_.Name)" }
Write-Host "kept newest $Keep."
