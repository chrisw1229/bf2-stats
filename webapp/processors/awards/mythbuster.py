from processors.awards import AwardProcessor,Column,PLAYER_COL
from models.weapons import CARBINE

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the player with the most kills using c4 (spec ops).
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'MythBuster', 'Most Kills with C4',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):
        #Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.weapon.id == 'c4_explosives':
            self.results[e.attacker] += 1
