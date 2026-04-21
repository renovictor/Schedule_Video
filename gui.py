from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDateTimeEdit, QPushButton, QMessageBox, QLineEdit, QFileDialog, QComboBox, QTextEdit, QTabWidget, QSlider
from PySide6.QtCore import QDateTime, Qt, QUrl, QTimer
from PySide6.QtGui import QIcon, QFont
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from capture import VideoRecorder
from scheduler import RecordingScheduler
import sys
from datetime import datetime
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.recorder = VideoRecorder()
        self.scheduler = RecordingScheduler(self.recorder)
        self.init_ui()
        self.apply_styles()
        # Register callback with scheduler after UI is initialized
        self.scheduler.set_status_callback(self.add_status_message)

    def init_ui(self):
        self.setWindowTitle('Video Recorder Scheduler')
        self.setGeometry(100, 100, 700, 800)

        # Set window icon
        icon_path = os.path.join(os.path.dirname(__file__), 'global_search_international.ico')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        # Create tab widget
        self.tabs = QTabWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)
        
        # Create tabs
        self.recording_tab = QWidget()
        self.display_tab = QWidget()
        
        self.tabs.addTab(self.recording_tab, "Recording")
        self.tabs.addTab(self.display_tab, "Display")
        
        # Initialize Recording Tab
        self.init_recording_tab()
        
        # Initialize Display Tab
        self.init_display_tab()

    def init_recording_tab(self):
        """Initialize the Recording tab with original UI elements"""
        layout = QVBoxLayout()

        # LED Status Indicator
        led_layout = QHBoxLayout()
        led_layout.addWidget(QLabel('Recording Status:'))
        self.led_indicator = QLabel('●')
        self.led_indicator.setFont(QFont('Arial', 20, QFont.Bold))
        self.led_indicator.setStyleSheet('color: green;')  # Default to green (stopped)
        self.led_indicator.setAlignment(Qt.AlignCenter)
        led_layout.addWidget(self.led_indicator)
        led_layout.addStretch()
        layout.addLayout(led_layout)

        # Start time
        start_layout = QHBoxLayout()
        
        # Fresh button to reset start time to current
        fresh_button = QPushButton('Fresh')
        fresh_button.setObjectName('freshBtn')
        fresh_button.setMaximumWidth(80)
        fresh_button.clicked.connect(self.on_refresh_start_time)
        start_layout.addWidget(fresh_button)
        
        start_layout.addWidget(QLabel('Start Time:'))
        self.start_time_edit = QDateTimeEdit()
        self.start_time_edit.setDateTime(QDateTime.currentDateTime())
        start_layout.addWidget(self.start_time_edit)
        layout.addLayout(start_layout)

        # Duration selection
        duration_layout = QHBoxLayout()
        duration_layout.addWidget(QLabel('Duration:'))
        self.duration_combo = QComboBox()
        self.duration_options = [
            ('2m', 2 * 60),  # Test option
            ('30m', 30 * 60),
            ('1H', 1 * 3600),
            ('1.5H', int(1.5 * 3600)),
            ('2H', 2 * 3600),
            ('2.5H', int(2.5 * 3600)),
            ('3H', 3 * 3600)
        ]
        for label, _ in self.duration_options:
            self.duration_combo.addItem(label)
        self.duration_combo.setCurrentIndex(1)  # Default to 30m
        duration_layout.addWidget(self.duration_combo)
        layout.addLayout(duration_layout)

        # Output file
        output_layout = QHBoxLayout()
        output_layout.addWidget(QLabel('Output File:'))
        self.path_edit = QLineEdit()
        self.path_edit.setText(f"C:\\Users\\vhuang01\\Videos\\Video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4")
        output_layout.addWidget(self.path_edit)
        browse_button = QPushButton('Browse...')
        browse_button.setObjectName('browseBtn')
        browse_button.clicked.connect(self.browse_file)
        output_layout.addWidget(browse_button)
        layout.addLayout(output_layout)

        # Record source selection
        source_layout = QHBoxLayout()
        source_layout.addWidget(QLabel('Record Source:'))
        self.source_combo = QComboBox()
        self.source_combo.addItems(['Camera', 'Screen 1', 'Screen 2', 'Screen 3'])
        self.source_combo.setCurrentIndex(1)  # Default to Screen 1
        self.source_combo.currentIndexChanged.connect(self.on_source_changed)
        source_layout.addWidget(self.source_combo)
        layout.addLayout(source_layout)

        # Initialize the source
        self.on_source_changed()

        # Audio source selection
        audio_layout = QHBoxLayout()
        audio_layout.addWidget(QLabel('Audio Source:'))
        self.audio_combo = QComboBox()
        self.audio_combo.currentIndexChanged.connect(self.on_audio_source_changed)
        audio_layout.addWidget(self.audio_combo)
        layout.addLayout(audio_layout)

        # Populate audio devices
        self.populate_audio_devices()

        # Schedule button
        self.schedule_button = QPushButton('Schedule Recording')
        self.schedule_button.setObjectName('scheduleBtn')
        self.schedule_button.clicked.connect(self.schedule_recording)
        layout.addWidget(self.schedule_button)

        # Control buttons layout
        control_layout = QHBoxLayout()
        
        # Start button
        self.start_button = QPushButton('Start')
        self.start_button.setObjectName('startBtn')
        self.start_button.clicked.connect(self.on_start_recording)
        control_layout.addWidget(self.start_button)

        # Pause button
        self.pause_button = QPushButton('Pause')
        self.pause_button.setObjectName('pauseBtn')
        self.pause_button.clicked.connect(self.on_pause_recording)
        self.pause_button.setEnabled(False)
        control_layout.addWidget(self.pause_button)

        # Stop button
        self.stop_button = QPushButton('Stop')
        self.stop_button.setObjectName('stopBtn')
        self.stop_button.clicked.connect(self.on_stop_recording)
        self.stop_button.setEnabled(False)
        control_layout.addWidget(self.stop_button)
        
        layout.addLayout(control_layout)

        # Status text area
        layout.addWidget(QLabel('Status:'))
        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)
        self.status_text.setMinimumHeight(200)
        self.status_text.setPlaceholderText("Recording status will be displayed here...")
        layout.addWidget(self.status_text, 1)  # Give it stretch factor of 1

        # Exit button
        exit_button = QPushButton('Exit')
        exit_button.setObjectName('exitBtn')
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

        self.recording_tab.setLayout(layout)

    def init_display_tab(self):
        """Initialize the Display tab with video playback functionality"""
        layout = QVBoxLayout()
        
        # File path selection
        file_layout = QHBoxLayout()
        file_layout.addWidget(QLabel('Video File:'))
        self.video_path_edit = QLineEdit()
        self.video_path_edit.setPlaceholderText("Select a video file to play...")
        file_layout.addWidget(self.video_path_edit)
        browse_video_button = QPushButton('Browse...')
        browse_video_button.setObjectName('browseBtn')
        browse_video_button.clicked.connect(self.browse_video_file)
        file_layout.addWidget(browse_video_button)
        layout.addLayout(file_layout)
        
        # Player status label
        self.player_status_label = QLabel('Status: Ready')
        self.player_status_label.setStyleSheet('color: #2196F3; font-weight: bold;')
        layout.addWidget(self.player_status_label)
        
        # Video player widget
        self.video_widget = QVideoWidget()
        self.video_widget.setStyleSheet('background-color: #000000;')
        self.video_widget.setMinimumHeight(300)
        layout.addWidget(self.video_widget, 1)  # Give it stretch factor
        
        # Media player (not visible, just for playback control)
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_widget)
        
        # Audio output for volume control
        self.audio_output = QAudioOutput()
        self.audio_output.setVolume(0.8)  # Default 80%
        self.media_player.setAudioOutput(self.audio_output)
        
        self.media_player.errorOccurred.connect(self.on_media_error)
        
        # Play button
        play_button = QPushButton('Play')
        play_button.setObjectName('playBtn')
        play_button.clicked.connect(self.play_video)
        
        # Pause button
        video_pause_button = QPushButton('Pause')
        video_pause_button.setObjectName('pauseBtn')
        video_pause_button.clicked.connect(self.pause_video)
        
        # Stop button
        video_stop_button = QPushButton('Stop')
        video_stop_button.setObjectName('stopBtn')
        video_stop_button.clicked.connect(self.stop_video)
        
        # Control buttons layout
        control_layout = QHBoxLayout()
        control_layout.addWidget(play_button)
        control_layout.addWidget(video_pause_button)
        control_layout.addWidget(video_stop_button)
        control_layout.addStretch()
        layout.addLayout(control_layout)
        
        # Video adjustment sliders
        sliders_layout = QVBoxLayout()
        sliders_layout.setSpacing(10)
        
        # Volume slider
        volume_layout = QHBoxLayout()
        volume_layout.addWidget(QLabel('Audio Volume:'))
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(80)
        self.volume_slider.setTickPosition(QSlider.TicksBelow)
        self.volume_slider.setTickInterval(10)
        self.volume_slider.valueChanged.connect(self.set_volume)
        volume_layout.addWidget(self.volume_slider)
        self.volume_label = QLabel('80%')
        self.volume_label.setMinimumWidth(40)
        volume_layout.addWidget(self.volume_label)
        sliders_layout.addLayout(volume_layout)
        
        # Video quality/brightness slider (simulated)
        quality_layout = QHBoxLayout()
        quality_layout.addWidget(QLabel('Video Brightness:'))
        self.brightness_slider = QSlider(Qt.Horizontal)
        self.brightness_slider.setMinimum(0)
        self.brightness_slider.setMaximum(200)
        self.brightness_slider.setValue(100)
        quality_layout.addWidget(self.brightness_slider)
        self.brightness_label = QLabel('100%')
        self.brightness_label.setMinimumWidth(40)
        quality_layout.addWidget(self.brightness_label)
        sliders_layout.addLayout(quality_layout)
        
        layout.addLayout(sliders_layout)
        
        # Position slider for video playback
        position_layout = QHBoxLayout()
        position_layout.addWidget(QLabel('Position:'))
        self.position_slider = QSlider(Qt.Horizontal)
        self.position_slider.setMinimum(0)
        self.position_slider.sliderMoved.connect(self.set_position)
        position_layout.addWidget(self.position_slider)
        self.time_label = QLabel('00:00 / 00:00')
        self.time_label.setMinimumWidth(100)
        self.time_label.setStyleSheet('font-weight: bold;')
        position_layout.addWidget(self.time_label)
        layout.addLayout(position_layout)
        
        # Update position and duration when media changes
        self.media_player.durationChanged.connect(self.on_duration_changed)
        self.media_player.positionChanged.connect(self.on_position_changed)
        self.media_player.playbackStateChanged.connect(self.on_playback_state_changed)
        
        layout.addStretch()
        self.display_tab.setLayout(layout)
    
    def on_media_error(self, error):
        """Handle media player errors"""
        error_msg = self.media_player.errorString()
        self.player_status_label.setText(f'Error: {error_msg}')
        self.player_status_label.setStyleSheet('color: #f44336; font-weight: bold;')
        QMessageBox.warning(self, 'Playback Error', f'Media player error: {error_msg}')
    
    def on_playback_state_changed(self, state):
        """Update status label based on playback state"""
        from PySide6.QtMultimedia import QMediaPlayer
        if state == QMediaPlayer.PlayingState:
            self.player_status_label.setText('Status: Playing ▶')
            self.player_status_label.setStyleSheet('color: #4CAF50; font-weight: bold;')
        elif state == QMediaPlayer.PausedState:
            self.player_status_label.setText('Status: Paused ⏸')
            self.player_status_label.setStyleSheet('color: #FF9800; font-weight: bold;')
        elif state == QMediaPlayer.StoppedState:
            self.player_status_label.setText('Status: Stopped ⏹')
            self.player_status_label.setStyleSheet('color: #f44336; font-weight: bold;')
    
    def browse_video_file(self):
        """Browse for a video file"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", "Video Files (*.mp4 *.avi *.mov *.mkv);;All Files (*)", options=options)
        if file_name:
            self.video_path_edit.setText(file_name)
    
    def play_video(self):
        """Play the selected video"""
        video_path = self.video_path_edit.text()
        if not video_path:
            QMessageBox.warning(self, 'Error', 'Please select a video file first.')
            self.player_status_label.setText('Status: No file selected')
            self.player_status_label.setStyleSheet('color: #f44336; font-weight: bold;')
            return
        
        if not os.path.exists(video_path):
            QMessageBox.warning(self, 'Error', f'Video file not found: {video_path}')
            self.player_status_label.setText('Status: File not found')
            self.player_status_label.setStyleSheet('color: #f44336; font-weight: bold;')
            return
        
        try:
            # Set the source and play
            self.media_player.setSource(QUrl.fromLocalFile(video_path))
            self.player_status_label.setText('Status: Loading...')
            self.player_status_label.setStyleSheet('color: #FF9800; font-weight: bold;')
            
            # Small delay to ensure media is loaded before playing
            QTimer.singleShot(500, self.media_player.play)
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Failed to play video: {str(e)}')
            self.player_status_label.setText(f'Status: Error - {str(e)}')
            self.player_status_label.setStyleSheet('color: #f44336; font-weight: bold;')
    
    def pause_video(self):
        """Pause the video"""
        self.media_player.pause()
    
    def stop_video(self):
        """Stop the video"""
        self.media_player.stop()
    
    def set_volume(self, value):
        """Set the media player volume"""
        # Convert from 0-100 to 0.0-1.0 for QAudioOutput
        volume_level = value / 100.0
        self.audio_output.setVolume(volume_level)
        self.volume_label.setText(f'{value}%')
    
    def set_position(self, position):
        """Set the video position"""
        self.media_player.setPosition(position)
    
    def on_duration_changed(self, duration):
        """Update max value of position slider when duration changes"""
        self.position_slider.setMaximum(duration)
        self.update_time_label()
    
    def on_position_changed(self, position):
        """Update position slider when video plays"""
        self.position_slider.blockSignals(True)
        self.position_slider.setValue(position)
        self.position_slider.blockSignals(False)
        self.update_time_label()
    
    def update_time_label(self):
        """Update the time label with current position and duration"""
        position = self.media_player.position()
        duration = self.media_player.duration()
        
        def ms_to_time_str(ms):
            if ms < 0:
                ms = 0
            seconds = ms // 1000
            minutes = seconds // 60
            seconds = seconds % 60
            return f'{minutes:02d}:{seconds:02d}'
        
        self.time_label.setText(f'{ms_to_time_str(position)} / {ms_to_time_str(duration)}')

    def browse_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Select Output File", "", "MP4 Files (*.mp4);;All Files (*)", options=options)
        if file_name:
            self.path_edit.setText(file_name)

    def on_refresh_start_time(self):
        """Update start time to current time when Fresh button is clicked"""
        current_time = QDateTime.currentDateTime()
        self.start_time_edit.setDateTime(current_time)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.status_text.append(f"[{timestamp}] Start time refreshed to: {current_time.toString()}")

    def add_status_message(self, message):
        """Add a message to the status text area (used by scheduler callbacks)"""
        self.status_text.append(message)

    def on_source_changed(self):
        source = self.source_combo.currentText()
        source_index = self.source_combo.currentIndex()
        if source == 'Camera':
            self.recorder.set_source('camera', 0)
        else:
            screen_num = source_index
            self.recorder.set_source('screen', screen_num)

    def populate_audio_devices(self):
        """Populate audio device list from sounddevice"""
        try:
            import sounddevice as sd
            devices = sd.query_devices()
            audio_inputs = []
            audio_input_ids = []
            realtek_index = -1
            
            for i, device in enumerate(devices):
                # Only add input devices
                if device['max_input_channels'] > 0:
                    audio_inputs.append(f"{device['name']}")
                    audio_input_ids.append(i)
                    # Look for Microphone Array (Realtek(R) Audio)
                    if 'Microphone Array' in device['name'] and 'Realtek' in device['name']:
                        realtek_index = len(audio_inputs) - 1
            
            # Add "All of Above" option at the end
            audio_inputs.append("All of Above")
            audio_input_ids.append("all")  # Special marker for all devices
            
            self.audio_input_ids = audio_input_ids
            self.audio_combo.addItems(audio_inputs)
            
            # Set default to Microphone Array (Realtek(R) Audio) if found, otherwise use default device
            if realtek_index >= 0:
                self.audio_combo.setCurrentIndex(realtek_index)
            else:
                # Fallback to default input device
                default_device = sd.default.device[0]
                if default_device in audio_input_ids:
                    self.audio_combo.setCurrentIndex(audio_input_ids.index(default_device))
        except Exception as e:
            print(f"Error populating audio devices: {e}")
            self.audio_combo.addItem("Default Audio Input")
            self.audio_input_ids = [None]

    def on_audio_source_changed(self):
        """Handle audio source selection"""
        if hasattr(self, 'audio_input_ids'):
            device_id = self.audio_input_ids[self.audio_combo.currentIndex()]
            self.recorder.set_audio_device(device_id)

    def on_start_recording(self):
        output_path = self.path_edit.text()
        self.recorder.output_file = output_path
        self.recorder.start_recording()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        source = self.source_combo.currentText()
        audio_source = self.audio_combo.currentText()
        self.status_text.append(f"[{timestamp}] Start Record: {output_path}")
        self.status_text.append(f"[{timestamp}] Source: {source} | Audio: {audio_source}")
        self.update_button_states('recording')

    def on_pause_recording(self):
        self.recorder.stop_recording()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.status_text.append(f"[{timestamp}] Pause Record")
        self.update_button_states('paused')

    def on_stop_recording(self):
        self.recorder.stop_recording()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.status_text.append(f"[{timestamp}] Stop Record")
        self.update_button_states('stopped')

    def update_button_states(self, state):
        if state == 'recording':
            # When recording: Start disabled, Pause and Stop enabled, LED red
            self.start_button.setEnabled(False)
            self.pause_button.setEnabled(True)
            self.stop_button.setEnabled(True)
            self.led_indicator.setStyleSheet('color: red;')
        elif state == 'paused':
            # When paused: Start and Stop enabled, Pause disabled, LED yellow
            self.start_button.setEnabled(True)
            self.pause_button.setEnabled(False)
            self.stop_button.setEnabled(True)
            self.led_indicator.setStyleSheet('color: orange;')
        elif state == 'stopped':
            # When stopped: Start enabled, Pause and Stop disabled, LED green
            self.start_button.setEnabled(True)
            self.pause_button.setEnabled(False)
            self.stop_button.setEnabled(False)
            self.led_indicator.setStyleSheet('color: green;')

    def schedule_recording(self):
        from datetime import timedelta
        start_dt = self.start_time_edit.dateTime().toPython()
        current_dt = datetime.now()
        
        # Get the selected duration in seconds
        duration_index = self.duration_combo.currentIndex()
        duration_seconds = self.duration_options[duration_index][1]
        
        # Calculate end time by adding duration to start time
        end_dt = start_dt + timedelta(seconds=duration_seconds)
        output_path = self.path_edit.text()

        if start_dt >= end_dt:
            QMessageBox.warning(self, 'Invalid Time', 'Start time must be before end time.')
            return

        # Check if start time is in the future
        if start_dt <= current_dt:
            QMessageBox.warning(self, 'Invalid Time', 'Start time must be in the future. Use "Fresh" button to update to current time.')
            return

        # Configure recorder with current settings
        output_path = self.path_edit.text()
        self.recorder.output_file = output_path
        source = self.source_combo.currentText()
        audio_source = self.audio_combo.currentText()

        # Schedule the recording
        self.scheduler.schedule_recording(start_dt, end_dt, output_path)
        duration_label = self.duration_options[duration_index][0]
        
        # Add to status log
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.status_text.append(f"[{timestamp}] Scheduled Recording")
        self.status_text.append(f"  Start: {start_dt.strftime('%Y-%m-%d %H:%M:%S')}")
        self.status_text.append(f"  Duration: {duration_label}")
        self.status_text.append(f"  Output: {output_path}")
        self.status_text.append(f"  Source: {source} | Audio: {audio_source}")
        
        QMessageBox.information(self, 'Scheduled', f'Recording scheduled from {start_dt.strftime("%H:%M:%S")} for {duration_label}.')

    def stop_recording(self):
        self.recorder.stop_recording()
        QMessageBox.information(self, 'Stopped', 'Recording stopped.')

    def apply_styles(self):
        """Apply colorful stylesheet to the application"""
        stylesheet = """
            QWidget {
                background-color: #f0f0f0;
            }
            
            QTabWidget {
                background-color: #ffffff;
            }
            
            QTabBar::tab {
                background-color: #e0e0e0;
                color: #333333;
                padding: 8px 20px;
                margin-right: 2px;
                border: 1px solid #cccccc;
                border-bottom: none;
                border-radius: 4px 4px 0px 0px;
                font-weight: bold;
            }
            
            QTabBar::tab:selected {
                background-color: #4CAF50;
                color: white;
                border: 1px solid #45a049;
            }
            
            QTabBar::tab:hover {
                background-color: #45a049;
                color: white;
            }
            
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
                font-size: 11pt;
            }
            
            QPushButton:hover {
                background-color: #0b7dda;
            }
            
            QPushButton:pressed {
                background-color: #084298;
            }
            
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
            
            QPushButton#startBtn {
                background-color: #4CAF50;
            }
            
            QPushButton#startBtn:hover {
                background-color: #45a049;
            }
            
            QPushButton#pauseBtn {
                background-color: #FF9800;
            }
            
            QPushButton#pauseBtn:hover {
                background-color: #fb8500;
            }
            
            QPushButton#stopBtn {
                background-color: #f44336;
            }
            
            QPushButton#stopBtn:hover {
                background-color: #da190b;
            }
            
            QPushButton#exitBtn {
                background-color: #9c27b0;
            }
            
            QPushButton#exitBtn:hover {
                background-color: #7b1fa2;
            }
            
            QPushButton#freshBtn {
                background-color: #00BCD4;
            }
            
            QPushButton#freshBtn:hover {
                background-color: #0097a7;
            }
            
            QPushButton#playBtn {
                background-color: #4CAF50;
            }
            
            QPushButton#playBtn:hover {
                background-color: #45a049;
            }
            
            QPushButton#browseBtn {
                background-color: #FF5722;
            }
            
            QPushButton#browseBtn:hover {
                background-color: #e64a19;
            }
            
            QPushButton#scheduleBtn {
                background-color: #9C27B0;
            }
            
            QPushButton#scheduleBtn:hover {
                background-color: #7b1fa2;
            }
            
            QLabel {
                color: #333333;
                font-size: 10pt;
            }
            
            QLineEdit {
                border: 2px solid #cccccc;
                border-radius: 4px;
                padding: 5px;
                background-color: #ffffff;
                color: #333333;
            }
            
            QLineEdit:focus {
                border: 2px solid #2196F3;
            }
            
            QComboBox {
                border: 2px solid #cccccc;
                border-radius: 4px;
                padding: 5px;
                background-color: #ffffff;
                color: #333333;
            }
            
            QComboBox:focus {
                border: 2px solid #2196F3;
            }
            
            QComboBox::drop-down {
                border: none;
                background-color: #2196F3;
                width: 20px;
            }
            
            QComboBox::down-arrow {
                image: none;
                color: white;
            }
            
            QTextEdit {
                border: 2px solid #cccccc;
                border-radius: 4px;
                background-color: #fafafa;
                color: #333333;
            }
            
            QSlider::groove:horizontal {
                border: 1px solid #cccccc;
                height: 8px;
                background: #e0e0e0;
                border-radius: 4px;
            }
            
            QSlider::handle:horizontal {
                background: #2196F3;
                border: 1px solid #1976d2;
                width: 18px;
                margin: -5px 0;
                border-radius: 9px;
            }
            
            QSlider::handle:horizontal:hover {
                background: #1976d2;
            }
            
            QDateTimeEdit {
                border: 2px solid #cccccc;
                border-radius: 4px;
                padding: 5px;
                background-color: #ffffff;
                color: #333333;
            }
            
            QDateTimeEdit:focus {
                border: 2px solid #2196F3;
            }
        """
        self.setStyleSheet(stylesheet)

    def closeEvent(self, event):
        self.scheduler.shutdown()
        self.recorder.stop_recording()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
