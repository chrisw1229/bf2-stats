
import models

from processors import BaseProcessor
from models import model_mgr
from stats import GameItemStats, stat_mgr

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 20

    def on_ammo(self, e):
        game_stats = stat_mgr.get_game_stats(model_mgr.get_game())

        # Increment the total game teamwork
        game_stats.teamwork += 1

        # Increment teamwork for the giver
        if not e.giver in game_stats.players:
            game_stats.players[e.giver] = GameItemStats()
        game_stats.players[e.giver].teamwork += 1

    def on_assist(self, e):
        game_stats = stat_mgr.get_game_stats(model_mgr.get_game())

        # Increment the total game teamwork
        game_stats.teamwork += 1

        # Increment teamwork for the player
        if not e.player in game_stats.players:
            game_stats.players[e.player] = GameItemStats()
        game_stats.players[e.player].teamwork += 1

    def on_death(self, e):
        game_stats = stat_mgr.get_game_stats(model_mgr.get_game())

        # Increment the total game deaths
        game_stats.deaths += 1

        # Increment the victim deaths
        if not e.player in game_stats.players:
            game_stats.players[e.player] = GameItemStats()
        game_stats.players[e.player].deaths += 1

    def on_heal(self, e):
        game_stats = stat_mgr.get_game_stats(model_mgr.get_game())

        # Increment the total game teamwork
        game_stats.teamwork += 1

        # Increment teamwork for the giver
        if not e.giver in game_stats.players:
            game_stats.players[e.giver] = GameItemStats()
        game_stats.players[e.giver].teamwork += 1

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        game_stats = stat_mgr.get_game_stats(model_mgr.get_game())

        # Increment the total game kills
        game_stats.kills += 1

        # Increment the attacker kills
        if not e.attacker in game_stats.players:
            game_stats.players[e.attacker] = GameItemStats()
        game_stats.players[e.attacker].kills += 1

    def on_repair(self, e):
        game_stats = stat_mgr.get_game_stats(model_mgr.get_game())

        # Increment the total game teamwork
        game_stats.teamwork += 1

        # Increment teamwork for the giver
        if not e.giver in game_stats.players:
            game_stats.players[e.giver] = GameItemStats()
        game_stats.players[e.giver].teamwork += 1

    def on_revive(self, e):
        game_stats = stat_mgr.get_game_stats(model_mgr.get_game())

        # Increment the total game teamwork
        game_stats.teamwork += 1

        # Increment teamwork for the giver
        if not e.giver in game_stats.players:
            game_stats.players[e.giver] = GameItemStats()
        game_stats.players[e.giver].teamwork += 1

    def on_score(self, e):
        game_stats = stat_mgr.get_game_stats(model_mgr.get_game())

        # Increment the total game score
        game_stats.kills += e.value

        # Increment score count for the player
        if not e.player in game_stats.players:
            game_stats.players[e.player] = GameItemStats()
        game_stats.players[e.player].score += e.value
