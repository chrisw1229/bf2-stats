from processors.awards import AwardProcessor,Column
from models.weapons import MINE

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the player with the most deaths by mines while driving.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Drunk Driver', 'Most Deaths from Mines while Driving a Vehicle', [
                Column('Players'), Column('Deaths', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):
        if e.victim.driver and e.weapon.weapon_type == MINE:
            self.results[e.victim] += 1
