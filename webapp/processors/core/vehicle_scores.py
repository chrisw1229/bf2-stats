
import models

from processors import BaseProcessor
from models import model_mgr
from stats import VehicleItemStats, stat_mgr

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 20
        self.vehicles = dict()

    def on_death(self, e):

        # Get the vehicle used by the player
        vehicle_id = None
        if e.player in self.vehicles:
            vehicle_id = self.vehicles[e.player]
            del self.vehicles[e.player]
        player_vehicle = model_mgr.get_vehicle(vehicle_id)
        vehicle_stats = stat_mgr.get_vehicle_stats(player_vehicle)

        # Increment the total vehicle deaths
        vehicle_stats.deaths += 1

        # Increment the player deaths
        if not e.player in vehicle_stats.players:
            vehicle_stats.players[e.player] = VehicleItemStats()
        vehicle_stats.players[e.player].deaths += 1

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Store the vehicle of the victim for future use
        if e.victim.vehicle_id:
            self.vehicles[e.victim] = e.victim.vehicle_id

        # Get the vehicle for the attacker
        attacker_vehicle = model_mgr.get_vehicle(e.attacker.vehicle_id)
        attacker_vehicle_stats = stat_mgr.get_vehicle_stats(attacker_vehicle)

        # Increment the total vehicle kills
        attacker_vehicle_stats.kills += 1

        # Increment the attacker kills
        if not e.attacker in attacker_vehicle_stats.players:
            attacker_vehicle_stats.players[e.attacker] = VehicleItemStats()
        attacker_vehicle_stats.players[e.attacker].kills += 1
