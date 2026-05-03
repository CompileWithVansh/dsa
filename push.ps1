# push.ps1 - Commit and push to GitHub
# Usage:
#   .\push.ps1
#   .\push.ps1 "LC-42 Trapping Rain Water solved"

Write-Host ""
Write-Host "  Push to GitHub" -ForegroundColor Cyan
Write-Host ""

Set-Location $PSScriptRoot

Write-Host "  Changed files:" -ForegroundColor Gray
git status --short
Write-Host ""

if ($args[0]) {
    $message = $args[0]
} else {
    $message = Read-Host "  Commit message"
}

if ([string]::IsNullOrWhiteSpace($message)) {
    Write-Host "  Commit message cannot be empty." -ForegroundColor Red
    exit 1
}

git add .
git commit -m $message
git push

Write-Host ""
Write-Host "  Done! Pushed to GitHub." -ForegroundColor Green
Write-Host ""
