
import cherrypy

from model import model_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self, name=None):
        if name:
            return model_mgr.get_player(name).__dict__

        return model_mgr.get_player_names()