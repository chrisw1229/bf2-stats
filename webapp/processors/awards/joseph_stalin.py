
from processors.awards import AwardProcessor,Column
from models import teams
from models import players
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
                'Most Soldier Deaths as Commander', [
                Column('Players'), Column('Deaths', Column.TIME, Column.DESC)])


    def on_death(self, e):

        team = model_mgr.get_team(e.player.team_id)
        if team == None or team == teams.EMPTY:
            return

        commander = model_mgr.get_player( team.commander_id )
        if commander == None or commander == players.EMPTY:
            return

        self.results[commander] += 1
