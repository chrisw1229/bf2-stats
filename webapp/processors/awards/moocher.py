
from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most support received (ammo/heal/revive/repair).

    Implementation
	Whenever a ammo/heal/revive/repair event occurs it's cached (for me!)

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Moocher', 'Most Support Received',
                [PLAYER_COL, Column('Supported', Column.NUMBER, Column.DESC)])

    def on_ammo(self, e):

        self.results[e.receiver] += 1

    def on_heal(self, e):

        self.results[e.receiver] += 1
        
    def on_revive(self, e):

        self.results[e.receiver] += 1
