
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import model_mgr
from models.vehicles import HELICOPTER, JET, PARACHUTE

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of kills from jets hitting parachuters.

    Implementation
    Check if the victim is in a parachute and was hit by a jet

    Notes
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Bug Splat',
                'Most Kills Against Parachuters with an Aircraft',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])
        
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return
            
        victim_vehicle = model_mgr.get_vehicle(e.victim.vehicle_id)
        if victim_vehicle.vehicle_type == PARACHUTE:
            if (e.vehicle.vehicle_type == JET
                    or e.vehicle.vehicle_type == HELICOPTER):
                self.results[e.attacker] += 1
