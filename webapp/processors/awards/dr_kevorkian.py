
from processors.awards import AwardProcessor,Column
from models.kits import MEDIC

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of kills as a medic.

    Implementation
	Whenever a kill event is received involving a medic, the kill event
    is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Dr. Kevorkian', 'Most Kills as Medic', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])
		
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.attacker.kit_id == MEDIC:
            self.results[e.attacker] += 1
