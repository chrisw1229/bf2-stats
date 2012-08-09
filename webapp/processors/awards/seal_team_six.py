
from processors.awards import AwardProcessor,Column
from models import model_mgr
from models.kits import SPEC_OPS

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of deaths from a medic.

    Implementation
	Whenever a kill event is received involving a medic, the death event
    is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'SEAL Team 6', 'Most Kills as Special Forces', [
                Column('Players'), Column('Deaths', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        attacker_kit = model_mgr.get_kit(e.attacker.kit_id)
        if attacker_kit.kit_type == SPEC_OPS:
            self.results[e.attacker] += 1