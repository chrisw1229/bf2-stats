
import cherrypy

@cherrypy.expose()
class Handler:

    def GET(self, id=None):
        if id:
            return 'AWARD: ', id
        return 'AWARD INDEX'