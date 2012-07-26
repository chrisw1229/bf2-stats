from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most typed messages

    Implementation
	Whenever a chat event is received the text is cached if it's over
	one character and not spamming

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Chatty Cathy', 'Most Typed Messages', [
                Column('Players'), Column('Text', Column.NUMBER, Column.DESC)])

	self.previous = ""
	
    def on_chat(self, e):
        if "server" in e.channel:
            return
        if len(e.text) < 2 or e.text == self.previous:
            return

        self.previous = e.text
        self.results[e.player] += len(e.text)
                        
