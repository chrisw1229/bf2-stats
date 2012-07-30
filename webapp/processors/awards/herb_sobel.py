
from processors.awards import AwardProcessor,Column
from models import squads
from models import players
from models import model_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of deaths while squad leader

    Implementation
    Increment the death count for the squad leader for each death

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Herb Sobel',
                'Most Soldier Deaths as Squad Leader', [
                Column('Players'), Column('Deaths', Column.TIME, Column.DESC)])


    def on_death(self, e):

        squad = model_mgr.get_squad(e.player.squad_id)
        if squad == None or squad == squads.EMPTY:
            return

        leader = model_mgr.get_player( squad.leader_id )
        if leader == None or leader == players.EMPTY:
            return

        self.results[leader] += 1

