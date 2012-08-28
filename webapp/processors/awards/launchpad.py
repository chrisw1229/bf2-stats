
from processors.awards import AwardProcessor,Column,PLAYER_COL
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
        AwardProcessor.__init__(self, 'Launchpad',
                'Most Passenger Team Kills as Pilot',
                [PLAYER_COL, Column('Team Kills', Column.NUMBER, Column.DESC)])

        self.vehicles = dict()
        
    def on_vehicle_destroy(self, e):

        # Check whether a driver caused a vehicle to crash
        if e.attacker == EMPTY and e.driver != EMPTY:
            self.vehicles[e.vehicle] = e

    def on_kill(self, e):

        # Ignore kills where victim isn't passenger
        if not e.victim.passenger:
            return

        # Check whether the victim was in an aircraft
        v = model_mgr.get_vehicle(e.victim.vehicle_id)
        if v.group == AIR:

            # Check whether the vehicle was destroyed at the same time
            if v in self.vehicles and self.vehicles[v].tick == e.tick:

                # Make sure the victim and driver are teammates
                driver = self.vehicles[v].driver
                if driver.team_id == e.victim.team_id:
                    self.results[driver] += 1
