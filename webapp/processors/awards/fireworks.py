
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models.weapons import ROCKET
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the person with the most kills by front projectile shots

    Implementation
	Check whether the a rocket weapon was used and if the attackers are facing
    

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Fireworks',
                'Most Kills by Front Projectiles',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Check whether a projectile weapon was used
        if e.weapon.weapon_type == ROCKET:

            # Check whether the attacker and victim are facing each other
            if stat_mgr.angle_opp(e.victim_pos, e.attacker_pos):
                self.results[e.attacker] += 1
