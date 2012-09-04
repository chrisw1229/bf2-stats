
from processors.awards import AwardProcessor,Column,PLAYER_COL
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor is awarded to the player with the most kills in a row
    without a death.

    Implementation
    Just use the maximum kill streak that is included in the core player stats.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Kill Frenzy', 'Max Kill Streak',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Get the current maximum kill streak from the core stats
        attacker_stats = stat_mgr.get_player_stats(e.attacker)
        self.results[e.attacker] = attacker_stats.kills_streak_max
