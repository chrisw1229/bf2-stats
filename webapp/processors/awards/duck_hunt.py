
from processors.awards import AwardProcessor,Column
from models import model_mgr
from models.vehicles import PARACHUTE

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most kills against parachuters

    Implementation
	Whenever a kill event is received involving a vehicle, the kill event
    is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Duck Hunt', 'Most Kills Against Players Parachuting', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        victim_vehicle = model_mgr.get_vehicle(e.victim.vehicle_id)
        if victim_vehicle.vehicle_type == PARACHUTE:
            self.results[e.attacker] += 1
