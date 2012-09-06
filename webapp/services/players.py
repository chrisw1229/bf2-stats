
import cherrypy
import os.path

import models.players

from models import model_mgr
from stats import PlayerStats, stat_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    MODEL_FIELDS = ['aliases', 'id', 'name']

    STATS_FIELDS = ['assisted_total', 'assists_total', 'bullets_fired',
            'bullets_hit', 'commander_time', 'deaths_total',
            'deaths_streak_max', 'flag_capture_assists_total',
            'flag_captures_total', 'flag_defends_total',
            'flag_neutralize_assists_total', 'flag_neutralizes_total', 'games',
            'healed_total', 'heals_total', 'leader_time', 'losses',
            'kills_5_total', 'kills_10_total', 'kills_ratio_total',
            'kills_streak_max', 'kills_total', 'place_overall', 'play_time',
            'repairs_total', 'revived_total', 'revives_total', 'score_total',
            'spec_time', 'squad_time', 'suicides_total', 'supplied_total',
            'supplies_total', 'team_killed_total', 'team_kills_total',
            'teamwork_total', 'wins', 'wounds_total']

    def GET(self, id=None, data_type=None):
        '''
        Provides an index of available players or details for a specific player
        based on the given player identifier.

        Args:
            id (string): The unique identifier of a player. None indicates an
                    index of all players should be returned.
            data_type (string): The type of player data to return. None
                    indicates basic statistics should be returned.

        Returns:
            players (list): Returns the list of all players.
            player (object): Detailed information for a specific player.
        '''

        # Make sure the data type is case-insensitive
        if data_type:
            data_type = data_type.lower()

        # Handle requests for specific players
        if id and id != 'index.json':
            data_type = os.path.splitext(data_type)[0]
            if data_type == 'statistics':
                return self.get_player_stats(id)
            elif data_type == 'enemies':
                return self.get_player_enemies(id)
            elif data_type == 'kits':
                return self.get_player_kits(id)
            elif data_type == 'maps':
                return self.get_player_maps(id)
            elif data_type == 'teams':
                return self.get_player_teams(id)
            elif data_type == 'vehicles':
                return self.get_player_vehicles(id)
            elif data_type == 'weapons':
                return self.get_player_weapons(id)
            else:
                raise cherrypy.HTTPError(404)

        # Handle requests for the full player index
        return self.get_players()

    def get_player_stats(self, id):
        '''
        Provides a map of various statistics for a specific player based on the
        given player identifier.

        Args:
            id (string): The unique identifier of a player.

        Returns:
            statistics (tuple): Detailed statistics for a specific player.
        '''

        # Get the model for the requested player
        player = model_mgr.get_player(id)
        if not player: raise cherrypy.HTTPError(404)

        # Get the stats for the requested player
        player_stats = stat_mgr.get_player_stats(player)

        # Respond with a summary of the player model and stats
        results = list()
        for key in Handler.MODEL_FIELDS:
            results.append({ 'key': key, 'value': player.__dict__[key] })
        for key in Handler.STATS_FIELDS:
            results.append({ 'key': key, 'value': player_stats.__dict__[key] })
        results.sort(key=lambda r: r['key'])
        return results

    def get_player_enemies(self, id):
        '''
        Provides enemy details for a specific player based on the given player
        identifier.

        Args:
           id (string): The unique identifier of a player.

        Returns:
            enemies (object): Detailed enemy information for a specific player.
        '''

        # Get the model for the requested player
        player = model_mgr.get_player(id)
        if not player: raise cherrypy.HTTPError(404)

        # Get the stats for the requested player
        player_stats = stat_mgr.get_player_stats(player)

        # Build a list of column descriptors
        columns = [{ 'name': 'Players', 'data': 'player' },
                { 'name': 'Wounds', 'data': 'number', 'sorted': False },
                { 'name': 'Deaths', 'data': 'number' },
                { 'name': 'Kills', 'data': 'number' }]

        # Build a list of enemy statistics
        rows = list()
        for player in player_stats.enemies:
            if player != models.players.EMPTY:
                object_stats = player_stats.enemies[player]
                player_tuple = {
                    'id': player.id,
                    'name': player.name,
                    'photo': player.photo_s
                }
                rows.append([player_tuple, object_stats.wounds,
                        object_stats.deaths, object_stats.kills])

        # Sort the results by deaths to enemies
        rows.sort(key=lambda r: r[1], reverse=True)

        return { 'columns' : columns, 'rows': rows }

    def get_player_kits(self, id):
        '''
        Provides kit details for a specific player based on the given player
        identifier.

        Args:
           id (string): The unique identifier of a player.

        Returns:
            kits (object): Detailed kit information for a specific player.
        '''

        # Get the model for the requested player
        player = model_mgr.get_player(id)
        if not player: raise cherrypy.HTTPError(404)

        # Get the stats for the requested player
        player_stats = stat_mgr.get_player_stats(player)

        # Build a list of column descriptors
        columns = [{ 'name': 'Kits', 'data': 'kit' },
                { 'name': 'Score', 'data': 'number', 'sorted': False },
                { 'name': 'Kills', 'data': 'number' },
                { 'name': 'Deaths', 'data': 'number' }]

        # Build a list of kit statistics
        rows = list()
        for kit in player_stats.kits:
            if kit != models.kits.EMPTY:
                object_stats = player_stats.kits[kit]
                kit_tuple = { 'id': kit.id, 'name': kit.name }
                rows.append([kit_tuple, object_stats.score, object_stats.kills,
                        object_stats.deaths])

        # Sort the results by score
        rows.sort(key=lambda r: r[1], reverse=True)

        return { 'columns' : columns, 'rows': rows }

    def get_player_maps(self, id):
        '''
        Provides map details for a specific player based on the given player
        identifier.

        Args:
           id (string): The unique identifier of a player.

        Returns:
            maps (object): Detailed map information for a specific player.
        '''

        # Get the model for the requested player
        player = model_mgr.get_player(id)
        if not player: raise cherrypy.HTTPError(404)

        # Get the stats for the requested player
        player_stats = stat_mgr.get_player_stats(player)

        # Build a list of column descriptors
        columns = [{ 'name': 'Maps', 'data': 'map' },
                { 'name': 'Score', 'data': 'number', 'sorted': False },
                { 'name': 'Kills', 'data': 'number' },
                { 'name': 'Deaths', 'data': 'number' }]

        # Build a list of map statistics
        rows = list()
        for map_obj in player_stats.maps:
            if map_obj != models.maps.EMPTY:
                object_stats = player_stats.maps[map_obj]
                map_tuple = { 'id': map_obj.id, 'name': map_obj.name }
                rows.append([map_tuple, object_stats.score,
                        object_stats.kills, object_stats.deaths])

        # Sort the results by score
        rows.sort(key=lambda r: r[1], reverse=True)

        return { 'columns' : columns, 'rows': rows }

    def get_player_teams(self, id):
        '''
        Provides team details for a specific player based on the given player
        identifier.

        Args:
           id (string): The unique identifier of a player.

        Returns:
            teams (object): Detailed team information for a specific player.
        '''

        # Get the model for the requested player
        player = model_mgr.get_player(id)
        if not player: raise cherrypy.HTTPError(404)

        # Get the stats for the requested player
        player_stats = stat_mgr.get_player_stats(player)

        # Build a list of column descriptors
        columns = [{ 'name': 'Teams', 'data': 'team' },
                { 'name': 'Score', 'data': 'number', 'sorted': False },
                { 'name': 'Kills', 'data': 'number' },
                { 'name': 'Deaths', 'data': 'number' }]

        # Build a list of team statistics
        rows = list()
        for team in player_stats.teams:
            if team != models.teams.EMPTY:
                object_stats = player_stats.teams[team]
                team_tuple = { 'id': team.id, 'name': team.name }
                rows.append([team_tuple, object_stats.score, object_stats.kills,
                        object_stats.deaths])

        # Sort the results by score
        rows.sort(key=lambda r: r[1], reverse=True)

        return { 'columns' : columns, 'rows': rows }

    def get_player_vehicles(self, id):
        '''
        Provides vehicle details for a specific player based on the given player
        identifier.

        Args:
           id (string): The unique identifier of a player.

        Returns:
            vehicles (object): Detailed vehicle information for a specific
            player.
        '''

        # Get the model for the requested player
        player = model_mgr.get_player(id)
        if not player: raise cherrypy.HTTPError(404)

        # Get the stats for the requested player
        player_stats = stat_mgr.get_player_stats(player)

        # Build a list of column descriptors
        columns = [{ 'name': 'Vehicles', 'data': 'vehicle' },
                { 'name': 'Kills', 'data': 'number', 'sorted': False },
                { 'name': 'Deaths', 'data': 'number' }]

        # Build a list of vehicle statistics
        rows = list()
        for vehicle in player_stats.vehicles:
            if vehicle != models.vehicles.EMPTY:
                object_stats = player_stats.vehicles[vehicle]
                vehicle_tuple = { 'id': vehicle.id, 'name': vehicle.name }
                rows.append([vehicle_tuple, object_stats.kills,
                        object_stats.deaths])

        # Sort the results by kills
        rows.sort(key=lambda r: r[1], reverse=True)

        return { 'columns' : columns, 'rows': rows }

    def get_player_weapons(self, id):
        '''
        Provides weapon details for a specific player based on the given player
        identifier.

        Args:
           id (string): The unique identifier of a player.

        Returns:
            weapons (object): Detailed weapon information for a specific player.
        '''

        # Get the model for the requested player
        player = model_mgr.get_player(id)
        if not player: raise cherrypy.HTTPError(404)

        # Get the stats for the requested player
        player_stats = stat_mgr.get_player_stats(player)

        # Build a list of column descriptors
        columns = [{ 'name': 'Weapons', 'data': 'weapon' },
                { 'name': 'Kills', 'data': 'number', 'sorted': False },
                { 'name': 'Deaths', 'data': 'number' },
                { 'name': 'Accuracy', 'data': 'percent' }]

        # Build a list of weapon statistics
        rows = list()
        for weapon in player_stats.weapons:
            if weapon != models.weapons.EMPTY:
                object_stats = player_stats.weapons[weapon]
                weapon_tuple = { 'id': weapon.id, 'name': weapon.name }
                rows.append([weapon_tuple, object_stats.kills, object_stats.deaths,
                        [object_stats.bullets_hit, object_stats.bullets_fired]])

        # Sort the results by kills
        rows.sort(key=lambda r: r[1], reverse=True)

        return { 'columns' : columns, 'rows': rows }

    def get_players(self):
        '''
        Provides an index of available players.

        Args:
            None

        Returns:
            players (list): Returns the list of all players.
        '''

        # Build an index of the available players
        results = list()
        for player in model_mgr.get_players():
            results.append({ 'id': player.id, 'name': player.name })

        # Sort the index by player name
        results.sort(key=lambda r: r['name'].lower())
        return results
