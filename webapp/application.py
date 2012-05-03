import os.path

import cherrypy

import rest.award

# Create an empty class to handle root directory requests
class Root(object):
    pass
root = Root()

# Register all the REST request handlers
root.award = rest.award.Handler()

# Get the path to the configuration file
confPath = os.path.join(os.path.dirname(__file__), 'application.conf')

# Start the web application server
if __name__ == '__main__':
    cherrypy.quickstart(root, '/', confPath)