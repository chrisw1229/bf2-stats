
from processors.awards import AwardProcessor,Column
from models import model_mgr
from models.vehicles import AIR

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

    def on_kill(self, e):

        # Ignore kills where victim isn't passenger
        if not e.victim.passenger:
            return

        victim_vehicle = model_mgr.get_vehicle(e.victim.vehicle_id)
        if victim_vehicle.group == AIR:
            players = model_mgr.get_player_names()
            for player in players:
                playerObj = model_mgr.get_player_by_name(player)
                if playerObj.vehicle_id == e.victim.vehicle_id:
                    if playerObj.driver:
                        self.results[playerObj] += 1
