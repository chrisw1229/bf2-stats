
from processors.awards import AwardProcessor,Column,PLAYER_COL
from timer import Timer

class Processor(AwardProcessor):
    '''
    Overview
    Tracks the shortest life

    Implementation
    This implementation uses the timer object to automatically compute elapsed
    time based on game ticks as events are processed.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Stillborn', 'Shortest Life',
                [PLAYER_COL, Column('Time', Column.TIME, Column.ASC)])

        # Setup the results to store timers instead of numbers
        self.results = dict()
        self.timers = dict()

    def on_spawn(self, e):

        # Create a timer for the player as needed
        if not e.player in self.timers:
            self.timers[e.player] = Timer(e.player)

        self.timers[e.player].reset()
        self.timers[e.player].start(e.tick)

    def on_death(self, e):
        
        # Stop the timer for the player
        self.timers[e.player].stop(e.tick)

        if self.timers[e.player].elapsed == 0:
            return

        if not e.player in self.results:
            self.results[e.player] = Timer(e.player)
            self.results[e.player].elapsed = self.timers[e.player].elapsed
            
        if self.timers[e.player] < self.results[e.player]:
            self.results[e.player].elapsed = self.timers[e.player].elapsed
