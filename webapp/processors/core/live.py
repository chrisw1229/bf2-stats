
import models

from models import model_mgr
from processors import BaseProcessor
from stats import stat_mgr

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 30
        self.game_packet = None
        self.id_to_player = dict()
        self.id_to_control_point = dict()
        self.tick_to_packets = dict()
        self.last_tick = None

    def get_packets(self, packet_type, tick):
        packets = list()

        # Check whether any packets have been received
        if self.last_tick == None:
            return packets

        # Check whether the full game state is needed
        if not tick or tick > self.last_tick:

            # Merge the current state of all packets
            packets.append(self.game_packet)
            packets.extend(self.id_to_player.values())
            packets.extend(self.id_to_control_point.values())
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
            packets.append({ 'type': 'TT', 'tick': self.last_tick,
                    'time': self._get_time() })
        return packets

    def on_connect(self, e):
        self._replace_player_packet(e, e.player)

    def on_control_point(self, e):

        # Create a packet to store the event info
        packet = self._add_event_packet(e)
        self.id_to_control_point[e.control_point.id] = packet

        # Extract information about the flag
        control_point_tuple = {
            'id': e.control_point.id,
            'state': e.control_point.status,
            'team': e.control_point.team_id,
            'time': self._get_time(),
            'x': self._convert_x(e.control_point.pos[0]),
            'y': self._convert_y(e.control_point.pos[2])
        }
        packet['control_point'] = control_point_tuple

    def on_disconnect(self, e):

        # Create a packet to store the player info
        packet = self._add_player_packet(e)
        del self.id_to_player[e.player.id]

        # Extract information about the player
        packet['player'] = self._convert_player(e.player)

    def on_game_status(self, e):
        if e.game.starting:

            # Clear cached packets when the game resets
            self.game_packet = None
            self.id_to_control_point.clear()
            self.tick_to_packets.clear()
            self.last_tick = None
        elif e.game.playing:

            # Add a packet when the game starts
            packet = self._add_event_packet(e)

            # Extract information about the victim
            game_tuple = {
                'id': e.game.id,
                'map_id': e.game.map_id,
                'clock_limit': e.game.clock_limit,
                'score_limit': e.game.score_limit
            }
            packet['game'] = game_tuple
            self.game_packet = packet

    def on_event(self, e):
        self.last_tick = e.tick

    def on_kill(self, e):

        # Create a packet to store the event info
        packet = self._add_event_packet(e)

        # Extract information about the victim
        victim_tuple = self._convert_player(e.victim, e.victim_pos)
        packet['victim'] = victim_tuple
        self._replace_stats_packet(e, e.victim)

        # Add optional attacker info to the packet
        if e.attacker != models.players.EMPTY:
            attacker_tuple = self._convert_player(e.attacker, e.attacker_pos, e.weapon)
            packet['attacker'] = attacker_tuple
            self._replace_stats_packet(e, e.attacker)

    def on_spawn(self, e):
        self._replace_player_packet(e, e.player)

    def on_score(self, e):
        self._replace_stats_packet(e, e.player)

    def on_vehicle_destroy(self, e):

        # Create a packet to store the event info
        packet = self._add_event_packet(e)

        # Extract information about the vehicle
        vehicle_tuple = {
            'id': e.vehicle.id,
            'name': e.vehicle.name,
            'x': self._convert_x(e.vehicle_pos[0]),
            'y': self._convert_y(e.vehicle_pos[2])
        }
        packet['vehicle'] = vehicle_tuple

    def _add_event_packet(self, e):
        return self._add_packet(e.tick, e.TYPE)

    def _add_player_packet(self, e):
        return self._add_packet(e.tick, 'PL')

    def _add_packet(self, tick, event_type):

        # Create a packet container for the event
        packet = {
            'tick': tick,
            'type': event_type
        }

        # Add the packet to the buffer based on tick
        if tick not in self.tick_to_packets:
            self.tick_to_packets[tick] = list()
        self.tick_to_packets[tick].append(packet)
        self.last_tick = tick
        return packet

    def _replace_stats_packet(self, e, player):
    
        # Create a packet to store the event info
        packet = self._add_player_packet(e)

        # Extract information about the player
        stats_tuple = self._convert_stats(player)
        packet['player'] = stats_tuple

        # Update the full player object with the new values
        self._update_player(player, stats_tuple)

    def _replace_player_packet(self, e, player):

        # Create a packet to store the player info
        packet = self._add_player_packet(e)
        self.id_to_player[player.id] = packet

        # Extract information about the player
        player_tuple = self._convert_player(player)
        stats_tuple = self._convert_stats(player)
        packet['player'] = self._merge_tuples(player_tuple, stats_tuple)

    def _get_time(self):
        return self.last_tick - self.game_packet['tick']

    def _convert_x(self, x):
        return 8 * x + 8191

    def _convert_y(self, y):
        return 8 * y + 8191

    def _convert_player(self, player, pos=None, weapon=None):
        player_tuple = {
            'id': player.id,
            'name': player.name,
            'team': player.team_id
        }
        if pos:
            player_tuple['x'] = self._convert_x(pos[0])
            player_tuple['y'] = self._convert_y(pos[2])
        if weapon:
            player_tuple['weapon'] = {
                'id': weapon.id,
                'name': weapon.name
            }
        return player_tuple

    def _convert_stats(self, player):
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

    def _update_player(self, player, src_tuple):
        player_packet = self.id_to_player[player.id]
        player_tuple = player_packet['player']

        return self._merge_tuples(player_tuple, src_tuple)

    def _merge_tuples(self, dest_tuple, src_tuple):
        for key in src_tuple:
            dest_tuple[key] = src_tuple[key]
        return dest_tuple
