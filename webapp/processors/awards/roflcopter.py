
from processors.awards import AwardProcessor,Column
from models import model_mgr
from models.vehicles import AIR

# TODO

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of kills for each player that do not include any
    assisting help from other players.

    Implementation
    This implementation takes advantage of the fact that every kill event is guaranteed to be
    immediately followed by its associatd assists. Whenever a kill event is received, the attacker
    gets an award point and the kill event is cached. If there are no subsequent assists, then the
    point stands as is. If there is at least one assist event received, then we remove the most
    recently awarded point.

    Notes
    Make sure a point is only subtracted once, since a kill could have multiple assists. Do not
    count suicides or team kills.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'ROFLcopter', 'Most Deaths Within 30 Seconds of Piloting an Aircraft', [
                Column('Players'), Column('Deaths', Column.NUMBER, Column.DESC)])

        # Keep track of the last kill event
        self.last_vehicle_entrance = dict()

    def on_death(self, e):
        if e.player in self.last_vehicle_entrance:
            # Arbitrarily set the death without an exit to within 30 seconds
            if e.elapsed(self.last_vehicle_entrance[e.player]) < 30:
                self.results[e.player] += 1
                del self.last_vehicle_entrance[e.player]
        
    def on_vehicle_enter(self, e):
        # Make sure we're only logging for air vehicle entrances
        player_vehicle = model_mgr.get_vehicle(e.player.vehicle_id)
        if player_vehicle.group != AIR:
            return
            
        if e.player not in self.last_vehicle_entrance:
            self.last_vehicle_entrance[e.player] = e
            
    def on_vehicle_exit(self, e):
        # Remove vehicle entrance log when the player exits the vehicle
        if e.player in self.last_vehicle_entrance:
            del self.last_vehicle_entrance[e.player]
