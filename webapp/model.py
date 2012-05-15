
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

    # Sentinel object to avoid none checks everywhere
    NONE_PLAYER = Player('', '')

    players = []
    name_to_player = {}
    addr_to_player = {}

    # This method will be called to initialize the manager
    def start(self):
        print 'MODEL MANAGER - STARTING'

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
        player = None
        if name in self.name_to_player:
            player = self.name_to_player[name]
        else:
            print 'ERROR - Missing player reference: ', name
        return player

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
