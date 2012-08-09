
import collections
from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of kills against specific players.

    Implementation
    Count the number of kills each player has against every other player using
    a dictionary of counters. Whenever a kill happens, check whether the total
    kills against that particular victim is the new maximum out of all the
    attacker's victims.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Predator',
                'Most Kills Against a Single Player', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])
        
        self.attacker_to_victims = dict()
        
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Make sure the attacker is registered
        if not e.attacker in self.attacker_to_victims:
            self.attacker_to_victims[e.attacker] = collections.Counter()

        # Increment the kill for the attacker against the victim
        victims = self.attacker_to_victims[e.attacker]
        victims[e.victim] += 1

        # Check whether total kills for the victim is the new maximum
        for victim in victims:
            if victims[victim] > self.results[e.attacker]:
                self.results[e.attacker] = victims[victim]
