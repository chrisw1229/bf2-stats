from processors.awards import AwardProcessor,Column,PLAYER_COL
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
                [PLAYER_COL, Column('Time', Column.TIME, Column.DESC)])

        # Setup the results to store timers instead of numbers
        self.results = dict()

    def on_death(self, e):
        if e.player in self.results:
            self.results[e.player].stop(e.tick)

    def on_commander(self, e):
        self._update_timer(e.player, e.tick)
        self._update_timer(e.old_player, e.tick)

    def on_spawn(self, e):
        self._update_timer(e.player, e.tick)

    def on_squad(self, e):
        self._update_timer(e.player, e.tick)

    def on_squad_leader(self, e):
        self._update_timer(e.player, e.tick)
        self._update_timer(e.old_player, e.tick)

    def _update_timer(self, player, tick):
        if not player.leader and not player.squader:
            if not player in self.results:
                self.results[player] = Timer(player)
            self.results[player].start(tick)
        else:
            if player in self.results:
                self.results[player].stop(tick)
