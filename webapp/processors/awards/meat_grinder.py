
from processors.awards import AwardProcessor,Column
from models.weapons import LMG

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of kills using LMG weapons.

    Implementation
	Whenever a kill event is received involving a LMG, the kill event
    is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Meat Grinder', 'Most Kills with LMG', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])
		
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.weapon.weapon_type == LMG:
            self.results[e.attacker] += 1
