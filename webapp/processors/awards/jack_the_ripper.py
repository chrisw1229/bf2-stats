
from processors.awards import AwardProcessor,Column
from models.weapons import MELEE

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of kills using a Knife.

    Implementation
	Whenever a kill event is received involving a knife, the kill event
    is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Jack the Ripper', 'Most Kills with Knives', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])
		
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.weapon.weapon_type == MELEE:
			self.results[e.attacker] += 1
