
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
        AwardProcessor.__init__(self, 'Serial Killer',
                'Most Consecutive Kills Against a Single Player',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

        self.lastVictim = dict()
        self.tempCounter = collections.Counter()

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            #set last victim so team kills end streak
            self.lastVictim[e.attacker] = e.victim
            return

        if e.attacker not in self.lastVictim:
            self.lastVictim[e.attacker] = e.victim

        if e.victim == self.lastVictim[e.attacker]:
            self.tempCounter[e.attacker] += 1
        else:
            self.tempCounter[e.attacker] = 1

        self.lastVictim[e.attacker] = e.victim
        self.results[e.attacker] = max(self.tempCounter[e.attacker],
                                       self.results[e.attacker])
