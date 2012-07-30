
from processors.awards import AwardProcessor,Column
from models import squads
from models import players
from models import model_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of kills while squad leader

    Implementation
    Increment the kill count for the squad leader for each kill

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Dick Winters',
                'Most Soldier Kills as Squad Leader', [
                Column('Players'), Column('Kills', Column.TIME, Column.DESC)])


    def on_kill(self, e):

        if not e.valid_kill:
            return
        
        squad = model_mgr.get_squad(e.attacker.squad_id)
        if squad == None or squad == squads.EMPTY:
            return

        leader = model_mgr.get_player( squad.leader_id )
        if leader == None or leader == players.EMPTY:
            return

        self.results[leader] += 1

