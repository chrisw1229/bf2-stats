
from processors.awards import AwardProcessor,Column,PLAYER_COL
from stats import stat_mgr
from models.weapons import ARTILLERY

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the player with the most kills against higher ranked players.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Underdog',
                'Most Kills Against Higher Ranked Players',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):
        if e.weapon.weapon_type != ARTILLERY:
            attacker_stats = stat_mgr.get_player_stats(e.attacker)
            victim_stats = stat_mgr.get_player_stats(e.victim)

            if attacker_stats.rank <= 1 and victim_stats.rank >= 3:
                self.results[e.attacker] += 1
