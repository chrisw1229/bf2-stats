
from processors.awards import AwardProcessor,Column,PLAYER_COL
import collections

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most damage received in a single life.

    Implementation
    Can't track damage, so this implementation tracks the number of heals/revives.
    The more times someone is healed the more damage they can take before dying.

    Notes
	May want to differentiate points for heal/revive?  Maybe make heal a random amount between 50-100?
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Black Knight',
                'Most Damage Received in a Single Life',
                [PLAYER_COL, Column('Damage', Column.NUMBER, Column.DESC)])

        self.tempCounter = collections.Counter()

    def on_heal(self, e):

        self.tempCounter[e.receiver] += 100.0
        
    def on_revive(self, e):

        self.tempCounter[e.receiver] += 100.0

    def on_death(self, e):

        self.results[e.player] = max( self.results[e.player], self.tempCounter[e.player] )

        self.tempCounter[e.player] = 0
