
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import model_mgr
from models.kits import SPEC_OPS

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of kills as spec-ops

    Implementation
	Cache kill events involving spec-ops.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'SEAL Team Six',
                'Most Kills with Spec-Ops Kit',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Check whether the kill weapon belongs to the spec-ops kit
        attacker_kit = model_mgr.get_kit(e.attacker.kit_id)
        if attacker_kit.kit_type == SPEC_OPS:
            if e.weapon.id in attacker_kit.weapon_ids:
                self.results[e.attacker] += 1
