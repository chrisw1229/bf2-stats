
import cherrypy

from event import ConnectEvent,DisconnectEvent,GameStatusEvent
import processor.core
import processor.award

from parse import parse_mgr
from model import model_mgr
from stats import stats_mgr

class StatsPlugin(cherrypy.process.plugins.SimplePlugin):

    log_file_path = None
    log_file = None

    # This method will be called when the plugin engine starts
    def start(self):
        print 'STATS PLUGIN - STARTING'

        # Register all the processors
        # TODO Load these dynamically
        stats_mgr.processors = [processor.core.Processor(), processor.award.Processor()]

        # Start the singletons
        parse_mgr.start()
        model_mgr.start()
        stats_mgr.start()

        # Build a path to the log file
        if not self.log_file_path:
            raise Exception('Stats log file not configured')
        print 'Opening stats log file: ', self.log_file_path

        # Open the log file in read mode
        try:
            self.log_file = open(self.log_file_path, 'r')
        except IOError:
            raise Exception('Unable to open stats log file: ' + self.log_file_path)

        print 'STATS PLUGIN - STARTED'
    start.priority = 100

    # This method will be called by the plugin engine at regular intervals (about every 100ms)
    def main(self):
        if not self.log_file or self.log_file.closed:
            return

        # Keep reading lines until the stream is exhausted
        running = True
        count = 0
        while running:

            # Attempt to read the next available log entry
            line = self.log_file.readline().strip()
            if (len(line) > 0):
                self._process(line)
                count += 1
            else:
                running = False
        if count > 0:
            print 'Log lines read: ', count

    # This method will be called when the plugin engine stops
    def stop(self):
        print 'STATS PLUGIN - STOPPING'

        # Clean up the file log file handle
        if self.log_file:
            print 'Closing stats log file: ', self.log_file_path
            self.log_file.close()

        # Stop the singletons
        stats_mgr.stop()
        model_mgr.stop()
        parse_mgr.stop()

        print 'STATS PLUGIN - STOPPED'

    def _process(self, line):

        # Parse the line into a raw values model
        entry = parse_mgr.parse(line)

        # Pre-process player connect and disconnect events
        log_type = entry.log_type
        if log_type == ConnectEvent.ID:
            model_mgr.add_player(entry.values[0], entry.values[1])
        elif log_type == DisconnectEvent.ID:
            model_mgr.remove_player(entry.values[0], entry.values[1])
        elif log_type == GameStatusEvent.ID:
            model_mgr.set_game_status(entry.values[0], entry.values[1], int(entry.values[2]),
                    int(entry.values[3]))

        # Convert the log entry into a type-safe event
        event = parse_mgr.convert(entry)

        # Process the event into useable statistics
        stats_mgr.process_event(event)

# Register this class with the plugin engine
cherrypy.engine.statsplugin = StatsPlugin(cherrypy.engine)
