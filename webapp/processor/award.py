from processor import BaseProcessor

class Processor(BaseProcessor):

    def start(self):
        print 'AWARD START'

    def stop(self):
        print 'AWARD STOP'

    def on_kill(self, event):
        #print 'AWARD KILL: ', event
        pass
