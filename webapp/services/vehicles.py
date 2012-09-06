
import cherrypy
import os.path

import models.vehicles

from models import model_mgr
from stats import stat_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self, id=None):
        '''
        Provides an index of available vehicles or details for a specific
        vehicle based on the given vehicle identifier.

        Args:
            id (string): The unique identifier of a vehicle. None indicates an
                    index of all vehicles should be returned.

        Returns:
            vehicles (list): Returns the list of all vehicles.
            vehicle (object): Detailed information for a specific vehicle.
        '''

        # Handle requests for specific vehicles
        if id and id != 'index.json':
            id = os.path.splitext(id)[0]
            return self.get_vehicle(id)

        # Handle requests for the full vehicle index
        return self.get_vehicles()

    def get_vehicle(self, id):
        '''
        Provides details for a specific vehicle based on the given vehicle
        identifier.

        Args:
           id (string): The unique identifier of a vehicle.

        Returns:
            vehicle (object): Detailed information for a specific vehicle.
        '''

        # Get the model for the requested vehicle
        vehicle = model_mgr.get_vehicle(id)
        if not vehicle: raise cherrypy.HTTPError(404)

        # Get the stats for the requested vehicle
        vehicle_stats = stat_mgr.get_vehicle_stats(vehicle)

        # Build a list of column descriptors
        columns = [{ 'name': 'Players', 'data': 'player' },
                { 'name': 'Kills', 'data': 'number', 'sorted': False },
                { 'name': 'Deaths', 'data': 'number' }]

        # Build a list of vehicle statistics
        rows = list()
        for player in vehicle_stats.players:
            if player != models.players.EMPTY:
                object_stats = vehicle_stats.players[player]
                player_tuple = {
                    'id': player.id,
                    'name': player.name,
                    'photo': player.photo_s
                }
                rows.append([player_tuple, object_stats.kills,
                        object_stats.deaths])

        # Sort the results by kills
        rows.sort(key=lambda r: r[1], reverse=True)

        return { 'id': vehicle.id, 'name': vehicle.name, 'columns' : columns,
                'rows': rows }

    def get_vehicles(self):
        '''
        Provides an index of available vehicles.

        Args:
            None

        Returns:
            vehicles (list): Returns the list of all vehicles.
        '''

        # Build an index of the available players
        results = list()
        for vehicle in model_mgr.get_vehicles():
            results.append({ 'id': vehicle.id, 'name': vehicle.name })

        # Sort the index by vehicle name
        results.sort(key=lambda r: r['name'].lower())
        return results
