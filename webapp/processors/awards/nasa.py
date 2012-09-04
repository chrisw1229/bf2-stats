
from processors.awards import AwardProcessor,Column,PLAYER_COL
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
        AwardProcessor.__init__(self, 'NASA','Highest Flight',
                [PLAYER_COL, Column('Meters', Column.NUMBER, Column.DESC)])

    def on_vehicle_exit(self, e):

        if e.vehicle.group == AIR:
            self.results[e.player] = round(max(self.results[e.player], e.player_pos[1]))

    def on_kill(self, e):

        self.results[e.attacker] = round(max(self.results[e.attacker], e.attacker_pos[1]))

        self.results[e.victim] = round(max(self.results[e.victim], e.victim_pos[1]))
