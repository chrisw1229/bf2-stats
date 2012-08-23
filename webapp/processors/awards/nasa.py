
from processors.awards import AwardProcessor,Column
from models.vehicles import AIR
from models.vehicles import PARACHUTE

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the highest flight

    Implementation
    Check height for vehicle exits and 
    
    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'NASA','Highest Flight', [
                Column('Players'), Column('Height', Column.NUMBER, Column.DESC)])

    def on_vehicle_exit(self, e):

        if e.vehicle.group == AIR:
            self.results[e.player] = max( self.results[e.player], e.player_pos[1] )

    def on_kill(self, e):

        self.results[e.attacker] = max( self.results[e.attacker], e.attacker_pos[1] )

        self.results[e.victim] = max( self.results[e.victim], e.victim_pos[1] )
