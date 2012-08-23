
from processors.awards import AwardProcessor,Column
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor is awarded to the player with the most ammo used.

    Implementation
    Get bullets fired from player stats

    Notes
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Trigger Happy', 'Most Ammo Used', [
                Column('Players'), Column('Bullets Fired', Column.NUMBER, Column.DESC)])

    def on_accuracy(self, e):

        player_stats = stat_mgr.get_player_stats(e.player)
        self.results[e.player] = player_stats.bullets_fired
