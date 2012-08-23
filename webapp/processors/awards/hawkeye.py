
from processors.awards import AwardProcessor,Column
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor is awarded to the player with the highest accuracy.

    Implementation
    Get bullets fired and hit from player stats

    Notes
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Hawkeye', 'Highest Weapon Accuracy', [
                Column('Players'), Column('Accuracy', Column.NUMBER, Column.DESC)])

    def on_accuracy(self, e):

        player_stats = stat_mgr.get_player_stats(e.player)
        hits = player_stats.bullets_hit
        fired = player_stats.bullets_fired
        self.results[e.player] = 100.0 * ( hits ) / ( fired * 1.0 )
