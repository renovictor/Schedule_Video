@echo off
REM ============================================================
REM Video Recorder - Create Single EXE File Script
REM ============================================================
REM This script will create a single VideoRecorder.exe file
REM ============================================================

echo.
echo ============================================================
echo Video Recorder - EXE Creation Script
echo ============================================================
echo.

REM Check if we're in the right directory
if not exist main.py (
    echo ERROR: main.py not found!
    echo Please run this script from the Video_Record directory.
    pause
    exit /b 1
)

REM Check if PyInstaller is installed
echo Checking if PyInstaller is installed...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
    if errorlevel 1 (
        echo ERROR: Failed to install PyInstaller
        pause
        exit /b 1
    )
)

echo PyInstaller is installed.
echo.

REM Check if icon exists
if not exist global_search_international.ico (
    echo WARNING: Icon file not found. Creating EXE without custom icon.
    echo.
    pyinstaller --onefile --windowed --name=VictorVideo main.py
) else (
    echo Icon file found. Creating EXE with custom icon...
    echo.
    REM Read version from VERSION.py - more robust parsing
    setlocal enabledelayedexpansion
    for /f "tokens=*" %%i in ('type VERSION.py ^| findstr "VERSION = "') do (
        set VERSIONLINE=%%i
        REM Remove 'VERSION = "' and trailing '"'
        set VERSION=!VERSIONLINE:VERSION = "=!
        set VERSION=!VERSION:"=!
    )
    if not defined VERSION (
        set VERSION=1.0.0
    )
    echo Creating EXE with version: %VERSION%
    pyinstaller --onefile --windowed --icon=global_search_international.ico --name=VictorVideo_%VERSION% main.py
    endlocal
)

if errorlevel 1 (
    echo.
    echo ERROR: Failed to create EXE file.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo SUCCESS! Your EXE file has been created!
echo ============================================================
echo.
echo Location: %cd%\dist\VictorVideo_%VERSION%.exe
echo.
echo Next steps:
echo 1. Navigate to the dist folder
echo 2. Run VictorVideo_%VERSION%.exe to test it
echo 3. Create a shortcut if desired
echo.
echo Files created:
echo - dist\VictorVideo_%VERSION%.exe (Main executable)
echo - build\ (Build artifacts - can be deleted)
echo - VictorVideo.spec (Build spec file - can be deleted)
echo.
pause
