
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import model_mgr
from models.kits import SNIPER

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of kills as sniper

    Implementation
	Cache kill events involving a sniper.
    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Scopetastic',
                'Most Kills with Sniper Kit',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Check whether the kill weapon belongs to the sniper kit
        attacker_kit = model_mgr.get_kit(e.attacker.kit_id)
        if attacker_kit.kit_type == SNIPER:
            if e.weapon.id in attacker_kit.weapon_ids:
                self.results[e.attacker] += 1
