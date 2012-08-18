
from processors.awards import AwardProcessor,Column
from models.vehicles import ARTILLERY

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most artillery destroyed

    Implementation
    Cache vehicle destroy events when the type is artillery

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Mission Impossible', 'Most Artillery Destroyed', [
                Column('Players'), Column('Artillery Destroyed', Column.NUMBER, Column.DESC)])
		
    def on_vehicle_destroy(self, e):

        if e.vehicle.vehicle_type == ARTILLERY:
            self.results[e.attacker] += 1
