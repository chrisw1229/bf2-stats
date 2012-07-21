
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
		
    def on_kill(self, e):


        type = e.vehicle.vehicle_type;
        if type == HELICOPTER or type == JET:
            if e.attacker is None and e.victim_pos[1] > 100:
                self.results[e.victim] += 1
