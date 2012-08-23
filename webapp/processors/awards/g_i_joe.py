
from processors.awards import AwardProcessor,Column
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
        AwardProcessor.__init__(self, 'G.I. Joe', 'Most Ammo and Fewest Kills', [
                Column('Players'), Column('Anti-Performance', Column.NUMBER, Column.DESC)])

    def on_accuracy(self, e):

        player_stats = stat_mgr.get_player_stats(e.player)
        kills = player_stats.kills_total + 1 #ensure the kill total is at least 1
        ammo = player_stats.bullets_fired
        self.results[e.player] = ( ammo * 1.0 ) / ( kills * 1.0 )
