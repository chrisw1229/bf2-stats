import processor.award

class StatsManager(object):

    processors = []
    ticked = False
    prev_time = 0
    curr_time = 0
    prev_events = []
    curr_events = []
    last_events = {}

    # This method will be called to initialize the manager
    def start(self):
        print 'STATS MANAGER - STARTING'

        # Register all the processors
        # TODO Load these dynamically
        self.processors = [processor.award.Processor()]
        print 'Processors registered: ', len(self.processors)

        # Start all the log processors
        for proc in self.processors:
            proc.start()

        print 'STATS MANAGER - STARTED'

    # This method will be called to shutdown the manager
    def stop(self):
        print 'STATS MANAGER - STOPPING'

        # Stop all the log processors
        for proc in reversed(self.processors):
            proc.stop()

        print 'STATS MANAGER - STOPPED'

    def process_event(self, event):
        '''
        Takes in a log event and processes it into useful statistics.

        Args:
           event (BaseEvent): Object representation of a log entry.

        Returns:
            None
        '''
        if not event: return

        # Swap the event history when the time advances
        if event.time > self.curr_time:
            self.prev_time = self.curr_time
            self.prev_events = self.curr_events

            self.curr_time = event.time
            self.curr_events = []
            ticked = True
        else:
            ticked = False

        # Allow each processor to handle the event
        self._fire(event)

        # Store the current event for future use
        self.curr_events.append(event)
        self.last_events[event.ID] = event

    def _fire(self, event):
        '''
        Passes the given log event to all the registered processors.

        Args:
           event (BaseEvent): Object representation of a log entry.

        Returns:
            None
        '''
        if event and event.CALLBACK:
            for processor in self.processors:

                # Attempt to invoke the processor callback
                try:
                    callback = getattr(processor, event.CALLBACK)
                    callback(event)

                    # Terminate the loop if the processor consumed the event
                    if event.consumed:
                        break
                except AttributeError:
                    print 'Missing callback for processor: %s[%s]' % (processor, event.callback)
        else:
            print 'Missing callback for event: ', event

# Create a shared singleton instance of the stats manager
stats_mgr = StatsManager()
