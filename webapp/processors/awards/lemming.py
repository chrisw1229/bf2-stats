from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Lemming is awarded to the player with the most suicides.

    This stat can be tracked using any weapon on any map.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Lemming', 'Suicides', [
                Column('Players'), Column('Suicides', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):
        if e.attacker == e.victim:
            self.results[e.attacker] += 1
