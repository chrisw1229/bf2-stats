
from processors.awards import AwardProcessor,Column
from models.vehicles import AIR
from models.vehicles import PARACHUTE

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most ejections

    Implementation
	Check to make sure a player has exited aircraft at altitude, increment results.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Skydiver',
                'Most Ejections', [
                Column('Players'), Column('Ejections', Column.NUMBER, Column.DESC)])

    def on_vehicle_exit(self, e):

        # Check whether a player ejected from an aircraft at altitude
        # Parachutes are included here since that could still cause death
        if e.vehicle.group == AIR and e.vehicle.vehicle_type != PARACHUTE and e.player_pos[1] > 30:
            self.results[e.player] += 1
