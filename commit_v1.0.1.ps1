#!/usr/bin/env powershell
# ============================================================
# VictorVideo v1.0.1 - Commit and Tag Script (PowerShell)
# ============================================================
# This script commits all changes and creates a release tag
# ============================================================

Write-Host "`n" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "VictorVideo v1.0.1 - Commit & Tag Script" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "`n"

Set-Location C:\Users\vhuang01\PycharmProjects\Video_Record

# Check if git is initialized
if (-not (Test-Path ".git")) {
    Write-Host "Initializing git repository..." -ForegroundColor Yellow
    git init
    Write-Host "Git repository initialized." -ForegroundColor Green
    Write-Host "`n"
}

# Show current status
Write-Host "Current Git Status:" -ForegroundColor Yellow
Write-Host "`n"
git status
Write-Host "`n"

# Add all changes
Write-Host "Adding all changes to staging area..." -ForegroundColor Yellow
git add -A
Write-Host "Changes added." -ForegroundColor Green
Write-Host "`n"

# Commit with descriptive message
Write-Host "Committing with message..." -ForegroundColor Yellow
$commitMessage = @"
Release v1.0.1: Fixed audio/video sync, volume boost, EXE naming, and added All of Above audio feature

Changes:
- Fixed audio/video synchronization using threading.Event
- Added 2x volume boost with audio normalization
- Fixed audio-only recording issue
- Added 'All of Above' audio source for multi-device recording
- Fixed EXE filename (VictorVideo_1.0.1.exe)
- Added Fresh button for quick time updates
- Enhanced status logging and error handling
- Improved schedule recording validation
"@

git commit -m $commitMessage
Write-Host "Changes committed." -ForegroundColor Green
Write-Host "`n"

# Create annotated tag
Write-Host "Creating release tag v1.0.1..." -ForegroundColor Yellow
$tagMessage = @"
VictorVideo v1.0.1 Release
Date: April 19, 2026
Author: VictorVideo Team

Features:
- Audio/Video Synchronization Fix (Perfect lip-sync)
- 2x Volume Boost with Normalization (Louder audio)
- All of Above Audio Source (Multi-device recording)
- Fresh Button for Schedule (Quick time updates)
- EXE Naming with Version (VictorVideo_1.0.1.exe)
- Enhanced Logging and Error Handling

Bug Fixes:
- Fixed video-only recording issue
- Fixed missing version number in EXE
- Fixed schedule recording timing
- Improved thread synchronization
"@

git tag -a v1.0.1 -m $tagMessage
Write-Host "Tag created: v1.0.1" -ForegroundColor Green
Write-Host "`n"

# Show tag info
Write-Host "`n"
Write-Host "Tag Information:" -ForegroundColor Yellow
git show v1.0.1
Write-Host "`n"

# Show recent commits
Write-Host "`n"
Write-Host "Recent Commits:" -ForegroundColor Yellow
git log --oneline -10
Write-Host "`n"

Write-Host "============================================================" -ForegroundColor Green
Write-Host "SUCCESS! v1.0.1 tagged and ready." -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host "`n"

Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Push to remote: git push origin main" -ForegroundColor White
Write-Host "2. Push tags: git push origin v1.0.1" -ForegroundColor White
Write-Host "`n"

# Ask to push
$response = Read-Host "Would you like to push now? (y/n)"
if ($response -eq 'y' -or $response -eq 'yes') {
    Write-Host "`nPushing to remote..." -ForegroundColor Yellow
    git push origin main
    git push origin v1.0.1
    Write-Host "Push complete!" -ForegroundColor Green
}

Write-Host "`n"

