
from models import weapons
from processors.awards import AwardProcessor,Column,PLAYER_COL
from stats import stat_mgr

class AwardResult(object):

    def __init__(self, kills, weapon):
        self.kills = kills
        self.weapon = weapon

    def __repr__(self):
        return [self.kills, self.weapon.name]

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most kills by a single weapon.

    Implementation
    Use player stats
    
    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'One Trick Pony',
                'Most Kills by a Single Weapon',
                [PLAYER_COL, Column('Kills', Column.ARRAY, Column.DESC)])

        self.results = dict()

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Make sure a weapon was used
        if e.weapon == weapons.EMPTY:
            return

        player_stats = stat_mgr.get_player_stats(e.attacker)
        weapon_stats = player_stats.weapons[e.weapon]

        if not e.attacker in self.results:
            self.results[e.attacker] = AwardResult(weapon_stats.kills, e.weapon)
        result = self.results[e.attacker]

        if weapon_stats.kills > result.kills:
            result.kills = weapon_stats.kills
            result.weapon = e.weapon
