
import os.path

import cherrypy

# Importing the stats plugin registers it with the cherrypy engine
import plugin
import services.awards
import services.games
import services.kits
import services.leaderboard
import services.live
import services.maps
import services.players
import services.replays
import services.teams
import services.vehicles
import services.weapons

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
root.services.games = services.games.Handler()
root.services.kits = services.kits.Handler()
root.services.leaderboard = services.leaderboard.Handler();
root.services.maps = services.maps.Handler()
root.services.live = services.live.Handler()
root.services.players = services.players.Handler()
root.services.replays = services.replays.Handler()
root.services.teams = services.teams.Handler()
root.services.vehicles = services.vehicles.Handler()
root.services.weapons = services.weapons.Handler()

# The current directory is needed in the config file
current_dir = os.path.abspath(os.path.dirname(__file__))

# Get the path to the configuration file
confPath = os.path.join(os.path.dirname(__file__), 'application.conf')

# Disable screen output for the access log
cherrypy.log._set_screen_handler(cherrypy.log.access_log, False)

# Start the web application server
if __name__ == '__main__':
    cherrypy.quickstart(root, '/', confPath)
