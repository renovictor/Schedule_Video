# Installation & Verification Checklist

## Pre-Installation Requirements

- [ ] Windows 11 installed
- [ ] Python 3.8 or higher installed (verify: `python --version`)
- [ ] pip working (verify: `pip --version`)
- [ ] Internet connection (for downloads)
- [ ] 2 GB free disk space (for FFmpeg + test recordings)

## Step 1: Install Python Dependencies ✅

```bash
cd C:\Users\vhuang01\PycharmProjects\Video_Record
pip install -r requirements.txt
```

- [ ] Command completed without errors
- [ ] All packages installed:
  - [ ] PySide6
  - [ ] opencv-python
  - [ ] apscheduler
  - [ ] mss
  - [ ] numpy
  - [ ] sounddevice
  - [ ] soundfile
  - [ ] scipy

## Step 2: Download FFmpeg ⬇️

Visit: https://www.gyan.dev/ffmpeg/builds/

- [ ] Go to gyan.dev/ffmpeg/builds/
- [ ] Download "essentials_build.zip" (NOT full build)
- [ ] File size should be ~50 MB
- [ ] Save location noted: _________

## Step 3: Extract FFmpeg 📁

- [ ] Extract downloaded ZIP file
- [ ] Extracted folder named: `ffmpeg-YYYY-XX-XX-essentials_build`
- [ ] Inside folder, you should see: `bin`, `doc` folders
- [ ] Copy/Move to: `C:\ffmpeg` (create folder if needed)
- [ ] Verify path exists: `C:\ffmpeg\bin\ffmpeg.exe`

## Step 4: Add FFmpeg to PATH 🛣️

**Method 1: Via GUI (Recommended)**

- [ ] Right-click "This PC" → Properties
- [ ] Click "Advanced system settings"
- [ ] Click "Environment Variables" button
- [ ] Under "System variables", find "Path" → Edit
- [ ] Click "New"
- [ ] Add: `C:\ffmpeg\bin`
- [ ] Click OK × 3
- [ ] **Restart your computer**

**Method 2: Via Command Prompt (Admin)**

```bash
setx PATH "%PATH%;C:\ffmpeg\bin"
```

- [ ] Run Command Prompt as Administrator
- [ ] Paste above command
- [ ] Press Enter
- [ ] Restart computer

## Step 5: Verify FFmpeg Installation ✓

- [ ] Open new Command Prompt
- [ ] Type: `ffmpeg -version`
- [ ] Should see version information
- [ ] Example output:
  ```
  ffmpeg version N-110xxx
  built with gcc ...
  ```

| Check | Result | Status |
|-------|--------|--------|
| `ffmpeg -version` works | See version output | ✓ |
| Path contains bin folder | `C:\ffmpeg\bin` added | ✓ |
| ffmpeg.exe exists | File found | ✓ |

## Step 6: Create Output Folder 📂

- [ ] Open File Explorer
- [ ] Navigate to: `C:\Users\vhuang01\Videos\`
- [ ] If doesn't exist, create it
- [ ] Folder should be empty

```bash
# Or via Command Prompt:
mkdir C:\Users\vhuang01\Videos
```

## Step 7: Start the App 🚀

```bash
cd C:\Users\vhuang01\PycharmProjects\Video_Record
python main.py
```

- [ ] App window opens
- [ ] No error messages in console
- [ ] Window shows all controls:
  - [ ] Start Time picker
  - [ ] End Time picker
  - [ ] Output File input
  - [ ] Record Source dropdown
  - [ ] **Audio Source dropdown** ← NEW!
  - [ ] Schedule button
  - [ ] Start/Pause/Stop buttons
  - [ ] Status log area

## Step 8: Audio Device Detection 🎤

In the running app:

- [ ] Audio Source dropdown populated
- [ ] Shows at least one device (default)
- [ ] Device name visible (e.g., "Microphone")
- [ ] Can click and select different devices
- [ ] Default device pre-selected

**Audio Devices You Might See:**
- [ ] Microphone
- [ ] Headphones
- [ ] USB Device
- [ ] Stereo Mix (if enabled)
- [ ] Line In
- [ ] Other audio inputs

## Step 9: Do a Test Recording 🎬

1. **Configure**
   - [ ] Video Source: "Camera"
   - [ ] Audio Source: "Microphone" (or your device)
   - [ ] Output File: (use default or browse)

2. **Record**
   - [ ] Click "Start" button
   - [ ] Wait 5 seconds
   - [ ] Click "Stop" button

3. **Verify Status Log**
   - [ ] Shows: `[timestamp] Start Record: ...`
   - [ ] Shows: `[timestamp] Source: Camera | Audio: Microphone`
   - [ ] Shows: `[timestamp] Stop Record`

4. **Check File**
   - [ ] Open: `C:\Users\vhuang01\Videos\`
   - [ ] Find: `Video_YYYYMMDD_HHMMSS.mp4`
   - [ ] File size: > 100 KB (should have audio)

5. **Play Recording**
   - [ ] Right-click file → Open with Windows Media Player
   - [ ] Video appears ✓
   - [ ] Audio plays ✓
   - [ ] No errors ✓

## Step 10: Advanced Testing 🔧

**Test Screen Recording**
- [ ] Video Source: "Screen 1"
- [ ] Audio Source: "Microphone"
- [ ] Click Start
- [ ] Record 5 seconds
- [ ] Click Stop
- [ ] Verify file created

**Test Different Audio Devices**
- [ ] Plug in USB microphone (if available)
- [ ] Run app again
- [ ] Audio Source dropdown should show new device
- [ ] Select USB device
- [ ] Do test recording
- [ ] Verify audio from USB device

**Test Scheduled Recording**
- [ ] Set Start Time: 1 minute from now
- [ ] Set End Time: 2 minutes from now
- [ ] Click "Schedule Recording"
- [ ] Wait for start time
- [ ] App should automatically start recording
- [ ] Verify file created

## Troubleshooting Checklist 🔧

### "FFmpeg command not found"
- [ ] Verify `C:\ffmpeg\bin\ffmpeg.exe` exists
- [ ] Check PATH contains `C:\ffmpeg\bin`
- [ ] Try restarting computer
- [ ] Try: `C:\ffmpeg\bin\ffmpeg.exe -version` (full path)

### "No audio devices found"
- [ ] Check microphone is plugged in
- [ ] Check Windows Sound Settings
- [ ] Try different audio device
- [ ] Restart app
- [ ] Restart computer

### "Recording has no audio"
- [ ] Check volume levels (Windows Sound)
- [ ] Verify microphone not muted
- [ ] Select different audio device
- [ ] Check microphone works in Sound Settings

### "App won't start"
- [ ] Check Python installed: `python --version`
- [ ] Check dependencies: `pip list`
- [ ] Re-run: `pip install -r requirements.txt`
- [ ] Check console for error messages
- [ ] Try: `python -u main.py` (unbuffered output)

### "Video but no audio"
- [ ] Verify FFmpeg installed
- [ ] Check audio device selected in app
- [ ] Try different audio device
- [ ] Check: `C:\ffmpeg\bin\ffmpeg.exe -version`

## Success Verification ✅

### Minimum Requirements Met:
- [ ] App starts without errors
- [ ] Dropdown menus populated
- [ ] Audio device showing in dropdown
- [ ] Test recording created
- [ ] File plays with audio

### Full Setup Complete:
- [ ] All above PLUS:
- [ ] FFmpeg working (`ffmpeg -version`)
- [ ] Audio-video merge successful
- [ ] Multiple audio devices selectable
- [ ] Screen recording works
- [ ] Schedule recording works
- [ ] Status log shows all actions

## Final Verification

Run this command to verify everything:

```bash
echo Testing FFmpeg... && ffmpeg -version && echo Testing Python packages... && python -c "import PySide6, cv2, sounddevice; print('All packages OK')" && echo All systems ready!
```

Expected output:
```
Testing FFmpeg...
ffmpeg version N-...
...
Testing Python packages...
All packages OK
All systems ready!
```

- [ ] FFmpeg version shows
- [ ] Python packages imported successfully
- [ ] "All systems ready!" appears

## Setup Complete! ✨

If all checkboxes are checked, your system is ready to:
- ✅ Record video from camera
- ✅ Record video from screens
- ✅ Record audio from any input device
- ✅ Automatically merge audio + video
- ✅ Schedule recordings
- ✅ View real-time status

## Next Steps

1. Read: `QUICK_START.md` for operation instructions
2. Read: `README.md` for full feature documentation
3. Start recording!
4. Enjoy your videos! 🎥🎙️

## Support

If something isn't working:

1. **Check documentation:**
   - QUICK_START.md
   - README.md
   - FFMPEG_SETUP.md

2. **Check status log** in app for error messages

3. **Run this diagnostic:**
   ```bash
   python -c "
   import sounddevice as sd
   print('Audio devices:')
   for i, device in enumerate(sd.query_devices()):
       print(f'{i}: {device[\"name\"]} (inputs: {device[\"max_input_channels\"]})')
   print('\nDefault device:', sd.default.device[0])
   "
   ```

4. **Check console output** for error messages

---

**Date Completed:** _________

**Notes:** _________________________________


