
import cherrypy

import models.kits

from models import model_mgr
from stats import stat_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self, id=None):
        '''
        Provides an index of available kits or details for a specific kit
        based on the given kit identifier.

        Args:
            id (string): The unique identifier of a kit. None indicates an
                    index of all kits should be returned.

        Returns:
            kits (list): Returns the list of all kits.
            kit (object): Detailed information for a specific kit.
        '''

        # Handle requests for specific kits
        if id:
            return self.get_kit(id)

        # Handle requests for the full kit index
        return self.get_kits()

    def get_kit(self, id):
        '''
        Provides details for a specific kit based on the given kit identifier.

        Args:
           id (string): The unique identifier of a kit.

        Returns:
            kit (object): Detailed information for a specific kit.
        '''

        # Get the model for the requested kit
        kit = model_mgr.get_kit(id)
        if not kit: raise cherrypy.HTTPError(404)

        # Get the stats for the requested kit
        kit_stats = stat_mgr.get_kit_stats(kit)

        # Build a list of column descriptors
        columns = [{ 'name': 'Players', 'data': 'string' },
                { 'name': 'Score', 'data': 'number', 'sorted': False },
                { 'name': 'Kills', 'data': 'number' },
                { 'name': 'Deaths', 'data': 'number' }]

        # Build a list of kit statistics
        rows = list()
        for player in kit_stats.players:
            if player != models.players.EMPTY:
                object_stats = kit_stats.players[player]
                rows.append([player.name, object_stats.score,
                        object_stats.kills, object_stats.deaths])

        # Sort the results by score
        rows.sort(key=lambda r: r[1], reverse=True)

        return { 'id': kit.id, 'name': kit.name, 'columns' : columns,
                'rows': rows }

    def get_kits(self):
        '''
        Provides an index of available kits.

        Args:
            None

        Returns:
            kits (list): Returns the list of all kits.
        '''

        # Build an index of the available players
        results = list()
        for kit in model_mgr.get_kits():
            results.append({ 'id': kit.id, 'name': kit.name })

        # Sort the index by kit name
        results.sort(key=lambda r: r['name'].lower())
        return results
