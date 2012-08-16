
from processors.awards import AwardProcessor,Column
from stats import stat_mgr
from models.players import EMPTY

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the distance traveled by each player.

    Implementation
	Set the initial spawn position in on_spawn event, then update the
	position and calculate the distance from the last position on every
	event where the position is given.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Explorer', 'Most Distance Traveled', [
                Column('Players'), Column('Meters', Column.NUMBER, Column.DESC)])

        self.lastPos = dict();
        self.lastPos[EMPTY] = EMPTY.pos

    def on_spawn(self, e):
        self.lastPos[e.player] = e.player_pos

    def on_ammo(self, e):
        dist = stat_mgr.dist_3d(self.lastPos[e.giver], e.giver_pos);
        self.results[e.giver] += round(dist)
        self.lastPos[e.giver] = e.giver_pos

        dist = stat_mgr.dist_3d(self.lastPos[e.receiver], e.receiver_pos);
        self.results[e.receiver] += round(dist)
        self.lastPos[e.receiver] = e.receiver_pos

    def on_assist(self, e):
        dist = stat_mgr.dist_3d(self.lastPos[e.player], e.player_pos);
        self.results[e.player] += round(dist)
        self.lastPos[e.player] = e.player_pos

    def on_death(self, e):
        dist = stat_mgr.dist_3d(self.lastPos[e.player], e.player_pos);
        self.results[e.player] += round(dist)
        self.lastPos[e.player] = e.player_pos
        
    def on_heal(self, e):
        dist = stat_mgr.dist_3d(self.lastPos[e.giver], e.giver_pos);
        self.results[e.giver] += round(dist)
        self.lastPos[e.giver] = e.giver_pos

        dist = stat_mgr.dist_3d(self.lastPos[e.receiver], e.receiver_pos);
        self.results[e.receiver] += round(dist)
        self.lastPos[e.receiver] = e.receiver_pos
        
    def on_kill(self, e):
        dist = stat_mgr.dist_3d(self.lastPos[e.attacker], e.attacker_pos);
        self.results[e.attacker] += round(dist)
        self.lastPos[e.attacker] = e.attacker_pos

        dist = stat_mgr.dist_3d(self.lastPos[e.victim], e.victim_pos);
        self.results[e.victim] += round(dist)
        self.lastPos[e.victim] = e.victim_pos

    def on_kit_drop(self, e):
        dist = stat_mgr.dist_3d(self.lastPos[e.player], e.player_pos);
        self.results[e.player] += round(dist)
        self.lastPos[e.player] = e.player_pos
        
    def on_kit_pickup(self, e):
        dist = stat_mgr.dist_3d(self.lastPos[e.player], e.player_pos);
        self.results[e.player] += round(dist)
        self.lastPos[e.player] = e.player_pos

    def on_repair(self, e):
        dist = stat_mgr.dist_3d(self.lastPos[e.giver], e.giver_pos);
        self.results[e.giver] += round(dist)
        self.lastPos[e.giver] = e.giver_pos

    def on_revive(self, e):
        dist = stat_mgr.dist_3d(self.lastPos[e.giver], e.giver_pos);
        self.results[e.giver] += round(dist)
        self.lastPos[e.giver] = e.giver_pos

        dist = stat_mgr.dist_3d(self.lastPos[e.receiver], e.receiver_pos);
        self.results[e.receiver] += round(dist)
        self.lastPos[e.receiver] = e.receiver_pos

    def on_team_damage(self, e):
        dist = stat_mgr.dist_3d(self.lastPos[e.attacker], e.attacker_pos);
        self.results[e.attacker] += round(dist)
        self.lastPos[e.attacker] = e.attacker_pos

        dist = stat_mgr.dist_3d(self.lastPos[e.victim], e.victim_pos);
        self.results[e.victim] += round(dist)
        self.lastPos[e.victim] = e.victim_pos

    def on_vehicle_destroy(self, e):
        dist = stat_mgr.dist_3d(self.lastPos[e.attacker], e.attacker_pos);
        self.results[e.attacker] += round(dist)
        self.lastPos[e.attacker] = e.attacker_pos

    def on_vehicle_enter(self, e):
        dist = stat_mgr.dist_3d(self.lastPos[e.player], e.player_pos);
        self.results[e.player] += round(dist)
        self.lastPos[e.player] = e.player_pos

    def on_vehicle_exit(self, e):
        dist = stat_mgr.dist_3d(self.lastPos[e.player], e.player_pos);
        self.results[e.player] += round(dist)
        self.lastPos[e.player] = e.player_pos

    def on_weapon(self, e):
        dist = stat_mgr.dist_3d(self.lastPos[e.player], e.player_pos);
        self.results[e.player] += round(dist)
        self.lastPos[e.player] = e.player_pos
