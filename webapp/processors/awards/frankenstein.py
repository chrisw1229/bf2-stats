
from processors.awards import AwardProcessor,Column

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
        AwardProcessor.__init__(self, 'Frankenstein', 'Most Revivals Given', [
                Column('Players'), Column('Revivals', Column.NUMBER, Column.DESC)])

    def on_revive(self, e):

        self.results[e.giver] += 1
