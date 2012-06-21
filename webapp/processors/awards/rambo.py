from processors.awards import AwardProcessor,Column
from collections import Counter

class Processor(AwardProcessor):
    '''
    Rambo is awarded to the player with the most kills in a single life.
    '''
    def __init__(self):
        AwardProcessor.__init__(self, 'Rambo', 'Most Kills in a Single Life', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

        self.current = Counter()

    def on_kill(self, e):

        if not e.valid_kill:
            return

        self.current[e.attacker] += 1

    def on_death(self, e):

        self.results[e.player] = max(self.results[e.player], self.current[e.player])

        self.current[e.player] = 0
