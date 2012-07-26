from processors.awards import AwardProcessor,Column
from models.weapons import MINE

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the player with the most deaths by mines.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Watch Your Step', 'Most Deaths by Mines', [
                Column('Players'), Column('Deaths', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):
        if e.weapon.weapon_type == MINE:
            self.results[e.victim] += 1
