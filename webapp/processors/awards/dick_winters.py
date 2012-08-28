
from processors.awards import AwardProcessor,Column,PLAYER_COL
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
                'Most Subordinate Kills as Squad Leader',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore team kills and suicides
        if not e.valid_kill:
            return

        # Get the leader for the attacker's squad
        squad = model_mgr.get_squad(e.attacker.squad_id)
        leader = model_mgr.get_player(squad.leader_id)

        # Give a point to the squad leader
        self.results[leader] += 1
