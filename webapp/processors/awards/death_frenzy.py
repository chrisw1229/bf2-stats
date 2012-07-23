from processors.awards import AwardProcessor,Column
from collections import Counter

class Processor(AwardProcessor):
    '''
    Overview
    This processor is awarded to the player with the most deaths in a row
    without a kill.

    Implementation
    The basic idea is to keep track of the current death streak and check whether
    it is a new personal best for the player.

    Notes
    
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Death Frenzy', 'Most Deaths in a row', [
                Column('Players'), Column('Deaths', Column.NUMBER, Column.DESC)])

        # Keep track of the current kill streak
        self.current = Counter()

    def on_death(self, e):
        self.current[e.player] += 1
        self.results[e.victim] = max(self.results[e.victim], self.current[e.victim])

    def on_kill(self, e):

        # Ignore suicides
        if e.suicide:
            self.current[e.victim] -= 1
            return
        
        #reset for attacker
        self.current[e.attacker] = 0
