
from processors.awards import AwardProcessor,Column,PLAYER_COL
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the player with the most kit pickups other than the
    one they spawn with.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Scavenger', 'Most Kit Pickups',
                [PLAYER_COL, Column('Pickups', Column.NUMBER, Column.DESC)])

        self.pickups = dict()

    def on_kit_pickup(self, e):
        if not e.player in self.pickups:
            return

        if self.pickups[e.player]:
            self.results[e.player] += 1
        else:
            self.pickups[e.player] = True

    def on_spawn(self, e):
        self.pickups[e.player] = False
