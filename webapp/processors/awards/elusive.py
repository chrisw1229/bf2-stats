from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the person with the least kills and deaths

    Implementation
	Whenever a kill or death event is received it's cached
    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Elusive', 'Fewest Kills and Deaths',
                [PLAYER_COL, Column('Kills/Deaths', Column.NUMBER, Column.ASC)])
		
    def on_kill(self, e):
        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        self.results[e.attacker] += 1
        self.results[e.victim] += 1
