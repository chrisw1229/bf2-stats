
from processors.awards import AwardProcessor,Column,PLAYER_COL
from stats import stat_mgr

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
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        player_stats = stat_mgr.get_player_stats(e.attacker)
        kills = 0
        for weapon in player_stats.weapons:
            w = player_stats.weapons[weapon]
            kills = max( w.kills, kills )

        self.results[e.attacker] = kills
