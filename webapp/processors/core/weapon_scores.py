
import models

from processors import BaseProcessor
from models import model_mgr
from stats import WeaponItemStats, stat_mgr

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 20

    def on_death(self, e):

        # Get the weapon for the player
        player_weapon = model_mgr.get_weapon(e.player.weapon_id)
        weapon_stats = stat_mgr.get_weapon_stats(player_weapon)

        # Increment the total weapon deaths
        weapon_stats.deaths += 1

        # Increment the player deaths
        if not e.player in weapon_stats.players:
            weapon_stats.players[e.player] = WeaponItemStats()
        weapon_stats.players[e.player].deaths += 1

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Increment the total weapon kills
        weapon_stats = stat_mgr.get_weapon_stats(e.weapon)
        weapon_stats.kills += 1

        # Increment the attacker kills
        if not e.attacker in weapon_stats.players:
            weapon_stats.players[e.attacker] = WeaponItemStats()
        weapon_stats.players[e.attacker].kills += 1
