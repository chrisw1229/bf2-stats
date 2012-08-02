
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
                'Longest Time Without a Kill', [
                Column('Players'), Column('Time', Column.TIME, Column.DESC)])

        # Setup the results to store timers instead of numbers
        self.results = dict()

        # Store temporary timers for each player
        self.timers = dict()

    def on_death(self, e):

        # Stop the player timer
        self.timers[e.player].stop(e.tick)

        # Swap timers if the time difference is the new maximum
        if self.timers[e.player].elapsed > self.results[e.player].elapsed:
            temp_timer = self.results[e.player]
            self.results[e.player] = self.timers[e.player]
            self.timers[e.player] = temp_timer

    def on_disconnect(self, e):

        # Stop the player timer
        self.timers[e.player].stop(e.tick)

        # Swap timers if the time difference is the new maximum
        if self.timers[e.player].elapsed > self.results[e.player].elapsed:
            temp_timer = self.results[e.player]
            self.results[e.player] = self.timers[e.player]
            self.timers[e.player] = temp_timer

    def on_kill(self, e):

        # Ignore team kills and suicides
        if not e.valid_kill:
            return

        # Ignore the empty player
        if not e.attacker in self.timers:
            return

        # Stop the timer for the current kill
        self.timers[e.attacker].stop(e.tick)

        # Swap timers if the time difference is the new maximum
        if self.timers[e.attacker].elapsed > self.results[e.attacker].elapsed:
            temp_timer = self.results[e.attacker]
            self.results[e.attacker] = self.timers[e.attacker]
            self.timers[e.attacker] = temp_timer

        # Reset the attacker timer for the next kill
        self.timers[e.attacker].reset()
        self.timers[e.attacker].start(e.tick)

    def on_spawn(self, e):

        # Create timers for the player
        if not e.player in self.results:
            self.results[e.player] = Timer(e.player)
            self.timers[e.player] = Timer(e.player)

        # Start the player timer
        self.timers[e.player].start(e.tick)
