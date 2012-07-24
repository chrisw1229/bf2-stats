
from processors.awards import AwardProcessor,Column
from models.vehicles import STATION

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of kills against players on turrets (ground mounted).

    Implementation
	Whenever a kill event is received involving the killing of a player on a
	ground mounted turret, the kill event is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Assassin', 'Most Kills Against Players on Turrets', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])
		
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.vehicle.group == STATION:
            self.results[e.attacker] += 1
