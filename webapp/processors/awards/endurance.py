from processors.awards import AwardProcessor,Column
from timer import Timer
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the amount of time a player is playing.
    
    Implementation
    This implementation uses the timer object to automatically compute elapsed
    time based on game ticks as events are processed.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Commander In Chief',
                'Most Time As Commander', [
                Column('Players'), Column('Time', Column.TIME, Column.DESC)])

    def on_spawn(self, e):

        player_stats = stat_mgr.get_player_stats(e.player)
        self.results[e.player] = player_stats.play_time
