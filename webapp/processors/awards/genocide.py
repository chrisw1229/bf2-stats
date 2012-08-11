
import collections
from processors.awards import AwardProcessor,Column
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
                'Most Kills Against a Single Team', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

        self.teams = dict()
        
    def on_kill(self, e):

        # Ignore team kills and suicides
        if not e.valid_kill:
            return

        team = model_mgr.get_team(e.victim.team_id)
        if e.attacker not in self.teams:
            self.teams[e.attacker] = collections.Counter()

        (self.teams[e.attacker])[team] += 1
        if (self.teams[e.attacker])[team] > self.results[e.attacker]:
            self.results[e.attacker] = (self.teams[e.attacker])[team]

