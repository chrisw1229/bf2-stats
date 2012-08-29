
import cherrypy

import models.games

from models import model_mgr
from stats import stat_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self, id=None):
        '''
        Provides an index of available games or details for a specific game
        based on the given game identifier.

        Args:
            id (string): The unique identifier of a game. None indicates an
                    index of all games should be returned.

        Returns:
            games (list): Returns the list of all games.
            game (object): Detailed information for a specific game.
        '''

        # Handle requests for specific games
        if id:
            return self.get_game(id)

        # Handle requests for the full game index
        return self.get_games()

    def get_game(self, id):
        '''
        Provides details for a specific game based on the given game identifier.

        Args:
           id (string): The unique identifier of a game.

        Returns:
            game (object): Detailed information for a specific game.
        '''

        # Get the model for the requested game
        game = model_mgr.get_game(id)
        if not game: raise cherrypy.HTTPError(404)

        # Get the stats for the requested game
        game_stats = stat_mgr.get_game_stats(game)

        # Build a list of column descriptors
        columns = [{ 'name': 'Players', 'data': 'player' },
                { 'name': 'Score', 'data': 'number', 'sorted': False },
                { 'name': 'Help', 'data': 'number' },
                { 'name': 'Kills', 'data': 'number' },
                { 'name': 'Deaths', 'data': 'number' }]

        # Build a list of game statistics
        rows = list()
        for player in game_stats.players:
            if player != models.players.EMPTY:
                object_stats = game_stats.players[player]
                player_tuple = {
                    'id': player.id,
                    'name': player.name,
                    'photo': player.photo_s
                }
                rows.append([player_tuple, object_stats.score,
                        object_stats.teamwork, object_stats.kills,
                        object_stats.deaths])

        # Sort the results by score
        rows.sort(key=lambda r: r[1], reverse=True)

        map_obj = model_mgr.get_map(game.map_id)
        return { 'id': game.id, 'name': map_obj.name, 'columns' : columns,
                'rows': rows }

    def get_games(self):
        '''
        Provides an index of available games.

        Args:
            None

        Returns:
            games (list): Returns the list of all games.
        '''

        # Build an index of the available games
        results = list()
        for game in model_mgr.get_games():
            game_stats = stat_mgr.get_game_stats(game)
            if game_stats.kills > 0:
                map_obj = model_mgr.get_map(game.map_id)
                results.append({ 'id': game.id, 'name': map_obj.name })

        # Sort the index by game id
        results.sort(key=lambda r: int(r['id']))
        return results
