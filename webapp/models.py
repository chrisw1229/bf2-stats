
import kits
import maps
import teams
import vehicles
import weapons

class Player(object):

    counter = 0

    def __init__(self, address, name):
        self.id = Player.counter
        self.address = address
        self.name = name
        self.team_id = None
        self.artificial = False
        self.connected = False

        Player.counter += 1

class Game(object):

    counter = 0

    def __init__(self, status, map_id, clock_limit, score_limit):
        self.id = Game.counter
        self.status = status
        self.map_id = map_id
        self.clock_limit = clock_limit
        self.score_limit = score_limit

        Game.counter += 1

    def is_starting(self):
        return self.status == 'pre'

    def is_playing(self):
        return self.status == 'play'

    def is_ending(self):
        return self.status == 'end'

class ModelManager(object):

    # Sentinel objects to avoid none checks everywhere
    EMPTY_PLAYER = Player('', '')
    EMPTY_GAME = Game('', '', 0, 0)

    def __init__(self):
        self.players = []
        self.name_to_player = {}
        self.addr_to_player = {}

        self.games = []
        self.id_to_game = {}

        self.kits = []
        self.id_to_kit = {}
        self.type_to_kits = {}

        self.maps = []
        self.id_to_map = {}

        self.teams = []
        self.id_to_team = {}

        self.vehicles = []
        self.id_to_vehicle = {}
        self.type_to_vehicles = {}

        self.weapons = []
        self.id_to_weapon = {}
        self.type_to_weapons = {}

    # This method will be called to initialize the manager
    def start(self):
        print 'MODEL MANAGER - STARTING'

        # Register all the kit models
        self.kits = kits.registry
        for kit in self.kits:
            assert not kit.id in self.id_to_kit, 'Duplicate kit ID: %s' % kit.id
            self.id_to_kit[kit.id] = kit

            if not kit.kit_type in self.type_to_kits:
                self.type_to_kits[kit.kit_type] = []
            self.type_to_kits[kit.kit_type].append(kit)
        print 'Kits registered: ', len(self.kits)

        # Register all the map models
        self.maps = maps.registry
        for map in self.maps:
            assert not map.id in self.id_to_map, 'Duplicate map ID: %s' % map.id
            self.id_to_map[map.id] = map
        print 'Maps registered: ', len(self.maps)

        # Register all the team models
        self.teams = teams.registry
        for team in self.teams:
            assert not team.id in self.id_to_team, 'Duplicate team ID: %s' % team.id
            self.id_to_team[team.id] = team
        print 'Teams registered: ', len(self.teams)

        # Register all the vehicle models
        self.vehicles = vehicles.registry
        for vehicle in self.vehicles:
            assert not vehicle.id in self.id_to_vehicle, 'Duplicate vehicle ID: %s' % vehicle.id
            self.id_to_vehicle[vehicle.id] = vehicle

            if not vehicle.vehicle_type in self.type_to_vehicles:
                self.type_to_vehicles[vehicle.vehicle_type] = []
            self.type_to_vehicles[vehicle.vehicle_type].append(vehicle)
        print 'Vehicles registered: ', len(self.vehicles)

        # Register all the weapon models
        self.weapons = weapons.registry
        for weapon in self.weapons:
            assert not weapon.id in self.id_to_weapon, 'Duplicate weapon ID: %s' % weapon.id
            self.id_to_weapon[weapon.id] = weapon

            if not weapon.weapon_type in self.type_to_weapons:
                self.type_to_weapons[weapon.weapon_type] = []
            self.type_to_weapons[weapon.weapon_type].append(weapon)
        print 'Weapons registered: ', len(self.weapons)

        print 'MODEL MANAGER - STARTED'

    # This method will be called to shutdown the manager
    def stop(self):
        print 'MODEL MANAGER - STOPPING'

        print 'MODEL MANAGER - STOPPED'

    def add_player(self, address, name):
        '''
        Adds or updates the player model registered for the given unique composite key.

        Args:
           address (string): The IP address of the player. This could be 'None' for bot players.
           name (string): The name of the player.

        Returns:
            Player (Player): Returns the registered player model.
        '''

        # Get a model for the player
        player = self._update_player(address, name)
        if not player: return None
        print 'Player added: %s (%s)' % (name, address)

        # Flag the player as connected
        player.connected = True
        return player

    def remove_player(self, address, name):
        '''
        Removes the player model registered for the given unique composite key.

        Args:
           address (string): The IP address of the player. This could be 'None' for bot players.
           name (string): The name of the player.

        Returns:
            Player (Player): Returns the unregistered player model.
        '''

        # Get a model for the player
        player = self._update_player(address, name)
        if not player: return None
        print 'Player removed: %s (%s)' % (name, address)

        # Flag the player as disconnected
        player.connected = False
        return player

    def get_player(self, name):
        '''
        Looks up the player object associated with the given name.

        Args:
           name (string): The name of the player to get.

        Returns:
            Player (Player): Returns a registered player model.
        '''

        # Handle requests for missing players
        if not name:
            return self.EMPTY_PLAYER

        # Get a model for the player
        if name in self.name_to_player:
            return self.name_to_player[name]

        print 'ERROR - Missing player reference: ', name
        return None

    def get_player_names(self):
        '''
        Gets a sorted list of names for all the player objects.

        Args:
           None

        Returns:
            Names (list): Returns a sorted list of names for all the player objects.
        '''

        names = [p.name for p in self.players]
        names.sort(key=str.lower)
        return names

    def set_game_status(self, status, map_id, clock_limit, score_limit):
        '''
        Sets the current game status based on the given parameters.

        Args:
           status (string): The current status of the game.
           map_id (string): The unique identifier of the current map.
           clock_limit (integer): The maximum number of seconds before the game ends.
           score_limit (integer): The maximum score before the game ends.

        Returns:
            game (Game): Returns the registered game model.
        '''

        game = None
        if status == 'pre':

            # Create a new model when the game is starting
            game = Game(status, map_id, clock_limit, score_limit)
            self.games.append(game)
            print 'Game added: %i %s' % (game.id, game.map_id)
        else:

            # Update the game to reflect the current status    
            game = self.get_game()
            game.status = status
            game.map_id = map_id
            game.clock_limit = clock_limit
            game.score_limit = score_limit
        return game

    def get_game(self, id=None):
        '''
        Looks up the game object associated with the given id or gets the currently active game if
        no id is provided.

        Args:
           id (string): The id of the game to get. None is equivalent to the current game.

        Returns:
            game (Game): Returns a registered game model.
        '''

        # Handle requests for missing games or the current game
        if not id:
            if len(self.games) == 0:
                return self.EMPTY_GAME
            return self.games[-1]

        # Get a model for the game
        if id in self.id_to_game:
            return self.id_to_game[id]

        print 'ERROR - Missing game reference: ', id
        return None

    def get_kit(self, id):
        '''
        Looks up the kit object associated with the given id.

        Args:
           id (string): The id of the kit to get.

        Returns:
            kit (Kit): Returns a registered kit model.
        '''

        # Handle requests for missing kits
        if not id:
            return kits.EMPTY

        # Get a model for the kit
        if id in self.id_to_kit:
            return self.id_to_kit[id]

        print 'ERROR - Missing kit reference: ', id
        return None

    def get_kit_types(self):
        '''
        Gets a list of registered kit types.

        Args:
           None

        Returns:
            types (list): Returns a list of registered kit types.
        '''

        return self.type_to_kits.keys()

    def get_kits(self, kit_type):
        '''
        Gets a list of registered kits that match the given type.

        Args:
           kit_type (string): The type of kits to get.

        Returns:
            kits (list): Returns a list of kits based on type.
        '''

        if kit_type and kit_type in self.type_to_kits:
            return self.type_to_kits[kit_type]
        return []

    def get_map(self, id):
        '''
        Looks up the map object associated with the given id.

        Args:
           id (string): The id of the map to get.

        Returns:
            map (Map): Returns a registered map model.
        '''

        # Handle requests for missing maps
        if not id:
            return maps.EMPTY

        # Get a model for the map
        if id in self.id_to_map:
            return self.id_to_map[id]

        print 'ERROR - Missing map reference: ', id
        return None

    def get_team(self, id):
        '''
        Looks up the team object associated with the given id.

        Args:
           id (string): The id of the team to get.

        Returns:
            team (Team): Returns a registered team model.
        '''

        # Handle requests for missing teams
        if not id:
            return teams.EMPTY

        # Get a model for the team
        if id in self.id_to_team:
            return self.id_to_team[id]

        print 'ERROR - Missing team reference: ', id
        return None

    def get_vehicle(self, id):
        '''
        Looks up the vehicle object associated with the given id.

        Args:
           id (string): The id of the vehicle to get.

        Returns:
            vehicle (Vehicle): Returns a registered vehicle model.
        '''

        # Handle requests for missing vehicles
        if not id:
            return vehicles.EMPTY

        # Get a model for the vehicle
        if id in self.id_to_vehicle:
            return self.id_to_vehicle[id]

        print 'ERROR - Missing vehicle reference: ', id
        return None

    def get_vehicle_types(self):
        '''
        Gets a list of registered vehicle types.

        Args:
           None

        Returns:
            types (list): Returns a list of registered vehicle types.
        '''

        return self.type_to_vehicles.keys()

    def get_vehicles(self, vehicle_type):
        '''
        Gets a list of registered vehicles that match the given type.

        Args:
           vehicle_type (string): The type of vehicles to get.

        Returns:
            vehicles (list): Returns a list of vehicles based on type.
        '''

        if vehicle_type and vehicle_type in self.type_to_vehicles:
            return self.type_to_vehicles[vehicle_type]
        return []

    def get_weapon(self, id):
        '''
        Looks up the weapon object associated with the given id.

        Args:
           id (string): The id of the weapon to get.

        Returns:
            weapon (Weapon): Returns a registered weapon model.
        '''

        # Handle requests for missing weapons
        if not id:
            return weapons.EMPTY

        # Get a model for the weapon
        if id in self.id_to_weapon:
            return self.id_to_weapon[id]

        print 'ERROR - Missing weapon reference: ', id
        return None

    def get_weapon_types(self):
        '''
        Gets a list of registered weapon types.

        Args:
           None

        Returns:
            types (list): Returns a list of registered weapon types.
        '''

        return self.type_to_weapons.keys()

    def get_weapons(self, weapon_type):
        '''
        Gets a list of registered weapons that match the given type.

        Args:
           weapon_type (string): The type of weapons to get.

        Returns:
            weapons (list): Returns a list of weapons based on type.
        '''

        if weapon_type and weapon_type in self.type_to_weapons:
            return self.type_to_weapons[weapon_type]
        return []

    def _update_player(self, address, name):

        # Attempt to get the player by name and then address
        player = None
        if name and name in self.name_to_player:
            player = self.name_to_player[name]
        elif address and address in self.addr_to_player:
            player = self.addr_to_player[address]
        else:
            player = Player(address, name)

        # Make sure the player model is up to date
        player.address = address
        player.name = name
        player.artificial = (address == None)

        # Update the address mapping for human players
        if address:
            self.addr_to_player[address] = player

        # Update the name mapping for all players
        self.name_to_player[name] = player

        # Update the master player index
        if not player in self.players:
            self.players.append(player)
        return player

# Create a shared singleton instance of the model manager
model_mgr = ModelManager()
