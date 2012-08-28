
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import players
from models import model_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most money wasted via destroyed vehicles

    Implementation
	Whenever a vehicle is destroyed, add the cost of the vehicle to the player's total

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Deficit', 'Most Money Wasted',
                [PLAYER_COL, Column('Million$', Column.NUMBER, Column.DESC)])

    def on_vehicle_destroy(self, e):
        self.results[e.driver] += round(e.vehicle.cost)
