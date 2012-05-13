
class Player(object):

    def __init__(self, address, name):
        self.address = address
        self.name = name

class PlayerManager(object):

    players = []

    # This method will be called to initialize the manager
    def start(self):
        print 'PLAYER MANAGER - STARTING'

        print 'PLAYER MANAGER - STARTED'

    # This method will be called to shutdown the manager
    def stop(self):
        print 'PLAYER MANAGER - STOPPING'

        print 'PLAYER MANAGER - STOPPED'

    def add_player(self, address, name):
        '''
        Adds or updates the player model registered for the given unique composite key.

        Args:
           address (string): The IP address of the player. This could be 'None' for bot players.
           name (string): The name of the player.

        Returns:
            Player (Player): Returns the registered player model.
        '''

        # TODO Add logic to update the player model
        pass

    def remove_player(self, address, name):
        '''
        Removes the player model registered for the given unique composite key.

        Args:
           address (string): The IP address of the player. This could be 'None' for bot players.
           name (string): The name of the player.

        Returns:
            Player (Player): Returns the unregistered player model.
        '''

        # TODO Add logic to remove the player model
        pass

    def get_player(self, name):
        '''
        Looks up the player object associated with the given name.

        Args:
           name (string): The name of the player to get.

        Returns:
            Player (Player): Returns a registered player model.
        '''

        # TODO Look up the player by name
        return Player('', name)

# Create a shared singleton instance of the player manager
player_mgr = PlayerManager()
