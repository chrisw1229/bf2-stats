
from processors.awards import AwardProcessor,Column
from models import players
from models.vehicles import HELICOPTER
from models.vehicles import JET
from models.vehicles import PARACHUTE
from models import model_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most deaths from ejecting

    Implementation
        Set the eject status to false on spawning.
	Check to make sure a player has exited aircraft at altitude.
	When a player is killed see if the attacker is nobody.
	Also check if a player has parachuted a significant height 

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Goose',
                'Most Deaths from Ejections', [
                Column('Players'), Column('Deaths', Column.NUMBER, Column.DESC)])

        self.startPos = dict()
        self.ejectPos = dict()
        self.eject = dict()

    def on_spawn(self, e):
        
        self.startPos[e.player] = 0.0
        self.ejectPos[e.player] = 0.0
        self.eject[e.player] = False

    def on_vehicle_enter(self, e):

        if e.vehicle.vehicle_type == HELICOPTER or e.vehicle.vehicle_type == JET:
            self.startPos[e.player] = e.player_pos[1]

    def on_vehicle_exit(self, e):

        if e.vehicle.vehicle_type == HELICOPTER or e.vehicle.vehicle_type == JET:
            if (e.player_pos[1] - self.startPos[e.player]) > 100:
                self.eject[e.player] = True #player ejected at altitude
                self.ejectPos[e.player] = e.player_pos[1]

        if e.vehicle.vehicle_type == PARACHUTE:
            if (self.ejectPos[e.player] - e.player_pos[1]) > 200:
                self.eject[e.player] = False #player must have parachuted safely over 200 meters

    def on_kill(self, e):

        # Check whether the victim died to nobody
        if e.attacker == players.EMPTY and self.eject[e.victim] == True:
            self.results[e.victim] += 1
