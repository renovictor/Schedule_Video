# Video Recorder v1.0.1 - Complete Guide

## 🎬 What is Video Recorder?

A powerful, user-friendly Windows 11 screen and camera recording application with scheduled recording support and video playback capabilities. Features a modern, colorful GUI with real-time status monitoring.

## ✨ Key Features

### Recording Features
- ✅ **Screen Recording**: Capture Screen 1, 2, 3 independently
- ✅ **Camera Recording**: Record from integrated or external cameras
- ✅ **Audio Recording**: Capture audio from multiple sources
- ✅ **Scheduled Recording**: Set up future recordings automatically
- ✅ **Flexible Duration**: 2m (test), 30m, 1H, 1.5H, 2H, 2.5H, 3H options
- ✅ **Real-time Controls**: Start, Pause, Stop buttons for immediate recording
- ✅ **Status Monitoring**: Live status updates with timestamps
- ✅ **LED Indicators**: Visual status (Recording 🔴, Paused 🟠, Ready 🟢)

### Playback Features
- ✅ **Multiple Formats**: MP4, AVI, MOV, MKV support
- ✅ **Full Playback Controls**: Play, Pause, Stop buttons
- ✅ **Seek Capability**: Position slider to jump to any point
- ✅ **Volume Control**: 0-100% audio volume adjustment
- ✅ **Brightness Control**: 0-200% video brightness adjustment
- ✅ **Time Display**: Current position / Total duration (MM:SS format)
- ✅ **Player Status**: Real-time playback status with emoji indicators

### UI Features
- ✅ **Colorful Design**: Modern, professional color scheme
- ✅ **Tab Interface**: Recording and Display tabs for organized workflow
- ✅ **Color-Coded Buttons**: Intuitive button colors (Green=Action, Red=Stop, etc.)
- ✅ **Professional Styling**: Polished CSS-based UI with hover effects
- ✅ **Responsive Layout**: Adapts to window resizing
- ✅ **User-Friendly**: Clear labels, helpful placeholders, visual feedback

## 🚀 Quick Start

### Installation

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd Video_Record
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

### First Recording

1. Open the **Recording** tab (default)
2. Click the **Fresh** button to set start time to now
3. Choose a **Duration** (30m is default)
4. Click the **Start** button (green) to begin recording
5. Click the **Stop** button (red) to finish
6. Video saves to `C:\Users\vhuang01\Videos\`

### First Playback

1. Go to the **Display** tab
2. Click **Browse...** button to select a video file
3. Click the **Play** button (green)
4. Adjust **Audio Volume** and **Video Brightness** as needed
5. Use the position slider to navigate through the video

## 📋 System Requirements

### Minimum
- **OS**: Windows 11
- **Python**: 3.8+
- **RAM**: 2GB
- **Disk Space**: 500MB free

### Recommended
- **OS**: Windows 11 Pro
- **Python**: 3.10+
- **RAM**: 4GB+
- **Disk Space**: 2GB+ free
- **Audio Device**: Microphone or headset
- **FFmpeg**: System installation for codec support

## 📦 Dependencies

All dependencies are listed in `requirements.txt`:

```
PySide6              → GUI Framework
opencv-python       → Video capture
apscheduler         → Task scheduling
mss                 → Screen capture
numpy               → Array operations
sounddevice         → Audio device management
soundfile           → Audio file I/O
scipy               → Signal processing
pyaudio             → Audio device support
```

## 🎨 Color Scheme

### Button Colors
| Color | Hex | Purpose | Examples |
|-------|-----|---------|----------|
| 🟢 Green | #4CAF50 | Start/Play actions | Start, Play |
| 🟠 Orange | #FF9800 | Pause/Transition | Pause, Fresh |
| 🔴 Red | #f44336 | Stop actions | Stop |
| 🔵 Blue | #2196F3 | Primary action | General buttons |
| 🟣 Purple | #9C27B0 | Special functions | Schedule, Exit |
| 🔵 Cyan | #00BCD4 | Refresh actions | Fresh |
| 🟠 Orange-Red | #FF5722 | File selection | Browse |

## 📱 Interface Overview

### Recording Tab
```
Record Source      → Camera, Screen 1/2/3
Audio Source       → Microphone, Multiple devices
Start Time         → When to start recording
Duration           → How long to record
Output File        → Save location and filename
Status Area        → Real-time recording updates
Controls           → Start, Pause, Stop buttons
```

### Display Tab
```
Video File         → Select MP4/AVI/MOV/MKV
Player Status      → Current playback state
Video Display      → Black background window
Playback Controls  → Play, Pause, Stop buttons
Volume Slider      → 0-100% audio control
Brightness Slider  → 0-200% video adjustment
Position Slider    → Seek through video
Time Display       → MM:SS format
```

## 🔧 Configuration

### Default Settings
- **Record Source**: Screen 1
- **Audio Source**: Microphone Array (Realtek(R) Audio)
- **Duration**: 30 minutes
- **Output Path**: `C:\Users\vhuang01\Videos\`
- **File Format**: `Video_YYYYMMDD_HHMMSS.mp4`
- **Playback Volume**: 80%
- **Video Brightness**: 100%

### Customization
All defaults can be changed in the GUI before recording/playback:
1. Change Record Source via dropdown
2. Select different Audio Source
3. Set custom output file path via Browse button
4. Adjust duration for each session
5. Change start time as needed

## 📖 Documentation Files

### Quick Start Guides
- **PLAYBACK_QUICK_START.md** - Video playback getting started
- **START_HERE.md** - Initial setup guide
- **QUICK_START.md** - General quick start

### Detailed Guides
- **VIDEO_PLAYBACK_GUIDE.md** - Complete troubleshooting guide
- **GUI_IMPROVEMENTS.md** - All GUI features explained
- **CREATE_EXE_GUIDE.md** - Creating standalone EXE
- **FFMPEG_SETUP.md** - FFmpeg installation guide

### Reference Materials
- **COLOR_SCHEME.md** - Design specifications
- **QUICK_REFERENCE.md** - Button and control reference
- **UPDATE_SUMMARY_v1_0_1.md** - This version's changes
- **README.md** - Standard README

## 🐛 Troubleshooting

### Video Not Recording
1. Verify screen/camera is active
2. Check output file path is writable
3. Ensure audio device is available
4. See VIDEO_PLAYBACK_GUIDE.md

### Video Not Playing
1. Check file format is supported
2. Verify FFmpeg is installed
3. Confirm file exists
4. Check file permissions

### No Audio
1. Volume slider not at 0%
2. System volume not muted
3. Audio device connected
4. FFmpeg installed properly

### Application Crashes
1. Restart application
2. Check Python version (3.8+)
3. Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
4. Check system resources (RAM, disk space)

## 📄 File Structure

```
Video_Record/
├── main.py                          # Application entry point
├── gui.py                           # GUI interface (updated v1.0.1)
├── capture.py                       # Video/audio capture
├── scheduler.py                     # Recording scheduler
├── VERSION.py                       # Version information
├── requirements.txt                 # Python dependencies
├── global_search_international.ico # Application icon
│
├── README.md                        # General readme
├── README_GITHUB.md                 # GitHub specific readme
├── QUICK_REFERENCE.md               # Quick reference card
├── QUICK_START.md                   # Quick start guide
├── START_HERE.md                    # Getting started
│
├── VIDEO_PLAYBACK_GUIDE.md          # Playback troubleshooting
├── GUI_IMPROVEMENTS.md              # GUI features guide
├── COLOR_SCHEME.md                  # Design reference
├── PLAYBACK_QUICK_START.md          # Playback quick start
├── UPDATE_SUMMARY_v1_0_1.md         # This version info
│
├── CREATE_EXE_GUIDE.md              # EXE creation
├── EXE_CREATION_README.md           # EXE guide
├── EXE_QUICK_REFERENCE.md           # EXE reference
├── CREATE_EXE_README.md             # EXE readme
│
├── FFMPEG_SETUP.md                  # FFmpeg setup
├── INSTALLATION_CHECKLIST.md        # Installation steps
├── RELEASE_NOTES.md                 # Release notes
└── build/                           # PyInstaller build artifacts
```

## 💾 Recording Output

### Default Location
```
C:\Users\vhuang01\Videos\
```

### File Naming Convention
```
Video_YYYYMMDD_HHMMSS.mp4
Example: Video_20260421_143000.mp4
```

### File Format
- **Video Codec**: H.264 (MP4)
- **Audio Codec**: AAC
- **Resolution**: Source dependent (screen resolution or camera)
- **Frame Rate**: 30 FPS
- **Bit Rate**: Variable

## 🔐 Security

### Permissions Required
- Read/Write access to Videos folder
- Audio device access
- Screen capture capability (Windows allows)
- Process scheduling capability

### Data Privacy
- No data is sent to external servers
- All files stored locally
- Scheduled tasks run locally
- No tracking or telemetry

## 🎓 Usage Tips

### Recording Tips
1. **Test First**: Use 2m duration for test recording
2. **Check Path**: Verify output file location before starting
3. **Audio Levels**: Ensure microphone is at appropriate volume
4. **Screen**: Only one source at a time (can't record multiple screens simultaneously)

### Playback Tips
1. **MP4 First**: Try MP4 files first for best compatibility
2. **Close Background**: Close other applications for smooth playback
3. **Volume Slider**: 0% = muted, not zero audio device
4. **Position Slider**: Drag to seek, smooth playback updates

### Performance Tips
1. Close web browsers and background applications
2. Ensure sufficient disk space (minimum 500MB)
3. Update graphics drivers
4. Disable unnecessary overlays
5. Use local storage, not network drives

## 📞 Support & Contact

### Getting Help
1. Check relevant documentation file (see list above)
2. Review QUICK_REFERENCE.md for button guide
3. See VIDEO_PLAYBACK_GUIDE.md for troubleshooting
4. Check console output for error messages

### Common Issues
- **Black video during playback**: Install FFmpeg (see FFMPEG_SETUP.md)
- **No audio**: Check volume slider and system audio
- **Scheduling fails**: Use Fresh button to update start time
- **File format issues**: Convert to MP4 using FFmpeg

## 🔄 Version History

### v1.0.1 (Current)
- ✅ Colorful GUI redesign
- ✅ Tab-based interface
- ✅ Video playback Display tab
- ✅ Volume and brightness controls
- ✅ Enhanced player status feedback
- ✅ Improved error handling

### v1.0.0 (Previous)
- Basic recording functionality
- Scheduler support
- Status monitoring
- Original GUI

## 🚀 Future Plans

### Planned Features
- [ ] Video effects and filters
- [ ] Playback speed control
- [ ] Keyboard shortcuts
- [ ] Dark mode theme
- [ ] Custom color schemes
- [ ] Batch processing
- [ ] Recording history
- [ ] Advanced audio controls

### Potential Enhancements
- Subtitle/caption support
- Video rotation and flip
- Advanced codec options
- Network stream support
- Cloud backup integration
- Android app companion

## 📝 License

This project is provided as-is for personal and commercial use.

## 👨‍💻 Development

### Built With
- **Python 3.8+**: Programming language
- **PySide6**: Qt-based GUI framework
- **OpenCV**: Video processing
- **FFmpeg**: Codec support
- **apscheduler**: Task scheduling
- **mss**: Screen capture
- **PyAudio**: Audio I/O

### Contributing
If you'd like to improve this project:
1. Fork the repository
2. Create a feature branch
3. Make improvements
4. Submit a pull request

## 📅 Support Timeline

**Current Version**: 1.0.1
**Release Date**: April 21, 2026
**Status**: Production Ready
**Maintenance**: Active

---

## 🎯 Quick Navigation

**Just Starting?** → See PLAYBACK_QUICK_START.md
**Need Help?** → See QUICK_REFERENCE.md
**Issues?** → See VIDEO_PLAYBACK_GUIDE.md
**Want EXE?** → See CREATE_EXE_GUIDE.md
**Design Details?** → See COLOR_SCHEME.md

---

**Video Recorder v1.0.1**
Professional screen and camera recording with video playback
Windows 11 | Python 3.8+ | PySide6

