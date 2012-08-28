from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most characters typed in chat channels.

    Implementation
	Whenever a chat event is received the text is cached if it's over
	one character and not spamming

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Chatty Cathy', 'Most Text Typed',
                [PLAYER_COL, Column('Text', Column.NUMBER, Column.DESC)])

	self.previous = ''
	
    def on_chat(self, e):
        if 'server' in e.channel:
            return
        if len(e.text) < 2 or e.text == self.previous:
            return

        self.previous = e.text
        self.results[e.player] += len(e.text)
