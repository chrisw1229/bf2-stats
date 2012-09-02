
from processors.awards import AwardProcessor,Column,PLAYER_COL
from stats import stat_mgr
from models.players import EMPTY
from models.vehicles import JET
from models.vehicles import HELICOPTER

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
        AwardProcessor.__init__(self, 'Explorer', 'Most Distance Traveled',
                [PLAYER_COL, Column('Meters', Column.NUMBER, Column.DESC)])

        self.lastPos = dict();
        self.lastPos[EMPTY] = EMPTY.pos
        self.disableAir = dict();
        self.disableAir[EMPTY] = True

    def on_spawn(self, e):
        self.lastPos[e.player] = e.player_pos
        self.disableAir[e.player] = False

    def on_ammo(self, e):
        if not self.disableAir[e.giver]:
            dist = stat_mgr.dist_3d(self.lastPos[e.giver], e.giver_pos);
            self.results[e.giver] += round(dist)
            self.lastPos[e.giver] = e.giver_pos

        if not self.disableAir[e.receiver]:
            dist = stat_mgr.dist_3d(self.lastPos[e.receiver], e.receiver_pos)
            self.results[e.receiver] += round(dist)
            self.lastPos[e.receiver] = e.receiver_pos

    def on_assist(self, e):
        if self.disableAir[e.player]:
            return
        dist = stat_mgr.dist_3d(self.lastPos[e.player], e.player_pos);
        self.results[e.player] += round(dist)
        self.lastPos[e.player] = e.player_pos

    def on_death(self, e):
        if self.disableAir[e.player]:
            return
        dist = stat_mgr.dist_3d(self.lastPos[e.player], e.player_pos);
        self.results[e.player] += round(dist)
        self.lastPos[e.player] = e.player_pos
        
    def on_heal(self, e):
        if not self.disableAir[e.giver]:
            dist = stat_mgr.dist_3d(self.lastPos[e.giver], e.giver_pos);
            self.results[e.giver] += round(dist)
            self.lastPos[e.giver] = e.giver_pos

        if not self.disableAir[e.receiver]:
            dist = stat_mgr.dist_3d(self.lastPos[e.receiver], e.receiver_pos)
            self.results[e.receiver] += round(dist)
            self.lastPos[e.receiver] = e.receiver_pos
        
    def on_kill(self, e):
        if not self.disableAir[e.attacker]:
            dist = stat_mgr.dist_3d(self.lastPos[e.attacker], e.attacker_pos);
            self.results[e.attacker] += round(dist)
            self.lastPos[e.attacker] = e.attacker_pos

        if not self.disableAir[e.victim]:
            dist = stat_mgr.dist_3d(self.lastPos[e.victim], e.victim_pos)
            self.results[e.victim] += round(dist)
            self.lastPos[e.victim] = e.victim_pos

    def on_kit_drop(self, e):
        if self.disableAir[e.player]:
            return
        dist = stat_mgr.dist_3d(self.lastPos[e.player], e.player_pos);
        self.results[e.player] += round(dist)
        self.lastPos[e.player] = e.player_pos
        
    def on_kit_pickup(self, e):
        if self.disableAir[e.player]:
            return
        dist = stat_mgr.dist_3d(self.lastPos[e.player], e.player_pos);
        self.results[e.player] += round(dist)
        self.lastPos[e.player] = e.player_pos

    def on_repair(self, e):
        if self.disableAir[e.giver]:
            return
        dist = stat_mgr.dist_3d(self.lastPos[e.giver], e.giver_pos);
        self.results[e.giver] += round(dist)
        self.lastPos[e.giver] = e.giver_pos

    def on_revive(self, e):
        if not self.disableAir[e.giver]:
            dist = stat_mgr.dist_3d(self.lastPos[e.giver], e.giver_pos);
            self.results[e.giver] += round(dist)
            self.lastPos[e.giver] = e.giver_pos

        if not self.disableAir[e.receiver]:
            dist = stat_mgr.dist_3d(self.lastPos[e.receiver], e.receiver_pos)
            self.results[e.receiver] += round(dist)
            self.lastPos[e.receiver] = e.receiver_pos

    def on_team_damage(self, e):
        if not self.disableAir[e.attacker]:
            dist = stat_mgr.dist_3d(self.lastPos[e.attacker], e.attacker_pos);
            self.results[e.attacker] += round(dist)
            self.lastPos[e.attacker] = e.attacker_pos

        if not self.disableAir[e.victim]:
            dist = stat_mgr.dist_3d(self.lastPos[e.victim], e.victim_pos)
            self.results[e.victim] += round(dist)
            self.lastPos[e.victim] = e.victim_pos

    def on_vehicle_destroy(self, e):
        if self.disableAir[e.attacker]:
            return
        dist = stat_mgr.dist_3d(self.lastPos[e.attacker], e.attacker_pos);
        self.results[e.attacker] += round(dist)
        self.lastPos[e.attacker] = e.attacker_pos

    def on_vehicle_enter(self, e):
        dist = stat_mgr.dist_3d(self.lastPos[e.player], e.player_pos);
        self.results[e.player] += round(dist)
        self.lastPos[e.player] = e.player_pos
        vehicle_type = e.vehicle.vehicle_type
        if vehicle_type == HELICOPTER or vehicle_type == JET:
            self.disableAir[e.player] = True
            

    def on_vehicle_exit(self, e):
        if self.disableAir[e.player]:
            self.lastPos[e.player] = e.player_pos
            self.disableAir[e.player] = False
            return
        dist = stat_mgr.dist_3d(self.lastPos[e.player], e.player_pos)
        self.results[e.player] += round(dist)
        self.lastPos[e.player] = e.player_pos

    def on_weapon(self, e):
        if self.disableAir[e.player]:
            return
        dist = stat_mgr.dist_3d(self.lastPos[e.player], e.player_pos);
        self.results[e.player] += round(dist)
        self.lastPos[e.player] = e.player_pos
