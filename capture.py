import cv2
import threading
import time
from datetime import datetime
import mss
import numpy as np
import sounddevice as sd
import soundfile as sf
import os
from scipy.io import wavfile

class VideoRecorder:
    def __init__(self, camera_index=0, output_file=None):
        self.camera_index = camera_index
        self.output_file = output_file or f"C:\\Users\\vhuang01\\Videos\\Video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
        self.cap = None
        self.out = None
        self.recording = False
        self.thread = None
        self.video_thread = None
        self.audio_thread = None
        self.source_type = 'camera'  # 'camera' or 'screen'
        self.screen_index = 0  # Screen number for screen recording
        self.audio_frames = []
        self.sample_rate = 44100
        self.audio_file = None
        self.audio_device = None  # Audio device ID, None = default

    def set_source(self, source_type, source_index):
        """Set the recording source: 'camera' or 'screen'"""
        self.source_type = source_type
        if source_type == 'camera':
            self.camera_index = source_index
        else:
            self.screen_index = source_index

    def set_audio_device(self, device_id):
        """Set the audio input device"""
        self.audio_device = device_id

    def start_recording(self):
        if self.recording:
            return
        self.recording = True
        self.audio_frames = []
        # Create temp audio file path
        base_output = os.path.splitext(self.output_file)[0]
        self.audio_file = f"{base_output}_audio.wav"
        
        # Start video and audio threads
        self.video_thread = threading.Thread(target=self._record_video)
        self.audio_thread = threading.Thread(target=self._record_audio)
        self.video_thread.start()
        self.audio_thread.start()

    def stop_recording(self):
        if not self.recording:
            return
        self.recording = False
        
        # Wait for threads to finish
        if self.video_thread:
            self.video_thread.join()
        if self.audio_thread:
            self.audio_thread.join()
        
        # Release video resources
        if self.cap:
            self.cap.release()
        if self.out:
            self.out.release()
        cv2.destroyAllWindows()
        
        # Save audio file
        if len(self.audio_frames) > 0:
            try:
                audio_data = np.concatenate(self.audio_frames, axis=0)
                sf.write(self.audio_file, audio_data, self.sample_rate)
                self._merge_audio_video()
            except Exception as e:
                print(f"Error saving audio: {e}")

    def _record_video(self):
        if self.source_type == 'camera':
            self._record_camera()
        else:
            self._record_screen()

    def _record_audio(self):
        """Record audio from selected device"""
        try:
            channels = 2
            blocksize = 2048
            
            def audio_callback(indata, frames, time_info, status):
                if status:
                    print(f"Audio recording status: {status}")
                if self.recording:
                    self.audio_frames.append(indata.copy())
            
            # Use selected device or default
            device = self.audio_device
            
            with sd.InputStream(device=device, samplerate=self.sample_rate, channels=channels, 
                               blocksize=blocksize, callback=audio_callback):
                while self.recording:
                    time.sleep(0.1)
        except Exception as e:
            print(f"Error during audio recording: {e}")

    def _record_camera(self):
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            return

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = self.cap.get(cv2.CAP_PROP_FPS) or 30
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.out = cv2.VideoWriter(self.output_file, fourcc, fps, (width, height))

        while self.recording:
            ret, frame = self.cap.read()
            if ret:
                self.out.write(frame)
            else:
                break
            time.sleep(0.01)

        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()

    def _record_screen(self):
        try:
            with mss.mss() as sct:
                monitors = sct.monitors
                if self.screen_index >= len(monitors):
                    print(f"Error: Screen {self.screen_index} not found.")
                    return
                
                monitor = monitors[self.screen_index]
                width = monitor['width']
                height = monitor['height']
                
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                fps = 30
                self.out = cv2.VideoWriter(self.output_file, fourcc, fps, (width, height))
                
                while self.recording:
                    screenshot = sct.grab(monitor)
                    frame = np.array(screenshot)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                    self.out.write(frame)
                    time.sleep(1/fps)
                
                self.out.release()
        except Exception as e:
            print(f"Error during screen recording: {e}")
            if self.out:
                self.out.release()

    def _merge_audio_video(self):
        """Merge audio and video using ffmpeg-python"""
        try:
            import subprocess
            output_with_audio = self.output_file
            temp_output = self.output_file.replace('.mp4', '_temp.mp4')
            
            # Check if ffmpeg is available
            result = subprocess.run(['ffmpeg', '-version'], capture_output=True)
            if result.returncode != 0:
                print("FFmpeg not found. Skipping audio-video merge.")
                return
            
            # Use ffmpeg to merge audio and video
            cmd = [
                'ffmpeg', '-i', self.output_file, '-i', self.audio_file,
                '-c:v', 'copy', '-c:a', 'aac', '-map', '0:v:0', '-map', '1:a:0',
                temp_output, '-y'
            ]
            
            subprocess.run(cmd, capture_output=True)
            
            # Replace original with merged file
            if os.path.exists(temp_output):
                os.remove(self.output_file)
                os.rename(temp_output, output_with_audio)
            
            # Clean up audio file
            if os.path.exists(self.audio_file):
                os.remove(self.audio_file)
            
            print(f"Video with audio saved: {output_with_audio}")
        except Exception as e:
            print(f"Error merging audio and video: {e}")


