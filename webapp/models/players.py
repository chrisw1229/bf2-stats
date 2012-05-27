
class Player(object):

    counter = 0

    def __init__(self, address, name):
        self.id = str(Player.counter)
        self.address = address
        self.name = name

        self.aliases = set()
        self.artificial = False
        self.commander = False
        self.connected = False
        self.kit_id = None
        self.leader = False
        self.squad_id = None
        self.team_id = None
        self.vehicle_id = None
        self.weapon_id = None

        Player.counter += 1
EMPTY = Player('', '')
