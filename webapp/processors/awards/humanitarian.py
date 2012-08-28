
from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most support given (ammo/heal/revive/repair).

    Implementation
	Whenever a ammo/heal/revive/repair event occurs it's cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Humanitarian', 'Most Support Given',
                [PLAYER_COL, Column('Support', Column.NUMBER, Column.DESC)])

    def on_ammo(self, e):

        self.results[e.giver] += 1

    def on_heal(self, e):

        self.results[e.giver] += 1
        
    def on_revive(self, e):

        self.results[e.giver] += 1

    def on_repair(self, e):

        self.results[e.giver] += 1
