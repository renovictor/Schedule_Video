# GUI Quick Reference Card

## Tabs Overview

```
┌─────────────────────────────────────────────────────────┐
│  🎙️ Recording  📺 Display                                │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  RECORDING TAB: Recording controls, scheduling, status  │
│  DISPLAY TAB: Video playback, audio/video adjustments  │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

## Recording Tab - Button Guide

```
┌─────────────────────────────────────────────────┐
│ Recording Controls                              │
├─────────────────────────────────────────────────┤
│ ●  Recording Status: 🟢 Ready / 🔴 Recording   │
│ 🔄 Fresh    [____Start Time____]              │
│ ⏱️ Duration  [▼ 30m        ]                  │
│ 📁 Output   [____File Path____] 📂 Browse     │
│ 📹 Source   [▼ Screen 1    ]                  │
│ 🔊 Audio    [▼ Realtek...  ]                  │
│ 📅 Schedule Recording                          │
│ ▶️  Start   ⏸️  Pause   ⏹️  Stop              │
│                                                 │
│ ┌───── Status Area (Large) ─────────────────┐ │
│ │ [Timestamp] Action: Recording started...  │ │
│ │ [Timestamp] Source: Screen 1 | Audio: ... │ │
│ │ ...                                        │ │
│ └────────────────────────────────────────────┘ │
│ 🚪 Exit                                        │
└─────────────────────────────────────────────────┘
```

## Display Tab - Button Guide

```
┌──────────────────────────────────────────────────┐
│ Display & Playback                               │
├──────────────────────────────────────────────────┤
│ Video File: [____File Path____] 📂 Browse       │
│ 🔵 Status: Ready                                 │
│                                                  │
│ ┌──────── Video Display (Black) ───────────────┐│
│ │                                               ││
│ │         [Video Plays Here]                   ││
│ │                                               ││
│ └──────────────────────────────────────────────┘│
│                                                  │
│ ▶️  Play   ⏸️  Pause   ⏹️  Stop                 │
│                                                  │
│ 🔊 Audio Volume: [─────●───] 80%               │
│ ☀️ Brightness:  [──────●──] 100%              │
│ ⏱️ Position:    [─────●────] 00:23 / 02:15    │
└──────────────────────────────────────────────────┘
```

## Color Legend

| Color | Hex Code | Meaning | Buttons |
|-------|----------|---------|---------|
| 🟢 Green | #4CAF50 | Action/Go | Start, Play |
| 🟠 Orange | #FF9800 | Pause/Wait | Pause, Fresh |
| 🔴 Red | #f44336 | Stop/Danger | Stop |
| 🔵 Blue | #2196F3 | Info | General buttons |
| 🟣 Purple | #9C27B0 | Special | Schedule, Exit |
| 🔵 Cyan | #00BCD4 | Refresh | Fresh button |
| 🟠 Orange-Red | #FF5722 | Browse | Browse buttons |

## Button Reference

### Recording Tab
```
Fresh (Cyan)           → Update start time to now
Start (Green)          → Begin recording
Pause (Orange)         → Pause recording
Stop (Red)             → Stop recording
Browse... (Orange-Red) → Select output file
Schedule (Purple)      → Schedule future recording
Exit (Purple)          → Close application
```

### Display Tab
```
Browse... (Orange-Red) → Select video file
Play (Green)           → Start playback
Pause (Orange)         → Pause playback
Stop (Red)             → Stop playback
```

## Status Indicator Quick Reference

### Recording Tab LED
```
● Red    = Currently recording (active)
● Orange = Recording paused
● Green  = Stopped/Ready (idle)
```

### Display Tab Status Label
```
Status: Ready (Blue)         = No file loaded
Status: Loading... (Orange)  = Loading video
Status: Playing ▶ (Green)    = Video playing
Status: Paused ⏸ (Orange)   = Video paused
Status: Stopped ⏹ (Red)     = Video stopped
Status: Error (Red)          = Error occurred
```

## Workflow: Recording + Playback

```
1. Recording Tab
   ├─ Set Start Time (use Fresh button)
   ├─ Select Duration (30m default)
   ├─ Choose Record Source (Screen 1 default)
   ├─ Select Audio (Realtek default)
   ├─ Click Start ▶️ (Green)
   └─ Click Stop ⏹️ (Red) when done

2. Display Tab
   ├─ Click Browse... 📂
   ├─ Select recorded file
   ├─ Click Play ▶️ (Green)
   ├─ Adjust Volume 🔊 (0-100%)
   ├─ Adjust Brightness ☀️ (0-200%)
   └─ Use Position Slider ⏱️ to seek
```

## Keyboard Shortcuts

```
(Framework supports standard shortcuts)
Tab     → Switch between tabs
Alt+S   → Start recording (if focus on button)
Alt+P   → Play video (if focus on button)
Enter   → Activate focused button
```

## Input Fields

| Field | Purpose | Example |
|-------|---------|---------|
| Start Time | Recording begins at this time | 2026-04-21 14:30:00 |
| Duration | How long to record | 30m (options: 2m, 30m, 1H, 1.5H, 2H, 2.5H, 3H) |
| Output File | Where video saves | C:\Users\vhuang01\Videos\Video_20260421_143000.mp4 |
| Video File | Which video to play | C:\Users\...\myrecording.mp4 |

## Combo Box Options

### Record Source
```
▼ Camera      → Internal/external camera
▼ Screen 1    → Primary monitor (DEFAULT)
▼ Screen 2    → Secondary monitor
▼ Screen 3    → Tertiary monitor
```

### Duration Options
```
▼ 2m      → 2 minutes (test recording)
▼ 30m     → 30 minutes (DEFAULT)
▼ 1H      → 1 hour
▼ 1.5H    → 1.5 hours
▼ 2H      → 2 hours
▼ 2.5H    → 2.5 hours
▼ 3H      → 3 hours
```

### Audio Source
```
▼ [Default Device]
▼ Microphone Array (Realtek(R) Audio)  ← DEFAULT
▼ [Other Audio Devices]
▼ All of Above          → Record all audio sources
```

## Slider Controls

### Recording Tab (Display Tab)
```
Volume Slider:     [0%  ←───●───→  100%]
Display: 80%

Brightness Slider: [0%  ←────●─→  200%]
Display: 100%

Position Slider:   [Start ←──●──→ End]
Display: 00:23 / 02:15
```

## Tips & Tricks

### Quick Recording
```
1. Click Start ▶️
2. Record video
3. Click Stop ⏹️
→ File saved automatically
```

### Quick Playback
```
1. Recording Tab → Note file path
2. Display Tab → Click Browse 📂
3. Select file → Click Play ▶️
4. Drag Position Slider ⏱️ to navigate
```

### Adjust Audio
```
① Default: 80% volume
② Drag slider left: Quieter (lower %)
③ Drag slider right: Louder (higher %)
④ 0% = Muted
```

### Adjust Video
```
① Default: 100% brightness
② Drag slider left: Darker (0-100%)
③ Drag slider right: Brighter (100-200%)
④ 50% = Half brightness
```

## File Format Support

```
PLAYBACK FORMATS:
✅ MP4  (Recommended - Best compatibility)
✅ AVI  (Good - Older format)
✅ MOV  (Good - Apple format)
✅ MKV  (Good - High quality)

RECORDING FORMATS:
✅ MP4  (Default - Best compatibility)
```

## Status Messages Examples

```
[2026-04-21 14:30:45] Start Record: C:\...\Video_20260421_143000.mp4
[2026-04-21 14:30:45] Source: Screen 1 | Audio: Microphone Array (Realtek(R) Audio)
[2026-04-21 14:30:50] Pause Record
[2026-04-21 14:30:55] Stop Record
```

## Error Messages & Solutions

| Error | Cause | Fix |
|-------|-------|-----|
| "No file selected" | Browse button not clicked | Click Browse 📂 first |
| "Video file not found" | File deleted/moved | Check file location |
| "Error: ..." | Media player issue | Check VIDEO_PLAYBACK_GUIDE.md |

## System Indicators

```
Windows Title Bar:     [Video Recorder Scheduler] 🎙️ 📺
Window Icon:           [global_search_international.ico]
App Starts:            700x800 pixels default size
```

---

**Quick Reference v1.0.1**
**Updated: April 21, 2026**

Print this card for quick reference!

