# nq.ps1 - New LeetCode Question
# Usage: .\nq.ps1

Write-Host ""
Write-Host "  New LeetCode Question" -ForegroundColor Cyan
Write-Host ""

$lcNumber = Read-Host "  LC Number (e.g. 42)"

Write-Host ""
Write-Host "  Language:" -ForegroundColor Yellow
Write-Host "    1. Python (.py)"
Write-Host "    2. Java   (.java)"
Write-Host ""
$langChoice = Read-Host "  Pick (1 or 2)"

if ($langChoice -eq "2") {
    $ext = "java"
} else {
    $ext = "py"
}

Write-Host ""
Write-Host "  Topic:" -ForegroundColor Yellow
Write-Host "    1. Daily Streak"
Write-Host "    2. Arrays"
Write-Host "    3. Strings"
Write-Host "    4. Linked List"
Write-Host "    5. Stack and Queue"
Write-Host "    6. Trees"
Write-Host "    7. Graph"
Write-Host "    8. Dynamic Programming"
Write-Host "    9. Recursion and Backtracking"
Write-Host ""
$topicChoice = Read-Host "  Pick (1-9)"

$isDaily = $false
if ($topicChoice -eq "1") {
    $topicFolder = "dailystreak"
    $isDaily = $true
} elseif ($topicChoice -eq "2") {
    $topicFolder = "arrays"
} elseif ($topicChoice -eq "3") {
    $topicFolder = "strings"
} elseif ($topicChoice -eq "4") {
    $topicFolder = "linked-list"
} elseif ($topicChoice -eq "5") {
    $topicFolder = "stack-queue"
} elseif ($topicChoice -eq "6") {
    $topicFolder = "trees"
} elseif ($topicChoice -eq "7") {
    $topicFolder = "graph"
} elseif ($topicChoice -eq "8") {
    $topicFolder = "dynamic-programming"
} elseif ($topicChoice -eq "9") {
    $topicFolder = "recursion-backtracking"
} else {
    Write-Host "  Invalid choice." -ForegroundColor Red
    exit 1
}

$dateLabel = ""
if ($isDaily) {
    $day = (Get-Date).Day
    $month = (Get-Date).ToString("MMM")
    $year = (Get-Date).ToString("yy")
    if ($day -eq 1 -or $day -eq 21 -or $day -eq 31) {
        $suffix = "st"
    } elseif ($day -eq 2 -or $day -eq 22) {
        $suffix = "nd"
    } elseif ($day -eq 3 -or $day -eq 23) {
        $suffix = "rd"
    } else {
        $suffix = "th"
    }
    $dateLabel = "$day$suffix$month$year"
}

Write-Host ""
Write-Host "  Fetching from LeetCode..." -ForegroundColor Gray

$pythonScript = Join-Path $PSScriptRoot "fq.py"
$pyOutput = python $pythonScript $lcNumber $dateLabel 2>&1

$errorLine = $pyOutput | Where-Object { $_ -match "^ERROR:" } | Select-Object -First 1

if ($errorLine) {
    Write-Host "  Could not fetch: $errorLine" -ForegroundColor Yellow
    Write-Host "  Creating empty template instead." -ForegroundColor Yellow
    $title = "LC-$lcNumber"
    $markdown = "# LC-$lcNumber`n`n## Problem Statement`n`n<!-- Paste from LeetCode -->`n"
} else {
    $titleLine = $pyOutput | Where-Object { $_ -match "^TITLE:" } | Select-Object -First 1
    $title = $titleLine -replace "^TITLE:", ""
    $mdStartIdx = ($pyOutput | Select-String "^MARKDOWN_START").LineNumber
    $markdown = ($pyOutput | Select-Object -Skip $mdStartIdx) -join "`n"
    Write-Host "  Got: $title" -ForegroundColor Green
}

if ($isDaily) {
    $folderName = "LC-$lcNumber($dateLabel)"
} else {
    $folderName = "LC-$lcNumber"
}

$folderPath = Join-Path $PSScriptRoot (Join-Path $topicFolder $folderName)

if (Test-Path $folderPath) {
    Write-Host "  Already exists: $folderPath" -ForegroundColor Yellow
    exit 1
}

New-Item -ItemType Directory -Path $folderPath | Out-Null

if ($ext -eq "py") {
    $bfContent = "# Time Complexity: O() -`n# Space Complexity: O() -`n`nclass Solution:`n    def solve(self):`n        # TODO: brute force`n        pass`n"
    $optContent = "# Time Complexity: O() -`n# Space Complexity: O() -`n`nclass Solution:`n    def solve(self):`n        # TODO: optimal`n        pass`n"
} else {
    $bfContent = "// Time Complexity: O() -`n// Space Complexity: O() -`n`nclass Solution {`n    public void solve() {`n        // TODO: brute force`n    }`n}`n"
    $optContent = "// Time Complexity: O() -`n// Space Complexity: O() -`n`nclass Solution {`n    public void solve() {`n        // TODO: optimal`n    }`n}`n"
}

Set-Content -Path (Join-Path $folderPath "bruteforce.$ext") -Value $bfContent -Encoding UTF8
Set-Content -Path (Join-Path $folderPath "optimal.$ext") -Value $optContent -Encoding UTF8

if ($isDaily) {
    $mdName = "problem.md"
} else {
    $mdName = "$title.md"
}

Set-Content -Path (Join-Path $folderPath $mdName) -Value $markdown -Encoding UTF8

Write-Host ""
Write-Host "  Done! $topicFolder/$folderName" -ForegroundColor Green
Write-Host "    bruteforce.$ext"
Write-Host "    optimal.$ext"
Write-Host "    $mdName"
Write-Host ""

$open = Read-Host "  Open in VS Code? (y/n)"
if ($open -eq "y") {
    code $folderPath
}
