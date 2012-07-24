from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the player with the most weapon changes.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Weapon Tester', 'Most Weapon Changes', [
                Column('Players'), Column('Weapon Changes', Column.NUMBER, Column.ASC)])

    def on_weapon(self, e):
        self.results[e.player] += 1
