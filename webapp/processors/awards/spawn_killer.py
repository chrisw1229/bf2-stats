from processors.awards import AwardProcessor,Column
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the players with the most kills on people near
    spawn points.

    Implementation
    Capture spawn locations and compare to victim kill location
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Spawn Killer', 'Most Kills on People Near Spawn Points', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

        self.spawn_pos = dict()

    def on_spawn(self, e):
        self.spawn_pos[e.player] = e.player_pos

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return
        
        dist = stat_mgr.dist_3d(self.spawn_pos[e.victim], e.victim_pos)
        if dist < 10:
            self.results[e.attacker] += 1
