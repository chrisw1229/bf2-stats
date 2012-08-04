
import collections
from processors.awards import AwardProcessor,Column
from models import model_mgr
from models.kits import ANTI_TANK

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of kills while playing as the anti-tank class.

    Implementation
    Increment count if attacker's kit is anti-tank

    Notes
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Bomberman', 'Most Kills As Anti-Tank', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])
        
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return
            
        attacker_kit = model_mgr.get_kit(e.attacker.kit_id)
        if attacker_kit.kit_type == ANTI_TANK:
            self.results[e.attacker] += 1
