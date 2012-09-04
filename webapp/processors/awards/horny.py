
from models import model_mgr
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
        AwardProcessor.__init__(self, 'Horny', 'Most Vehicle Horn Honks',
                [PLAYER_COL, Column('Honks', Column.NUMBER, Column.DESC)])
        self.horn_ids = ['car_horn', 'car_horn2', 'truck_horn']

    def on_accuracy(self, e):

        if e.weapon.id in self.horn_ids:
            player_stats = stat_mgr.get_player_stats(e.player)

            honks = 0
            for horn_id in self.horn_ids:
                weapon = model_mgr.get_weapon(horn_id)
                if weapon in player_stats.weapons:
                    honks += player_stats.weapons[weapon].bullets_fired
            self.results[e.player] = honks
