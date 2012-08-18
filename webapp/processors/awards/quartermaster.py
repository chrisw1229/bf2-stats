
from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most ammo given.

    Implementation
	Whenever a ammo event occurs it's cached

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Quartermaster', 'Most Ammo Given', [
                Column('Players'), Column('Ammo Given', Column.NUMBER, Column.DESC)])

    def on_ammo(self, e):

        self.results[e.giver] += 1
