
import models

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
        receiver_stats.supported += 1
        receiver_stats.supported_total += 1

        # Increment support points for the giver
        giver_stats.supports += 1
        giver_stats.supports_total += 1

    def on_assist(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Increment assist count for the player
        player_stats.assists += 1
        player_stats.assists_total += 1

    def on_death(self, e):
        player_stats = stat_mgr.get_player_stats(e.player)

        # Increment death count for the player
        player_stats.deaths += 1
        player_stats.deaths_total += 1

        # Update death streaks for the player
        player_stats.deaths_streak += 1
        if player_stats.deaths_streak > player_stats.deaths_streak_max:
            player_stats.deaths_streak_max = player_stats.deaths_streak
        player_stats.kills_streak = 0

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
        victim_kit = model_mgr.get_kit(e.victim.kit_id)

        attacker_stats = stat_mgr.get_player_stats(e.attacker)
        attacker_kit = model_mgr.get_kit(e.attacker.kit_id)

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

        # Increment the enemy kill count for the attacker
        if not e.victim in attacker_stats.enemies:
            attacker_stats.enemies[e.victim] = PlayerItemStats()
        attacker_stats.enemies[e.victim].kills += 1

        # Increment the enemy death count for the victim
        if not e.attacker in victim_stats.enemies:
            victim_stats.enemies[e.attacker] = PlayerItemStats()
        victim_stats.enemies[e.attacker].deaths += 1

        # Increment the kit kill count for the attacker
        if not current_map in attacker_stats.maps:
            attacker_stats.maps[current_map] = PlayerItemStats()
        attacker_stats.maps[current_map].kills += 1

        # Increment the kit death count for the victim
        if not victim_kit in victim_stats.kits:
            victim_stats.kits[victim_kit] = PlayerItemStats()
        victim_stats.kits[victim_kit].deaths += 1

        # Increment the map kill count for the attacker
        if not attacker_kit in attacker_stats.kits:
            attacker_stats.kits[attacker_kit] = PlayerItemStats()
        attacker_stats.kits[attacker_kit].kills += 1

        # Increment the map death count for the victim
        if not current_map in victim_stats.maps:
            victim_stats.maps[current_map] = PlayerItemStats()
        victim_stats.maps[current_map].deaths += 1

        # Increment the weapon kill count for the attacker
        if not e.weapon in attacker_stats.weapons:
            attacker_stats.weapons[e.weapon] = PlayerItemStats()
        attacker_stats.weapons[e.weapon].kills += 1

        # Increment the weapon death count for the victim
        if not e.weapon in victim_stats.weapons:
            victim_stats.weapons[e.weapon] = PlayerItemStats()
        victim_stats.weapons[e.weapon].deaths += 1

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
