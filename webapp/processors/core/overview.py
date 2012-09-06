
from models import model_mgr
from processors import BaseProcessor
from stats import stat_mgr

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 20

    def on_connect(self, e):
        players = model_mgr.get_players(True)

        overall_stats = stat_mgr.get_stats()
        overall_stats.players = max(overall_stats.players, len(players))

    def on_death(self, e):
        overall_stats = stat_mgr.get_stats()
        overall_stats.deaths += 1

    def on_event(self, e):
        overall_stats = stat_mgr.get_stats()
        overall_stats.lines += 1
        
    def on_kill(self, e):
        overall_stats = stat_mgr.get_stats()
        overall_stats.kills += 1

    def on_score(self, e):
        overall_stats = stat_mgr.get_stats()
        overall_stats.score += e.value
