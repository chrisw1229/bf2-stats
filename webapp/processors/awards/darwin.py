
from processors.awards import AwardProcessor,Column
from models.players import EMPTY

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most deaths from crashing into buildings

    Implementation
	Whenever a kill event is received involving a helicopter/jet, the attacker
    is null, and the victim is above the ground the event is cached. The
    threshold after some play testing is 100ft. or about 30m.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Darwin', 'Most Deaths from Environment', [
                Column('Players'), Column('Deaths', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):
        # Check whether the victim died to nobody
        if e.attacker == EMPTY:
            self.results[e.victim] += 1
