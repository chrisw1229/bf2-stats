
from models import model_mgr,weapons
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
        AwardProcessor.__init__(self, 'Evasive Action',
                'Most Vehicle Countermeasures',
                [PLAYER_COL, Column('Counters', Column.NUMBER, Column.DESC)])

    def on_accuracy(self, e):

        if e.weapon.weapon_type == weapons.COUNTER:
            player_stats = stat_mgr.get_player_stats(e.player)

            counters = 0
            for weapon in model_mgr.get_weapons(weapons.COUNTER):
                if weapon in player_stats.weapons:
                    counters += player_stats.weapons[weapon].bullets_fired
            self.results[e.player] = counters
