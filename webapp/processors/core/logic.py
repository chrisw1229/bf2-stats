
import models

from processors import BaseProcessor
from models import model_mgr
from stats import stat_mgr

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 10

    def on_ammo(self, e):

        # Update position for the players
        e.receiver.pos = e.receiver_pos
        e.giver.pos = e.giver_pos

    def on_assist(self, e):

        # Update position for the player
        e.player.pos = e.player_pos

    def on_commander(self, e):

        # Remove the commander flag from the previous player
        if e.team.commander_id:
            old_player = model_mgr.get_player(e.team.commander_id)
            if old_player:
                old_player.commander = False

        # Update the commander for the team
        if e.player == models.players.EMPTY:
            e.team.commander_id = None
        else:
            e.team.commander_id = e.player.id

        # Add the commander flag to the new player
        e.player.commander = True

    def on_connect(self, e):

        # Update the connection flag for the player
        e.player.connected = True
        e.player.bot = (e.player.address == None)

    def on_control_point(self, e):

        # Update the state of the control point
        e.control_point.status = e.status
        e.control_point.team_id = e.team.id
        e.control_point.trigger_id = e.trigger_id

    def on_death(self, e):

        # Update the state of the player
        e.player.spawned = False
        e.player.pos = e.player_pos
        e.player.wounded = False

    def on_disconnect(self, e):

        # Update the connected flag for the player
        e.player.connected = False

    def on_game_status(self, e):

        # Reset the game models on game start
        if e.game.starting:
            model_mgr.reset_models()

    def on_heal(self, e):

        # Update position for the players
        e.receiver.pos = e.receiver_pos
        e.giver.pos = e.giver_pos

    def on_kill(self, e):

        # Update position for the players
        e.victim.pos = e.victim_pos
        e.attacker.pos = e.attacker_pos

    def on_kit_drop(self, e):
    
        # Update the kit for the player
        e.player.kit_id = None

        # Update the position for the player
        e.player.pos = e.player_pos

    def on_kit_pickup(self, e):
    
        # Update the kit for the player
        e.player.kit_id = e.kit.id

        # Update the position for the player
        e.player.pos = e.player_pos

    def on_repair(self, e):

        # Update position for the player
        e.giver.pos = e.giver_pos

    def on_revive(self, e):

        # Update the wounded status for the player
        e.receiver.wounded = False

        # Update position for the players
        e.receiver.pos = e.receiver_pos
        e.giver.pos = e.giver_pos

    def on_spawn(self, e):

        # Update the spawned status for the player
        e.player.spawned = True

        # Update the team for the player
        self._update_team(e.player, e.team)

        # Update position for the player
        e.player.pos = e.player_pos

    def on_squad(self, e):

        # Make sure the squad is associated with a team
        if e.squad != models.squads.EMPTY:
            team = model_mgr.get_team(e.player.team_id)
            team.squad_ids.add(e.squad.id)

        # Remove the player from the previous squad
        if e.player.squad_id:
            old_squad = model_mgr.get_squad(e.squad.id)
            if old_squad and old_squad != models.squads.EMPTY:
                old_squad.player_ids.remove(e.player.id)
                if old_squad.leader_id == e.player.id:
                    old_squad.leader_id = None

        # Add the player to the new squad
        e.squad.player_ids.add(e.player.id)

        # Update the squad for the player
        e.player.squad_id = e.squad.id

        # Remove the squad leader flag from the player if needed
        if e.player.squad_id == models.squads.EMPTY.id:
            e.player.leader = False

    def on_squad_leader(self, e):

        # Remove the squad leader flag from the previous player
        if e.squad.leader_id:
            old_player = model_mgr.get_player(e.squad.leader_id)
            if old_player:
                old_player.leader = False

        # Update the leader for the squad
        if e.player == models.players.EMPTY:
            e.squad.leader_id = None
        else:
            e.squad.leader_id = e.player.id

        # Add the squad leader flag to the new player
        e.player.leader = True

    def on_team(self, e):

        # Update the team for the player
        self._update_team(e.player, e.team)

    def on_team_damage(self, e):

        # Update position for the players
        e.victim.pos = e.victim_pos
        e.attacker.pos = e.attacker_pos

    def on_vehicle_destroy(self, e):

        # Update position for the player
        e.attacker.pos = e.attacker_pos

    def on_vehicle_enter(self, e):

        # Update the vehicle for the player
        e.player.vehicle_id = e.vehicle.id
        e.player.vehicle_slot_id = e.vehicle_slot_id

        # Update the vehicle states for the player
        if e.vehicle_slot_id:
            if e.vehicle_slot_id.endswith('driver'):
                if e.vehicle.group == models.vehicles.STATION:
                    e.player.driver = False
                    e.player.passenger = False
                    e.player.operator = True
                else:
                    e.player.driver = True
                    e.player.passenger = False
                    e.player.operator = False
            else:
                e.player.driver = False
                e.player.passenger = True
                e.player.operator = False
        else:
            e.player.driver = False
            e.player.passenger = False
            e.player.operator = False

        # Update position for the player
        e.player.pos = e.player_pos

    def on_vehicle_exit(self, e):

        # Update the vehicle for the player
        e.player.vehicle_id = None
        e.player.vehicle_slot_id = None

        # Update the vehicle states for the player
        e.player.driver = False
        e.player.passenger = False
        e.player.operator = False

        # Update position for the player
        e.player.pos = e.player_pos

    def on_weapon(self, e):

        # Update the weapon for the player
        e.player.weapon_id = e.weapon.id

        # Update position for the player
        e.player.pos = e.player_pos

    def _update_team(self, player, team):

        # Check whether the team needs to be updated
        if player.team_id and player.team_id == team.id:
            return

        # Remove the player from the previous team
        if player.team_id:
            old_team = model_mgr.get_team(player.team_id)
            if old_team:
                old_team.player_ids.remove(player.id)
                if old_team.commander_id == player.id:
                    old_team.commander_id = None
                    player.commander = False

        # Add the player to the new team
        team.player_ids.add(player.id)

        # Update the team for the player
        player.team_id = team.id
