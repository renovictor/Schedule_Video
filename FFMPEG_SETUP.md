# FFmpeg Setup Guide for Windows 11

This app requires FFmpeg to merge audio and video streams into a single MP4 file.

## Recommended: gyan.dev Builds (Easiest)

1. **Download FFmpeg**
   - Go to: https://www.gyan.dev/ffmpeg/builds/
   - Choose **"essentials" build** (smallest, ~50MB)
   - Download the ZIP file (e.g., `ffmpeg-2024-XX-XX-essentials_build.zip`)

2. **Extract and Install**
   - Extract to a convenient location, e.g., `C:\ffmpeg`
   - The folder structure should be: `C:\ffmpeg\bin\ffmpeg.exe`

3. **Add to PATH (Optional but Recommended)**
   - This allows the app to find FFmpeg automatically
   - Steps:
     1. Right-click "This PC" or "My Computer" → Properties
     2. Click "Advanced system settings"
     3. Click "Environment Variables" button
     4. Under "System variables", click "New"
     5. Variable name: `PATH`
     6. Variable value: `C:\ffmpeg\bin` (adjust if installed elsewhere)
     7. Click OK three times

4. **Verify Installation**
   - Open Command Prompt and type: `ffmpeg -version`
   - If you see version info, it's installed correctly!

## Alternative: btbn Builds

- Go to: https://github.com/BtbN/FFmpeg-Builds/releases
- Download a Windows build (look for `.zip` files)
- Extract and add to PATH as above

## Alternative: Chocolatey (Package Manager)

If you have Chocolatey installed:
```bash
choco install ffmpeg
```

## What if FFmpeg is Not Found?

The app will still work, but:
- Video and audio will be saved as separate files
- You'll need to merge them manually using FFmpeg
- Check the console output for details

## Troubleshooting

**"FFmpeg not found" error:**
1. Ensure FFmpeg is installed in one of these locations:
   - `C:\ffmpeg\bin\ffmpeg.exe`
   - `C:\Program Files\ffmpeg\bin\ffmpeg.exe`
   - Or anywhere in your system PATH

2. Try adding FFmpeg to PATH again and restart the app

3. Run from Command Prompt to see full error messages

**Audio/Video not merging properly:**
1. Check that the audio file was created (check with audio device)
2. Try manually converting using:
   ```bash
   ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
   ```

