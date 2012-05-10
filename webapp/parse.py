import event

class StatParser(object):

    event_types = {}

    # This method will be called to initialize the parser
    def start(self):
        print 'STAT PARSER - STARTING'

        # Register all the event types by identifer
        for event_class in event.registry:

            # Make sure the id is valid
            event_id = event_class.ID
            event_callback = event_class.CALLBACK
            assert len(event_id) == 2, 'Invalid event ID: %s' % event_id
            assert len(event_callback) > 0, 'Invalid event callback: %s' % event_callback

            # Make sure the id is not already registered
            assert not hasattr(self.event_types, event_id), 'Duplicate event ID: %s' % event_id
            self.event_types[event_id] = event_class
        print 'Event types registered: ', len(self.event_types)

        print 'STAT PARSER - STARTED'

    # This method will be called to shutdown the parser
    def stop(self):
        print 'STAT PARSER - STOPPING'

        print 'STAT PARSER - STOPPED'

    def parse(self, line):
        '''
        Takes in a log entry line and parses it into an event data structure more convenient to use.

        Args:
           line (string): Raw log entry from Battle Field 2 mod.

        Returns:
            Event (BaseEvent): Returns an event data structure dependent on the log entry type.
        '''
        if not line: return

        # Break the line into individual elements
        elements = line.split(';')
        assert len(elements) > 1, 'Invalid log line %s' % line

        # Extract the log time and type
        timestamp = int(elements[0])
        log_type = str(elements[1])
        values = elements[2:]

        # Attempt to parse the log entry based on type
        try:
            event_type = self.event_types[log_type]
            event = event_type(values)
            event.time = timestamp
            return event
        except KeyError:
            print 'Unknown log entry type: ', log_type

stat_parser = StatParser()
