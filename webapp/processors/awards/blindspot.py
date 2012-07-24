
from processors.awards import AwardProcessor,Column
from models.vehicles import HELICOPTER
from models.vehicles import JET

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most deaths

    Implementation
	Whenever a kill event is received involving a helicopter/jet, the attacker
        is null, and the victim is above the ground the event is cached

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Blindspot', 'Most Aircraft Deaths from Buildings', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

        self.startPos = dict()

    def on_vehicle_enter(self, e):
        self.startPos[e.player] = e.player_pos[1]
		
    def on_kill(self, e):
        vehicle_type = e.vehicle.vehicle_type

        if vehicle_type == HELICOPTER or vehicle_type == JET:
            height = e.victim_pos[1] - self.startPos[e.victim]

            if e.attacker is None and height > 100:
                #need to playtest the height
                self.results[e.victim] += 1
