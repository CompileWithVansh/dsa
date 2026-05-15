# refetch.ps1 - Smart Re-fetch for Empty Problem Markdown Files
# Scans ALL folders, finds .md files that are empty or just placeholders,
# and re-fetches the problem content from LeetCode.
#
# DOES NOT modify nq.ps1 or fq.py — uses fq.py as-is.
#
# Usage:
#   .\refetch.ps1           — scan all, show what's empty, ask to fix
#   .\refetch.ps1 153       — re-fetch just LC-153 wherever it exists
#   .\refetch.ps1 --all     — re-fetch ALL empty ones without asking

Write-Host ""
Write-Host "  Smart Re-fetch (Empty Problem Files)" -ForegroundColor Cyan
Write-Host ""

$root = $PSScriptRoot
$pythonScript = Join-Path $root "fq.py"

$allFolders = @(
    "arrays", "strings", "linked-list", "stack-queue",
    "trees", "graph", "dynamic-programming",
    "recursion-backtracking", "dailystreak"
)

# ─────────────────────────────────────────────
#  HELPER: Check if a .md file has real content
# ─────────────────────────────────────────────
function Test-MdHasContent {
    param([string]$Path)
    if (-not (Test-Path $Path)) { return $false }
    $content = Get-Content $Path -Raw -ErrorAction SilentlyContinue
    if (-not $content) { return $false }
    # Consider it "empty" if less than 150 chars or missing "Problem Statement" with actual text after it
    if ($content.Length -lt 150) { return $false }
    if ($content -match "<!-- Paste from LeetCode -->") { return $false }
    if ($content -match "Problem Statement" -and $content.Length -gt 200) { return $true }
    return $false
}

# ─────────────────────────────────────────────
#  HELPER: Extract LC number from folder name
# ─────────────────────────────────────────────
function Get-LCNumber {
    param([string]$FolderName)
    if ($FolderName -match "^LC-(\d+)") {
        return $Matches[1]
    }
    return $null
}

# ─────────────────────────────────────────────
#  HELPER: Re-fetch a single problem
# ─────────────────────────────────────────────
function Invoke-Refetch {
    param(
        [string]$LCNumber,
        [string]$FolderPath,
        [string]$FolderName,
        [bool]$IsDaily
    )

    $dateLabel = ""
    if ($FolderName -match "\((.+)\)$") {
        $dateLabel = $Matches[1]
    }

    Write-Host "    Fetching LC-$LCNumber..." -ForegroundColor Gray -NoNewline

    $pyOutput = python $pythonScript $LCNumber $dateLabel 2>&1
    $errorLine = $pyOutput | Where-Object { $_ -match "^ERROR:" } | Select-Object -First 1

    if ($errorLine) {
        Write-Host " FAILED ($errorLine)" -ForegroundColor Red
        return $false
    }

    $titleLine = $pyOutput | Where-Object { $_ -match "^TITLE:" } | Select-Object -First 1
    $title = $titleLine -replace "^TITLE:", ""
    $mdStartIdx = ($pyOutput | Select-String "^MARKDOWN_START").LineNumber
    $markdown = ($pyOutput | Select-Object -Skip $mdStartIdx) -join "`n"

    # Determine .md filename
    if ($IsDaily) {
        $mdName = "problem.md"
    } else {
        # Check if there's already a .md file (use its name)
        $existingMd = Get-ChildItem -Path $FolderPath -Filter "*.md" -File | Select-Object -First 1
        if ($existingMd) {
            $mdName = $existingMd.Name
        } else {
            $mdName = "$title.md"
        }
    }

    Set-Content -Path (Join-Path $FolderPath $mdName) -Value $markdown -Encoding UTF8
    Write-Host " OK ($title)" -ForegroundColor Green
    return $true
}

# ─────────────────────────────────────────────
#  MAIN LOGIC
# ─────────────────────────────────────────────

$targetNumber = $null
$autoAll = $false

if ($args.Count -gt 0) {
    if ($args[0] -eq "--all") {
        $autoAll = $true
    } else {
        $targetNumber = $args[0]
    }
}

# Scan all folders for empty .md files
$emptyProblems = @()

foreach ($folder in $allFolders) {
    $folderPath = Join-Path $root $folder
    if (-not (Test-Path $folderPath)) { continue }

    $isDaily = ($folder -eq "dailystreak")

    Get-ChildItem -Path $folderPath -Directory | ForEach-Object {
        $lcNum = Get-LCNumber $_.Name
        if (-not $lcNum) { return }

        # If targeting a specific number, skip others
        if ($targetNumber -and $lcNum -ne $targetNumber) { return }

        # Check all .md files in this folder
        $mdFiles = Get-ChildItem -Path $_.FullName -Filter "*.md" -File
        $hasContent = $false

        if ($mdFiles.Count -eq 0) {
            # No .md file at all
            $hasContent = $false
        } else {
            foreach ($md in $mdFiles) {
                if (Test-MdHasContent $md.FullName) {
                    $hasContent = $true
                    break
                }
            }
        }

        if (-not $hasContent) {
            $emptyProblems += [PSCustomObject]@{
                LCNumber   = $lcNum
                Folder     = $folder
                FolderName = $_.Name
                FullPath   = $_.FullName
                IsDaily    = $isDaily
            }
        }
    }
}

if ($emptyProblems.Count -eq 0) {
    if ($targetNumber) {
        Write-Host "  LC-$targetNumber not found or already has content." -ForegroundColor Green
    } else {
        Write-Host "  All problem files have content. Nothing to re-fetch." -ForegroundColor Green
    }
    Write-Host ""
    exit 0
}

# Show what we found
Write-Host "  Found $($emptyProblems.Count) empty/placeholder problem file(s):" -ForegroundColor Yellow
Write-Host ""

foreach ($p in $emptyProblems) {
    Write-Host "    LC-$($p.LCNumber)  $($p.Folder)/$($p.FolderName)" -ForegroundColor White
}

Write-Host ""

# Ask or auto-proceed
if (-not $autoAll -and -not $targetNumber) {
    $proceed = Read-Host "  Re-fetch all of these? (y/n)"
    if ($proceed -ne "y") {
        Write-Host "  Cancelled." -ForegroundColor Gray
        Write-Host ""
        exit 0
    }
}

# Do the re-fetch
Write-Host ""
Write-Host "  Re-fetching..." -ForegroundColor Gray
Write-Host ""

$successCount = 0
$failCount = 0

foreach ($p in $emptyProblems) {
    $result = Invoke-Refetch -LCNumber $p.LCNumber -FolderPath $p.FullPath -FolderName $p.FolderName -IsDaily $p.IsDaily
    if ($result) { $successCount++ } else { $failCount++ }

    # Small delay to not hammer LeetCode API
    Start-Sleep -Milliseconds 500
}

Write-Host ""
Write-Host "  Done! $successCount fetched, $failCount failed." -ForegroundColor Green
Write-Host ""
