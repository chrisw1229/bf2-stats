
from processors.awards import AwardProcessor,Column
from models.vehicles import BOAT
from timer import Timer

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the amount of time a player spends driving
    boats.

    Implementation
    This implementation uses the timer object to automatically compute elapsed
    time based on game ticks as events are processed.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Jack Sparrow',
                'Most Time Driving Boats', [
                Column('Players'), Column('Time', Column.TIME, Column.DESC)])

        # Setup the results to store timers instead of numbers
        self.results = dict()

    def on_vehicle_enter(self, e):

        # Create a timer for the player as needed
        if not e.player in self.results:
            self.results[e.player] = Timer(e.player)

        # Start the timer for boat vehicles
        vehicle_type = e.vehicle.vehicle_type;
        if e.player.driver:
            if vehicle_type == BOAT:
                self.results[e.player].start(e.tick)

    def on_vehicle_exit(self, e):

        # Stop the timer for the player
        self.results[e.player].stop(e.tick)
