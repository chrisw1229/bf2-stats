
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models.weapons import PISTOL

class Processor(AwardProcessor):
    '''
    Overview
        This processor keeps track of kills using pistols.

    Implementation
	Kills where attacker's weapon is a pistol are cached

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Cowboy', 'Most Kills with Pistols',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])
		
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.weapon.weapon_type == PISTOL:
            self.results[e.attacker] += 1
