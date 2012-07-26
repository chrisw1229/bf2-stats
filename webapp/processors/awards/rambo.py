
from processors.awards import AwardProcessor,Column
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor is awarded to the player with the most kills in a single life.

    Implementation
    The basic idea is to keep track of the current kill streak and check whether
    it is a new personal best for the player.

    Notes
    Just use the maximum death streak that is included in the core player stats.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Rambo', 'Most Kills in a Single Life', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Get the current maximum kill streak from the core stats
        player_stats = stat_mgr.get_player_stats(e.attacker)
        self.results[e.attacker] = player_stats.kills_streak_max
