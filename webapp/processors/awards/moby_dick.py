
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import model_mgr
from models.vehicles import BOAT

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of kills using a boat.

    Implementation
	Check whether the attacker for a kill was using a boat.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Moby Dick', 'Most Kills from Boats',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        attacker_vehicle = model_mgr.get_vehicle(e.attacker.vehicle_id)
        if attacker_vehicle.vehicle_type == BOAT:
            self.results[e.attacker] += 1
