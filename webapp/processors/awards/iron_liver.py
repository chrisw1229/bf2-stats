from processors.awards import AwardProcessor,Column
import os.path

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most drinks as reported via chat.

    Implementation
	Whenever a chat event is received the text is compared to a list of keywords
    (chuck, beer, etc)

    Notes
	Make sure all the string comparisons are case-insensitive.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Iron Liver', 'Most Drinks', [
                Column('Players'), Column('Drinks', Column.NUMBER, Column.DESC)])

        # Create a list of acceptable drinking phases
        self.phrases = list(['beer', 'chuck', 'need one'])

    def on_chat(self, e):
        if e.text.lower() in self.phrases:
            self.results[e.player] += 1
