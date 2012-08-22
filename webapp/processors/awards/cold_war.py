
from processors.awards import AwardProcessor,Column
from models import players
from models import model_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most money wasted for the opposing team via destroyed vehicles

    Implementation
	Whenever a vehicle is destroyed, add the cost of the vehicle to the player's total

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Cold War', 'Most Money Wasted (for them)', [
                Column('Players'), Column('Million$', Column.NUMBER, Column.DESC)])

    def on_vehicle_destroy(self, e):
        self.results[e.attacker] += round(e.vehicle.cost)
