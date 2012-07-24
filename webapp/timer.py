
from datetime import date, datetime, time, timedelta

class TimerManager(object):

    def __init__(self):
        self.enabled_timers = dict()
        self.disabled_timers = dict()
        self.last_tick = None

    def reset_timers(self):
        self.last_tick = None

        # Reset the state of each enabled timer
        for timer in self.enabled_timers.iterkeys():
            timer._reset()

        # Disable all timers
        self.disabled_timers.update(self.enabled_timers)
        self.enabled_timers.clear()
    
    def apply_tick(self, tick, auto_stop=False):

        # Skip processing when no time has actually elapsed
        if self.last_tick == tick: return
        self.last_tick = tick

        # Add elapsed time to each enabled timer
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
        self.debug = False

    def __repr__(self):
        delta_time = timedelta(seconds=self.elapsed)
        return str((Timer._BASE_TIME + delta_time).time())

    def start(self, tick):
        if self.running: return

        self.start_tick = tick
        self.last_tick = tick
        self.running = True

        timer_mgr._update_timer(self)

    def update(self, tick):
        if not self.running:
            print 'WARNING - Attempted to update a stopped timer'
            return

        if tick < self.last_tick:
            print 'WARNING - Elapsed time is going backwards'

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

        timer_mgr._update_timer(self)

    def _reset(self):
        self.running = False
        self.start_tick = None
        self.last_tick = None
        self.stop_tick = None
