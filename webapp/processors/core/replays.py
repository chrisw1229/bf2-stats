
import models

from models import model_mgr
from processors import BaseProcessor

class GameState(object):

    def __init__(self, id, map_id, map_name, clock_limit):
        self.id = id
        self.map_id = map_id
        self.map_name = map_name
        self.clock_limit = clock_limit
        self.packets = list()

    def __repr__(self):
        return self.__dict__

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 30
        self.games = dict()
        self.game = None

    def get_game_state(self, id):
        '''
        Provides a full game state model that includes all the kill packets
        parsed for the game with the given identifier.

        Args:
           id (string): The unique identifier of the game for which to get the
                        full game state.

        Returns:
            state (GameState): Returns the full game state including kill
                            packets.
        '''

        if id in self.games:
            return self.games[id]

    def on_game_status(self, e):

        # Create a status model when a new game starts
        if e.game.playing:
            map_obj = model_mgr.get_map(e.game.map_id)
            self.game = GameState(e.game.id, e.game.map_id, map_obj.name,
                    e.game.clock_limit)
            self.games[e.game.id] = self.game

    def on_kill(self, e):

        # Create a packet to store the event info
        packet = self._add_packet(e)

        # Extract information about the victim
        victim_packet = {
            'id': e.victim.id,
            'name': e.victim.name,
            'team': e.victim.team_id,
            'x': self._convert_x(e.victim_pos[0]),
            'y': self._convert_y(e.victim_pos[2])
        }
        packet['victim'] = victim_packet

        # Add optional attacker info to the packet
        attacker_packet = None
        if e.attacker != models.players.EMPTY:
            attacker_packet = {
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
            packet['attacker'] = attacker_packet

    def on_vehicle_destroy(self, e):

        # Create a packet to store the event info
        packet = self._add_packet(e)

        # Extract information about the vehicle
        vehicle_packet = {
            'id': e.vehicle.id,
            'name': e.vehicle.name,
            'x': self._convert_x(e.vehicle_pos[0]),
            'y': self._convert_y(e.vehicle_pos[2])
        }
        packet['vehicle'] = vehicle_packet

    def _add_packet(self, e):
        packet = {
            'tick': e.tick,
            'type': e.TYPE
        }
        self.game.packets.append(packet)
        return packet

    def _convert_x(self, x):
        return x

    def _convert_y(self, y):
        return y
