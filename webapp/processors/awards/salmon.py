from processors.awards import AwardProcessor,Column,PLAYER_COL
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the players with the most deaths near spawn points.

    Implementation
    Capture spawn location and compare it to death location
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Salmon', 'Most Deaths Near Spawn Points',
                [PLAYER_COL, Column('Deaths', Column.NUMBER, Column.DESC)])

        self.spawn_pos = dict()

    def on_spawn(self, e):
        self.spawn_pos[e.player] = e.player_pos

    def on_death(self, e):
        dist = stat_mgr.dist_3d(self.spawn_pos[e.player], e.player_pos)
        if dist < 10:
            self.results[e.player] += 1
