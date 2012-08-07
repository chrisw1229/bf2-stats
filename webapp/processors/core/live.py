
import models

from models import model_mgr
from processors import BaseProcessor

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

        # Create a packet to store the player info
        packet = self._add_packet(e)
        self.id_to_player[e.player.id] = packet

        # TODO Add more fields to the player packet
        player = {
            'id': e.player.id,
            'name': e.player.name,
            'team': e.player.team_id
        }
        packet['player'] = player

    def on_control_point(self, e):

        # Create a packet to store the event info
        packet = self._add_packet(e)
        self.id_to_control_point[e.control_point.id] = packet

        # Extract information about the flag
        control_point = {
            'id': e.control_point.id,
            'state': e.control_point.status,
            'team': e.control_point.team_id,
            'time': self._get_time(),
            'x': self._convert_x(e.control_point.pos[0]),
            'y': self._convert_y(e.control_point.pos[2])
        }
        packet['control_point'] = control_point

    def ___on_disconnect(self, e):
        values = {
            'id': e.player.id,
            'team': ''
        }
        self._add_packet(e.id, 'player', values)

    def on_game_status(self, e):
        if e.game.starting:

            # Clear cached packets when the game resets
            self.game_packet = None
            self.id_to_control_point.clear()
            self.tick_to_packets.clear()
            self.last_tick = None
        elif e.game.playing:

            # Add a packet when the game starts
            packet = self._add_packet(e)

            # Extract information about the victim
            game = {
                'id': e.game.id,
                'map_id': e.game.map_id,
                'clock_limit': e.game.clock_limit,
                'score_limit': e.game.score_limit
            }
            packet['game'] = game
            self.game_packet = packet

    def on_event(self, e):
        self.last_tick = e.tick

    def on_kill(self, e):

        # Create a packet to store the event info
        packet = self._add_packet(e)

        # Extract information about the victim
        victim = {
            'id': e.victim.id,
            'name': e.victim.name,
            'team': e.victim.team_id,
            'x': self._convert_x(e.victim_pos[0]),
            'y': self._convert_y(e.victim_pos[2])
        }
        packet['victim'] = victim

        # Add optional attacker info to the packet
        if e.attacker != models.players.EMPTY:
            attacker = {
                'id': e.attacker.id,
                'name': e.attacker.name,
                'team': e.attacker.team_id,
                'weapon': {
                    'id': e.weapon.id,
                    'name': e.weapon.name
                },
                'x': self._convert_x(e.attacker_pos[0]),
                'y': self._convert_y(e.attacker_pos[2])
            }
            packet['attacker'] = attacker

    def on_vehicle_destroy(self, e):

        # Create a packet to store the event info
        packet = self._add_packet(e)

        # Extract information about the vehicle
        vehicle = {
            'id': e.vehicle.id,
            'name': e.vehicle.name,
            'team': 'na',
            'x': self._convert_x(e.vehicle_pos[0]),
            'y': self._convert_y(e.vehicle_pos[2])
        }
        packet['vehicle'] = vehicle

    def _add_packet(self, e):

        # Create a packet container for the event
        packet = {
            'tick': e.tick,
            'type': e.TYPE
        }

        # Add the packet to the buffer based on tick
        if e.tick not in self.tick_to_packets:
            self.tick_to_packets[e.tick] = list()
        self.tick_to_packets[e.tick].append(packet)
        self.last_tick = e.tick
        return packet

    def _get_time(self):
        return self.last_tick - self.game_packet['tick']

    def _convert_x(self, x):
        return 8 * x + 8191

    def _convert_y(self, y):
        return 8 * y + 8191
