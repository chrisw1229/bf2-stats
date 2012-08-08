
from processors.awards import AwardProcessor,Column
from models import players
from models import model_mgr
from models import games

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of wins while commander

    Implementation
    Increment the count for the commander for each win

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'George Patton',
                'Most Wins as Commander', [
                Column('Players'), Column('Wins', Column.NUMBER, Column.DESC)])

    def on_win(self, e):

        # Get the commander of the team that won
        commander = model_mgr.get_player(e.team.commander_id)

        # Give a point to the commander
        self.results[commander] += 1
