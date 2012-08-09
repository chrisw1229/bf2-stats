
from processors.awards import AwardProcessor,Column
from stats import stat_mgr

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
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Nomad',
                'Longest Distance Between Kills', [
                Column('Players'), Column('Distance', Column.NUMBER, Column.DESC)])

        # Store the last known position for each player
        self.player_to_pos = dict()

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Ignore empty attackers
        if not e.attacker in self.player_to_pos:
            return

        # Calculate the distance traveled by the attacker to get the kill
        last_pos = self.player_to_pos[e.attacker]
        distance = stat_mgr.dist_3d(last_pos, e.attacker_pos)

        # Increment the distance for the attacker
        self.results[e.attacker] += round(distance)

        # Store the current position for next time
        self.player_to_pos[e.attacker] = e.attacker_pos

    def on_spawn(self, e):

        # Store the initial player position
        self.player_to_pos[e.player] = e.player_pos
