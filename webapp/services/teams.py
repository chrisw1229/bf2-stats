
import cherrypy

import models.teams

from models import model_mgr
from stats import stat_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self, id=None):
        '''
        Provides an index of available teams or details for a specific team
        based on the given team identifier.

        Args:
            id (string): The unique identifier of a team. None indicates an
                    index of all teams should be returned.

        Returns:
            teams (list): Returns the list of all teams.
            team (object): Detailed information for a specific team.
        '''

        # Handle requests for specific teams
        if id:
            return self.get_team(id)

        # Handle requests for the full team index
        return self.get_teams()

    def get_team(self, id):
        '''
        Provides details for a specific team based on the given team identifier.

        Args:
           id (string): The unique identifier of a team.

        Returns:
            team (object): Detailed information for a specific team.
        '''

        # Get the model for the requested team
        team = model_mgr.get_team(id)
        if not team: raise cherrypy.HTTPError(404)

        # Get the stats for the requested team
        team_stats = stat_mgr.get_team_stats(team)

        # Build a list of column descriptors
        columns = [{ 'name': 'Players', 'data': 'string' },
                { 'name': 'Score', 'data': 'number', 'sorted': False },
                { 'name': 'Kills', 'data': 'number' },
                { 'name': 'Deaths', 'data': 'number' }]

        # Build a list of team statistics
        rows = list()
        for player in team_stats.players:
            if player != models.players.EMPTY:
                object_stats = team_stats.players[player]
                rows.append([player.name, object_stats.score,
                        object_stats.kills, object_stats.deaths])

        # Sort the results by score
        rows.sort(key=lambda r: r[1], reverse=True)

        return { 'id': team.id, 'name': team.name, 'columns' : columns,
                'rows': rows }

    def get_teams(self):
        '''
        Provides an index of available teams.

        Args:
            None

        Returns:
            teams (list): Returns the list of all teams.
        '''

        # Build an index of the available players
        results = list()
        for team in model_mgr.teams:
            results.append({ 'id': team.id, 'name': team.name })

        # Sort the index by team name
        results.sort(key=lambda r: r['name'].lower())
        return results
