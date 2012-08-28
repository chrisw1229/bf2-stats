
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models.weapons import GRENADE
from stats import stat_mgr
from models import model_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of kills for each player that occur
    when their victim is facing them.

    Implementation
    This implementation determines the directionality of a kill based on the
    rotation parameter of both the victim and the attacker. No throwable weapons
    are counted.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'In Your Face',
                'Most Kills by Front Shots',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Check to make sure the weapon type is not a throwable type (GRENADE)
        attacker_weapon = model_mgr.get_weapon(e.attacker.weapon_id)
        if attacker_weapon == GRENADE:
            return

        # Check whether the attacker and victim are facing each other
        if stat_mgr.angle_opp(e.victim.pos, e.attacker.pos):
            self.results[e.attacker] += 1
