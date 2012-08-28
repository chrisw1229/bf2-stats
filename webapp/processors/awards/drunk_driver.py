from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the player with the most deaths by mines while driving.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Drunk Driver',
                'Most Deaths from Mines while Driving a Vehicle',
                [PLAYER_COL, Column('Deaths', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):
        if e.victim.driver:
            if e.weapon.id == 'at_mine' or e.weapon.id == 'usmin_claymore':
                self.results[e.victim] += 1
