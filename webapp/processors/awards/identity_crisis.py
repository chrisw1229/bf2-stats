
from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most name changes

    Implementation
    On spawn events check the size of the player's aliases list

    Notes
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Identity Crisis', 'Most Name Changes', [
                Column('Players'), Column('Names', Column.NUMBER, Column.DESC)])
		
    def on_spawn(self, e):

        self.results[e.player] = len(e.player.aliases)
