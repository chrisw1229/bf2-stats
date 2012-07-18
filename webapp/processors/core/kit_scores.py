
import models

from processors import BaseProcessor
from events import event_mgr
from models import model_mgr
from stats import KitItemStats, stat_mgr

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 20

    def on_death(self, e):

        # Get the last known kit for the player
        # Player will no longer have an active kit at this point
        player_kit = event_mgr.get_last_kit(e.player)
        kit_stats = stat_mgr.get_kit_stats(player_kit)

        # Increment the total kit deaths
        kit_stats.deaths += 1

        # Increment the player deaths
        if not e.player in kit_stats.players:
            kit_stats.players[e.player] = KitItemStats()
        kit_stats.players[e.player].deaths += 1

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Get the last known kit for the attacker
        # Attacker may be dead and may not have an active kit
        attacker_kit = event_mgr.get_last_kit(e.attacker)
        kit_stats = stat_mgr.get_kit_stats(attacker_kit)

        # Increment the total kit kills
        kit_stats.kills += 1

        # Increment the attacker kills
        if not e.attacker in kit_stats.players:
            kit_stats.players[e.attacker] = KitItemStats()
        kit_stats.players[e.attacker].kills += 1

    def on_score(self, e):

        # Get the last known kit for the player
        # Player may be dead and would not have a kit
        player_kit = event_mgr.get_last_kit(e.player)
        kit_stats = stat_mgr.get_kit_stats(player_kit)

        # Increment the total kit score
        kit_stats.score += e.value

        # Increment score count for the player
        if not e.player in kit_stats.players:
            kit_stats.players[e.player] = KitItemStats()
        kit_stats.players[e.player].score += e.value
