
from processors.awards import AwardProcessor,Column,PLAYER_COL

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
        AwardProcessor.__init__(self, 'Traitor', 'Most Team Kills',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])
		
    def on_kill(self, e):

        if e.team_kill:
            self.results[e.attacker] += 1
