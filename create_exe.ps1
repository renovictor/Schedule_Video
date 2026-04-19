# ============================================================
# Video Recorder - Create Single EXE File Script (PowerShell)
# ============================================================
# This script will create a single VideoRecorder.exe file
# ============================================================

Write-Host "`n" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Video Recorder - EXE Creation Script" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "`n"

# Check if we're in the right directory
if (-not (Test-Path "main.py")) {
    Write-Host "ERROR: main.py not found!" -ForegroundColor Red
    Write-Host "Please run this script from the Video_Record directory." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if PyInstaller is installed
Write-Host "Checking if PyInstaller is installed..." -ForegroundColor Yellow
$pyinstallerCheck = pip show pyinstaller 2>$null
if (-not $pyinstallerCheck) {
    Write-Host "PyInstaller not found. Installing..." -ForegroundColor Yellow
    pip install pyinstaller
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERROR: Failed to install PyInstaller" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

Write-Host "PyInstaller is installed." -ForegroundColor Green
Write-Host "`n"

# Check if icon exists
$iconExists = Test-Path "global_search_international.ico"
if (-not $iconExists) {
    Write-Host "WARNING: Icon file not found. Creating EXE without custom icon." -ForegroundColor Yellow
    Write-Host "`n"
    $command = "pyinstaller --onefile --windowed --name=VictorVideo main.py"
} else {
    Write-Host "Icon file found. Creating EXE with custom icon..." -ForegroundColor Green
    Write-Host "`n"
    # Read version from VERSION.py with better parsing
    $versionContent = Get-Content "VERSION.py" | Select-String 'VERSION\s*=\s*"([^"]+)"'
    if ($versionContent -match 'VERSION\s*=\s*"([^"]+)"') {
        $version = $matches[1]
        Write-Host "Creating EXE with version: $version" -ForegroundColor Cyan
        $command = "pyinstaller --onefile --windowed --icon=global_search_international.ico --name=VictorVideo_$version main.py"
    } else {
        Write-Host "Could not read version from VERSION.py, using default name" -ForegroundColor Yellow
        $version = "1.0.0"
        $command = "pyinstaller --onefile --windowed --icon=global_search_international.ico --name=VictorVideo_$version main.py"
    }
}

Write-Host "Running: $command" -ForegroundColor Cyan
Invoke-Expression $command

if ($LASTEXITCODE -ne 0) {
    Write-Host "`nERROR: Failed to create EXE file." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Success!
Write-Host "`n" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host "SUCCESS! Your EXE file has been created!" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host "`n"

$exePath = Join-Path (Get-Location) "dist\VictorVideo_$version.exe"
Write-Host "Location: $exePath" -ForegroundColor Cyan
Write-Host "`nNext steps:" -ForegroundColor Yellow
Write-Host "1. Navigate to the dist folder" -ForegroundColor White
Write-Host "2. Run VictorVideo_$version.exe to test it" -ForegroundColor White
Write-Host "3. Create a shortcut if desired" -ForegroundColor White
Write-Host "`n"

Write-Host "Files created:" -ForegroundColor Yellow
Write-Host "- dist\VictorVideo_$version.exe (Main executable)" -ForegroundColor White
Write-Host "- build\ (Build artifacts - can be deleted)" -ForegroundColor White
Write-Host "- VictorVideo.spec (Build spec file - can be deleted)" -ForegroundColor White
Write-Host "`n"

# Show file size
if (Test-Path $exePath) {
    $fileSize = (Get-Item $exePath).Length
    $fileSizeMB = [math]::Round($fileSize / 1MB, 2)
    Write-Host "EXE File Size: $fileSizeMB MB" -ForegroundColor Cyan
    Write-Host "`n"
}

Write-Host "Press Enter to open the dist folder..." -ForegroundColor Yellow
Read-Host

# Open the dist folder in Explorer
$distPath = Join-Path (Get-Location) "dist"
if (Test-Path $distPath) {
    Start-Process "explorer.exe" -ArgumentList $distPath
}
