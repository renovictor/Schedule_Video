# Video Recorder Scheduler

A professional Windows 11 video recording application with audio capture, scheduling, and multi-source support.

## Features

✅ **Video Recording**
- Camera recording (webcam)
- Screen recording (multiple monitors: Screen 1, 2, 3)
- MP4 output format

✅ **Audio Recording**
- Simultaneous audio capture from any input device
- Dropdown menu to select audio source (microphone, line-in, etc.)
- Automatic audio-video merging
- Stereo recording at 44.1 kHz

✅ **Scheduling**
- Schedule recordings for specific date/time ranges
- Automated start/stop

✅ **GUI Controls**
- Start/Pause/Stop buttons with intelligent state management
- File browser for output location
- Real-time status log with timestamps
- All recordings save to `C:\Users\vhuang01\Videos\` by default

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install FFmpeg (Required for audio-video merging)

**Recommended: gyan.dev (Easiest)**
1. Visit https://www.gyan.dev/ffmpeg/builds/
2. Download the **essentials** build (ZIP file)
3. Extract to `C:\ffmpeg`
4. Add `C:\ffmpeg\bin` to your Windows PATH

See `FFMPEG_SETUP.md` for detailed instructions.

## Usage

### Starting the App

```bash
python main.py
```

### Recording Steps

1. **Select Video Source**: Choose Camera or Screen (1-3)
2. **Select Audio Source**: Pick microphone or audio input device
3. **Set Output File**: Browse or manually set the file path
4. **Click Start**: Begin recording
5. **Click Pause/Stop**: Control recording
6. **View Status**: Check timestamp log at the bottom

### Scheduling Recordings

1. Set Start Time and End Time
2. Choose video and audio sources
3. Select output file
4. Click "Schedule Recording"
5. App will automatically start/stop at specified times

## File Structure

```
Video_Record/
├── main.py              # Entry point
├── gui.py              # PySide6 GUI interface
├── capture.py          # Video/audio recording engine
├── scheduler.py        # APScheduler integration
├── requirements.txt    # Python dependencies
├── FFMPEG_SETUP.md     # FFmpeg installation guide
└── README.md           # This file
```

## Dependencies

- **PySide6**: GUI framework
- **opencv-python**: Video capture and encoding
- **apscheduler**: Scheduled recording
- **mss**: Screen capture
- **numpy**: Image processing
- **sounddevice**: Audio input
- **soundfile**: Audio file writing
- **scipy**: Audio processing
- **FFmpeg**: Audio-video merging (external)

## System Requirements

- Windows 11
- Python 3.8+
- Webcam or screen for recording
- Microphone or audio input for recording
- 2GB free disk space (for recordings)
- FFmpeg installed (optional, but recommended)

## Troubleshooting

### "No audio devices found"
- Check that your microphone/audio input is connected
- Try restarting the app
- Check Windows Sound Settings

### "FFmpeg not found"
- Audio-video merge will fail silently
- Install FFmpeg following `FFMPEG_SETUP.md`
- Or manually merge using: `ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4`

### Video/Audio sync issues
- Ensure FFmpeg is properly installed
- Try recording a shorter test video first

### Poor video quality
- Check camera/screen resolution
- Adjust output folder storage space

## Tips

1. **Use full paths** for output files to avoid permission issues
2. **Test schedule** before important recordings
3. **Check status log** for any errors or warnings
4. **Keep FFmpeg updated** for best compatibility
5. **Create output folder** if it doesn't exist

## License

Use freely for personal and commercial projects.

## Support

For issues or questions, check:
- Console output for error messages
- Status log in the GUI
- System logs in `C:\Users\vhuang01\AppData\Local\...`


