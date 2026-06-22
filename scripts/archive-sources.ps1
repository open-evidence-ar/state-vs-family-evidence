# Archive source URLs via archive.is API
# Usage: .\scripts\archive-sources.ps1
# Submits all source URLs to archive.is and saves the archive snapshot URLs

$ErrorActionPreference = "Stop"
$sourcesFile = "sections\12-sources.md"
$archiveData = "_data\archive-links.yml"

Write-Host "=== Archive Source URLs Script ===" -ForegroundColor Cyan
Write-Host ""

# Read sources file
$sourcesContent = Get-Content $sourcesFile -Raw
$urls = [regex]::Matches($sourcesContent, '\((https?://[^\)]+)\)') | ForEach-Object { $_.Groups[1].Value }

Write-Host "Found $($urls.Count) URLs to archive" -ForegroundColor Yellow

# Initialize archive data
$archiveLinks = @{}

foreach ($url in $urls) {
    Write-Host "Archiving: $url" -ForegroundColor Gray
    
    try {
        # Submit to archive.is via POST API
        $body = @{ url = $url } | ConvertTo-Json
        $response = Invoke-RestMethod -Uri "https://archive.is/submit" `
            -Method Post `
            -Body $body `
            -ContentType "application/json" `
            -MaximumRedirection 5
        
        # Extract archive URL from response
        if ($response -match "archive\.(is|today)/") {
            $archiveUrl = $response
            $archiveLinks[$url] = $archiveUrl
            Write-Host "  -> $archiveUrl" -ForegroundColor Green
        } else {
            Write-Host "  -> Unexpected response: $response" -ForegroundColor Red
        }
        
        # Rate limiting - wait between requests
        Start-Sleep -Seconds 3
        
    } catch {
        Write-Host "  -> Error: $($_.Exception.Message)" -ForegroundColor Red
        
        # Try alternative method using GET request
        try {
            $saveUrl = "https://archive.is/save/$url"
            $response = Invoke-WebRequest -Uri $saveUrl -MaximumRedirection 5
            $finalUrl = $response.BaseResponse.ResponseUri.AbsoluteUri
            
            if ($finalUrl -match "archive\.(is|today)/[0-9]+") {
                $archiveLinks[$url] = $finalUrl
                Write-Host "  -> $finalUrl (via GET)" -ForegroundColor Green
            }
        } catch {
            Write-Host "  -> Failed both methods" -ForegroundColor Red
        }
        
        Start-Sleep -Seconds 2
    }
}

# Save archive links to YAML
if ($archiveLinks.Count -gt 0) {
    Write-Host ""
    Write-Host "Saving archive links to $archiveData..." -ForegroundColor Cyan
    
    $yamlContent = "# Archive links for source URLs`n"
    foreach ($url in $archiveLinks.Keys) {
        $archiveUrl = $archiveLinks[$url]
        $yamlContent += "${url}: ${archiveUrl}`n"
    }
    
    Set-Content -Path $archiveData -Value $yamlContent
    Write-Host "Saved $($archiveLinks.Count) archive links" -ForegroundColor Green
    
    # Update sources.md with archived links
    Write-Host ""
    Write-Host "Updating $sourcesFile with archive links..." -ForegroundColor Cyan
    
    $updatedContent = $sourcesContent
    
    foreach ($url in $archiveLinks.Keys) {
        $archiveUrl = $archiveLinks[$url]
        # Add (archived) link after each source URL
        $updatedContent = $updatedContent.Replace(
            "($url)",
            "($url) ([archived]($archiveUrl))"
        )
    }
    
    Set-Content -Path $sourcesFile -Value $updatedContent
    Write-Host "Updated $sourcesFile" -ForegroundColor Green
    
} else {
    Write-Host "No archive links saved" -ForegroundColor Red
}

Write-Host ""
Write-Host "Archive complete!" -ForegroundColor Cyan
Write-Host "Archive links saved to: $archiveData" -ForegroundColor Gray
Write-Host "Sources file updated: $sourcesFile" -ForegroundColor Gray