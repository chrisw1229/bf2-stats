
from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most weapon type deaths

    Implementation
	Cache kill events involving a sniper.
    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Rasputin', 'Most Weapon Type Deaths',
                [PLAYER_COL, Column('Types', Column.NUMBER, Column.DESC)])

        self.types = dict()
        
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        if not e.victim in self.types:
            self.types[e.victim] = set()

        self.types[e.victim].add( e.weapon )

        self.results[e.victim] = len( self.types[e.victim] )
