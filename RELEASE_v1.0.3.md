# Release Notes - Video Recorder v1.0.3
**Release Date:** April 22, 2026

## Summary
Video Recorder v1.0.3 focuses on improving audio/video synchronization capabilities and enhancing the user interface with a larger, more visible recording status LED.

## What's New in v1.0.3

### 🔊 Audio Synchronization Features
- **Audio Sync Slider**: New slider in the Display tab allows manual audio/video synchronization
  - Range: -5.0 to +5.0 seconds
  - Precision: 0.1 second increments
  - Real-time visual feedback
- **Save Synced Video**: New button to save videos with applied audio offset
  - Uses FFmpeg for professional audio processing
  - Supports both delay and advance audio options
  - AAC audio codec for compatibility

### 🎨 User Interface Improvements
- **Larger LED Indicator**: Recording Status LED increased 3x in size (60pt font)
  - Red: Recording
  - Yellow/Orange: Paused
  - Green: Stopped
- **Improved Layout**: Exit button moved outside tabs for better accessibility
  - Access Exit from any tab without switching
  - Better workflow and user experience

### 🎥 Display Tab Enhancements
- Video playback with proper audio handling
- Volume and brightness adjustment sliders
- Position slider for seeking through videos
- Audio sync slider for synchronization adjustment
- Real-time status feedback

## Technical Details

### Audio Sync Processing
- **Positive Offset** (e.g., +1.5s): Delays audio by adding silence at the beginning
- **Negative Offset** (e.g., -0.5s): Advances audio by trimming the beginning
- **FFmpeg Integration**: Professional audio/video processing using FFmpeg filters

### System Requirements
- Windows 11
- Python 3.8+
- FFmpeg (for audio sync feature)
- PySide6 6.0+

## Bug Fixes
- Fixed audio sync slider not functioning properly
- Corrected millisecond to second conversion for better UX
- Improved FFmpeg command construction

## Known Issues
- FFmpeg must be installed for Save Synced Video feature to work
- Audio sync processing may take a few seconds depending on video length

## Breaking Changes
None

## Migration Guide
No migration necessary. Simply update to v1.0.3 from v1.0.2.

## Contributors
Victor Huang

## Support
For issues or feature requests, please create an issue on the GitHub repository.

---
**Version:** 1.0.3  
**Build Date:** April 22, 2026  
**Status:** Stable Release

