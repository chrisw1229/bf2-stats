
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models.vehicles import AIR
from models import model_mgr
from stats import stat_mgr
import collections

class Processor(AwardProcessor):
    '''
    Overview
    This processor tracks the maximum distance travelled between kills.
    
    Implementation
    This implementation tracks the distance travelled between kills...
    (Distance between prior kill and current kill) The fact that you ran
    around like a madman for 5 minutes doing laps around the map doesn't
    help you out in this case.

    Notes
    Only count kills that occur on the ground.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Nomad',
                'Longest Avg. Distance Between Kills',
                [PLAYER_COL, Column('Meters', Column.NUMBER, Column.DESC)])

        # Store the last known position for each player
        self.player_to_pos = dict()
        self.distance = collections.Counter()
        self.kills = collections.Counter()

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Ignore empty attackers
        if not e.attacker in self.player_to_pos:
            return

        # Ignore aircraft kills
        vehicle = model_mgr.get_vehicle(e.attacker.vehicle_id)
        if vehicle.group == AIR:
            return

        # Calculate the distance traveled by the attacker to get the kill
        last_pos = self.player_to_pos[e.attacker]
        distance = stat_mgr.dist_3d(last_pos, e.attacker_pos)

        # Increment the distance and kills for the attacker
        self.distance[e.attacker] += round(distance)
        self.kills[e.attacker] += 1
        # Display the average
        self.results[e.attacker] = round(self.distance[e.attacker] / self.kills[e.attacker])

        # Store the current position for next time
        self.player_to_pos[e.attacker] = e.attacker_pos

    def on_spawn(self, e):

        # Store the initial player position
        self.player_to_pos[e.player] = e.player_pos
