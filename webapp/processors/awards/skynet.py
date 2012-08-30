
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import model_mgr
from models.kits import ENGINEER

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of kills as an engineer

    Implementation
	Whenever a kill event is received involving an engineer, the kill event
    is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Skynet', 'Most Kills with Engineer Kit',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Check whether the kill weapon belongs to the engineer kit
        attacker_kit = model_mgr.get_kit(e.attacker.kit_id)
        if attacker_kit.kit_type == ENGINEER:
            if e.weapon.id in attacker_kit.weapon_ids:
                self.results[e.attacker] += 1
