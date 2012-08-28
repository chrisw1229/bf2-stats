from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This processor is awarded to the player with the most assisted kills.

    Implementation Details
    Based upon print statements and execution trace, assist events always occur directly
    after kill events.  Hang onto a kill event on_kill then if an assist is processed,
    increment the result and null out the current kill event in case of multiple assists.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Welfare', 'Most Assisted Kills',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

        self.last_kill = None

    def on_kill(self, e):
        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        self.last_kill = e

    def on_assist(self, e):
        if self.last_kill != None:
            self.results[self.last_kill.attacker] += 1
            self.last_kill = None
