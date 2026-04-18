from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDateTimeEdit, QPushButton, QMessageBox, QLineEdit, QFileDialog, QComboBox, QTextEdit
from PySide6.QtCore import QDateTime
from capture import VideoRecorder
from scheduler import RecordingScheduler
import sys
from datetime import datetime

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.recorder = VideoRecorder()
        self.scheduler = RecordingScheduler(self.recorder)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Video Recorder Scheduler')
        self.setGeometry(100, 100, 500, 500)

        layout = QVBoxLayout()

        # Start time
        start_layout = QHBoxLayout()
        start_layout.addWidget(QLabel('Start Time:'))
        self.start_time_edit = QDateTimeEdit()
        self.start_time_edit.setDateTime(QDateTime.currentDateTime())
        start_layout.addWidget(self.start_time_edit)
        layout.addLayout(start_layout)

        # End time
        end_layout = QHBoxLayout()
        end_layout.addWidget(QLabel('End Time:'))
        self.end_time_edit = QDateTimeEdit()
        self.end_time_edit.setDateTime(QDateTime.currentDateTime().addSecs(3600))  # Default 1 hour later
        end_layout.addWidget(self.end_time_edit)
        layout.addLayout(end_layout)

        # Output file
        output_layout = QHBoxLayout()
        output_layout.addWidget(QLabel('Output File:'))
        self.path_edit = QLineEdit()
        self.path_edit.setText(f"C:\\Users\\vhuang01\\Videos\\Video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4")
        output_layout.addWidget(self.path_edit)
        browse_button = QPushButton('Browse...')
        browse_button.clicked.connect(self.browse_file)
        output_layout.addWidget(browse_button)
        layout.addLayout(output_layout)

        # Record source selection
        source_layout = QHBoxLayout()
        source_layout.addWidget(QLabel('Record Source:'))
        self.source_combo = QComboBox()
        self.source_combo.addItems(['Camera', 'Screen 1', 'Screen 2', 'Screen 3'])
        self.source_combo.currentIndexChanged.connect(self.on_source_changed)
        source_layout.addWidget(self.source_combo)
        layout.addLayout(source_layout)

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
        self.schedule_button.clicked.connect(self.schedule_recording)
        layout.addWidget(self.schedule_button)

        # Control buttons layout
        control_layout = QHBoxLayout()
        
        # Start button
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.on_start_recording)
        control_layout.addWidget(self.start_button)

        # Pause button
        self.pause_button = QPushButton('Pause')
        self.pause_button.clicked.connect(self.on_pause_recording)
        self.pause_button.setEnabled(False)
        control_layout.addWidget(self.pause_button)

        # Stop button
        self.stop_button = QPushButton('Stop')
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

        self.setLayout(layout)

    def browse_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Select Output File", "", "MP4 Files (*.mp4);;All Files (*)", options=options)
        if file_name:
            self.path_edit.setText(file_name)

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
            
            for i, device in enumerate(devices):
                # Only add input devices
                if device['max_input_channels'] > 0:
                    audio_inputs.append(f"{device['name']}")
                    audio_input_ids.append(i)
            
            self.audio_input_ids = audio_input_ids
            self.audio_combo.addItems(audio_inputs)
            
            # Select default input device
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
            # When recording: Start disabled, Pause and Stop enabled
            self.start_button.setEnabled(False)
            self.pause_button.setEnabled(True)
            self.stop_button.setEnabled(True)
        elif state == 'paused':
            # When paused: Start and Stop enabled, Pause disabled
            self.start_button.setEnabled(True)
            self.pause_button.setEnabled(False)
            self.stop_button.setEnabled(True)
        elif state == 'stopped':
            # When stopped: Start enabled, Pause and Stop disabled
            self.start_button.setEnabled(True)
            self.pause_button.setEnabled(False)
            self.stop_button.setEnabled(False)

    def schedule_recording(self):
        start_dt = self.start_time_edit.dateTime().toPython()
        end_dt = self.end_time_edit.dateTime().toPython()
        output_path = self.path_edit.text()

        if start_dt >= end_dt:
            QMessageBox.warning(self, 'Invalid Time', 'Start time must be before end time.')
            return

        self.scheduler.schedule_recording(start_dt, end_dt, output_path)
        QMessageBox.information(self, 'Scheduled', f'Recording scheduled from {start_dt} to {end_dt}.')

    def stop_recording(self):
        self.recorder.stop_recording()
        QMessageBox.information(self, 'Stopped', 'Recording stopped.')

    def closeEvent(self, event):
        self.scheduler.shutdown()
        self.recorder.stop_recording()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
