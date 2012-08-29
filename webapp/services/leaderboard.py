
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
 
        # Build a list of columns
        columns = list()
        columns.append({ 'name': 'Players', 'data': 'player' })
        columns.append({ 'name': 'Score', 'data': 'number', 'sorted': False })
        columns.append({ 'name': 'Help', 'data': 'number' })
        columns.append({ 'name': 'Kills', 'data': 'number' })
        columns.append({ 'name': 'Deaths', 'data': 'number' })
        columns.append({ 'name': 'Time', 'data': 'string' })

        # Build a row of statistics for each player
        rows = list()
        for player in model_mgr.get_players():
            player_stats = stat_mgr.get_player_stats(player);
            player_tuple = {
                'id': player.id,
                'name': player.name,
                'photo': player.photo_s
            }
            rows.append([player_tuple, player_stats.score_total,
                    player_stats.teamwork_total, player_stats.kills_total,
                    player_stats.deaths_total, player_stats.play_time])

        # Sort the results by score
        rows.sort(key=lambda r: r[1], reverse=True)
        return { 'columns': columns, 'rows': rows }
