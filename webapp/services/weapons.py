
import cherrypy

import models.weapons

from models import model_mgr
from stats import stat_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self, id=None):
        '''
        Provides an index of available weapons or details for a specific weapon
        based on the given weapon identifier.

        Args:
            id (string): The unique identifier of a weapon. None indicates an
                    index of all weapons should be returned.

        Returns:
            weapons (list): Returns the list of all weapons.
            weapon (object): Detailed information for a specific weapon.
        '''

        # Handle requests for specific weapons
        if id:
            return self.get_weapon(id)

        # Handle requests for the full weapon index
        return self.get_weapons()

    def get_weapon(self, id):
        '''
        Provides details for a specific weapon based on the given weapon
        identifier.

        Args:
           id (string): The unique identifier of a weapon.

        Returns:
            weapon (object): Detailed information for a specific weapon.
        '''

        # Get the model for the requested weapon
        weapon = model_mgr.get_weapon(id)
        if not weapon: raise cherrypy.HTTPError(404)

        # Get the stats for the requested weapon
        weapon_stats = stat_mgr.get_weapon_stats(weapon)

        # Build a list of column descriptors
        columns = [{ 'name': 'Players', 'data': 'string' },
                { 'name': 'Kills', 'data': 'number', 'sorted': False },
                { 'name': 'Deaths', 'data': 'number' }]

        # Build a list of weapon statistics
        rows = list()
        for player in weapon_stats.players:
            if player != models.players.EMPTY:
                object_stats = weapon_stats.players[player]
                rows.append([player.name, object_stats.kills,
                        object_stats.deaths])

        # Sort the results by score
        rows.sort(key=lambda r: r[1], reverse=True)

        return { 'id': weapon.id, 'name': weapon.name, 'columns' : columns,
                'rows': rows }

    def get_weapons(self):
        '''
        Provides an index of available weapons.

        Args:
            None

        Returns:
            weapons (list): Returns the list of all weapons.
        '''

        # Build an index of the available players
        results = list()
        for weapon in model_mgr.get_weapons():
            results.append({ 'id': weapon.id, 'name': weapon.name })

        # Sort the index by weapon name
        results.sort(key=lambda r: r['name'].lower())
        return results
