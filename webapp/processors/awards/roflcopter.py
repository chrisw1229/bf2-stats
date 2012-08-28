
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import model_mgr
from models.vehicles import AIR

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of aircraft destroyed within the
    first 30 seconds of entering it.

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
        AwardProcessor.__init__(self, 'ROFLcopter',
                'Most Aircraft Crashed Within 30 Seconds of Takeoff',
                [PLAYER_COL, Column('Crashed', Column.NUMBER, Column.DESC)])

        # Keep track of the last vehicle enter event
        self.last_vehicle_entrance = dict()

    def on_vehicle_destroy(self, e):

        # Check whether the driver entered within the last 30 seconds
        if e.driver in self.last_vehicle_entrance:
            if e.elapsed(self.last_vehicle_entrance[e.driver]) < 30:
                self.results[e.driver] += 1
                del self.last_vehicle_entrance[e.driver]
        
    def on_vehicle_enter(self, e):

        # Store the time when a player gets in an aircraft
        player_vehicle = model_mgr.get_vehicle(e.player.vehicle_id)
        if player_vehicle.group == AIR:
            self.last_vehicle_entrance[e.player] = e
