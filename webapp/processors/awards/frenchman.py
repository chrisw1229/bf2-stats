
from processors.awards import AwardProcessor,Column
from models import players
from models import model_mgr
from models import games

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of losses while commander

    Implementation
    Increment the count for the commander for each loss

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Frenchman',
                'Most Losses as Commander', [
                Column('Players'), Column('Losses', Column.NUMBER, Column.DESC)])

    def on_loss(self, e):

        # Get the commander of the team that lost
        commander = model_mgr.get_player(e.team.commander_id)

        # Give a point to the commander
        self.results[commander] += 1
