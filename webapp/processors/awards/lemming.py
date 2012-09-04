from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Lemming is awarded to the player with the most suicides.

    This stat can be tracked using any weapon on any map.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Lemming', 'Most Suicides',
                [PLAYER_COL, Column('Suicides', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):
        if e.suicide:
            self.results[e.attacker] += 1
