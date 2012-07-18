
import models

from processors import BaseProcessor
from events import event_mgr
from models import model_mgr
from stats import TeamItemStats, stat_mgr

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 20

    def on_death(self, e):

        # Get the team for the player
        player_team = model_mgr.get_team(e.player.team_id)
        team_stats = stat_mgr.get_team_stats(player_team)

        # Increment the total team deaths
        team_stats.deaths += 1

        # Increment the player deaths
        if not e.player in team_stats.players:
            team_stats.players[e.player] = TeamItemStats()
        team_stats.players[e.player].deaths += 1

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Get the team for the attacker
        attacker_team = model_mgr.get_team(e.attacker.team_id)
        team_stats = stat_mgr.get_team_stats(attacker_team)

        # Increment the total team kills
        team_stats.kills += 1

        # Increment the attacker kills
        if not e.attacker in team_stats.players:
            team_stats.players[e.attacker] = TeamItemStats()
        team_stats.players[e.attacker].kills += 1

    def on_score(self, e):

        # Get the team for the player
        player_team = model_mgr.get_team(e.player.team_id)
        team_stats = stat_mgr.get_team_stats(player_team)

        # Increment the total team score
        team_stats.score += e.value

        # Increment score count for the player
        if not e.player in team_stats.players:
            team_stats.players[e.player] = TeamItemStats()
        team_stats.players[e.player].score += e.value
