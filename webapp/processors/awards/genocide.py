
import collections

from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import model_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of kills against each team

    Implementation
    Track the kills against each team and use the maximum value as the result

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Genocide',
                'Most Kills Against a Single Team',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

        self.teams = dict()
        
    def on_kill(self, e):

        # Ignore team kills and suicides
        if not e.valid_kill:
            return

        if e.attacker not in self.teams:
            self.teams[e.attacker] = collections.Counter()
        counter = self.teams[e.attacker]

        team = model_mgr.get_team(e.victim.team_id)
        counter[team] += 1
        if counter[team] > self.results[e.attacker]:
            self.results[e.attacker] = counter[team]
