@echo off
REM Commit script for Video Recorder v1.0.3
REM This script commits the latest changes and creates a git tag

echo.
echo ============================================
echo Video Recorder v1.0.3 - Release Commit
echo ============================================
echo.

REM Add all changes
echo Adding files to git...
git add .

REM Show status
echo.
echo Current changes to be committed:
git status

REM Commit with version message
echo.
echo Committing changes...
git commit -m "Release v1.0.3: Enhanced audio sync features and improved UI

- Increased Recording Status LED size 3x (60pt font)
- Added Audio Sync slider in Display tab (-5.0 to +5.0 seconds)
- Audio Sync slider with real-time seconds display
- Added Save Synced Video button for audio/video synchronization
- Moved Exit button outside tabs for accessibility from any tab
- FFmpeg integration for audio delay processing
- Support for both positive (delay) and negative (advance) audio offsets
- Improved audio sync workflow with visual feedback
- Updated VERSION.py to 1.0.3
- Updated README.md with new features"

REM Create annotated tag
echo.
echo Creating git tag v1.0.3...
git tag -a v1.0.3 -m "Release version 1.0.3 - Audio Sync Enhancement and UI Improvements"

REM Show tags
echo.
echo Git tags:
git tag -l --format='%(refname:short) - %(creatordate:short) - %(subject)'

echo.
echo ============================================
echo Release v1.0.3 committed successfully!
echo ============================================
echo.
echo Next steps:
echo 1. Push to repository: git push origin master
echo 2. Push tags: git push origin --tags
echo 3. Create GitHub release from the tag
echo.
pause

