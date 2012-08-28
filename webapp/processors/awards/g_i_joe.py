
from processors.awards import AwardProcessor,Column,PLAYER_COL
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor is awarded to the player with the most ammo used and fewest kills.

    Implementation
    Divide ammo used by kills

    Notes
    May have to threshold kills or time played to avoid skewing results by people with only 1/2 kills.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'G.I. Joe', 'Most Ammo and Fewest Kills',
                [PLAYER_COL, Column('Ammo / Kills', Column.PERCENT, Column.DESC)])

    def on_accuracy(self, e):
        self._update(e.player)

    def on_kill(self, e):
        if not e.valid_kill:
            return

        self._update(e.attacker)

    def _update(self, player):
        player_stats = stat_mgr.get_player_stats(player)
        kills = player_stats.kills_total
        ammo = player_stats.bullets_fired
        self.results[player] = [ammo, kills]
