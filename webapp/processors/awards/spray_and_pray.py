
from processors.awards import AwardProcessor,Column
from models.weapons import SMG

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of kills using submachine guns.

    Implementation
	Whenever a kill event is received involving a smg, the kill event
    is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Spray \'n Pray', 'Most Kills with SMGs', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])
		
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.weapon.weapon_type == SMG:
            self.results[e.attacker] += 1
