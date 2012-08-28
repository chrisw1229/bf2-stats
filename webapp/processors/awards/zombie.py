
from processors.awards import AwardProcessor,Column,PLAYER_COL
import collections

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of consecutive kills
    against a single player

    Implementation
    Keep track of last victim for each player (ignoring team kills).
    If the current victim is the same as the last, increment the temp counter.
    Otherwise reset it to 1.
    If the temp counter is greater than the current result, update the result
    for that player.
    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Zombie',
                'Most Times Revived in a Single Life',
                [PLAYER_COL, Column('Revives', Column.NUMBER, Column.DESC)])

        self.tempCounter = collections.Counter()

    def on_revive(self, e):

        self.tempCounter[e.receiver] += 1

    def on_death(self, e):

        self.results[e.player] = max( self.results[e.player], self.tempCounter[e.player] )

        self.tempCounter[e.player] = 0
