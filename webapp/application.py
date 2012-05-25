
import os.path

import cherrypy

# Importing the stats plugin registers it with the cherrypy engine
import plugin
import services.awards
import services.live
import services.players

# Create an empty class to handle root directory requests
class Root(object):
    pass
root = Root()

# Create an empty class to handle service requests
class Services(object):
    pass
root.services = Services()

# Register all the service request handlers
root.services.awards = services.awards.Handler()
root.services.live = services.live.Handler()
root.services.players = services.players.Handler()

# The current directory is needed in the config file
current_dir = os.path.abspath(os.path.dirname(__file__))

# Get the path to the configuration file
confPath = os.path.join(os.path.dirname(__file__), 'application.conf')

# Disable screen output for the access log
cherrypy.log._set_screen_handler(cherrypy.log.access_log, False)

# Start the web application server
if __name__ == '__main__':
    cherrypy.quickstart(root, '/', confPath)
