
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import model_mgr
from models.kits import MEDIC

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of kills as a medic.

    Implementation
	Whenever a kill event is received involving a medic, the kill event
    is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Dr. Kevorkian', 'Most Kills as Medic',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        attacker_kit = model_mgr.get_kit(e.attacker.kit_id)
        if attacker_kit.kit_type == MEDIC:
            self.results[e.attacker] += 1
