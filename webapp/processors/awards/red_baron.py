
from processors.awards import AwardProcessor,Column
from models import model_mgr
from models.vehicles import AIR

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of air to air kills.

    Implementation
	Whenever a kill event is received involving two air vehicles, the kill event
    is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Red Baron', 'Most Air to Air Kills', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        attacker_vehicle = model_mgr.get_vehicle(e.attacker.vehicle_id)
        victim_vehicle = model_mgr.get_vehicle(e.victim.vehicle_id)
        if attacker_vehicle.group == AIR and victim_vehicle.group == AIR:
            self.results[e.attacker] += 1
