
from processors import BaseProcessor
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

        # Update the player team
        e.player.team_id = e.team.id

    def on_team(self, e):

        # Update the player team
        e.player.team_id = e.team.id
