
import models

from processors import BaseProcessor
from models import model_mgr
from stats import stat_mgr

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 0

    def on_ammo(self, e):
        giver_stats = stat_mgr.get_player_stats(e.giver)

        # Increment ammo points for the player
        giver_stats.ammo_points += 1
        giver_stats.ammo_points_total += 1

    def on_assist(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Increment assist count for the player
        player_stats.assists += 1
        player_stats.assists_total += 1

    def on_commander(self, e):

        # Remove the commander flag from the previous player
        if e.team.commander_id:
            old_player = model_mgr.get_player(e.team.commander_id)
            if old_player:
                old_player.commander = False

        # Update the commander for the team
        e.team.commander_id = e.player.id

        # Add the commander flag to the new player
        e.player.commander = True

    def on_connect(self, e):

        # Update the connection flag for the player
        e.player.connected = True
        e.player.artificial = (e.player.address == None)

    def on_death(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Increment death count for the player
        player_stats.deaths += 1
        player_stats.deaths_total += 1

        # Update death streaks for the player
        player_stats.death_streak += 1
        if player_stats.death_streak > player_stats.death_streak_max:
            player_stats.death_streak_max = player_stats.death_streak
        player_stats.kill_streak = 0

    def on_disconnect(self, e):

        # Update the connection flags for the player
        e.player.connected = False

    def on_heal(self, e):
        giver_stats = stat_mgr.get_player_stats(e.giver)

        # Increment heal points for the player
        giver_stats.heal_points += 1
        giver_stats.heal_points_total += 1

    def on_kill(self, e):
        victim_stats = stat_mgr.get_player_stats(e.victim)
        attacker_stats = stat_mgr.get_player_stats(e.attacker)

        # Check whether the kill was actually a suicide
        if e.victim == e.attacker:
            attacker_stats.suicides += 1
            attacker_stats.suicides_total += 1
            return

        # Check whether the kill was actually a teammate
        if e.victim.team_id == e.attacker.team_id:
            attacker_stats.team_kills += 1
            attacker_stats.team_kills_total += 1
            return

        # Increment wound count for the victim
        victim_stats.wounds += 1
        victim_stats.wounds_total += 1

        # Increment kill count for the attacker
        attacker_stats.kills += 1
        attacker_stats.kills_total += 1

        # Update kill streaks for the attacker
        attacker_stats.kill_streak += 1
        if attacker_stats.kill_streak > attacker_stats.kill_streak_max:
            attacker_stats.kill_streak_max = attacker_stats.kill_streak
        attacker_stats.death_streak = 0

    def on_repair(self, e):
        giver_stats = stat_mgr.get_player_stats(e.giver)

        # Increment repair points for the player
        giver_stats.repair_points += 1
        giver_stats.repair_points_total += 1

    def on_revive(self, e):
        giver_stats = stat_mgr.get_player_stats(e.giver)

        # Increment revive points for the player
        giver_stats.revive_points += 1
        giver_stats.revive_points_total += 1

    def on_score(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Increment score count for the player
        player_stats.score += e.value
        player_stats.score_total += e.value

    def on_spawn(self, e):

        # Update the team for the player
        self._update_team(e.player, e.team)

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
        e.squad.leader_id = e.player.id

        # Add the squad leader flag to the new player
        e.player.leader = True

    def on_team(self, e):

        # Update the team for the player
        self._update_team(e.player, e.team)

    def on_vehicle_enter(self, e):

        # Update the player vehicle
        e.player.vehicle_id = e.vehicle.id

    def on_vehicle_exit(self, e):

        # Update the player vehicle
        e.player.vehicle_id = None

    def _update_team(self, player, team):

        # Check whether the team needs to be updated
        if player.team_id and player.team_id == team.id:
            return

        # Remove the player from the previous team
        if player.team_id:
            old_team = model_mgr.get_team(player.team_id)
            if old_team:
                old_team.players_ids.remove(player.id)
                if old_team.commander_id == player.id:
                    old_team.commander_id = None
                    player.commander = False

        # Add the player to the new team
        team.player_ids.add(player.id)

        # Update the team for the player
        player.team_id = team.id
