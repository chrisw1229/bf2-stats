
import models

from processors import BaseProcessor
from events import event_mgr
from models import model_mgr
from stats import MapItemStats, stat_mgr

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 20

    def on_death(self, e):

        # Get the current map
        current_game = model_mgr.get_game()
        current_map = model_mgr.get_map(current_game.map_id)
        map_stats = stat_mgr.get_map_stats(current_map)

        # Increment the total map deaths
        map_stats.deaths += 1

        # Increment the player deaths
        if not e.player in map_stats.players:
            map_stats.players[e.player] = MapItemStats()
        map_stats.players[e.player].deaths += 1

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Get the current map
        current_game = model_mgr.get_game()
        current_map = model_mgr.get_map(current_game.map_id)
        map_stats = stat_mgr.get_map_stats(current_map)

        # Increment the total map kills
        map_stats.kills += 1

        # Increment the attacker kills
        if not e.attacker in map_stats.players:
            map_stats.players[e.attacker] = MapItemStats()
        map_stats.players[e.attacker].kills += 1

    def on_score(self, e):

        # Get the current map
        current_game = model_mgr.get_game()
        current_map = model_mgr.get_map(current_game.map_id)
        map_stats = stat_mgr.get_map_stats(current_map)

        # Increment the total map score
        map_stats.score += e.value

        # Increment score count for the player
        if not e.player in map_stats.players:
            map_stats.players[e.player] = MapItemStats()
        map_stats.players[e.player].score += e.value
