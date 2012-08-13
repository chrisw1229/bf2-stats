
from processors.awards import AwardProcessor,Column
from models import model_mgr
from models.vehicles import AIR
from models.players import EMPTY

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most passengers killed by their pilot.

    Implementation
    Check if the victim is a passenger of an air vehicle, find pilot and increment his/her count

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Launchpad', 'Most Passenger Kills as Pilot', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

        self.times = dict()
        self.drivers = dict()
        
    def on_vehicle_destroy(self, e):
        
        if e.attacker == EMPTY and e.driver != EMPTY:
            self.times[e.vehicle] = e.tick
            self.drivers[e.vehicle] = e.driver
            
    def on_kill(self, e):

        # Ignore kills where victim isn't passenger
        if not e.victim.passenger:
            return

        v = model_mgr.get_vehicle(e.victim.vehicle_id)
        if v.group == AIR:
            if v in self.times and v in self.drivers and self.times[v] == e.tick:
                driver = self.drivers[v]
                self.results[driver] += 1
