import cherrypy

from parse import stat_parser
from manager import stat_mgr

class StatPlugin(cherrypy.process.plugins.SimplePlugin):

    log_file_path = None
    log_file = None

    # This method will be called when the plugin engine starts
    def start(self):
        print 'STAT PLUGIN - STARTING'

        # Start the singletons
        stat_parser.start()
        stat_mgr.start()

        # Build a path to the log file
        if not self.log_file_path:
            raise Exception('Stats log file not configured')
        print 'Opening stats log file: ', self.log_file_path

        # Open the log file in read mode
        try:
            self.log_file = open(self.log_file_path, 'r')
        except IOError:
            raise Exception('Unable to open stat log file: ' + self.log_file_path)

        print 'STAT PLUGIN - STARTED'
    start.priority = 100

    # This method will be called by the plugin engine at regular intervals (about every 100ms)
    def main(self):
        if not self.log_file:
            return

        # Keep reading lines until the stream is exhausted
        running = True
        while running:

            # Attempt to read the next available log entry
            line = self.log_file.readline().strip()
            if (len(line) > 0):

                # Parse the line into an event model
                event = stat_parser.parse(line)

                # Process the event into useable statistics
                stat_mgr.process(event)
            else:
                running = False

    # This method will be called when the plugin engine stops
    def stop(self):
        print 'STAT PLUGIN - STOPPING'

        # Clean up the file log file handle
        if self.log_file:
            print 'Closing stats log file: ', self.log_file_path
            self.log_file.close()

        # Stop the singletons
        stat_mgr.stop()
        stat_parser.stop()

        print 'STAT PLUGIN - STOPPED'

# Register this class with the plugin engine
cherrypy.engine.statplugin = StatPlugin(cherrypy.engine)
