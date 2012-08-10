
import os

import models

from models import model_mgr
from processors import BaseProcessor
from stats import stat_mgr

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 30
        self.game = None
        self.control_points = set()
        self.players = set()
        self.tick_to_packets = dict()
        self.start_tick = None
        self.last_tick = None

    def get_packets(self, packet_type, tick):

        # Check whether any packets have been received
        packets = list()
        if self.last_tick == None:
            return packets

        # Check whether the full game state is needed
        if not tick or tick > self.last_tick:

            # Generate a snapshot of the current game
            packets.extend(self._get_packet_list())
        elif tick != self.last_tick:
 
            # Add all the packets received since the given tick
            for i in range(tick + 1, self.last_tick + 1):
                if i in self.tick_to_packets:
                    packets.extend(self.tick_to_packets[i])

        # Filter the list of packets based on the given type
        if packet_type and len(packets) > 0:
            packets = filter(lambda p: p.type == packet_type, packets)

        # Add a packet to represent the next tick threshold
        if self.last_tick:
            packets.append(self._get_tick_packet())
        return packets

    def on_connect(self, e):

        # Store the player model for future updates
        self.players.add(e.player)

        # Create a packet to store the event info
        packet = self._get_player_packet(e.player, True)
        self._add_packet(e.tick, packet)

    def on_control_point(self, e):

        # Store the control point model for future updates
        self.control_points.add(e.control_point)

        # Create a packet to store the event info
        packet = self._get_control_point_packet(e.control_point)
        self._add_packet(e.tick, packet)

    def on_disconnect(self, e):

        # Remove the player model from the cache
        if e.player in self.players:
            self.players.remove(e.player)

        # Create a packet to store the event info
        packet = self._get_player_packet(e.player, False)
        self._add_packet(e.tick, packet)

    def on_game_status(self, e):
        if e.game.starting:

            # Store the new game state
            self.game = e.game
            self.start_tick = e.tick

            # Clear cached packets when the game resets
            self.control_points.clear()
            self.tick_to_packets.clear()
            self.last_tick = None
        elif e.game.playing:

            # Create a packet to store the event info
            packet = self._get_game_packet(e.game)
            self._add_packet(e.tick, packet)

    def on_event(self, e):

        # Store the most recent game tick for any event
        self.last_tick = max(self.last_tick, e.tick)

    def on_kill(self, e):

        # Create a packet to store the event info
        packet = {
            'tick': e.tick,
            'type': 'KL',
            'victim': self._get_player_tuple(e.victim, e.victim_pos)
        }

        # Add optional attacker info to the packet
        if e.attacker != models.players.EMPTY:
            packet['attacker'] = self._get_player_tuple(e.attacker,
                    e.attacker_pos, e.weapon)
        self._add_packet(e.tick, packet)

    def on_spawn(self, e):

        # Create a packet to store the event info
        packet = self._get_player_packet(e.player, False)
        self._add_packet(e.tick, packet)

    def on_score(self, e):

        # Create a packet to store the event info
        packet = self._get_stats_packet(e.player)
        self._add_packet(e.tick, packet)

    def on_vehicle_destroy(self, e):

        # Create a packet to store the event info
        packet = self._get_vehicle_packet(e.tick, e.vehicle, e.vehicle_pos)
        self._add_packet(e.tick, packet)

    def _add_packet(self, tick, packet):
        if tick not in self.tick_to_packets:
            self.tick_to_packets[tick] = list()
        self.tick_to_packets[tick].append(packet)
        self.last_tick = max(self.last_tick, tick)

    def _convert_x(self, x):
        return 8 * x + 8191

    def _convert_y(self, y):
        return 8 * y + 8191

    def _get_control_point_packet(self, control_point):
        control_point_tuple = {
            'id': control_point.id,
            'state': control_point.status,
            'team': control_point.team_id,
            'time': self._get_time(),
            'x': self._convert_x(control_point.pos[0]),
            'y': self._convert_y(control_point.pos[2])
        }

        return {
            'type': 'CP',
            'control_point': control_point_tuple
        }

    def _get_game_packet(self, game):
        game_tuple = {
            'id': game.id,
            'map_id': game.map_id,
            'clock_limit': game.clock_limit,
            'score_limit': game.score_limit
        }

        return {
            'type': 'GS',
            'game': game_tuple
        }

    def _get_packet_list(self):
        packets = list()

        # Add the current game info
        packets.append(self._get_game_packet(self.game))

        # Add the current player info
        for player in self.players:
            packets.append(self._get_player_packet(player, True))

        # Add the current control point info
        for control_point in self.control_points:
            packets.append(self._get_control_point_packet(control_point))
        return packets

    def _get_player_packet(self, player, detailed):
        player_tuple = self._get_player_tuple(player)

        if detailed:
            stats_tuple = self._get_stats_tuple(player)
            player_tuple.update(stats_tuple)

        return {
            'type': 'PL',
            'player': player_tuple
        }

    def _get_player_tuple(self, player, pos=None, weapon=None):

        # Check whether a photo exists for the player
        photo_path = '/images/players/' + player.id + '-medium.jpg'
        if not os.path.isfile('www' + photo_path):
            photo_path = '/images/players/missing-medium.png'

        # Add basic player info
        player_tuple = {
            'id': player.id,
            'name': player.name,
            'team': player.team_id,
            'photo': photo_path
        }

        # Check whether the player is disconnected
        if not player.connected:
            player_tuple['connected'] = False

        # Add position coordinates
        if pos:
            player_tuple['x'] = self._convert_x(pos[0])
            player_tuple['y'] = self._convert_y(pos[2])

        # Add weapon info
        if weapon:
            player_tuple['weapon'] = {
                'id': weapon.id,
                'name': weapon.name
            }
        return player_tuple

    def _get_stats_packet(self, player):
        return {
            'type': 'PL',
            'player': self._get_stats_tuple(player)
        }

    def _get_stats_tuple(self, player):
        player_stats = stat_mgr.get_player_stats(player)

        stats_tuple = {
            'id': player.id,
            'deaths': player_stats.deaths,
            'kills': player_stats.kills,
            'rank': player_stats.rank,
            'score': player_stats.score,
            'teamwork': player_stats.teamwork
        }
        return stats_tuple

    def _get_tick_packet(self):
        return {
            'tick': self.last_tick,
            'type': 'TT',
            'time': self._get_time()
        }

    def _get_time(self):
        return self.last_tick - self.start_tick

    def _get_vehicle_packet(self, tick, vehicle, pos=None):
        vehicle_tuple = {
            'id': vehicle.id,
            'name': vehicle.name
        }

        if pos:
            vehicle_tuple['x'] = self._convert_x(pos[0])
            vehicle_tuple['y'] = self._convert_y(pos[2])

        return {
            'tick': tick,
            'type': 'VD',
            'vehicle': vehicle_tuple
        }
