
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import players
from models import model_mgr
from models.vehicles import AIR

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of aircraft kills from the ground

    Implementation
    Check if the vehicle destroyed is an aircraft, the attacker is not in an
    aircraft and the destroyed aircraft is actually in the air. Acceptable
    flight altitude will be represented by 30 feet, which is actually 10 meters
    in game units.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Fly Swatter',
                'Most Aircraft Destroyed from Ground',
                [PLAYER_COL, Column('Destroyed', Column.NUMBER, Column.DESC)])

    def on_vehicle_destroy(self, e):

        # Ignore events caused by the environment
        if e.attacker == players.EMPTY:
            return

        # Ignore air-to-air attacks
        attacker_vehicle = model_mgr.get_vehicle(e.attacker.vehicle_id)
        if attacker_vehicle.group == AIR:
            return

        # Check whether an aircraft was killed while in flight
        if e.vehicle.group == AIR:
            if (e.vehicle_pos[1] - e.attacker_pos[1]) > 10:
                self.results[e.attacker] += 1
