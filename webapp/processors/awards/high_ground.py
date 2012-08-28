
from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number of kills where the difference
    in height or altitude between the attacker and victim is more than a story.

    Implementation
	Whenever a kill event is received calculate the altitude difference between
    the two players involved. One story will be represented by 10 feet, which
    is actually 3 meters in game units.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'High Ground',
                'Most Kills from Above',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Check whether the attacker was at least a story higher than the victim
        if (e.attacker.pos[1] - e.victim.pos[1]) > 3:
            self.results[e.attacker] += 1
