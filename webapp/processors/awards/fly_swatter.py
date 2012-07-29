
from processors.awards import AwardProcessor,Column
from models import players
from models.vehicles import JET
from models.vehicles import HELICOPTER
from models import model_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of aircraft kills from the ground

    Implementation
    Check if the vehicle destroyed is an aircraft, the attacker is not in an aircraft
    and the destroyed aircraft is actually in the air

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Fly Swatter',
                'Most Aircraft Kills from Ground', [
                Column('Players'), Column('Aircraft Destroyed', Column.TIME, Column.DESC)])


    def on_vehicle_destroy(self, e):

        if e.attacker == players.EMPTY:
            return
        
        attack_vehicle = model_mgr.get_vehicle(e.attacker.vehicle_id)
        if attack_vehicle == HELICOPTER or attack_vehicle == JET:
            return #ignore kill
        
        vehicle_type = e.vehicle.vehicle_type;

        if vehicle_type == HELICOPTER or vehicle_type == JET:
            height = e.vehicle_pos[1] - e.attacker_pos[1]
            if height > 10: #playtest?
                self.results[e.attacker] += 1

