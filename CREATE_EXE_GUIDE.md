# How to Create a Single EXE File for Video Recorder

This guide will help you convert your Python Video Recorder application into a single standalone `.exe` file that can be distributed and run on Windows without requiring Python to be installed.

## Step 1: Install PyInstaller

PyInstaller is the recommended tool for converting Python applications to executable files.

### Option A: Using PowerShell (Recommended)
Open PowerShell and run:
```powershell
pip install pyinstaller
```

### Option B: Verify Installation
Check if PyInstaller is installed:
```powershell
pyinstaller --version
```

## Step 2: Prepare Your Project

Before creating the EXE, ensure all your files are in the project directory:

```
C:\Users\vhuang01\PycharmProjects\Video_Record\
├── gui.py                          (Main GUI file)
├── main.py                         (Entry point)
├── capture.py                      (Video capture module)
├── scheduler.py                    (Scheduling module)
├── global_search_international.ico (Icon file) ✅ IMPORTANT
├── requirements.txt                (Dependencies)
└── VERSION.py                      (Version file)
```

**Important:** Make sure `global_search_international.ico` is in the project root directory.

## Step 3: Install Required Dependencies

Before creating the EXE, install all required packages:

```powershell
cd C:\Users\vhuang01\PycharmProjects\Video_Record
pip install -r requirements.txt
```

Your `requirements.txt` should contain:
```
PySide6>=6.0.0
pyaudio>=0.2.11
sounddevice>=0.4.5
apscheduler>=3.10.0
opencv-python>=4.8.0
numpy>=1.24.0
```

## Step 4: Create the Single EXE File

### Method 1: Simple Command (Basic)
```powershell
cd C:\Users\vhuang01\PycharmProjects\Video_Record
pyinstaller --onefile --windowed main.py
```

**Explanation of flags:**
- `--onefile` : Creates a single executable file (instead of multiple files)
- `--windowed` : No console window will appear when running (use `--console` if you want to see debug output)
- `main.py` : Entry point of your application

### Method 2: Advanced Command (Recommended) - With Icon and More Options
```powershell
cd C:\Users\vhuang01\PycharmProjects\Video_Record
pyinstaller --onefile --windowed --icon=global_search_international.ico --name=VideoRecorder_1.0.0 --distpath="C:\Users\vhuang01\Videos\VideoRecorder" main.py
```

**Additional flags:**
- `--icon=global_search_international.ico` : Uses your app icon for the EXE
- `--name=VideoRecorder_1.0.0` : Names the output file "VideoRecorder_1.0.0.exe" instead of "main.exe"
- `--distpath="C:\Users\vhuang01\Videos\VideoRecorder"` : Output location for the final EXE

### Method 3: Using a Configuration File (Advanced)

Create a file named `VideoRecorder.spec` with advanced settings:

```python
# -*- mode: python ; coding: utf-8 -*-
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('global_search_international.ico', '.')],
    hiddenimports=['sounddevice', 'cv2', 'apscheduler'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='VideoRecorder',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='global_search_international.ico',
)
```

Then run:
```powershell
pyinstaller VideoRecorder.spec
```

## Step 5: Locate Your EXE File

After running PyInstaller, your single EXE file will be located in:

```
C:\Users\vhuang01\PycharmProjects\Video_Record\dist\VideoRecorder.exe
```

Or if you specified a custom `--distpath`:
```
C:\Users\vhuang01\Videos\VideoRecorder\VideoRecorder.exe
```

## Step 6: Test the EXE

1. Navigate to the `dist` folder
2. Double-click `VideoRecorder.exe`
3. Verify that:
   - Window opens with icon in title bar and taskbar
   - LED indicator appears
   - All buttons work (Start, Pause, Stop, Exit)
   - Status messages appear in the text area
   - Audio and video recording works
   - Exit button closes the app gracefully

## Common Issues and Solutions

### Issue 1: "Failed to execute script" Error
**Solution:** Make sure all dependencies in `requirements.txt` are installed:
```powershell
pip install -r requirements.txt --upgrade
```

### Issue 2: Missing Icon in EXE
**Solution:** Verify the icon file path and use the absolute path:
```powershell
pyinstaller --onefile --windowed --icon="C:\Users\vhuang01\PycharmProjects\Video_Record\global_search_international.ico" main.py
```

### Issue 3: Audio/Camera Not Working in EXE
**Solution:** Add hidden imports:
```powershell
pyinstaller --onefile --windowed --hidden-import=sounddevice --hidden-import=cv2 main.py
```

### Issue 4: EXE Takes Long Time to Start
**Solution:** This is normal for PyInstaller single-file executables. First launch can take 3-5 seconds as it extracts dependencies to a temporary folder.

### Issue 5: Windows Defender Warning
**Solution:** This is common for unsigned executables. You can either:
- Ignore the warning (it's safe - it's your code)
- Sign the executable with a code signing certificate
- Add an exception in Windows Defender

## Step 7: Clean Up (Optional)

After creating the EXE, you can delete the build folders to save space:

```powershell
cd C:\Users\vhuang01\PycharmProjects\Video_Record
Remove-Item -Recurse -Force build
Remove-Item -Recurse -Force dist (after backing up your EXE)
Remove-Item VideoRecorder.spec (if you used one)
```

## Distribution

Your final `VideoRecorder.exe` can now be:
- Shared with others via USB drive
- Installed on computers without Python
- Added to Start Menu for quick access
- Scheduled to run automatically

### Create a Desktop Shortcut (Optional)

Right-click on `VideoRecorder.exe` and select:
- Send to → Desktop (create shortcut)
- Or manually create a shortcut and customize the icon

## Full Command Line Examples

### Minimal (Most Basic)
```powershell
pyinstaller --onefile main.py
```

### Recommended for Your App
```powershell
pyinstaller --onefile --windowed --icon=global_search_international.ico --name=VideoRecorder main.py
```

### Complete with Output Path
```powershell
pyinstaller --onefile --windowed --icon=global_search_international.ico --name=VideoRecorder --distpath="C:\Users\vhuang01\Videos\VideoRecorder" --specpath="build" main.py
```

## Checking File Size

After creation, check your EXE size:
```powershell
$file = Get-Item C:\Users\vhuang01\PycharmProjects\Video_Record\dist\VideoRecorder.exe
Write-Host "File size: $([math]::Round($file.Length/1MB, 2)) MB"
```

Typical size: 100-150 MB (single-file executables are usually larger due to bundled libraries)

## Summary Checklist

- [ ] PyInstaller installed (`pip install pyinstaller`)
- [ ] All dependencies installed from `requirements.txt`
- [ ] Icon file (`global_search_international.ico`) in project root
- [ ] Run PyInstaller command from project directory
- [ ] Check `dist/VideoRecorder.exe` exists
- [ ] Test EXE works correctly
- [ ] Create shortcut if desired
- [ ] Distribute to other computers

## Troubleshooting Command

If you encounter issues, run this diagnostic command:
```powershell
pyinstaller --onefile --windowed --debug=imports main.py
```

This will show you what modules are being loaded, helping identify missing imports.

---

**Need Help?**
- PyInstaller Documentation: https://pyinstaller.org/
- PySide6 Deployment: https://doc.qt.io/qtforpython/
- Video Recorder Project: Check main.py for entry point
