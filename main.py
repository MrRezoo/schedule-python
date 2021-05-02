from functools import partial, update_wrapper


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
        self.job_func = None
        self.last_run = None
        self.next_run = None
        self.unit = None
        self.period = None

    @property
    def second(self):
        assert self.interval == 1
        return self.seconds

    @property
    def seconds(self):
        self.unit = 'seconds'
        return self

    @property
    def minute(self):
        assert self.interval == 1
        return self.minutes

    @property
    def minutes(self):
        self.unit = 'minutes'
        return self

    def do(self, jub_func, *args, **kwargs):
        self.job_func = partial(jub_func, *args, **kwargs)
        update_wrapper(self.job_func, jub_func)
        self._schedule_next_run()
        return self

    def _schedule_next_run(self):
        pass
