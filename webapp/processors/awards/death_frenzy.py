
from processors.awards import AwardProcessor,Column
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor is awarded to the player with the most deaths in a row
    without a kill.

    Implementation
    Just use the maximum death streak that is included in the core player stats.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Death Frenzy', 'Max Death Streak', [
                Column('Players'), Column('Deaths', Column.NUMBER, Column.DESC)])

    def on_death(self, e):

        # Get the current maximum death streak from the core stats
        player_stats = stat_mgr.get_player_stats(e.player)
        self.results[e.player] = player_stats.deaths_streak_max
