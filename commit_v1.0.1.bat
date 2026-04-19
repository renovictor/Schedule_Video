@echo off
REM ============================================================
REM VictorVideo v1.0.1 - Commit and Tag Script
REM ============================================================
REM This script commits all changes and creates a release tag
REM ============================================================

echo.
echo ============================================================
echo VictorVideo v1.0.1 - Commit & Tag Script
echo ============================================================
echo.

cd /d C:\Users\vhuang01\PycharmProjects\Video_Record

REM Check if git is initialized
if not exist .git (
    echo Initializing git repository...
    git init
    echo Git repository initialized.
    echo.
)

REM Show current status
echo Current Git Status:
echo.
git status
echo.

REM Add all changes
echo Adding all changes to staging area...
git add -A
echo Changes added.
echo.

REM Commit with descriptive message
echo Committing with message...
git commit -m "Release v1.0.1: Fixed audio/video sync, volume boost, EXE naming, and added All of Above audio feature"
echo Changes committed.
echo.

REM Create annotated tag
echo Creating release tag v1.0.1...
git tag -a v1.0.1 -m "VictorVideo v1.0.1 Release%nDate: April 19, 2026%nFeatures:%n- Audio/Video Synchronization Fix%n- 2x Volume Boost with Normalization%n- All of Above Audio Source%n- Fresh Button for Schedule%n- EXE Naming with Version%n- Enhanced Logging and Error Handling"
echo Tag created: v1.0.1
echo.

REM Show tag info
echo.
echo Tag Information:
git show v1.0.1
echo.

REM Show recent commits
echo.
echo Recent Commits:
git log --oneline -10
echo.

echo ============================================================
echo SUCCESS! v1.0.1 tagged and ready.
echo ============================================================
echo.
echo Next steps:
echo 1. Push to remote: git push origin main
echo 2. Push tags: git push origin v1.0.1
echo.
pause

