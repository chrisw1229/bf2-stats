
from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of times a player is revived.

    Implementation
	Whenever a revive event it's cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Frankenstein', 'Most Revivals', [
                Column('Players'), Column('Revivals', Column.NUMBER, Column.DESC)])

    def on_revive(self, e):

        self.results[e.receiver] += 1
