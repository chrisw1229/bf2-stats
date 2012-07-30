
from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of times a player repairs a vehicle.

    Implementation
	Caches each repair event.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Grease Monkey', 'Most Vehicle Repairs', [
                Column('Players'), Column('Repairs', Column.NUMBER, Column.DESC)])

    def on_repair(self, e):

        self.results[e.giver] += 1
