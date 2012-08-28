
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import model_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of kills while commander

    Implementation
    Increment the kill count for the commander for each kill

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Genghis Khan',
                'Most Subordinate Kills as Commander',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore team kills and suicides
        if not e.valid_kill:
            return

        # Get the commander for the attacker's team
        team = model_mgr.get_team(e.attacker.team_id)
        commander = model_mgr.get_player(team.commander_id)

        # Give a point to the commander
        self.results[commander] += 1
