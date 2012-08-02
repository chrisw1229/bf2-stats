
from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most team kills.

    Implementation
	Cache kill events that are team kills.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Traitor', 'Most Team Kills', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])
		
    def on_kill(self, e):

        if e.team_kill:
            self.results[e.attacker] += 1
