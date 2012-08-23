
from processors.awards import AwardProcessor,Column

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
        AwardProcessor.__init__(self, 'Rasputin', 'Most Weapon Type Deaths', [
                Column('Players'), Column('Types', Column.NUMBER, Column.DESC)])

        self.types = dict()
        
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        if not e.victim in self.types:
            self.types[e.victim] = set()

        self.types[e.victim].add( e.weapon )

        self.results[e.victim] = len( self.types[e.victim] )
