
import cherrypy

from models import model_mgr
from stats import stat_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self):
        '''
        Provides statistics that represent the overall performance of all players.

        Args:
           None

        Returns:
            leaders (object): Overall information for all players.
        '''
 
        # Get a list of all the players
        players = model_mgr.players

        # Build a list of columns
        columns = list()
        columns.append({ 'sorted': None, 'data': 'string', 'name': 'Players' })
        columns.append({ 'sorted': False, 'data': 'number', 'name': 'Score' })
        columns.append({ 'sorted': None, 'data': 'number', 'name': 'Kills' })
        columns.append({ 'sorted': None, 'data': 'number', 'name': 'Deaths' })

        # Build a row of statistics for each player
        rows = list()
        for player in players:
            player_stats = stat_mgr.get_player_stats(player);
            rows.append([player.name, player_stats.score_total,
                    player_stats.kills_total, player_stats.deaths_total])

        # Sort the results by score
        rows.sort(key=lambda r: r[1], reverse=True)
        return { 'columns': columns, 'rows': rows }
