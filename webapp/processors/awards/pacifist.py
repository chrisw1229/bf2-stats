
from processors.awards import AwardProcessor,Column,PLAYER_COL
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor is awarded to the player with the least ammo used.

    Implementation
    Get bullets fired from player stats

    Notes
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Pacifist', 'Least Ammo Used',
                [PLAYER_COL, Column('Bullets Fired', Column.NUMBER, Column.ASC)])

    def on_accuracy(self, e):

        player_stats = stat_mgr.get_player_stats(e.player)
        self.results[e.player] = player_stats.bullets_fired
