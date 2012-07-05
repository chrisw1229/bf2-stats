
from processors.awards import AwardProcessor,Column
from stats import stat_mgr

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
        AwardProcessor.__init__(self, 'High Ground', 'Max Kill Height Difference', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])
		
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Check whether the kill height was more than one story
        if stat_mgr.dist_alt(e.victim.pos, e.attacker.pos) > 3:
			self.results[e.attacker] += 1
