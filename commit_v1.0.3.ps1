# Commit script for Video Recorder v1.0.3
# This script commits the latest changes and creates a git tag

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Video Recorder v1.0.3 - Release Commit" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Add all changes
Write-Host "Adding files to git..." -ForegroundColor Yellow
git add .

# Show status
Write-Host ""
Write-Host "Current changes to be committed:" -ForegroundColor Yellow
git status

# Commit with version message
Write-Host ""
Write-Host "Committing changes..." -ForegroundColor Yellow
$commitMessage = @"
Release v1.0.3: Enhanced audio sync features and improved UI

- Increased Recording Status LED size 3x (60pt font)
- Added Audio Sync slider in Display tab (-5.0 to +5.0 seconds)
- Audio Sync slider with real-time seconds display
- Added Save Synced Video button for audio/video synchronization
- Moved Exit button outside tabs for accessibility from any tab
- FFmpeg integration for audio delay processing
- Support for both positive (delay) and negative (advance) audio offsets
- Improved audio sync workflow with visual feedback
- Updated VERSION.py to 1.0.3
- Updated README.md with new features
"@

git commit -m $commitMessage

# Create annotated tag
Write-Host ""
Write-Host "Creating git tag v1.0.3..." -ForegroundColor Yellow
git tag -a v1.0.3 -m "Release version 1.0.3 - Audio Sync Enhancement and UI Improvements"

# Show tags
Write-Host ""
Write-Host "Git tags:" -ForegroundColor Yellow
git tag -l --format='%(refname:short) - %(creatordate:short) - %(subject)'

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "Release v1.0.3 committed successfully!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Push to repository: git push origin master" -ForegroundColor White
Write-Host "2. Push tags: git push origin --tags" -ForegroundColor White
Write-Host "3. Create GitHub release from the tag" -ForegroundColor White
Write-Host ""

