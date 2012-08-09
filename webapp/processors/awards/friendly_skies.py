
from processors.awards import AwardProcessor,Column
from models.vehicles import JET
from models.vehicles import HELICOPTER
from timer import Timer

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the longest flight time without a kill.

    Implementation
    This implementation uses the timer object to automatically compute elapsed
    time based on game ticks as events are processed.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Friendly Skies',
                'Longest Flight Time without a Kill', [
                Column('Players'), Column('Time', Column.TIME, Column.DESC)])

        # Setup the results to store timers instead of numbers
        self.results = dict()

        # Store temporary timers for each player
        self.timers = dict()

    def on_vehicle_enter(self, e):

        # Create a timer for the player as needed
        if not e.player in self.results:
            self.results[e.player] = Timer(e.player)
            self.timers[e.player] = Timer(e.player)

        # Start the timer for aircraft vehicles
        vehicle_type = e.vehicle.vehicle_type;
        if e.player.driver:
            if vehicle_type == HELICOPTER or vehicle_type == JET:
                self.timers[e.player].reset()
                self.timers[e.player].start(e.tick)

    def on_vehicle_exit(self, e):

        # Stop the timer for the player
        self.timers[e.player].stop(e.tick)

        # Swap timers if the time difference is the new maximum
        if self.timers[e.player].elapsed > self.results[e.player].elapsed:
            temp_timer = self.results[e.player]
            self.results[e.player] = self.timers[e.player]
            self.timers[e.player] = temp_timer

    def on_kill(self, e):

        # Ignore kills if the attacker isn't in our results
        if not e.attacker in self.results:
            return
            
        # Stop the timer for the player
        self.timers[e.attacker].stop(e.tick)

        # Swap timers if the time difference is the new maximum
        if self.timers[e.attacker].elapsed > self.results[e.attacker].elapsed:
            temp_timer = self.results[e.attacker]
            self.results[e.attacker] = self.timers[e.attacker]
            self.timers[e.attacker] = temp_timer
