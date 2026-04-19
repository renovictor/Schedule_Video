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
        self.use_all_audio_devices = False  # Track if we're using all audio devices
        
        # Synchronization and volume controls
        self.sync_event = threading.Event()  # For synchronizing audio/video start
        self.audio_volume_boost = 2.0  # Volume multiplier for low audio
        self.audio_normalization = True  # Enable audio normalization

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
        # Track if we're using all devices
        self.use_all_audio_devices = (device_id == "all")

    def start_recording(self):
        if self.recording:
            print("Recording already in progress")
            return
        
        # Ensure output file is set
        if not self.output_file:
            self.output_file = f"C:\\Users\\vhuang01\\Videos\\Video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
        
        print(f"=== START RECORDING ===")
        print(f"Output file: {self.output_file}")
        print(f"Source type: {self.source_type}")
        print(f"Source index: {self.camera_index if self.source_type == 'camera' else self.screen_index}")
        
        self.recording = True
        self.audio_frames = []
        # Create temp audio file path
        base_output = os.path.splitext(self.output_file)[0]
        self.audio_file = f"{base_output}_audio.wav"
        
        # Reset sync event
        self.sync_event.clear()
        
        # Start video and audio threads
        self.video_thread = threading.Thread(target=self._record_video)
        self.audio_thread = threading.Thread(target=self._record_audio)
        
        # Start both threads
        self.video_thread.start()
        self.audio_thread.start()
        
        # Wait a brief moment for both threads to initialize
        time.sleep(0.1)
        
        # Signal both threads to start recording simultaneously
        self.sync_event.set()
        
        print(f"Video and audio recording threads started and synchronized")

    def stop_recording(self):
        if not self.recording:
            print("Recording not in progress")
            return
        
        print(f"=== STOP RECORDING ===")
        self.recording = False
        
        # Wait for threads to finish
        if self.video_thread:
            print("Waiting for video thread to finish...")
            self.video_thread.join(timeout=5.0)  # Add timeout
            if self.video_thread.is_alive():
                print("Warning: Video thread did not finish cleanly")
            else:
                print("Video thread finished")
        if self.audio_thread:
            print("Waiting for audio thread to finish...")
            self.audio_thread.join(timeout=5.0)  # Add timeout
            if self.audio_thread.is_alive():
                print("Warning: Audio thread did not finish cleanly")
            else:
                print("Audio thread finished")
        
        # Release video resources
        if self.cap:
            self.cap.release()
        if self.out:
            self.out.release()
        cv2.destroyAllWindows()
        
        # Process and save audio file
        if len(self.audio_frames) > 0:
            try:
                print(f"Saving audio: {len(self.audio_frames)} frames to {self.audio_file}")
                audio_data = np.concatenate(self.audio_frames, axis=0)
                
                # Apply volume boost and normalization
                if self.audio_normalization:
                    audio_data = self._normalize_audio(audio_data)
                
                # Apply volume boost
                audio_data = audio_data * self.audio_volume_boost
                
                # Ensure audio doesn't clip
                audio_data = np.clip(audio_data, -1.0, 1.0)
                
                sf.write(self.audio_file, audio_data, self.sample_rate)
                print(f"Audio saved successfully (volume boosted by {self.audio_volume_boost}x)")
                self._merge_audio_video()
            except Exception as e:
                print(f"Error saving audio: {e}")
        else:
            print("No audio frames recorded")
        
        print(f"Recording complete. Output: {self.output_file}")

    def _normalize_audio(self, audio_data):
        """Apply audio normalization to improve volume"""
        try:
            # Calculate RMS level
            rms = np.sqrt(np.mean(audio_data**2))
            
            # Target RMS level (adjustable - higher = louder)
            target_rms = 0.3  # This can be adjusted
            
            if rms > 0:
                # Calculate gain needed
                gain = target_rms / rms
                
                # Apply gain but don't exceed 1.0 to avoid clipping
                gain = min(gain, 1.0 / np.max(np.abs(audio_data)) if np.max(np.abs(audio_data)) > 0 else 1.0)
                
                audio_data = audio_data * gain
                print(f"Audio normalized with gain: {gain:.2f}")
            
            return audio_data
        except Exception as e:
            print(f"Error during audio normalization: {e}")
            return audio_data

    def _record_video(self):
        print(f"Starting video recording with source_type: {self.source_type}, screen_index: {self.screen_index}")
        if self.source_type == 'camera':
            self._record_camera()
        else:
            self._record_screen()

    def _record_audio(self):
        """Record audio from selected device or all devices"""
        try:
            channels = 2
            blocksize = 2048
            
            if self.use_all_audio_devices:
                # Record from all available input devices
                self._record_audio_from_all_devices()
            else:
                # Record from single selected device
                print("Audio stream opened. Waiting for sync signal...")
                
                # Wait for synchronization signal before starting audio recording
                self.sync_event.wait()
                
                print("Sync received. Starting synchronized audio recording...")
                
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

    def _record_audio_from_all_devices(self):
        """Record audio from all available input devices and mix them"""
        try:
            print("Recording from all available audio devices...")
            
            # Get all input devices
            devices = sd.query_devices()
            input_devices = []
            
            for i, device in enumerate(devices):
                if device['max_input_channels'] > 0:
                    input_devices.append((i, device['name']))
            
            print(f"Found {len(input_devices)} input devices:")
            for device_id, name in input_devices:
                print(f"  - Device {device_id}: {name}")
            
            if len(input_devices) == 0:
                print("No input devices found!")
                return
            
            print("Audio streams prepared. Waiting for sync signal...")
            
            # Wait for synchronization signal before starting all streams
            self.sync_event.wait()
            
            print("Sync received. Starting synchronized multi-device audio recording...")
            
            # Create audio streams for each device
            streams = []
            device_frames = {}  # Store frames for each device
            
            def create_callback(device_id):
                def audio_callback(indata, frames, time_info, status):
                    if status:
                        print(f"Audio device {device_id} status: {status}")
                    if self.recording:
                        if device_id not in device_frames:
                            device_frames[device_id] = []
                        device_frames[device_id].append(indata.copy())
                return audio_callback
            
            # Start all streams
            for device_id, device_name in input_devices:
                try:
                    stream = sd.InputStream(device=device_id, 
                                          samplerate=self.sample_rate, 
                                          channels=2, 
                                          blocksize=2048, 
                                          callback=create_callback(device_id))
                    stream.start()
                    streams.append((device_id, device_name, stream))
                    print(f"Started recording from: {device_name}")
                except Exception as e:
                    print(f"Failed to start recording from {device_name}: {e}")
            
            # Wait for recording to finish
            while self.recording:
                time.sleep(0.1)
            
            # Stop all streams
            for device_id, device_name, stream in streams:
                try:
                    stream.stop()
                    stream.close()
                    print(f"Stopped recording from: {device_name}")
                except Exception as e:
                    print(f"Error stopping stream for {device_name}: {e}")
            
            # Mix audio from all devices
            if device_frames:
                print("Mixing audio from all devices...")
                self._mix_audio_from_devices(device_frames)
            else:
                print("No audio frames recorded from any device")
                
        except Exception as e:
            print(f"Error during multi-device audio recording: {e}")

    def _mix_audio_from_devices(self, device_frames):
        """Mix audio frames from multiple devices"""
        try:
            # Find the device with the most frames (longest recording)
            max_frames = 0
            for device_id, frames in device_frames.items():
                if len(frames) > max_frames:
                    max_frames = len(frames)
            
            if max_frames == 0:
                print("No audio frames to mix")
                return
            
            print(f"Mixing {len(device_frames)} devices with {max_frames} frames each")
            
            # Initialize mixed audio array
            mixed_audio = np.zeros((max_frames * 2048, 2), dtype=np.float32)
            
            # Mix audio from each device
            for device_id, frames in device_frames.items():
                device_name = f"Device {device_id}"
                # Try to get device name
                try:
                    devices = sd.query_devices()
                    if device_id < len(devices):
                        device_name = devices[device_id]['name']
                except:
                    pass
                
                print(f"Processing {len(frames)} frames from {device_name}")
                
                # Concatenate frames from this device
                if frames:
                    device_audio = np.concatenate(frames, axis=0)
                    # Ensure device_audio is the right length
                    if len(device_audio) > len(mixed_audio):
                        device_audio = device_audio[:len(mixed_audio)]
                    elif len(device_audio) < len(mixed_audio):
                        # Pad with zeros if shorter
                        padding = np.zeros((len(mixed_audio) - len(device_audio), 2), dtype=np.float32)
                        device_audio = np.concatenate([device_audio, padding], axis=0)
                    
                    # Mix this device's audio into the final mix
                    # For "All of Above", don't divide volume since we apply boost later
                    if self.use_all_audio_devices:
                        mixed_audio += device_audio  # Full volume for each device
                    else:
                        mixed_audio += device_audio * (1.0 / len(device_frames))  # Normalize for single device mixing
            
            # Store the mixed audio
            self.audio_frames = [mixed_audio]
            print(f"Audio mixing complete. Final mixed audio has {len(mixed_audio)} samples")
            
        except Exception as e:
            print(f"Error mixing audio from devices: {e}")
            # Fallback: use frames from first available device
            for device_id, frames in device_frames.items():
                if frames:
                    self.audio_frames = frames
                    print(f"Fallback: Using audio from device {device_id}")
                    break

    def _record_camera(self):
        print(f"Opening camera with index: {self.camera_index}")
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            self.recording = False
            return

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = self.cap.get(cv2.CAP_PROP_FPS) or 30
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        print(f"Camera opened - FPS: {fps}, Width: {width}, Height: {height}")
        print(f"Opening video writer: {self.output_file}")
        
        self.out = cv2.VideoWriter(self.output_file, fourcc, fps, (width, height))
        
        if not self.out.isOpened():
            print(f"Error: Could not open video writer for {self.output_file}")
            self.cap.release()
            self.recording = False
            return
        
        print("Video writer opened successfully. Waiting for sync signal...")
        
        # Wait for synchronization signal
        self.sync_event.wait()
        
        print("Sync received. Starting synchronized frame capture...")
        frame_count = 0
        
        while self.recording:
            ret, frame = self.cap.read()
            if ret:
                self.out.write(frame)
                frame_count += 1
                if frame_count % 30 == 0:  # Log every 30 frames
                    print(f"Camera recording: {frame_count} frames captured")
            else:
                print(f"Failed to read frame from camera")
                break
            time.sleep(0.01)

        print(f"Camera recording stopped. Total frames: {frame_count}")
        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()

    def _record_screen(self):
        try:
            with mss.mss() as sct:
                monitors = sct.monitors
                print(f"Available monitors: {len(monitors)}")
                print(f"Requesting screen index: {self.screen_index}")
                
                if self.screen_index >= len(monitors):
                    print(f"Error: Screen {self.screen_index} not found. Available monitors: {len(monitors)}")
                    self.recording = False
                    return
                
                monitor = monitors[self.screen_index]
                width = monitor['width']
                height = monitor['height']
                
                print(f"Screen {self.screen_index}: Width={width}, Height={height}")
                print(f"Opening video writer for screen: {self.output_file}")
                
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                fps = 30
                self.out = cv2.VideoWriter(self.output_file, fourcc, fps, (width, height))
                
                if not self.out.isOpened():
                    print(f"Error: Could not open video writer for screen recording")
                    self.recording = False
                    return
                
                print("Screen video writer opened successfully. Waiting for sync signal...")
                
                # Wait for synchronization signal
                self.sync_event.wait()
                
                print("Sync received. Starting synchronized frame capture...")
                frame_count = 0
                
                while self.recording:
                    screenshot = sct.grab(monitor)
                    frame = np.array(screenshot)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                    self.out.write(frame)
                    frame_count += 1
                    if frame_count % 30 == 0:  # Log every 30 frames
                        print(f"Screen recording: {frame_count} frames captured")
                    time.sleep(1/fps)
                
                print(f"Screen recording stopped. Total frames: {frame_count}")
                self.out.release()
        except Exception as e:
            print(f"Error during screen recording: {e}")
            self.recording = False
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
