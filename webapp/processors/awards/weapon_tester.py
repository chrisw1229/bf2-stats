from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the player with the most weapon changes other than
    the one they spawn with.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Weapon Tester', 'Most Weapon Changes',
                [PLAYER_COL, Column('Weapon Changes', Column.NUMBER, Column.DESC)])

        self.pickups = dict()

    def on_weapon(self, e):
        if not e.player in self.pickups:
            return

        if self.pickups[e.player]:
            self.results[e.player] += 1
        else:
            self.pickups[e.player] = True

    def on_spawn(self, e):
        self.pickups[e.player] = False
