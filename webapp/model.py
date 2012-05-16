
import vehicle

class Player(object):

    counter = 0

    def __init__(self, address, name):
        self.id = Player.counter
        self.address = address
        self.name = name
        self.artificial = False
        self.connected = False

        Player.counter += 1

class ModelManager(object):

    # Sentinel objects to avoid none checks everywhere
    NONE_PLAYER = Player('', '')
    NONE_VEHICLE = vehicle.Vehicle('', '', '', '')

    players = []
    name_to_player = {}
    addr_to_player = {}

    vehicles = []
    id_to_vehicle = {}
    type_to_vehicles = {}

    # This method will be called to initialize the manager
    def start(self):
        print 'MODEL MANAGER - STARTING'

        self.vehicles = vehicle.registry
        for v in self.vehicles:
            self.id_to_vehicle[v.id] = v
            
            if not v.vehicle_type in self.type_to_vehicles:
                self.type_to_vehicles[v.vehicle_type] = []
            self.type_to_vehicles[v.vehicle_type].append(v)
        print 'Vehicles registered: ', len(self.vehicles)

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
        print 'Adding player: %s (%s)' % (name, address)

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
        print 'Removing player: %s (%s)' % (name, address)
        
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
            return self.NONE_PLAYER

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

    def get_vehicle(self, id):
        '''
        Looks up the vehicle object associated with the given id.

        Args:
           id (string): The id of the player to get.

        Returns:
            vehicle (Vehicle): Returns a registered vehicle model.
        '''

        # Handle requests for missing vehicles
        if not id:
            return self.NONE_VEHICLE

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
            vehicles (list): Returns a list vehicles based on type.
        '''

        if vehicle_type and vehicle_type in self.type_to_vehicles:
            return self.type_to_vehicles[vehicle_type]
        return None

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
