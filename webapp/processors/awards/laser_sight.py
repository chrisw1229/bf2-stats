
from processors.awards import AwardProcessor,Column
from stats import stat_mgr
from models.weapons import SOLDIER
from models.weapons import PRECISION
from models.players import EMPTY

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the longest kill distance (with bullet weapons).

    Implementation
	Whenever a kill event is received with a bullet weapon, calculate the distance
	and compare it to the attacker's current longest kill.  If longer, put it in
	the results.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Laser Signt', 'Longest Kill Distance', [
                Column('Players'), Column('Meters', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.weapon.group != SOLDIER or e.weapon.ammo != PRECISION:
            return

        if e.attacker == EMPTY:
            return

        dist = stat_mgr.dist_3d( e.attacker_pos, e.victim_pos )
        dist = abs(dist)
        if e.attacker not in self.results:
            self.results[e.attacker] = dist
        elif dist > self.results[e.attacker]:
            self.results[e.attacker] = dist
