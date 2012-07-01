
from processors.awards import AwardProcessor,Column
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
        AwardProcessor.__init__(self, 'Base Jumper', 'Most Parachute Flights', [
                Column('Players'), Column('Drops', Column.NUMBER, Column.DESC)])
		
    def on_vehicle_enter(self, e):

        # Check that the vehicle entered was a parachute
        if e.vehicle.group == PARACHUTE:
			self.results[e.attacker] += 1
