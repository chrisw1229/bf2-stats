
import copy

import cherrypy

from models import model_mgr
from stats import stat_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self, id=None):
        '''
        Provides an index of available players or details for a specific player
        based on the given player identifier.

        Args:
           id (string): The unique identifier of a player. None indicates an
                index of all players should be returned.

        Returns:
            players (list): Returns the list of all players.
            player (object): Detailed information for a specific player.
        '''

        # Handle requests for specific players
        if id:

            # Get the model for the requested player
            player = model_mgr.get_player(id)

            # Get the stats for the requested player
            player_stats = stat_mgr.get_player_stats(player)

            # Respond with a summary of the player information
            results = copy.deepcopy(player_stats)
            results.aliases = player.aliases
            return results

        # Build an index of the available players
        results = list()
        for player in model_mgr.players:
            results.append({ 'id': player.id, 'name': player.name })

        # Sort the index by player name
        results.sort(key=lambda a: a['name'].lower())
        return results
