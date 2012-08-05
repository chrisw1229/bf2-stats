
from processors.awards import AwardProcessor,Column
from models import model_mgr
from models.vehicles import AIR

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of ground kills using an air vehcile.

    Implementation
    Assume that if the victim isn't in an air vehcile they're on the ground.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Death From Avove', 'Most Ground Kills from Aircraft', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        attacker_vehicle = model_mgr.get_vehicle(e.attacker.vehicle_id)
        victim_vehicle = model_mgr.get_vehicle(e.victim.vehicle_id)
        if attacker_vehicle.group == AIR and victim_vehicle.group != AIR:
            self.results[e.attacker] += 1
