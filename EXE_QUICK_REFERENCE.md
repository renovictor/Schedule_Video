# Quick EXE Creation Reference

## 🚀 FASTEST WAY (One Command)

Open PowerShell in your project directory and run:

```powershell
pyinstaller --onefile --windowed --icon=global_search_international.ico --name=VideoRecorder main.py
```

**That's it!** Your EXE will be in `dist\VideoRecorder.exe`

---

## 📋 Using Helper Scripts (Even Faster)

### Option 1: Batch File (Easiest)
```powershell
.\create_exe.bat
```

### Option 2: PowerShell Script (More Features)
```powershell
powershell -ExecutionPolicy Bypass -File .\create_exe.ps1
```

---

## 🔧 STEP-BY-STEP Quick Guide

### Step 1: Install PyInstaller (One-time)
```powershell
pip install pyinstaller
```

### Step 2: Go to Project Directory
```powershell
cd C:\Users\vhuang01\PycharmProjects\Video_Record
```

### Step 3: Run PyInstaller
```powershell
pyinstaller --onefile --windowed --icon=global_search_international.ico --name=VideoRecorder main.py
```

### Step 4: Find Your EXE
- Location: `C:\Users\vhuang01\PycharmProjects\Video_Record\dist\VideoRecorder.exe`
- Double-click to run!

---

## 📦 What Each Flag Means

| Flag | Meaning |
|------|---------|
| `--onefile` | Creates ONE .exe file (instead of multiple files) |
| `--windowed` | No console window (use `--console` if you want debug output) |
| `--icon=...` | Use custom icon for the EXE |
| `--name=VideoRecorder` | Name the EXE file "VideoRecorder.exe" |
| `main.py` | Your Python entry point file |

---

## ⚡ Different Scenarios

### Basic (No Icon)
```powershell
pyinstaller --onefile --windowed main.py
```
Creates: `dist\main.exe`

### With Icon (Recommended)
```powershell
pyinstaller --onefile --windowed --icon=global_search_international.ico --name=VideoRecorder main.py
```
Creates: `dist\VideoRecorder.exe` with icon

### With Console (For Debugging)
```powershell
pyinstaller --onefile --console --icon=global_search_international.ico --name=VideoRecorder main.py
```
Creates: `dist\VideoRecorder.exe` with debug console window

### Custom Output Location
```powershell
pyinstaller --onefile --windowed --icon=global_search_international.ico --name=VideoRecorder --distpath="C:\Users\vhuang01\Videos\Output" main.py
```
Creates: `C:\Users\vhuang01\Videos\Output\VideoRecorder.exe`

---

## 🐛 Troubleshooting Quick Fixes

### Problem: "PyInstaller not found"
```powershell
pip install pyinstaller
```

### Problem: "Icon file not found"
Make sure `global_search_international.ico` is in your project directory

### Problem: "Failed to execute script"
Install all dependencies first:
```powershell
pip install -r requirements.txt
```

### Problem: "Audio/Camera not working in EXE"
Add hidden imports:
```powershell
pyinstaller --onefile --windowed --hidden-import=sounddevice --hidden-import=cv2 --icon=global_search_international.ico --name=VideoRecorder main.py
```

---

## 📊 File Locations After Creation

```
Video_Record/
├── dist/
│   └── VideoRecorder.exe  ← YOUR EXECUTABLE (Use this!)
├── build/                  ← Temporary files (can delete)
├── VideoRecorder.spec      ← Build config (can delete)
├── main.py
├── gui.py
└── ... (other files)
```

---

## ✅ Testing Your EXE

1. Navigate to `dist` folder
2. Double-click `VideoRecorder.exe`
3. Verify:
   - ✓ Window opens with icon
   - ✓ LED indicator appears
   - ✓ Buttons work
   - ✓ Recording works
   - ✓ Exit button closes app

---

## 🎁 Distribution

Your `VideoRecorder.exe` can now be:
- ✓ Shared via USB/email
- ✓ Installed on other computers (no Python needed!)
- ✓ Run from network drives
- ✓ Scheduled as a Windows task
- ✓ Made into an installer with NSIS

---

## 📈 File Size

Typical size: **100-150 MB**

This is normal because it includes:
- Python runtime
- All libraries (PySide6, OpenCV, etc.)
- Your application code
- Everything bundled into one file

---

## 💾 Clean Up (Optional)

After confirming the EXE works, you can delete:
```powershell
Remove-Item -Recurse -Force build
Remove-Item VideoRecorder.spec
```

Keep the `dist` folder and `VideoRecorder.exe`!

---

## 🔗 Quick Commands Reference

| Task | Command |
|------|---------|
| Create EXE | `pyinstaller --onefile --windowed --icon=global_search_international.ico --name=VideoRecorder main.py` |
| Check PyInstaller version | `pyinstaller --version` |
| Show help | `pyinstaller --help` |
| Clean build | `Remove-Item build, dist, *.spec -Recurse -Force` |
| Run helper script | `.\create_exe.ps1` |

---

**That's it! You now have a standalone executable!** 🎉

