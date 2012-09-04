
from models import model_mgr
from processors.awards import AwardProcessor,Column,PLAYER_COL
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor is awarded to the player with the most wins.

    Implementation
    Use the wins value from core player stats when a win event occurs.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Champion', 'Most Wins',
                [PLAYER_COL, Column('Wins', Column.NUMBER, Column.DESC)])

    def on_win(self, e):

        # Update the win count for all the active players on the team
        for player in model_mgr.get_players(True):
            if player.team_id == e.team.id:
                player_stats = stat_mgr.get_player_stats(player)
                self.results[player] = player_stats.wins
