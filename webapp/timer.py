
from datetime import date, datetime, time, timedelta

class TimerManager(object):

    def __init__(self):
        self.enabled_timers = dict()
        self.disabled_timers = dict()

    def apply_tick(self, tick):
        for timer in self.enabled_timers.iterkeys():
            timer.update(tick)

    def _update_timer(self, timer):
        if not timer: return

        if timer.running:
            if timer in self.disabled_timers:
                del self.disabled_timers[timer]
            self.enabled_timers[timer] = True
        else:
            if timer in self.enabled_timers:
                del self.enabled_timers[timer]
            self.disabled_timers[timer] = True

timer_mgr = TimerManager()

class Timer(object):

    _BASE_TIME = datetime.combine(date.today(), time())

    def __init__(self):
        self.running = False
        self.start_tick = None
        self.last_tick = None
        self.stop_tick = None
        self.elapsed = 0

    def start(self, tick):
        if self.running: return

        self.start_tick = tick
        self.last_tick = tick
        self.running = True

        timer_mgr._update_timer(self)

    def update(self, tick):
        if not self.running: return

        self.elapsed += (tick - self.last_tick)
        self.last_tick = tick

    def stop(self, tick):
        if not self.running: return

        self.stop_tick = tick
        self.update(tick)
        self.running = False

        timer_mgr._update_timer(self)

    def reset(self):
        self.running = False
        self.start_tick = None
        self.last_tick = None
        self.stop_tick = None
        self.elapsed = 0

        timer_mgr._update_timer(self)

    def format(self):
        delta_time = timedelta(seconds=self.elapsed)
        return str((Timer._BASE_TIME + delta_time).time())
