
import cherrypy

from stats import stat_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self):
        '''
        Provides statistics that represent the overall LAN party.

        Args:
           None

        Returns:
            overview (object): Overall information for the entire LAN party.
        '''
 
        return stat_mgr.get_stats()
