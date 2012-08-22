
import models

from events import FlagActionEvent, KillEvent, event_mgr
from processors import BaseProcessor
from models import model_mgr
from stats import PlayerItemStats, PlayerWeaponStats, stat_mgr

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 20
        self.vehicles = dict()

    def on_accuracy(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Update the accuracy for the player
        # Note that a base value must be used since accuracy is reset on death
        if not e.weapon in player_stats.weapons:
            player_stats.weapons[e.weapon] = PlayerWeaponStats()
        weapon_stats = player_stats.weapons[e.weapon]
        weapon_stats.bullets_hit = weapon_stats._bullets_hit + e.bullets_hit
        weapon_stats.bullets_fired = weapon_stats._bullets_fired + e.bullets_fired

        # Update ammo used for the player
        self._update_ammo(e.player)

    def on_ammo(self, e):
        receiver_stats = stat_mgr.get_player_stats(e.receiver)
        giver_stats = stat_mgr.get_player_stats(e.giver)

        # Increment supply points for the receiver
        receiver_stats.supplied += 1
        receiver_stats.supplied_total += 1

        # Increment supply points for the giver
        giver_stats.supplies += 1
        giver_stats.supplies_total += 1

        # Increment teamwork for the giver
        giver_stats.teamwork += 1
        giver_stats.teamwork_total += 1

    def on_assist(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Increment assist count for the player
        player_stats.assists += 1
        player_stats.assists_total += 1

        # Increment teamwork count for the player
        player_stats.teamwork += 1
        player_stats.teamwork_total += 1

        # Get the last kill event that occurred
        global_history = event_mgr.get_history()
        kill_event = global_history.get_new_event(KillEvent.TYPE)

        # Increment the assisted count for the attacker
        attacker_stats = stat_mgr.get_player_stats(kill_event.attacker)
        attacker_stats.assisted += 1
        attacker_stats.assisted_total += 1

    def on_commander(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)
        old_player_stats = stat_mgr.get_player_stats(e.old_player)

        # Update the associated commander timers
        player_stats.commander_time.start(e.tick)
        player_stats.squad_time.stop(e.tick)
        old_player_stats.commander_time.stop(e.tick)

    def on_connect(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Start the spectator timer when the player connects
        player_stats.spec_time.start(e.tick)

    def on_death(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)
        player_history = event_mgr.get_history(e.player)

        # Get the last known kit for the player
        # Player will no longer have an active kit at this point
        player_kit = event_mgr.get_last_kit(e.player)

        # Get the team and weapon for the player
        player_team = model_mgr.get_team(e.player.team_id)
        player_weapon = model_mgr.get_weapon(e.player.weapon_id)

        # Get the vehicle used by the player
        vehicle_id = None
        if e.player in self.vehicles:
            vehicle_id = self.vehicles[e.player]
            del self.vehicles[e.player]
        player_vehicle = model_mgr.get_vehicle(vehicle_id)

        # Get the current game and map
        current_game = model_mgr.get_game()
        current_map = model_mgr.get_map(current_game.map_id)

        # Increment death count for the player
        player_stats.deaths += 1
        player_stats.deaths_total += 1

        # Update death streaks for the player
        player_stats.deaths_streak += 1
        if player_stats.deaths_streak > player_stats.deaths_streak_max:
            player_stats.deaths_streak_max = player_stats.deaths_streak
        player_stats.kills_streak = 0

        # Update kill ratio for the player
        player_stats.kills_ratio = round(float(player_stats.kills)
                / float(player_stats.deaths), 2)
        player_stats.kills_ratio_max = round(float(player_stats.kills_total)
                / float(player_stats.deaths_total), 2)

        # Increment the enemy death count for the player
        kill_event = player_history.get_new_event(KillEvent.TYPE)
        if kill_event.valid_kill:
            if not kill_event.attacker in player_stats.enemies:
                player_stats.enemies[kill_event.attacker] = PlayerItemStats()
            player_stats.enemies[kill_event.attacker].deaths += 1

        # Increment the kit death count for the player
        if not player_kit in player_stats.kits:
            player_stats.kits[player_kit] = PlayerItemStats()
        player_stats.kits[player_kit].deaths += 1

        # Increment the map death count for the player
        if not current_map in player_stats.maps:
            player_stats.maps[current_map] = PlayerItemStats()
        player_stats.maps[current_map].deaths += 1

        # Increment the team death count for the player
        if not player_team in player_stats.teams:
            player_stats.teams[player_team] = PlayerItemStats()
        player_stats.teams[player_team].deaths += 1

        # Increment the vehicle death count for the player
        if not player_vehicle in player_stats.vehicles:
            player_stats.vehicles[player_vehicle] = PlayerItemStats()
        player_stats.vehicles[player_vehicle].deaths += 1

        # Increment the weapon death count for the player
        if not player_weapon in player_stats.weapons:
            player_stats.weapons[player_weapon] = PlayerWeaponStats()
        player_stats.weapons[player_weapon].deaths += 1

        # Reset all the temporary accuracy values
        self._update_accuracy(e.player)

        # Stop active timers
        player_stats.commander_time.stop(e.tick)
        player_stats.leader_time.stop(e.tick)
        player_stats.play_time.stop(e.tick)
        player_stats.squad_time.stop(e.tick)

        # Start the spectator timer
        player_stats.spec_time.start(e.tick)

    def on_disconnect(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Reset all the temporary accuracy values
        self._update_accuracy(e.player)

        # Stop any active timers
        player_stats.commander_time.stop(e.tick)
        player_stats.leader_time.stop(e.tick)
        player_stats.play_time.stop(e.tick)
        player_stats.spec_time.stop(e.tick)
        player_stats.squad_time.stop(e.tick)

    def on_flag_action(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Increment flag points for the player
        if e.action_type == FlagActionEvent.CAPTURE:
            player_stats.flag_captures += 1
            player_stats.flag_captures_total += 1
        elif e.action_type == FlagActionEvent.CAPTURE_ASSIST:
            player_stats.flag_capture_assists += 1
            player_stats.flag_capture_assists_total += 1
        elif e.action_type == FlagActionEvent.NEUTRALIZE:
            player_stats.flag_neutralizes += 1
            player_stats.flag_neutralizes_total += 1
        elif e.action_type == FlagActionEvent.NEUTRALIZE_ASSIST:
            player_stats.flag_neutralize_assists += 1
            player_stats.flag_neutralize_assists_total += 1
        elif e.action_type == FlagActionEvent.DEFEND:
            player_stats.flag_defends += 1
            player_stats.flag_defends_total += 1

        # Increment teamwork for the player
        player_stats.teamwork += 1
        player_stats.teamwork_total += 1

    def on_game_status(self, e):

        # Reset all the temporary accuracy values
        if e.game.starting:
            for player in model_mgr.get_players(True):
                self._update_accuracy(player)

        # Reset any active timers
        if e.game.ending:
            for player in model_mgr.get_players(True):
                player_stats = stat_mgr.get_player_stats(player)
                player_stats.commander_time.stop(e.tick)
                player_stats.leader_time.stop(e.tick)
                player_stats.play_time.stop(e.tick)
                player_stats.squad_time.stop(e.tick)

    def on_heal(self, e):
        receiver_stats = stat_mgr.get_player_stats(e.receiver)
        giver_stats = stat_mgr.get_player_stats(e.giver)

        # Increment healed points for the receiver
        receiver_stats.healed += 1
        receiver_stats.healed_total += 1

        # Increment heal points for the giver
        giver_stats.heals += 1
        giver_stats.heals_total += 1

        # Increment teamwork for the giver
        giver_stats.teamwork += 1
        giver_stats.teamwork_total += 1

    def on_kill(self, e):
        victim_stats = stat_mgr.get_player_stats(e.victim)
        attacker_stats = stat_mgr.get_player_stats(e.attacker)

        # Get the last known kit for the attacker
        # Attacker may be dead and may not have an active kit
        attacker_kit = event_mgr.get_last_kit(e.attacker)

        # Get the team and vehicle for the attacker
        attacker_team = model_mgr.get_team(e.attacker.team_id)
        attacker_vehicle = model_mgr.get_vehicle(e.attacker.vehicle_id)

        # Get the current game and map
        current_game = model_mgr.get_game()
        current_map = model_mgr.get_map(current_game.map_id)

        # Check whether the kill was actually a suicide
        if e.suicide:
            attacker_stats.suicides += 1
            attacker_stats.suicides_total += 1
            return

        # Check whether the kill was actually a teammate
        if e.team_kill:
            victim_stats.team_killed += 1
            victim_stats.team_killed_total += 1
            attacker_stats.team_kills += 1
            attacker_stats.team_kills_total += 1
            return

        # Store the vehicle of the victim for future use
        if e.victim.vehicle_id:
            self.vehicles[e.victim] = e.victim.vehicle_id

        # Increment wound count for the victim
        victim_stats.wounds += 1
        victim_stats.wounds_total += 1

        # Increment enemy wound count for the victim
        if not e.attacker in victim_stats.enemies:
            victim_stats.enemies[e.attacker] = PlayerItemStats()
        victim_stats.enemies[e.attacker].wounds += 1

        # Increment kill count for the attacker
        attacker_stats.kills += 1
        attacker_stats.kills_total += 1

        # Update kill streaks for the attacker
        attacker_stats.kills_streak += 1
        if attacker_stats.kills_streak > attacker_stats.kills_streak_max:
            attacker_stats.kills_streak_max = attacker_stats.kills_streak
        attacker_stats.deaths_streak = 0
        if attacker_stats.kills_streak == 5:
            attacker_stats.kills_5 += 1
            attacker_stats.kills_5_total += 1
        elif attacker_stats.kills_streak == 10:
            attacker_stats.kills_10 += 1
            attacker_stats.kills_10_total += 1

        # Update kill ratio for the attacker
        if attacker_stats.deaths == 0:
            attacker_stats.kills_ratio = 1.0
        else:
            attacker_stats.kills_ratio = round(float(attacker_stats.kills)
                    / float(attacker_stats.deaths), 2)
        if attacker_stats.deaths_total == 0:
            attacker_stats.kills_ratio_total = 1.0
        else:
            attacker_stats.kills_ratio_total = round(float(attacker_stats.kills_total)
                    / float(attacker_stats.deaths_total), 2)

        # Increment the enemy kill count for the attacker
        if not e.victim in attacker_stats.enemies:
            attacker_stats.enemies[e.victim] = PlayerItemStats()
        attacker_stats.enemies[e.victim].kills += 1

        # Increment the kit kill count for the attacker
        if not attacker_kit in attacker_stats.kits:
            attacker_stats.kits[attacker_kit] = PlayerItemStats()
        attacker_stats.kits[attacker_kit].kills += 1

        # Increment the map kill count for the attacker
        if not current_map in attacker_stats.maps:
            attacker_stats.maps[current_map] = PlayerItemStats()
        attacker_stats.maps[current_map].kills += 1

        # Increment the vehicle kill count for the attacker
        if not attacker_vehicle in attacker_stats.vehicles:
            attacker_stats.vehicles[attacker_vehicle] = PlayerItemStats()
        attacker_stats.vehicles[attacker_vehicle].kills += 1

        # Increment the team kill count for the attacker
        if not attacker_team in attacker_stats.teams:
            attacker_stats.teams[attacker_team] = PlayerItemStats()
        attacker_stats.teams[attacker_team].kills += 1

        # Increment the weapon kill count for the attacker
        if not e.weapon in attacker_stats.weapons:
            attacker_stats.weapons[e.weapon] = PlayerWeaponStats()
        attacker_stats.weapons[e.weapon].kills += 1

    def on_loss(self, e):

        # Increment the loss count for all the active players on the team
        for player in model_mgr.get_players(True):
            if player.team_id == e.team.id:
                player_stats = stat_mgr.get_player_stats(player)
                player_stats.losses += 1

    def on_repair(self, e):
        giver_stats = stat_mgr.get_player_stats(e.giver)

        # Increment repair points for the giver
        giver_stats.repairs += 1
        giver_stats.repairs_total += 1

        # Increment teamwork for the giver
        giver_stats.teamwork += 1
        giver_stats.teamwork_total += 1

    def on_revive(self, e):
        receiver_stats = stat_mgr.get_player_stats(e.receiver)
        giver_stats = stat_mgr.get_player_stats(e.giver)

        # Increment revived points for the receiver
        receiver_stats.revived += 1
        receiver_stats.revived_total += 1

        # Increment revive points for the giver
        giver_stats.revives += 1
        giver_stats.revives_total += 1

        # Increment teamwork for the giver
        giver_stats.teamwork += 1
        giver_stats.teamwork_total += 1

    def on_score(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Get the last known kit for the player
        # Player may be dead and would not have a kit
        player_kit = event_mgr.get_last_kit(e.player)

        # Get the current map
        current_game = model_mgr.get_game()
        current_map = model_mgr.get_map(current_game.map_id)

        # Get the team for the player
        player_team = model_mgr.get_team(e.player.team_id)

        # Increment score count for the player
        player_stats.score += e.value
        player_stats.score_total += e.value

        # Calculate the player rank based on score
        if player_stats.score >= 40:
            player_stats.rank = 4
        elif player_stats.score >= 30:
            player_stats.rank = 3
        elif player_stats.score >= 20:
            player_stats.rank = 2
        elif player_stats.score >= 10:
            player_stats.rank = 1

        # Increment the kit score for the player
        if not player_kit in player_stats.kits:
            player_stats.kits[player_kit] = PlayerItemStats()
        player_stats.kits[player_kit].score += e.value

        # Increment the map score for the player
        if not current_map in player_stats.maps:
            player_stats.maps[current_map] = PlayerItemStats()
        player_stats.maps[current_map].score += e.value

        # Increment the team score for the player
        if not player_team in player_stats.teams:
            player_stats.teams[player_team] = PlayerItemStats()
        player_stats.teams[player_team].score += e.value

        # Calculate the overall place of each player
        self._update_place()
        self._update_place_overall()

    def on_server_status(self, e):

        # Reset all the temporary accuracy values
        for player in model_mgr.get_players(True):
            self._update_accuracy(player)

        # Reset any active timers
        for player in model_mgr.get_players():
            player_stats = stat_mgr.get_player_stats(player)
            player_stats.commander_time.stop(e.tick)
            player_stats.leader_time.stop(e.tick)
            player_stats.play_time.stop(e.tick)
            player_stats.spec_time.stop(e.tick)
            player_stats.squad_time.stop(e.tick)

    def on_spawn(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Increment the game count when the player first spawns
        if not player_stats.played:
            player_stats.games += 1
            player_stats.played = True

        # Stop the spectator timer
        player_stats.spec_time.stop(e.tick)

        # Start relevant timers
        if e.player.commander:
            player_stats.commander_time.start(e.tick)
        if e.player.leader:
            player_stats.leader_time.start(e.tick)
        player_stats.play_time.start(e.tick)
        if e.player.squader:
            player_stats.squad_time.start(e.tick)

    def on_squad(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Update the squad timer for the player
        if e.player.squader:
            player_stats.squad_time.start(e.tick)
        else:
            player_stats.squad_time.stop(e.tick)

    def on_squad_leader(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)
        old_player_stats = stat_mgr.get_player_stats(e.old_player)

        # Update the associated leader timers
        player_stats.leader_time.start(e.tick)
        old_player_stats.leader_time.stop(e.tick)

    def on_win(self, e):

        # Increment the win count for all the active players on the team
        for player in model_mgr.get_players(True):
            if player.team_id == e.team.id:
                player_stats = stat_mgr.get_player_stats(player)
                player_stats.wins += 1

    def _update_accuracy(self, player):
        player_stats = stat_mgr.get_player_stats(player)

        # Use accuracy accumulated in the current game as the new base
        for weapon in player_stats.weapons:
            weapon_stats = player_stats.weapons[weapon]
            weapon_stats._bullets_hit = weapon_stats.bullets_hit
            weapon_stats._bullets_fired = weapon_stats.bullets_fired

    def _update_ammo(self, player):
        player_stats = stat_mgr.get_player_stats(player)

        bullets_fired = 0
        bullets_hit = 0
        for weapon in player_stats.weapons:
            weapon_stats = player_stats.weapons[weapon]
            bullets_fired += weapon_stats.bullets_fired
            bullets_hit += weapon_stats.bullets_hit
        player_stats.bullets_fired = bullets_fired
        player_stats.bullets_hit = bullets_hit

    def _update_place(self):

        # Sort the players by score
        players = model_mgr.get_players(True)
        players.sort(key=lambda p: stat_mgr.get_player_stats(p).score,
                reverse=True)

        # Assign a place value to each player based on index
        last_score = None
        place = None
        for index, player in enumerate(players):
            player_stats = stat_mgr.get_player_stats(player)

            # Check whether the place should be incremented
            if last_score != player_stats.score:
                last_score = player_stats.score
                place = index + 1

            # Update the trend of the player
            if place < player_stats.place:
                player_stats.trend = '+'
            elif place > player_stats.place:
                player_stats.trend = '-'
            else:
                player_stats.trend = '='
            player_stats.place = place

    def _update_place_overall(self):

        # Sort the players by total score
        players = model_mgr.get_players()
        players.sort(key=lambda p: stat_mgr.get_player_stats(p).score_total,
                reverse=True)

        # Assign an overall place value to each player based on index
        last_score = None
        place = None
        for index, player in enumerate(players):
            player_stats = stat_mgr.get_player_stats(player)

            if last_score != player_stats.score_total:
                last_score = player_stats.score_total
                place = index + 1
            player_stats.place_overall = place
