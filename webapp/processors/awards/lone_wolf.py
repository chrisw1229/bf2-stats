from processors.awards import AwardProcessor,Column
from timer import Timer
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the amount of time a player is playing without a squad.
    
    Implementation
    This implementation uses the timer object to automatically compute elapsed
    time based on game ticks as events are processed.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Lone Wolf', 'Most Time Without a Squad',
                [Column('Players'), Column('Time', Column.TIME, Column.DESC)])
        
        self.squadTime = dict()

    def on_spawn(self, e):

        player_stats = stat_mgr.get_player_stats(e.player)
        if not player_stats.play_time:
            return
        
        if e.player in self.squadTime:
            self.results[e.player] = player_stats.play_time.elapsed - self.squadTime[e.player].elapsed
        else: #require a minimum amount of squad time?
            self.results[e.player] = player_stats.play_time

    def on_squad(self, e):

        if e.player not in self.squadTime:
            self.squadTime[e.player] = Timer(e.player)

        if not e.squad:
            self.squadTime[e.player].stop(e.tick)
        else:
            self.squadTime[e.player].start(e.tick)
