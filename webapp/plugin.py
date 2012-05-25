
import pkgutil
import traceback

import cherrypy

from events import event_mgr
from models import model_mgr
from stats import stat_mgr

class StatsPlugin(cherrypy.process.plugins.SimplePlugin):

    def __init__(self, engine):
        super(StatsPlugin, self).__init__(engine)

        self.log_file_path = None
        self.log_file = None

    # This method will be called when the plugin engine starts
    def start(self):
        print 'STATS PLUGIN - STARTING'

        # Register all the processors dynamically
        self._load_processor_modules('processors')

        # Start the singletons
        model_mgr.start()
        event_mgr.start()
        stat_mgr.start()

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
        stat_mgr.stop()
        event_mgr.stop()
        model_mgr.stop()

        print 'STATS PLUGIN - STOPPED'

    def _load_processor_modules(self, parent_package):
 
        # Loop over all the sub-modules in the parent package
        package_path = parent_package.replace('.', '/')
        for importer, modname, ispkg in pkgutil.walk_packages([package_path]):

            # Dynamically import each sub-module
            full_module = parent_package + '.' + modname
            processor_module = __import__(full_module, fromlist=[''])

            # Recursively load any sub-packages or load the processor class in the current module
            if ispkg:
                self._load_processor_modules(full_module)
            else:
                self._load_processor_module(processor_module)

    def _load_processor_module(self, processor_module):

        # Attempt to get the constructor definition
        processor_class = None
        try:
            processor_class = getattr(processor_module, 'Processor')
        except Exception, err:
            print 'ERROR - Module must contain a class called "Processor": ', (
                    processor_module.__name__)
            traceback.print_exc(err)
            return

        # Attempt to create an instance of the class
        processor = None
        try:
            processor = processor_class()
        except Exception, err:
            print ('ERROR - Unable to invoke processor constructor: %s.%s'
                    % (processor_class.__module__, processor_class.__name__))
            traceback.print_exc(err)
            return

        # Register the processor for stats purposes
        stat_mgr.add_processor(processor)

    def _process(self, line):

        # Parse the log line into a into a type-safe event
        event = event_mgr.create_event(line)

        # Process the event into useable statistics
        stat_mgr.process_event(event)

# Register this class with the plugin engine
cherrypy.engine.statsplugin = StatsPlugin(cherrypy.engine)
