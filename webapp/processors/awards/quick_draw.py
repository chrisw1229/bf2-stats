
from processors.awards import AwardProcessor,Column
from timer import Timer

# TODO

class Processor(AwardProcessor):
    '''
    Overview
    This processor tracks the minimum time between kills.
    
    Implementation
    This implementation uses the timer object to automatically compute elapsed
    time based on game ticks as events are processed.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Quick Draw',
                'Shortest Time Between Kills', [
                Column('Players'), Column('Time', Column.TIME, Column.DESC)])

        # Setup the results to store timers instead of numbers
        self.results = dict()

        # Store temporary timers for each player
        self.timers = dict()

    def on_death(self, e):

        # Reset the timer for the player
        if e.player in self.timers:
            self.timers[e.player].reset()

    def on_disconnect(self, e):

        # Same as exit event but make sure the timer exists
        if e.player in self.timers:
            self.timers[e.player].stop(e.tick)

            # Swap timers if the time difference is the new minimum
            if self.results[e.player].elapsed > self.timers[e.player].elapsed:
                temp_timer = self.results[e.player]
                self.results[e.player] = self.timers[e.player]
                self.timers[e.player] = temp_timer

    def on_kill(self, e):

        # Ignore team kills and suicides
        if not e.valid_kill:
            return

        # Create timers for the attacker as needed
        if not e.attacker in self.results:
            self.results[e.attacker] = Timer(e.attacker)
            self.timers[e.attacker] = Timer(e.attacker)

        # Check whether the attacker has killed previously for the current life
        if self.timers[e.attacker].running:

            # Stop the timer for the current kill
            self.timers[e.attacker].stop(e.tick)

            # Swap timers if the time difference is the new minimum
            if self.results[e.attacker].elapsed > self.timers[e.attacker].elapsed:
                temp_timer = self.results[e.attacker]
                self.results[e.attacker] = self.timers[e.attacker]
                self.timers[e.attacker] = temp_timer

        # Reset the attacker timer for the next kill
        self.timers[e.attacker].reset()
        self.timers[e.attacker].start(e.tick)
