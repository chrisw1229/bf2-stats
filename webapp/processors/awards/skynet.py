
from processors.awards import AwardProcessor,Column
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
        AwardProcessor.__init__(self, 'Skynet', 'Most Kills as Engineer', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        attacker_kit = model_mgr.get_kit(e.attacker.kit_id)
        if attacker_kit.kit_type == ENGINEER:
            self.results[e.attacker] += 1
