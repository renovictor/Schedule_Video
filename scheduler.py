from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
from datetime import datetime

class RecordingScheduler:
    def __init__(self, recorder):
        self.recorder = recorder
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.status_callback = None  # Callback to update UI

    def set_status_callback(self, callback):
        """Set a callback function to update UI status"""
        self.status_callback = callback

    def _start_recording_wrapper(self):
        """Wrapper to start recording and update status"""
        try:
            self.recorder.start_recording()
            if self.status_callback:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.status_callback(f"[{timestamp}] Scheduled Recording Started")
        except Exception as e:
            if self.status_callback:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.status_callback(f"[{timestamp}] ERROR starting scheduled recording: {str(e)}")

    def _stop_recording_wrapper(self):
        """Wrapper to stop recording and update status"""
        try:
            self.recorder.stop_recording()
            if self.status_callback:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.status_callback(f"[{timestamp}] Scheduled Recording Stopped")
        except Exception as e:
            if self.status_callback:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.status_callback(f"[{timestamp}] ERROR stopping scheduled recording: {str(e)}")

    def schedule_recording(self, start_time, end_time, output_path=None):
        # Set output file if provided
        if output_path:
            self.recorder.output_file = output_path
        # Remove existing jobs if any
        self.scheduler.remove_all_jobs()

        # Schedule start
        start_trigger = DateTrigger(run_date=start_time)
        self.scheduler.add_job(self._start_recording_wrapper, trigger=start_trigger, id='start_recording')

        # Schedule stop
        stop_trigger = DateTrigger(run_date=end_time)
        self.scheduler.add_job(self._stop_recording_wrapper, trigger=stop_trigger, id='stop_recording')

    def shutdown(self):
        self.scheduler.shutdown()


