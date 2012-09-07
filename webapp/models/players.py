
import os

class Player(object):

    counter = 0

    def __init__(self, address, name):
        self.id = str(Player.counter)
        self.address = address      # Player's IP address
        self.name = name            # Player's current name

        self.aliases = set()        # Set of all names used by the player
        self.bot = False            # Flag when player is a bot
        self.connected = False      # Flag when player is connected

        self.reset();

        Player.counter += 1

    def __repr__(self):
        return self.__dict__

    def reset(self):
        self.commander = False      # Flag when player is commander
        self.driver = False         # Flag when player is vehicle driver
        self.kit_id = None          # ID for player's current kit
        self.leader = False         # Flag when player is squad leader
        self.operator = False       # Flag when player is operating a station
        self.pos = [0, 0, 0, 0]     # Player's current position
        self.passenger = False      # Flag when player is vehicle passenger
        self.spawned = False        # Flag when player is spawned
        self.squad_id = None        # ID for player's current squad
        self.squader = False        # Flag when player is in a squad
        self.team_id = None         # ID for player's current team
        self.vehicle_id = None      # ID for player's current vehicle
        self.vehicle_slot_id = None # ID for player's current vehicle slot
        self.weapon_id = None       # ID for player's current weapon
        self.wounded = False        # Flag when player is killed but revivable

        # Update the photo paths for the player
        self.photo_s = 'images/players/' + self.id + '-small.png'
        if not os.path.isfile('www/' + self.photo_s):
            self.photo_s = 'images/players/missing-small.png'
        self.photo_m = 'images/players/' + self.id + '-medium.jpg'
        if not os.path.isfile('www/' + self.photo_m):
            self.photo_m = 'images/players/missing-medium.png'

EMPTY = Player('', '')
