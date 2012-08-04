
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

        self.last_kill_pos = dict()
        
    def on_kill(self, e):

        if e.attacker in self.last_kill_pos:
            lastPos = self.last_kill_pos[e.attacker]
            distance = stat_mgr.dist_3d( lastPos, e.attacker_pos )
            self.results[e.attacker] += distance

        self.last_kill_pos[e.attacker] = e.attacker_pos

    def on_death(self, e):
        #remove last position on death/disconnect
        if e.player in self.last_kill_pos:
            del self.last_kill_pos[e.player]

    def on_disconnect(self, e):
        #remove last position on death/disconnect
        if e.player in self.last_kill_pos:
            del self.last_kill_pos[e.player]
