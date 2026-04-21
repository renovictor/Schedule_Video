# Quick Start: Video Playback Guide

## Getting Started with Display Tab (Video Playback)

### Step 1: Prepare a Video File

You can use your own video file or record one first:

**Option A - Record a new video:**
1. Go to "Recording" tab
2. Click "Start" button (green)
3. Record for a few seconds
4. Click "Stop" button (red)
5. Note the file location in the status area

**Option B - Use existing video:**
- Any MP4, AVI, MOV, or MKV file will work
- Ensure file is in accessible location

### Step 2: Open Display Tab

1. Click the "Display" tab at the top
2. You should see:
   - Video File input field (empty)
   - Large black video area
   - Play, Pause, Stop buttons
   - Volume and brightness sliders
   - Position slider at bottom
   - Status showing "Status: Ready" in blue

### Step 3: Select Video File

1. Click "Browse..." button (orange-red)
2. Navigate to your video file
3. Select the file and click "Open"
4. File path appears in "Video File" field
5. Status shows "Status: Ready"

### Step 4: Play Video

1. Click "Play" button (green)
2. Status changes to "Status: Loading..." (orange)
3. After 500ms, video starts playing
4. Status changes to "Status: Playing ▶" (green)
5. Video displays in black area
6. Audio plays through speakers

### Step 5: Control Playback

**Pause:**
- Click "Pause" button (orange)
- Video freezes on current frame
- Audio stops
- Status shows "Status: Paused ⏸" (orange)
- Click "Play" to resume

**Stop:**
- Click "Stop" button (red)
- Video returns to beginning
- Status shows "Status: Stopped ⏹" (red)
- Click "Play" to play from start

**Seek (Jump to Position):**
- Drag the position slider left or right
- Video jumps to that time
- Time display updates instantly
- Format: MM:SS / MM:SS (example: 01:23 / 05:00)

### Step 6: Adjust Audio Volume

1. Look for "Audio Volume:" slider
2. Drag slider to left to decrease volume
3. Drag slider to right to increase volume
4. Percentage updates next to slider (0% - 100%)
5. Audio volume changes immediately

### Step 7: Adjust Video Brightness

1. Look for "Video Brightness:" slider
2. Drag slider to left to darken video
3. Drag slider to right to brighten video
4. Percentage shows adjustment level (0% - 200%)
5. Visual changes instantly

## Keyboard Controls (If Supported)

- Space bar: Toggle Play/Pause
- Left arrow: Seek backward
- Right arrow: Seek forward

## Troubleshooting Quick Fixes

### Issue: "No file selected" error
**Solution**: Click Browse button and select a video file

### Issue: "Video file not found"
**Solution**: 
1. Check file location is correct
2. Ensure file wasn't moved or deleted
3. Try browsing again with absolute path

### Issue: Video plays but no video displays
**Solution**: See VIDEO_PLAYBACK_GUIDE.md for FFmpeg installation

### Issue: No audio output
**Solutions**:
1. Check volume slider is not at 0%
2. Check Windows system volume is not muted
3. Verify speakers/headphones connected
4. Check audio device in Recording tab

### Issue: Video playback stutters
**Solutions**:
1. Close other applications
2. Try smaller video file
3. Check system resources (CPU/Memory)
4. Restart application

### Issue: Playback position incorrect
**Solution**:
1. Make sure slider drag is complete
2. Wait for slider to update
3. Refresh by clicking Stop then Play

## Tips & Tricks

### Best Video Formats
- ✅ **MP4**: Best compatibility and performance
- ✅ **MOV**: Good compatibility
- ⚠️ **AVI**: Older format, may be slower
- ⚠️ **MKV**: Good quality but needs codecs

### Display Tab Features
- 🎬 **Full Media Controls**: Play, Pause, Stop
- 🔊 **Volume Control**: 0-100% precise adjustment
- ☀️ **Brightness Control**: 0-200% visual adjustment
- ⏱️ **Position Display**: Time remaining / Total duration
- 📊 **Real-time Updates**: Slider syncs with playback
- 🎨 **Black Background**: Reduces eye strain, better video display

### Performance Tips
1. Use MP4 files for smoothest playback
2. Close background applications
3. Ensure good disk space available
4. Use files on local drive (not network)
5. Update graphics drivers

### Recording + Playback Workflow

Perfect workflow for testing your recordings:

```
1. Recording Tab → Click "Start"
                 ↓
2. Record video (10-30 seconds recommended)
                 ↓
3. Click "Stop" (note file location)
                 ↓
4. Display Tab → Click "Browse..."
                 ↓
5. Select your recorded file
                 ↓
6. Click "Play"
                 ↓
7. Review and adjust audio/video
                 ↓
8. Check quality and make adjustments
```

## File Location Reference

### Default Recording Location
```
C:\Users\vhuang01\Videos\
```

### Files Support
- **Format**: MP4 (primary), AVI, MOV, MKV (secondary)
- **Size**: No limit (depends on storage)
- **Path**: Can contain spaces and special characters (use Browse button)

## Status Indicators Guide

### Status Label Colors & Meanings

**Recording Tab LED:**
- 🔴 Red (●): Recording in progress
- 🟠 Orange (●): Recording paused
- 🟢 Green (●): Stopped/Ready

**Display Tab Status Label:**
- 🔵 Status: Ready - No file loaded
- 🟠 Status: Loading... - Loading video file
- 🟢 Status: Playing ▶ - Video is playing
- 🟠 Status: Paused ⏸ - Video is paused
- 🔴 Status: Stopped ⏹ - Video stopped
- 🔴 Status: Error - Playback error occurred

## Next Steps

After recording and playing back videos:

1. **Quality Check**: Does video look good?
2. **Audio Check**: Does audio sound clear?
3. **Timing**: Is duration correct?
4. **File Size**: Is file size acceptable?
5. **Playback**: Does playback smooth and sync'd?

If everything looks good, you're ready for production use!

## Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Black screen | No file selected | Click Browse and select video |
| File not found | File deleted/moved | Check file location, try again |
| No audio | Volume at 0% | Drag volume slider to right |
| No audio | System muted | Check Windows volume control |
| Stuttering | Too many apps open | Close background apps |
| Playback lag | Weak CPU | Try smaller video file |
| Position wrong | Slider interaction issue | Click Stop then Play to reset |
| Error on open | FFmpeg missing | Install FFmpeg (see guide) |

## Getting Help

For detailed information, see:
- **VIDEO_PLAYBACK_GUIDE.md**: Complete troubleshooting
- **GUI_IMPROVEMENTS.md**: All GUI features explained
- **COLOR_SCHEME.md**: Design and color information

---

**Version**: 1.0.1
**Created**: April 21, 2026
**Framework**: PySide6

