
from processors.awards import AwardProcessor,Column
from models import model_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of deaths while commander

    Implementation
    Increment the death count for the commander for each death

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Joseph Stalin',
                'Most Subordinate Deaths as Commander', [
                Column('Players'), Column('Deaths', Column.NUMBER, Column.DESC)])


    def on_death(self, e):

        # Get the commander for the player's team
        team = model_mgr.get_team(e.player.team_id)
        commander = model_mgr.get_player(team.commander_id)

        # Give a point to the commander
        self.results[commander] += 1
