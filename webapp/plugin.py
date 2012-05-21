
import cherrypy

import processor.core
import processor.live
import processor.award

from event import event_mgr
from model import model_mgr
from stats import stats_mgr

class StatsPlugin(cherrypy.process.plugins.SimplePlugin):

    def __init__(self, engine):
        super(StatsPlugin, self).__init__(engine)

        self.log_file_path = None
        self.log_file = None

    # This method will be called when the plugin engine starts
    def start(self):
        print 'STATS PLUGIN - STARTING'

        # Register all the processors
        # TODO Load these dynamically
        stats_mgr.core_processor = processor.core.Processor()
        stats_mgr.live_processor = processor.live.Processor()
        stats_mgr.processors = [stats_mgr.core_processor, stats_mgr.live_processor,
                processor.award.Processor()]

        # Start the singletons
        model_mgr.start()
        event_mgr.start()
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
        event_mgr.stop()
        model_mgr.stop()

        print 'STATS PLUGIN - STOPPED'

    def _process(self, line):

        # Parse the log line into a into a type-safe event
        event = event_mgr.create_event(line)

        # Process the event into useable statistics
        stats_mgr.process_event(event)

# Register this class with the plugin engine
cherrypy.engine.statsplugin = StatsPlugin(cherrypy.engine)
