
from processors.awards import AwardProcessor,Column
from models.weapons import ROCKET

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
        AwardProcessor.__init__(self, 'Fireworks', 'Most Kills by Front Projectiles', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Check whether a projectile weapon was used
        if e.weapon.weapon_type == ROCKET:

            # Check whether the attacker victim are facing each other
            angle_diff = abs(e.victim_pos[3] - e.attacker_pos[3])
            if angle_diff >= 90 and angle_diff <= 270:
                self.results[e.attacker] += 1
