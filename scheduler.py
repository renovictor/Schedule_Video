from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger

class RecordingScheduler:
    def __init__(self, recorder):
        self.recorder = recorder
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    def schedule_recording(self, start_time, end_time, output_path=None):
        # Set output file if provided
        if output_path:
            self.recorder.output_file = output_path
        # Remove existing jobs if any
        self.scheduler.remove_all_jobs()

        # Schedule start
        start_trigger = DateTrigger(run_date=start_time)
        self.scheduler.add_job(self.recorder.start_recording, trigger=start_trigger, id='start_recording')

        # Schedule stop
        stop_trigger = DateTrigger(run_date=end_time)
        self.scheduler.add_job(self.recorder.stop_recording, trigger=stop_trigger, id='stop_recording')

    def shutdown(self):
        self.scheduler.shutdown()
