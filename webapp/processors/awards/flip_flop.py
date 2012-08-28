from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number team changes

    Implementation
	Whenever a team event is received the change is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Flip Flop', 'Most Team Changes',
                [PLAYER_COL, Column('Teams', Column.NUMBER, Column.DESC)])
		
    def on_team(self, e):
        self.results[e.player] += 1
                        
