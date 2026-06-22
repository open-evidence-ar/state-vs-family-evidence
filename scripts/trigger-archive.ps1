<#
.SYNOPSIS
  Triggers archive.is snapshots for every source URL in 12-sources.md.
  Uses Invoke-WebRequest with the /submit/ endpoint. Waits 15 s between URLs to avoid rate-limiting.
  Exports results to scripts/archive-results.csv after each URL so partial progress survives interruption.

.NOTES
  - The archive.is /submit/ endpoint returns HTML containing the snapshot URL when complete.
  - This is an unofficial/unauthenticated endpoint. No CAPTCHAs handled. If blocked, wait and retry.
  - Run time: ~39 URLs × 15s = ~10 min minimum. Real time will be longer due to server-side archiving.
#>

$ErrorActionPreference = "Continue"
$ProgressPreference = "SilentlyContinue"

$sourceFile = Join-Path $PSScriptRoot "..\sections\12-sources.md"
$outputFile = Join-Path $PSScriptRoot "archive-results.csv"

if (-not (Test-Path $sourceFile -PathType Leaf)) {
    Write-Error "Source file not found: $sourceFile"
    exit 1
}

# Extract URLs from markdown table — matches the main URL, not the [archived] one
$content = Get-Content $sourceFile -Raw -Encoding UTF8
$pattern = '\]\((?<url>https?://[^\)]+)\)\s*\(\[archived\]'
$matchesList = [regex]::Matches($content, $pattern)

$urls = $matchesList | ForEach-Object { $_.Groups['url'].Value } | Sort-Object -Unique
$total = $urls.Count

Write-Host "Found $total unique source URLs to archive." -ForegroundColor Cyan

# Already completed (from previous runs)
$done = @{}
if (Test-Path $outputFile) {
    Import-Csv $outputFile | ForEach-Object { $done[$_.SourceURL] = $_.ArchiveURL }
    Write-Host "Resuming: $($done.Count) URLs already processed." -ForegroundColor Yellow
}

$results = @()
$i = 0

foreach ($url in $urls) {
    $i++
    if ($done.ContainsKey($url)) {
        Write-Host "[$i/$total] SKIP (already done): $url" -ForegroundColor DarkGray
        continue
    }

    $submitUrl = "https://archive.is/submit/?url=$([uri]::EscapeDataString($url))"
    Write-Host "[$i/$total] Submitting: $url" -ForegroundColor Green

    try {
        $response = Invoke-WebRequest -Uri $submitUrl -Method Get -TimeoutSec 60 -UseBasicParsing
        # archive.is redirects to the snapshot page on success
        $archiveUrl = $response.BaseResponse.ResponseUri.AbsoluteUri
        $status = "OK"
        Write-Host "         -> $archiveUrl" -ForegroundColor White
    } catch {
        $archiveUrl = ""
        $status = "ERROR: $_"
        Write-Host "         -> $_" -ForegroundColor Red
    }

    $results += [PSCustomObject]@{
        SourceURL  = $url
        ArchiveURL = $archiveUrl
        Status     = $status
        Timestamp  = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
    }
    # Write progress after each URL so interrupted runs can resume
    $results | Export-Csv $outputFile -NoTypeInformation -Encoding UTF8

    Start-Sleep -Seconds 15
}

Write-Host "`nDone. Results saved to $outputFile" -ForegroundColor Cyan
Write-Host "Total: $total URLs processed. Check $outputFile for archive URLs." -ForegroundColor Cyan