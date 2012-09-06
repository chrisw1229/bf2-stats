
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models.vehicles import AIR
from models import model_mgr
from stats import stat_mgr
from collections import Counter

class Processor(AwardProcessor):
    '''
    Overview
    This processor tracks the minimum avg. distance travelled between deaths.
    
    Implementation
    This implementation tracks the avg. distance travelled between deaths.
    (Distance between prior death and current death)

    Notes
    Assuming the intent is not the cumulative amount
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Sittin\' Duck',
                'Shortest Avg. Distance Between Deaths',
                [PLAYER_COL, Column('Distance', Column.NUMBER, Column.ASC)])

        # Store the last known position for each player
        self.player_to_pos = dict()
        self.distance = Counter()
        self.deaths = Counter()

    def on_death(self, e):

        if not e.player in self.player_to_pos:
            self.player_to_pos[e.player] = e.player_pos
            return

        last_pos = self.player_to_pos[e.player]
        dist = round(stat_mgr.dist_3d(last_pos, e.player_pos))
        self.distance[e.player] += dist

        self.deaths[e.player] += 1
        
        self.results[e.player] = round(self.distance[e.player] / self.deaths[e.player])

        # Store the current position for next time
        self.player_to_pos[e.player] = e.player_pos

    def on_spawn(self, e):

        if not e.player in self.results:
            self.results[e.player] = 99999999999999

    def on_game_event(self, e):

        if e.game.ending:
            self.player_to_pos.clear()
