
import collections

from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import model_mgr

class AwardResult(object):

    def __init__(self, kills, team):
        self.kills = kills
        self.team = team

    def __repr__(self):
        return [self.kills, self.team.name]

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
                [PLAYER_COL, Column('Kills', Column.ARRAY, Column.DESC)])

        self.results = dict()
        self.teams = dict()

    def on_kill(self, e):

        # Ignore team kills and suicides
        if not e.valid_kill:
            return

        team = model_mgr.get_team(e.victim.team_id)

        if e.attacker not in self.teams:
            self.teams[e.attacker] = collections.Counter()
        counter = self.teams[e.attacker]
        counter[team] += 1

        if not e.attacker in self.results:
            self.results[e.attacker] = AwardResult(0, team)
        result = self.results[e.attacker]

        if counter[team] > result.kills:
            result.kills = counter[team]
