from processors.awards import AwardProcessor,Column
import os.path

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most drinks as reported via chat.

    Implementation
	Whenever a chat event is received the text is compared to a config file
	for keywords (chuck, beer, etc)

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Iron Liver', 'Most Drinks', [
                Column('Players'), Column('Drinks', Column.NUMBER, Column.DESC)])

        self.phrases = list()
	# Get the path to the configuration file
        confPath = os.path.join(os.path.dirname(__file__), 'drinks.conf')
        f = open( confPath, 'r' )
        for line in f:
            self.phrases.append(line)
            
    def on_chat(self, e):

        if e.text in self.phrases:
            self.results[e.player] += 1
