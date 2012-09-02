
from processors.awards import AwardProcessor,Column,PLAYER_COL
import collections

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most kills by a single shot.

    Implementation
    Keep track of the time of the last kill for each player.  If the current time
    is the same as the last time, increment a temporary counter. Compare it to the
    current results value. If times differ, set last kill time and reset counter to 1
    
    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Opportunist',
                'Most Kills by a Single Shot',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

        self.lastKillTime = dict()
        self.count = collections.Counter()

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.attacker not in self.lastKillTime:
            self.lastKillTime[e.attacker] = e.tick
            self.count[e.attacker] = self.results[e.attacker] = 1
            return
            
        elif e.tick == self.lastKillTime[e.attacker]:
            self.count[e.attacker] += 1
            self.results[e.attacker] = max( self.results[e.attacker], self.count[e.attacker] )
            
        else:
            self.lastKillTime[e.attacker] = e.tick
            self.count[e.attacker] = 0
            
