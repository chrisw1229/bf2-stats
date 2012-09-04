
from models import model_mgr
from processors.awards import AwardProcessor,Column,PLAYER_COL
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor is awarded to the player with the most losses.

    Implementation
    Use the losses value from core player stats when a loss event occurs.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Dead Weight', 'Most Losses',
                [PLAYER_COL, Column('Losses', Column.NUMBER, Column.DESC)])

    def on_loss(self, e):

        # Update the loss count for all the active players on the team
        for player in model_mgr.get_players(True):
            if player.team_id == e.team.id:
                player_stats = stat_mgr.get_player_stats(player)
                self.results[player] = player_stats.losses
