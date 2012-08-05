
from processors.awards import AwardProcessor,Column
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
        AwardProcessor.__init__(self, 'Deficit', 'Most $ Wasted', [
                Column('Players'), Column('Million$', Column.NUMBER, Column.DESC)])

    def on_vehicle_destroy(self, e):

        self.results[e.attacker] += e.vehicle.cost

    def on_kill(self, e):
        # give pilots/drivers who crash on their own 'credit'

        if e.victim.passenger:
            return
        
        if e.attacker == players.EMPTY:
            victim_vehicle = model_mgr.get_vehicle(e.victim.vehicle_id)
            self.results[e.victim] += victim_vehicle.cost
