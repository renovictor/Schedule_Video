# Video Playback Troubleshooting Guide

## Overview
This guide helps troubleshoot video and audio playback issues in the Display tab.

## Common Issues and Solutions

### 1. **Video Not Displaying**

**Symptoms:**
- Black screen when clicking Play
- Video widget stays empty
- No error message

**Solutions:**

#### Step 1: Check File Format
- Ensure the video file is one of the supported formats: MP4, AVI, MOV, MKV
- Try a different video file to verify

#### Step 2: Check FFmpeg Installation
FFmpeg is required by PySide6 for multimedia support.

**For Windows 11:**

Option A: **Download from gyan.dev (Recommended)**
1. Visit: https://www.gyan.dev/ffmpeg/builds/
2. Download the "full" version (includes all codecs)
3. Extract to `C:\ffmpeg`
4. Add to system PATH:
   - Open Environment Variables
   - Add `C:\ffmpeg\bin` to PATH
   - Restart your application

Option B: **Download from btbn**
1. Visit: https://github.com/BtbN/FFmpeg-Builds/releases
2. Download the Windows build
3. Extract and add to PATH as above

#### Step 3: Verify FFmpeg Installation
Run in PowerShell:
```powershell
ffmpeg -version
```

If not recognized, restart your IDE and Python environment.

### 2. **No Audio During Playback**

**Symptoms:**
- Video plays but no sound
- Volume slider doesn't seem to work
- Audio devices visible but not working

**Solutions:**

#### Step 1: Check Audio Device
1. Go to Recording tab
2. Check "Audio Source" dropdown
3. Verify your audio device is selected

#### Step 2: Check System Volume
1. Ensure Windows system volume is not muted
2. Check audio output device is connected
3. Test audio with Windows Media Player first

#### Step 3: Reinstall Audio Libraries
Run in PowerShell:
```powershell
pip install --upgrade pyaudio
pip install --upgrade sounddevice
```

#### Step 4: Verify Audio Codec
Some audio codecs may not be supported. FFmpeg includes most common codecs.

### 3. **Playback Stuttering or Freezing**

**Symptoms:**
- Video playback is jerky
- Audio out of sync
- Application becomes unresponsive

**Solutions:**

#### Step 1: Close Other Applications
- Close web browsers
- Close media players
- Close background processes

#### Step 2: Check System Resources
- Monitor CPU/Memory usage
- Disable hardware acceleration if needed
- Try smaller video file first

#### Step 3: Update Qt Multimedia Backend
```powershell
pip install --upgrade PySide6
```

### 4. **File Not Found Error**

**Symptoms:**
- Error message when clicking Play
- "Video file not found"

**Solutions:**

1. Verify file path is correct
2. Check file still exists
3. Use full absolute path (not relative)
4. Ensure no special characters in filename

## Testing Your Setup

### Quick Test Steps:

1. **Create a Test Video** (if you don't have one):
   - Open the Recording tab
   - Click "Start" to record a short video
   - Click "Stop" after 10 seconds
   - Note the file path

2. **Play Back the Test Video**:
   - Go to Display tab
   - Click "Browse..." and select your test video
   - Click "Play"
   - Verify video appears and audio plays

3. **Test Controls**:
   - Pause button should freeze video
   - Position slider should allow seeking
   - Volume slider should control audio level
   - Status label should show "Playing ▶"

## Dependencies

Ensure all packages are installed:
```powershell
pip install -r requirements.txt
```

Required packages:
- **PySide6**: GUI framework with multimedia support
- **pyaudio**: Audio input/output
- **sounddevice**: Audio device management
- **FFmpeg**: System-level codec support (must be installed separately)

## Advanced Troubleshooting

### Enable Debug Output

Edit `gui.py` and add at the top:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

This will show detailed error messages in the console.

### Check Media Player Status

The status label shows:
- **Status: Ready** - App ready to play
- **Status: Loading...** - Loading video file
- **Status: Playing ▶** - Video is playing
- **Status: Paused ⏸** - Video is paused
- **Status: Stopped ⏹** - Video is stopped
- **Status: Error** - An error occurred

### Performance Tips

1. Use MP4 format for best compatibility
2. Lower resolution videos play smoother
3. Ensure good internet if playing network files
4. Close unnecessary applications
5. Update graphics drivers

## Getting Help

If issues persist:

1. Check the console for error messages
2. Verify FFmpeg is installed: `ffmpeg -version`
3. Test with a different video file
4. Reinstall PySide6: `pip install --force-reinstall PySide6`
5. Restart your computer

## Performance Optimization

To improve video/audio sync and playback quality:

1. **Video Brightness Slider**: Adjusts visual appearance (GPU accelerated)
2. **Audio Volume Slider**: Controls playback volume (0-100%)
3. **Position Slider**: Seek to any point in the video

The GUI provides real-time feedback through the status label and time display.

