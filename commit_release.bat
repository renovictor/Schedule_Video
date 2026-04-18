@echo off
REM Video Recorder - Git Commit and Tag Script
REM This script commits all changes and creates a release tag

setlocal enabledelayedexpansion

echo.
echo ======================================
echo Video Recorder - Release 1.0.0
echo ======================================
echo.

cd /d "C:\Users\vhuang01\PycharmProjects\Video_Record"

REM Check if git is available
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or not in PATH
    echo Please install Git from https://git-scm.com/
    pause
    exit /b 1
)

echo Checking git status...
git status

echo.
echo Adding all changes to staging area...
git add -A

echo.
echo Current staged changes:
git diff --cached --name-only

echo.
echo Committing changes...
git commit -m "Release v1.0.0: Audio Source Selection + FFmpeg Integration

Features:
- Audio source dropdown menu with device selection
- Multi-device audio input support
- FFmpeg audio-video merging integration
- Enhanced status logging with audio device info
- Comprehensive documentation (8 files)
- Installation checklist and verification
- Complete troubleshooting guides

Files Added:
- VERSION.py - Version information
- PROJECT_SUMMARY.md - Project overview
- .gitignore - Git configuration
- 8 comprehensive documentation files

Code Updates:
- gui.py: Audio device dropdown and selection
- capture.py: Audio device support

Status: Production Ready"

if errorlevel 1 (
    echo.
    echo ERROR: Commit failed
    echo Please check your git configuration
    pause
    exit /b 1
)

echo.
echo Commit successful!

echo.
echo Creating release tag v1.0.0...
git tag -a v1.0.0 -m "Release v1.0.0: Video Recorder with Audio Source Selection

This is the first production release of the Video Recorder application.

Features:
- Video recording (Camera and multi-screen)
- Audio recording with device selection
- Professional MP4 output with audio-video merging
- Scheduling system
- Real-time status logging

See PROJECT_SUMMARY.md for complete details."

if errorlevel 1 (
    echo.
    echo ERROR: Tag creation failed
    echo Please check your git configuration
    pause
    exit /b 1
)

echo.
echo Tag created successfully!

echo.
echo ======================================
echo Release Information
echo ======================================
echo.
echo Version: v1.0.0
echo Date: April 18, 2026
echo Status: Production Ready
echo.

echo Showing commit log:
echo.
git log --oneline -5

echo.
echo Showing tags:
echo.
git tag -l -n1

echo.
echo ======================================
echo Setup Complete!
echo ======================================
echo.
echo Next steps:
echo 1. Push to remote: git push origin main
echo 2. Push tags: git push origin v1.0.0
echo 3. See PROJECT_SUMMARY.md for release notes
echo 4. Start recording: python main.py
echo.
echo ======================================
pause

