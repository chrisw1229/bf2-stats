
from processor import BaseProcessor
from stats import stats_mgr

class Processor(BaseProcessor):

    def on_kill(self, e):
        victim_stats = stats_mgr.get_player_stats(e.victim)
        victim_stats.deaths += 1

        attacker_stats = stats_mgr.get_player_stats(e.attacker)
        attacker_stats.kills += 1
