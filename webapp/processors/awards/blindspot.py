
from processors.awards import AwardProcessor,Column
from models import players
from models.vehicles import HELICOPTER
from models.vehicles import JET
from models import model_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most deaths from crashing into buildings

    Implementation
	Whenever a kill event is received involving a helicopter/jet, the attacker
    is null, and the victim is above the ground the event is cached. The
    threshold after some play testing is 100ft. or about 30m.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Blindspot',
                'Most Aircraft Deaths from Buildings', [
                Column('Players'), Column('Deaths', Column.NUMBER, Column.DESC)])

        self.startPos = dict()

    def on_vehicle_enter(self, e):
        self.startPos[e.player] = e.player_pos[1]

    def on_kill(self, e):

        # Make sure only the driver gets credit
        if e.victim.passenger:
            return
        
        # Check whether the victim vehicle was an aircraft
        victim_vehicle = model_mgr.get_vehicle(e.victim.vehicle_id)
        if (victim_vehicle.vehicle_type == HELICOPTER
                or victim_vehicle.vehicle_type == JET):

            # Compute the height difference of the victim
            height = e.victim_pos[1] - self.startPos[e.victim]

            # Check whether the victim died to nobody at a sufficient height
            if e.attacker == players.EMPTY and height > 30:
                self.results[e.victim] += 1
