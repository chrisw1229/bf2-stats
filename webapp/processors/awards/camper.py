
import collections
from processors.awards import AwardProcessor,Column
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the total distance traveled between kills.

    Implementation
    Store position after each kill and add distance between current kill position
    and last kill position.  Reset the position after dying.

    Notes
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Camper', 'Shortest Distance Between Kills', [
                Column('Players'), Column('Meters', Column.NUMBER, Column.ASC)])

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
