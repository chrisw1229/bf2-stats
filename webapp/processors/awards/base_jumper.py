
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models.vehicles import PARACHUTE

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of parachutes the player uses.

    Implementation
	Whenever a vehicle enter event is received involving the parachuting of a player, 
    the vehicle enter event is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Base Jumper', 'Most Parachute Jumps',
                [PLAYER_COL, Column('Jumps', Column.NUMBER, Column.DESC)])

    def on_vehicle_enter(self, e):

        # Check that the vehicle entered was a parachute
        if e.vehicle.vehicle_type == PARACHUTE:
			self.results[e.player] += 1
