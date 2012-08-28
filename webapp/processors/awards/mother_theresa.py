
from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most heals given.

    Implementation
	Whenever a heal event occurs it's cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Mother Theresa', 'Most Heals Given',
                [PLAYER_COL, Column('Heals', Column.NUMBER, Column.DESC)])

    def on_heal(self, e):

        self.results[e.giver] += 1
