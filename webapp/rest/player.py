
import cherrypy

from model import model_mgr
from stats import stats_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self, name=None, statistics=None):
        if name:
            player = model_mgr.get_player(name)
            if not player: return None

            if statistics:
                return stats_mgr.get_player_stats(player).__dict__
            return model_mgr.get_player(name).__dict__

        return model_mgr.get_player_names()
