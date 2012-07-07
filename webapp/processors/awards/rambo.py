from processors.awards import AwardProcessor,Column
from collections import Counter

class Processor(AwardProcessor):
    '''
    Overview
    This processor is awarded to the player with the most kills in a single life.

    Implementation
    The basic idea is to keep track of the current kill streak and check whether
    it is a new personal best for the player.

    Notes
    The current kill streak must be reset using the death callback, rather than
    the kill callback so that the streak continues when the player is revived.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Rambo', 'Most Kills in a Single Life', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

        # Keep track of the current kill streak
        self.current = Counter()

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Increment the current kill streak
        self.current[e.attacker] += 1

        # Update the personal best kill streak for the attacker
        self.results[e.player] = max(self.results[e.attacker], self.current[e.attacker])

    def on_death(self, e):

        # Reset the kill sterak when the player dies
        self.current[e.player] = 0
