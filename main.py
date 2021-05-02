class Schedule:
    def __init__(self):
        self.job = []

    def every(self, interval=1):
        job = Job(interval)
        self.job.append(job)
        return job


class Job:
    def __init__(self, interval):
        self.interval = interval
        self.job_dunc = None
        self.last_run = None
        self.next_run = None
        self.unit = None
        self.period = None
