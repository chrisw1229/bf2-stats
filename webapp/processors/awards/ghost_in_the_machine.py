
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import model_mgr
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of vehicles destroyed near a player

    Implementation
    When a vehicle is destroyed, find the distance of each player's current
    position to the destroyed vehicle and increment their count if less than 5 meters

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Ghost in the Machine',
                'Most Vehicles Destroyed Near Player',
                [PLAYER_COL, Column('Destroyed', Column.NUMBER, Column.DESC)])

    def on_vehicle_destroy(self, e):

        vpos = e.vehicle_pos

        for player in model_mgr.get_players():
            dist = stat_mgr.dist_3d(vpos, player.pos)
            if dist < 5:
                self.results[player] += 1
