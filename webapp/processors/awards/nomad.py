
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

        # Store temporary distances for each player
        self.locations = dict()

    def on_death(self, e):

        # Reset the location for the player
        if e.player in self.locations:
            del self.locations[e.player]

    def on_kill(self, e):

        # Ignore team kills and suicides
        if not e.valid_kill:
            return

        # Zero out the current max distance if there hasn't been one entered for the player yet
        if e.attacker not in self.results:
            self.results[e.attacker] = 0.0            
            
        # Log current position for the attacker as needed
        if e.attacker not in self.locations:
            self.locations[e.attacker] = e.attacker.pos
            return
        
        # If we enter at this point the attacker has a previous valid kill that we can
        # compare against
        dist = stat_mgr.dist_2d(self.locations[e.attacker], e.attacker.pos)
        if dist > self.results[e.attacker]:
            self.results[e.attacker] = dist
            
        # Log the current position for the player
        self.locations[e.attacker] = e.attacker.pos
