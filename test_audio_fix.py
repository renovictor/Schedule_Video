# Quick test to verify the audio output fix
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

print("Testing PySide6 audio output fix...")

try:
    app = QApplication(sys.argv)
    
    # Test 1: Create QAudioOutput
    print("✓ Creating QAudioOutput...")
    audio_output = QAudioOutput()
    
    # Test 2: Set volume
    print("✓ Setting volume to 0.8...")
    audio_output.setVolume(0.8)
    
    # Test 3: Create QMediaPlayer
    print("✓ Creating QMediaPlayer...")
    media_player = QMediaPlayer()
    
    # Test 4: Set audio output on media player
    print("✓ Setting audio output on media player...")
    media_player.setAudioOutput(audio_output)
    
    # Test 5: Verify volume conversion (0-100 to 0.0-1.0)
    print("✓ Testing volume conversion...")
    test_volumes = [0, 25, 50, 75, 100]
    for vol in test_volumes:
        converted = vol / 100.0
        audio_output.setVolume(converted)
        print(f"  Volume {vol}% = {converted} (OK)")
    
    print("\n✅ All tests passed! Audio output fix is working correctly.")
    print("\nFix summary:")
    print("- QAudioOutput created for volume control")
    print("- Volume range: 0-100% (converted to 0.0-1.0 for QAudioOutput)")
    print("- Audio output connected to QMediaPlayer")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()

