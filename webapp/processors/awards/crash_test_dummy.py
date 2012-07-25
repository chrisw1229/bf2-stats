
from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of deaths from vehicles.

    Implementation
	Whenever a kill event is received involving a vehicle, the kill event
    is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Crash Test Dummy', 'Most Deaths frm Vehicles', [
                Column('Players'), Column('Deaths', Column.NUMBER, Column.DESC)])
		
    def on_kill(self, e):
        # Ignore suicides
        if not e.suicide:
            return
        
        if e.vehicle:
            self.results[e.victim] += 1
                        
