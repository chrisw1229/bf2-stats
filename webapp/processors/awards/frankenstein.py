
from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of times a player revives a
    teammate.

    Implementation
	Whenever a revive event it's cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Frankenstein', 'Most Revivals Given',
                [PLAYER_COL, Column('Revivals', Column.NUMBER, Column.DESC)])

    def on_revive(self, e):

        self.results[e.giver] += 1
