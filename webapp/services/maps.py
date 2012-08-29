
import cherrypy

import models.maps

from models import model_mgr
from stats import stat_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self, id=None):
        '''
        Provides an index of available maps or details for a specific map
        based on the given map identifier.

        Args:
            id (string): The unique identifier of a map. None indicates an
                    index of all maps should be returned.

        Returns:
            maps (list): Returns the list of all maps.
            map (object): Detailed information for a specific map.
        '''

        # Handle requests for specific maps
        if id:
            return self.get_map(id)

        # Handle requests for the full map index
        return self.get_maps()

    def get_map(self, id):
        '''
        Provides details for a specific map based on the given map identifier.

        Args:
           id (string): The unique identifier of a map.

        Returns:
            map (object): Detailed information for a specific map.
        '''

        # Get the model for the requested map
        map_obj = model_mgr.get_map(id)
        if not map_obj: raise cherrypy.HTTPError(404)

        # Get the stats for the requested map
        map_stats = stat_mgr.get_map_stats(map_obj)

        # Build a list of column descriptors
        columns = [{ 'name': 'Players', 'data': 'player' },
                { 'name': 'Score', 'data': 'number', 'sorted': False },
                { 'name': 'Kills', 'data': 'number' },
                { 'name': 'Deaths', 'data': 'number' }]

        # Build a list of map statistics
        rows = list()
        for player in map_stats.players:
            if player != models.players.EMPTY:
                object_stats = map_stats.players[player]
                player_tuple = {
                    'id': player.id,
                    'name': player.name,
                    'photo': player.photo_s
                }
                rows.append([player_tuple, object_stats.score,
                        object_stats.kills, object_stats.deaths])

        # Sort the results by score
        rows.sort(key=lambda r: r[1], reverse=True)

        return { 'id': map_obj.id, 'name': map_obj.name, 'columns' : columns,
                'rows': rows }

    def get_maps(self):
        '''
        Provides an index of available maps.

        Args:
            None

        Returns:
            maps (list): Returns the list of all maps.
        '''

        # Build an index of the available players
        results = list()
        for map_obj in model_mgr.get_maps():
            results.append({ 'id': map_obj.id, 'name': map_obj.name })

        # Sort the index by map name
        results.sort(key=lambda r: r['name'].lower())
        return results
