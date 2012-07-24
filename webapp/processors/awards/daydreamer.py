
from processors.awards import AwardProcessor,Column
from timer import Timer

class Processor(AwardProcessor):
    '''
    Overview
    This processor tracks the maximum time between kills.
    
    Implementation
    This implementation uses the timer object to automatically compute elapsed
    time based on game ticks as events are processed.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Daydreamer',
                'Longest Time Between Kills', [
                Column('Players'), Column('Time', Column.TIME, Column.DESC)])

        # Setup the results to store timers instead of numbers
        self.timer = dict()

        self.results = dict()

    def on_kill(self, e):

        if not e.valid_kill:
            return

        # Create a timer for the player as needed
        if not e.attacker in self.timer:
            self.timer[e.attacker] = Timer()
            self.results[e.attacker] = Timer()

        # Get the time since the last kill and compare to current max time
        if self.timer[e.attacker].running:
            self.results[e.attacker] = max(self.results[e.attacker].elapsed, self.timer[e.attacker].elapsed)
            self.timer[e.attacker].reset()

        # Start the timer for new kill
        self.results[e.attacker].start(e.tick)

    def on_death(self, e):

        # Stop the timer for the player
        self.timer[e.player].reset()
