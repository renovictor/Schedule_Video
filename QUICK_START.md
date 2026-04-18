# Quick Start Guide

## First Time Setup (5 minutes)

### Step 1: Install Python Dependencies
```bash
cd C:\Users\vhuang01\PycharmProjects\Video_Record
pip install -r requirements.txt
```

### Step 2: Install FFmpeg

**Easiest Method - gyan.dev:**

1. Go to: https://www.gyan.dev/ffmpeg/builds/
2. Click "essentials_build.zip" (the smallest one)
3. Extract to: `C:\ffmpeg`
4. Right-click Start Menu → System → Advanced system settings
5. Environment Variables → System variables → New
   - Variable name: `Path`
   - Variable value: `C:\ffmpeg\bin`
6. Click OK three times, restart your computer

**Test It:**
- Open Command Prompt
- Type: `ffmpeg -version`
- Should show version information

### Step 3: Create Output Folder
```bash
mkdir C:\Users\vhuang01\Videos
```

### Step 4: Run the App
```bash
python main.py
```

## First Recording (2 minutes)

1. **Source Selection**
   - Video Source: Choose "Camera" or "Screen 1"
   - Audio Source: Choose "Microphone" (or your device)

2. **Output File**
   - Click Browse or manually enter path
   - Default: `C:\Users\vhuang01\Videos\Video_YYYYMMDD_HHMMSS.mp4`

3. **Start Recording**
   - Click "Start" button
   - Watch status log (bottom)
   - You'll see: `[timestamp] Start Record: C:\...`

4. **Stop Recording**
   - Click "Stop" button
   - App will:
     - Save video to file
     - Merge audio automatically
     - Show "Stop Record" in status log

5. **Find Your Video**
   - Open File Explorer
   - Go to: `C:\Users\vhuang01\Videos\`
   - Look for: `Video_YYYYMMDD_HHMMSS.mp4`

## Keyboard Controls

- None yet (use mouse/buttons)
- Planned for future version

## Common Tasks

### Record Just My Screen
1. Video Source: "Screen 1"
2. Audio Source: "Microphone" (or "Stereo Mix")
3. Click Start
4. Click Stop when done

### Record My Webcam with Microphone
1. Video Source: "Camera"
2. Audio Source: "Microphone"
3. Click Start
4. Click Stop when done

### Schedule a Recording
1. Set "Start Time" and "End Time"
2. Select video and audio sources
3. Set output file path
4. Click "Schedule Recording"
5. App will automatically start/stop

### Pause and Resume
1. Click "Start"
2. Click "Pause" (stops recording, video saved)
3. Click "Start" again (creates new file)
4. Click "Stop" when fully done

## Status Log Messages

| Message | Meaning | Action |
|---------|---------|--------|
| `Start Record: ...` | Recording started | Normal ✓ |
| `Source: Camera \| Audio: Microphone` | Sources selected | Normal ✓ |
| `Pause Record` | Paused | Resume with Start ✓ |
| `Stop Record` | Stopped | Video saved ✓ |

## Troubleshooting

### App won't start
```
- Ensure Python 3.8+ is installed
- Run: pip install -r requirements.txt
- Check for error messages in console
```

### No audio in recording
```
- Ensure microphone is plugged in
- Select correct device in "Audio Source"
- Check Windows Sound Settings
- Restart app if needed
```

### Can't find video file
```
- Default location: C:\Users\vhuang01\Videos\
- Check if folder exists (create if not)
- Look for Video_YYYYMMDD_HHMMSS.mp4
- Check browse dialog for custom paths
```

### FFmpeg errors
```
- Download from: https://www.gyan.dev/ffmpeg/builds/
- Extract to: C:\ffmpeg
- Add to PATH (see Step 2 above)
- Restart app
```

## Settings

Currently located in code - editable files:

**Default output folder**: `capture.py` line 14
```python
f"C:\\Users\\vhuang01\\Videos\\Video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
```

**Recording quality**: `capture.py` lines 126, 147
- Video: MP4V codec, 30 FPS
- Audio: AAC codec, 44.1 kHz, Stereo

**Window size**: `gui.py` line 18
```python
self.setGeometry(100, 100, 500, 500)
```

## Useful Keyboard Shortcuts (Windows)

| Shortcut | Action |
|----------|--------|
| `Win + E` | Open File Explorer |
| `Win + V` | Paste from clipboard |
| `Alt + Tab` | Switch windows while recording |
| `Print Screen` | Works with screen recording |

## Tips for Best Results

1. **Test before important recordings**
   - Do a 10-second test recording
   - Check audio and video work
   - Verify file was created

2. **Check microphone levels**
   - Windows Sound Settings
   - Ensure not muted
   - Not too quiet (< -3dB)

3. **Use external microphone for better audio**
   - Built-in: Lower quality
   - USB headset: Better quality
   - USB microphone: Best quality

4. **Close other apps while recording**
   - Less CPU interference
   - Better performance
   - Smaller file size

5. **Use SSD for recordings**
   - Faster write speeds
   - Smoother video
   - No dropped frames

## Storage Requirements

| Recording Duration | File Size |
|--------------------|-----------|
| 1 minute | 15-30 MB |
| 1 hour | 900 MB - 1.8 GB |
| 8 hours | 7.2 - 14.4 GB |

## Next Steps

1. Follow "First Time Setup"
2. Do a 1-minute test recording
3. Check the video file plays correctly
4. Try different audio sources if needed
5. Schedule a recording for later

## Support

- Check README.md for detailed docs
- See FFMPEG_SETUP.md for audio-video issues
- Check console output for error messages
- View status log in GUI for operation details

Happy Recording! 🎥🎙️

