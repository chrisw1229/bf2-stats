from processor import BaseProcessor

class Processor(BaseProcessor):

    def start(self):
        print 'START'

    def stop(self):
        print 'STOP'

    def onPlayerKilled(self, kill_log):
        print 'AWARD'
