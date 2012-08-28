from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the player with the most weapon changes.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Weapon Tester', 'Most Weapon Changes',
                [PLAYER_COL, Column('Weapon Changes', Column.NUMBER, Column.DESC)])

    def on_weapon(self, e):
        self.results[e.player] += 1
