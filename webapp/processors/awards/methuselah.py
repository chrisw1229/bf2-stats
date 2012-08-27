
import models
from processors.awards import AwardProcessor,Column
from timer import Timer
import collections

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the longest average life.

    Implementation
    This implementation uses the timer object to automatically compute elapsed
    time based on game ticks as events are processed.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Methuselah',
                'Longest Life', [
                Column('Players'), Column('Time', Column.TIME, Column.DESC)])

        # Setup the results to store timers instead of numbers
        self.results = dict()
        self.totalTime = dict()
        self.lives = collections.Counter()

    def on_spawn(self, e):

        # Create a timer for the player as needed
        if not e.player in self.totalTime:
            self.totalTime[e.player] = Timer(e.player)
            self.results[e.player] = Timer(e.player)

        # Start the timer
        self.totalTime[e.player].start(e.tick)
        # increment the number of lives
        self.lives[e.player] += 1

    def on_death(self, e):

        # Stop the timer for the player
        if e.player in self.totalTime:
            self.totalTime[e.player].stop(e.tick)

        if e.player in self.results:
            self.results[e.player].elapsed = self.totalTime[e.player].elapsed / self.lives[e.player]

    def on_disconnect(self, e):

        # Stop the timer for the player
        if e.player in self.totalTime:
            self.totalTime[e.player].stop(e.tick)

        if e.player in self.results:
            self.results[e.player].elapsed = self.totalTime[e.player].elapsed / self.lives[e.player]
