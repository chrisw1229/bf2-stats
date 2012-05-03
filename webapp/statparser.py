import cherrypy
import processor.award

class StatParser(cherrypy.process.plugins.SimplePlugin):

    log_file_path = None
    log_file = None
    processors = []

    # This method will be called when the plugin engine starts
    def start(self):
        print 'STAT PARSER - STARTING'

        # Build a path to the log file
        if not self.log_file_path:
            raise Exception('Stats log file not configured')
        print 'Opening stats log file: ', self.log_file_path

        # Open the log file in read mode
        try:
            self.log_file = open(self.log_file_path, 'r')
        except IOError:
            raise Exception('Unable to open stat log file: ' + self.log_file_path)

        # Start all the log processors
        self.processors = [processor.award.Processor()]
        for proc in self.processors:
            proc.start()

        print 'STAT PARSER - STARTED'
    start.priority = 100

    # This method will be called by the plugin engine at regular intervals (about every 100ms)
    def main(self):
        if not self.log_file:
            return

        # Keep reading lines until the stream is exhausted
        running = True
        while running:

            # Attempt to read the next log entry
            line = self.log_file.readline().strip()

            # Parse valid log entries
            if (len(line) > 0):
                self.parse(line)
            else:
                running = False

    # This method will be called when the plugin engine stops
    def stop(self):
        print 'STAT PARSER - STOPPING'

        # Stop all the log processors
        for proc in reversed(self.processors):
            proc.stop()

        # Clean up the file log file handle
        if self.log_file:
            print 'Closing stats log file: ', self.log_file_path
            self.log_file.close()

        print 'STAT PARSER - STOPPED'

    def parse(self, line):

        # Break the line into individual elements
        elements = line.split(';')
        assert len(elements) > 1, 'Invalid log line %s' % 'line'

        # Extract the log time and type
        timestamp = int(elements[0])
        type = elements[1]
        values = elements[2:]
        print timestamp, type, values

# Register this class with the plugin engine
cherrypy.engine.statparser = StatParser(cherrypy.engine)