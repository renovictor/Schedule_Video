# Video Recorder - Version Information

VERSION = "1.0.1"
BUILD_DATE = "April 19, 2026"
PROJECT_NAME = "Video Recorder with Audio Source Selection"

# Version History
HISTORY = {
    "1.0.1": {
        "date": "April 19, 2026",
        "features": [
            "Fixed audio/video synchronization using threading.Event",
            "Added 2x volume boost with audio normalization",
            "Fixed audio-only recording issue with proper video initialization",
            "Added 'All of Above' audio source option for multi-device recording",
            "Improved EXE filename with proper version number (VictorVideo_1.0.1.exe)",
            "Enhanced status logging and error handling",
            "Fixed Fresh button for quick start time updates",
            "Added schedule recording with validation"
        ]
    },
    "1.0.0": {
        "date": "April 18, 2026",
        "features": [
            "Video recording (Camera, Screen 1-3)",
            "Audio recording with device selection",
            "Start/Pause/Stop controls",
            "Scheduled recording",
            "Real-time status logging",
            "FFmpeg audio-video merging",
            "Multi-device audio input support",
            "Professional MP4 output"
        ],
        "improvements": [
            "Auto-detection of audio devices",
            "Enhanced status log with timestamps",
            "Comprehensive documentation (8 files)",
            "Installation checklist",
            "Troubleshooting guides"
        ],
        "status": "Release"
    }
}

# Requirements
REQUIREMENTS = {
    "python": "3.8+",
    "dependencies": [
        "PySide6",
        "opencv-python",
        "apscheduler",
        "mss",
        "numpy",
        "sounddevice",
        "soundfile",
        "scipy"
    ],
    "external": [
        "FFmpeg (2024+, gyan.dev build recommended)"
    ]
}

# System Requirements
SYSTEM_REQUIREMENTS = {
    "os": "Windows 11",
    "ram": "1GB minimum, 2GB recommended",
    "disk_space": "2GB for recordings",
    "processor": "Modern multi-core processor",
    "peripherals": [
        "Webcam (for camera recording)",
        "Microphone or audio input device",
        "Display (for screen recording)"
    ]
}

# Features
FEATURES = {
    "video_capture": {
        "camera": "Webcam recording",
        "screen": "Multi-monitor support (Screen 1-3)",
        "codec": "MP4V at 30 FPS",
        "formats": ["MP4"]
    },
    "audio_capture": {
        "device_selection": "Dropdown menu for any audio input",
        "sample_rate": "44,100 Hz (CD quality)",
        "channels": "Stereo (2 channels)",
        "formats": ["AAC in MP4 container"]
    },
    "controls": {
        "start": "Begin recording",
        "pause": "Pause without losing data",
        "stop": "Complete recording",
        "schedule": "Automated start/stop times"
    },
    "output": {
        "location": "C:\\Users\\vhuang01\\Videos\\",
        "filename": "Video_YYYYMMDD_HHMMSS.mp4",
        "format": "MP4 with audio and video"
    }
}

# File Structure
FILE_STRUCTURE = {
    "source_code": [
        "main.py",
        "gui.py",
        "capture.py",
        "scheduler.py"
    ],
    "documentation": [
        "INDEX.md",
        "QUICK_START.md",
        "FFMPEG_SETUP.md",
        "INSTALLATION_CHECKLIST.md",
        "README.md",
        "COMPLETE_SUMMARY.md",
        "AUDIO_SOURCE_SELECTION_FEATURE.md",
        "CHANGELOG.md"
    ],
    "configuration": [
        "requirements.txt",
        "VERSION.py"
    ]
}

# Support URLs
SUPPORT = {
    "ffmpeg": {
        "primary": "https://www.gyan.dev/ffmpeg/builds/",
        "alternative": "https://github.com/BtbN/FFmpeg-Builds/releases",
        "documentation": "https://ffmpeg.org/documentation.html"
    },
    "libraries": {
        "pyside6": "https://doc.qt.io/qtforpython/",
        "opencv": "https://docs.opencv.org/",
        "sounddevice": "https://python-sounddevice.readthedocs.io/"
    }
}

# Status
STATUS = {
    "development": "Complete",
    "testing": "Complete",
    "documentation": "Complete",
    "ready_for_production": True
}

if __name__ == "__main__":
    print(f"{PROJECT_NAME}")
    print(f"Version: {VERSION}")
    print(f"Build Date: {BUILD_DATE}")
    print(f"Status: {STATUS['development']}")
    print(f"Production Ready: {STATUS['ready_for_production']}")

