
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import players
from models.vehicles import LAND
from models import model_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most deaths from stuck vehicles

    Implementation
	Whenever a kill event is received involving a land vehicle and the attacker
    is null, the event is cached

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Thelma & Louise',
                'Most Deaths from Stuck Vehicles',
                [PLAYER_COL, Column('Deaths', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):
        
        victim_vehicle = model_mgr.get_vehicle(e.victim.vehicle_id)
        if victim_vehicle.group == LAND and e.attacker == players.EMPTY:
            self.results[e.victim] += 1
