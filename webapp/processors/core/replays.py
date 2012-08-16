
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

    def on_control_point(self, e):

        # Create a packet to store the event info
        packet = self._add_packet(e)

        # Extract information about the flag
        control_point = {
            'id': e.control_point.id,
            'state': e.control_point.status,
            'team_id': e.control_point.team_id,
            'x': self._convert_x(e.control_point.pos[0]),
            'y': self._convert_y(e.control_point.pos[2])
        }
        packet['control_point'] = control_point

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
        victim = {
            'id': e.victim.id,
            'name': e.victim.name,
            'team_id': e.victim.team_id,
            'x': self._convert_x(e.victim_pos[0]),
            'y': self._convert_y(e.victim_pos[2])
        }
        packet['victim'] = victim

        # Add optional attacker info to the packet
        if e.suicide:
            victim['suicide'] = True
        elif e.attacker != models.players.EMPTY:
            attacker = {
                'id': e.attacker.id,
                'name': e.attacker.name,
                'team_id': e.attacker.team_id,
                'x': self._convert_x(e.attacker_pos[0]),
                'y': self._convert_y(e.attacker_pos[2])
            }

            if e.team_kill:
                attacker['weapon'] = 'Teamkills';
            elif e.weapon != models.weapons.EMPTY:
                attacker['weapon'] = e.weapon.name
            elif e.vehicle != models.vehicles.EMPTY:
                attacker['weapon'] = e.vehicle.name
            packet['attacker'] = attacker

    def on_vehicle_destroy(self, e):

        # Create a packet to store the event info
        packet = self._add_packet(e)

        # Extract information about the vehicle
        vehicle = {
            'id': e.vehicle.id,
            'name': e.vehicle.name,
            'type': e.vehicle.vehicle_type,
            'x': self._convert_x(e.vehicle_pos[0]),
            'y': self._convert_y(e.vehicle_pos[2])
        }
        packet['vehicle'] = vehicle

    def _add_packet(self, e):
        packet = {
            'tick': e.tick,
            'type': e.TYPE
        }
        self.game.packets.append(packet)
        return packet

    def _convert_x(self, x):
        return 8 * x + 8191

    def _convert_y(self, y):
        return 8 * y + 8191
