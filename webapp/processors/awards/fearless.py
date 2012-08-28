
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models.weapons import SOLDIER

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of kills against vehicles
    using soldier carried weapons.

    Implementation
    On kill events check if the weapon is a soldier weapon and the victim is in a vehicle

    Notes
    Ignore kills with victim on stationary turrets?
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Fearless',
                'Most Kills Against Vehicles with Weapons',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])
		
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.weapon.group == SOLDIER and (e.victim.driver or e.victim.passenger):
            self.results[e.attacker] += 1
