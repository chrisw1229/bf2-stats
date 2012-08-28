from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most assists.

    Implementation
	Cache all assist events

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'John Stockton', 'Most Assists',
                [PLAYER_COL, Column('Assists', Column.NUMBER, Column.DESC)])
            
    def on_assist(self, e):

        self.results[e.player] += 1
