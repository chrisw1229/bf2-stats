from processors.awards import AwardProcessor,Column
from events import event_mgr
from models import model_mgr
from models.vehicles import ARMOR
from models.vehicles import TRANSPORT

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the players with the most tank kills by jeep passengers.
    Points are given to each member of the jeep.

    Implementation
    On kill, check if the victim's vehicle is a tank.
    Increment the count for the attacker if he is a passenger in a "jeep".
    
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Jeep Squad', 'Most Tank Kills by Vehicle Passenger', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):
        #Ignore suicides and team kills
        if not e.valid_kill:
            return

        tank_check = model_mgr.get_vehicle(e.victim.vehicle_id)
        if tank_check.vehicle_type != ARMOR:
            return

        jeep_check = model_mgr.get_vehicle(e.attacker.vehicle_id)
        if jeep_check.vehicle_type != TRANSPORT:
            return #may have to exclude some transports? i.e. amphibious
        
        if e.attacker.driver:
            return

        self.results[e.attacker] += 1
    #points for driver/other passengers?
