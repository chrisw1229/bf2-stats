
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models.weapons import ASSAULT

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of kills using assault rifles.

    Implementation
	Whenever a kill event is received involving a shotgun, the kill event
    is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'SWAT', 'Most Kills with Assault Rifles',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])
		
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.weapon.weapon_type == ASSAULT:
            self.results[e.attacker] += 1
