
class Player(object):

    counter = 0

    def __init__(self, address, name):
        self.id = str(Player.counter)
        self.address = address      # Player's IP address
        self.name = name            # Player's current name

        self.aliases = set()        # Set of all names used by the player
        self.bot = False            # Flag when player is a bot
        self.commander = False      # Flag when player is commander
        self.connected = False      # Flag when player is connected
        self.driver = False         # Flag when player is vehicle driver
        self.kit_id = None          # ID for player's current kit
        self.leader = False         # Flag when player is squad leader
        self.operator = False       # Flag when player is operating a station
        self.pos = [0, 0, 0, 0]     # Player's current position
        self.passenger = False      # Flag when player is vehicle passenger
        self.spawned = False        # Flag when player is spawned
        self.squad_id = None        # ID for player's current squad
        self.team_id = None         # ID for player's current team
        self.vehicle_id = None      # ID for player's current vehicle
        self.vehicle_slot_id = None # ID for player's current vehicle slot
        self.weapon_id = None       # ID for player's current weapon
        self.wounded = False        # Flag when player is killed but revivable

        Player.counter += 1
EMPTY = Player('', '')
