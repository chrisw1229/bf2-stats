
from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of kills against commanders/squad leaders.

    Implementation
    Increment count +5 if victim is commander, +1 if squad leader

    Notes
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Assassin',
                'Most Kills Against Commanders and Squad Leaders',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Give a point when the victim is commander or leader
        if e.victim.commander or e.victim.leader:
            self.results[e.attacker] += 1
