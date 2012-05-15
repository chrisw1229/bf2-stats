from processor import BaseProcessor

class Processor(BaseProcessor):

    def start(self):
        print 'AWARD START'

    def stop(self):
        print 'AWARD STOP'

    def on_kill(self, e):
        #print 'AWARD KILL: ', e
        pass
