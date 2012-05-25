
from processors import BaseProcessor

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 10
        self.packets = list() # List of all packets for the current game
        self.id_to_index = dict() # Mapping of event id to packet index
        self.last_id = None # Identifier of the last packet added

    def get_packets(self, packet_type, threshold):
        packets = list()

        # Check whether a valid id threshold was given
        if threshold and threshold in self.id_to_index:

            # Attempt to get the start index within the packet queue
            index = self.id_to_index[threshold]
            if index and index + 1 < len(self.packets):
 
                # Splice out the packets since the threshold
                packets = self.packets[index + 1:]
        else:

            # Copy all of the packets if a sub-set could not be extracted
            packets.extend(self.packets)

        # Filter the list of packets based on the given type
        if packet_type and len(packets) > 0:
            packets = filter(lambda p: p.type == packet_type, packets)

        # Add a packet to represent the next threshold
        if self.last_id:
            packets.append({ 'type': 'threshold', 'values': self.last_id })
        return packets

    def on_connect(self, e):

        # TODO Add more fields to the player packet
        values = {
            'id': e.player.id,
            'name': e.player.name,
            'team': e.player.team_id
        }
        self._add_packet(e.id, 'player', values)

    def on_disconnect(self, e):
        values = {
            'id': e.player.id,
            'team': ''
        }
        self._add_packet(e.id, 'player', values)

    def on_game_status(self, e):
        if e.game.starting:

            # Clear the packet queue when the game resets
            del self.packets[:]
            self.id_to_index.clear()
        elif e.game.playing:

            # Add a packet when the game starts
            values = {
                'map': e.game.map_id,
                'clock_limit': e.game.clock_limit,
                'score_limit': e.game.score_limit
            }
            self._add_packet(e.id, 'game', values)

    def on_kill(self, e):
        values = {
            'attacker': e.attacker.name,
            'ax': e.attacker_pos[0],
            'ay': e.attacker_pos[2],
            'victim': e.victim.name,
            'vx': e.victim_pos[0],
            'vy': e.victim_pos[2]
        }
        self._add_packet(e.id, 'map', values)

    def _add_packet(self, id, packet_type, values):
        self.last_id = id

        # Update the packet index as needed
        if not id in self.id_to_index:
            self.id_to_index[id] = len(self.packets)

        # Store a packet representation of the parameters
        packet = {
            'type': packet_type,
            'values': values
        }
        self.packets.append(packet)
        return packet
