
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import model_mgr
from models.kits import MEDIC

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
        AwardProcessor.__init__(self, 'Malpratice', 'Most Deaths from Medics',
                [PLAYER_COL, Column('Deaths', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        attacker_kit = model_mgr.get_kit(e.attacker.kit_id)
        if attacker_kit.kit_type == MEDIC:
            self.results[e.victim] += 1