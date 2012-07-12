
import models

from events import KillEvent, event_mgr
from processors import BaseProcessor
from models import model_mgr
from stats import PlayerItemStats, stat_mgr

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 20

    def on_ammo(self, e):
        receiver_stats = stat_mgr.get_player_stats(e.receiver)
        giver_stats = stat_mgr.get_player_stats(e.giver)

        # Increment supported points for the receiver
        receiver_stats.ammoed += 1
        receiver_stats.ammoed_total += 1

        # Increment support points for the giver
        giver_stats.ammos += 1
        giver_stats.ammos_total += 1

    def on_assist(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Increment assist count for the player
        player_stats.assists += 1
        player_stats.assists_total += 1

        # Get the last kill event that occurred
        global_history = event_mgr.get_history()
        kill_event = global_history.get_new_event(KillEvent.TYPE)

        # Increment the assisted count for the attacker
        attacker_stats = stat_mgr.get_player_stats(kill_event.attacker)
        attacker_stats.assisted += 1
        attacker_stats.assisted_total += 1

    def on_death(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Get the last known kit and weapon for the player
        # Player will no longer have a kit at this point
        player_kit = model_mgr.get_kit(e.player.kit_id_old)
        player_weapon = model_mgr.get_weapon(e.player.weapon_id)

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

        # Increment the enemy death count for the player
        player_history = event_mgr.get_history(e.player)
        kill_event = player_history.get_new_event(KillEvent.TYPE)
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

        # Increment the weapon death count for the player
        if not player_weapon in player_stats.weapons:
            player_stats.weapons[player_weapon] = PlayerItemStats()
        player_stats.weapons[player_weapon].deaths += 1

        # Stop play timer
        player_stats.play_time.stop(e.tick)

        # Start the spectator timer
        player_stats.spec_time.start(e.tick)

    def on_heal(self, e):
        receiver_stats = stat_mgr.get_player_stats(e.receiver)
        giver_stats = stat_mgr.get_player_stats(e.giver)

        # Increment healed points for the receiver
        receiver_stats.healed += 1
        receiver_stats.healed_total += 1

        # Increment heal points for the giver
        giver_stats.heals += 1
        giver_stats.heals_total += 1

    def on_kill(self, e):
        victim_stats = stat_mgr.get_player_stats(e.victim)
        attacker_stats = stat_mgr.get_player_stats(e.attacker)

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

        # Increment wound count for the victim
        victim_stats.wounds += 1
        victim_stats.wounds_total += 1

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

        # Get the last known kit for the attacker
        # Attacker may be dead and would not have a kit
        attacker_kit = None
        if e.attacker.kit_id:
            attacker_kit = model_mgr.get_kit(e.attacker.kit_id)
        else:
            attacker_kit = model_mgr.get_kit(e.attacker.kit_id_old)

        # Increment the enemy kill count for the attacker
        if not e.victim in attacker_stats.enemies:
            attacker_stats.enemies[e.victim] = PlayerItemStats()
        attacker_stats.enemies[e.victim].kills += 1

        # Increment the map kill count for the attacker
        if not current_map in attacker_stats.maps:
            attacker_stats.maps[current_map] = PlayerItemStats()
        attacker_stats.maps[current_map].kills += 1

        # Increment the kit kill count for the attacker
        if not attacker_kit in attacker_stats.kits:
            attacker_stats.kits[attacker_kit] = PlayerItemStats()
        attacker_stats.kits[attacker_kit].kills += 1

        # Increment the weapon kill count for the attacker
        if not e.weapon in attacker_stats.weapons:
            attacker_stats.weapons[e.weapon] = PlayerItemStats()
        attacker_stats.weapons[e.weapon].kills += 1

    def on_repair(self, e):
        giver_stats = stat_mgr.get_player_stats(e.giver)

        # Increment repair points for the giver
        giver_stats.repair_points += 1
        giver_stats.repair_points_total += 1

    def on_revive(self, e):
        receiver_stats = stat_mgr.get_player_stats(e.receiver)
        giver_stats = stat_mgr.get_player_stats(e.giver)

        # Increment revived points for the receiver
        receiver_stats.revived += 1
        receiver_stats.revived_total += 1

        # Increment revive points for the giver
        giver_stats.revives += 1
        giver_stats.revives_total += 1

    def on_score(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Get the last known kit for the player
        # Player may be dead and would not have a kit
        player_kit = None
        if e.player.kit_id:
            player_kit = model_mgr.get_kit(e.player.kit_id)
        else:
            player_kit = model_mgr.get_kit(e.player.kit_id_old)
        player_weapon = model_mgr.get_weapon(e.player.weapon_id)

        # Get the current game and map
        current_game = model_mgr.get_game()
        current_map = model_mgr.get_map(current_game.map_id)

        # Increment score count for the player
        player_stats.score += e.value
        player_stats.score_total += e.value

        # Calculate the player rank based on score
        if player_stats.score >= 50:
            player_stats.rank = 5
        elif player_stats.score >= 40:
            player_stats.rank = 4
        elif player_stats.score >= 30:
            player_stats.rank = 3
        elif player_stats.score >= 20:
            player_stats.rank = 2
        elif player_stats.score >= 10:
            player_stats.rank = 1

        # Increment the map score for the player
        if not current_map in player_stats.maps:
            player_stats.maps[current_map] = PlayerItemStats()
        player_stats.maps[current_map].score += e.value

        # Increment the kit score for the player
        if not player_kit in player_stats.kits:
            player_stats.kits[player_kit] = PlayerItemStats()
        player_stats.kits[player_kit].score += e.value

    def on_spawn(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Increment the game count when the player first spawns
        if not player_stats.played:
            player_stats.games += 1
            player_stats.played = True

        # Stop the spectator timer
        player_stats.spec_time.stop(e.tick)

        # Start play timer
        player_stats.play_time.start(e.tick)
