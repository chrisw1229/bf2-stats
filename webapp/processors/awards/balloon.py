
from processors.awards import AwardProcessor,Column
from models.vehicles import PARACHUTE
from timer import Timer

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the longest time someone is in a parachute

    Implementation
    This implementation uses the timer object to automatically compute elapsed
    time based on game ticks as events are processed.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Balloon',
                'Longest Parachute Flight', [
                Column('Players'), Column('Time', Column.TIME, Column.DESC)])

        # Setup the results to store timers instead of numbers
        self.results = dict()

        # Store temporary timers for each player
        self.timers = dict()

    def on_disconnect(self, e):

        # Same as exit event but make sure the timer exists
        if e.player in self.timers:
            self.timers[e.player].stop(e.tick)

            # Swap timers if the time difference is the new maximum
            if self.timers[e.player].elapsed > self.results[e.player].elapsed:
                temp_timer = self.results[e.player]
                self.results[e.player] = self.timers[e.player]
                self.timers[e.player] = temp_timer

    def on_vehicle_enter(self, e):

        vehicle_type = e.vehicle.vehicle_type;
        if not vehicle_type == PARACHUTE:
            return;

        # Create a timer for the player as needed
        if not e.player in self.results:
            self.results[e.player] = Timer(e.player)
            self.timers[e.player] = Timer(e.player)

        # Start the timer
        self.timers[e.player].reset()
        self.timers[e.player].start(e.tick)

    def on_vehicle_exit(self, e):

        if not e.player in self.results:
            return

        # Stop the timer for the player
        self.timers[e.player].stop(e.tick)

        # Swap timers if the time difference is the new maximum
        if self.timers[e.player].elapsed > self.results[e.player].elapsed:
            temp_timer = self.results[e.player]
            self.results[e.player] = self.timers[e.player]
            self.timers[e.player] = temp_timer
