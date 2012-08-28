
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import model_mgr
from models.vehicles import HELICOPTER

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of kills using a Helicopter.

    Implementation
	Whenever a kill event is received involving a helicopter, the kill event
    is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Airwolf', 'Most Kills from Helicopters',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        attacker_vehicle = model_mgr.get_vehicle(e.attacker.vehicle_id)
        if attacker_vehicle.vehicle_type == HELICOPTER:
            self.results[e.attacker] += 1
