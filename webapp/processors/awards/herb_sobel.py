
from processors.awards import AwardProcessor,Column,PLAYER_COL
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
                'Most Subordinate Deaths as Squad Leader',
                [PLAYER_COL, Column('Deaths', Column.NUMBER, Column.DESC)])

    def on_death(self, e):

        # Get the leader for the player's squad
        squad = model_mgr.get_squad(e.player.squad_id)
        leader = model_mgr.get_player(squad.leader_id)

        # Give a point to the squad leader
        self.results[leader] += 1
