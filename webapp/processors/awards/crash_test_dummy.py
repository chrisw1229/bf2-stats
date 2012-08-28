
from processors.awards import AwardProcessor,Column,PLAYER_COL

from models import vehicles

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of deaths from vehicles.

    Implementation
	Whenever a kill event is received involving a vehicle, the kill event
    is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Crash Test Dummy',
                'Most Deaths from Vehicles',
                [PLAYER_COL, Column('Deaths', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides
        if e.suicide:
            return

        # Check whether the attacker was using a vehicle
        if e.vehicle != vehicles.EMPTY:
            self.results[e.victim] += 1
