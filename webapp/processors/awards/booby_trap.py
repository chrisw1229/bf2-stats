
import collections
from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of kills from claymores.

    Implementation
    Increment count if weapon is claymore

    Notes
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Booby Trap', 'Most Kills with Claymores',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])
        
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return
            
        if e.weapon.id == 'usmin_claymore':
            self.results[e.attacker] += 1
