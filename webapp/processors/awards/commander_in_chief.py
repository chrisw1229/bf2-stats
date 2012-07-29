
from processors.awards import AwardProcessor,Column
from timer import Timer

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the amount of time a player is commander
    
    Implementation
    This implementation uses the timer object to automatically compute elapsed
    time based on game ticks as events are processed.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Commander in Chief',
                'Most Time as Commander', [
                Column('Players'), Column('Time', Column.TIME, Column.DESC)])

        # Setup the results to store timers instead of numbers
        self.results = dict()

        self.currentCommanders = dict()

    def on_commander(self, e): #is there an event when someone resigns/mutiny?

        # Create a timer for the player as needed
        if not e.player in self.results:
            self.results[e.player] = Timer(e.player)

        if e.team in self.currentCommanders:
            #stop timer for old commander
            old = self.currentCommanders[e.team]
            self.results[old].stop(e.tick)
            
        #set new commander and start timer
        self.currentCommanders[e.team] = e.player
        self.results[e.player].start(e.tick)
