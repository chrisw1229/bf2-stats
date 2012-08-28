from processors.awards import AwardProcessor,Column,PLAYER_COL
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the player with the most time spent in spectator.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Voyeur', 'Most Time Spent in Spectator',
                [PLAYER_COL, Column('Time', Column.NUMBER, Column.DESC)])

        self.results = dict()

    def on_spawn(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)
        self.results[e.player] = player_stats.spec_time
