from processors.awards import AwardProcessor,Column
from models.weapons import EXPLOSIVE

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of suicides as a passenger.

    Implementation
	Whenever a kill event is received involving a vehicle that's a suicide, the kill event
    is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Hindenburg', 'Most Suicides as Vehicle Passenger', [
                Column('Players'), Column('Suicides', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):
        # only suicides
        if not e.suicide:
            return

        if e.victim.passenger and e.weapon.ammo == EXPLOSIVE:
            self.results[e.victim] += 1
