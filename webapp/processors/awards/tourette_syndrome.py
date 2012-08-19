
from processors.awards import AwardProcessor,Column
from models import model_mgr
from models.vehicles import STATION

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of kills using turrets (ground mounted).

    Implementation
	Cache kill events where the attacker is using a turret.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Tourette Syndrome',
                'Most Kills with Turrets', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])
		
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        attack_vehicle = model_mgr.get_vehicle(e.attacker.vehicle_id)
        if attack_vehicle.group == STATION:
            self.results[e.attacker] += 1
