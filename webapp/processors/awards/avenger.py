
import collections
from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of kills against players who have killed your
    teammates within the previous 10 seconds.

    Implementation
    Create a hashmap of players with killers as the keys and victims as the values (array)
    When an attacker dies their keys are nulled to prevent ballooning.
    When a kill takes place check the hashmap to determine if that player has killed
    someone who has killed a teammate within the last 10 seconds (ticks). If they have
    then increment their score by the number of teammates the victim has killed in the
    last 10 seconds (ticks). It's easy baby!

    Notes
    Currently all weapons and maps are considered for both the attacker of your teammates
    and the avenger.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Avenger', 'Most Kills Against Players that killed a Teammate', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])
        
        self.last_kill = dict()
        
    def on_death(self, e):
        if e.player in self.last_kill:
            del self.last_kill[e.player]
        
    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return
            
        # Update the hash map of events with the current attacker event
        if e.attacker not in self.last_kill:
            self.last_kill[e.attacker] = []
        self.last_kill[e.attacker].append(e)
            
        # Check the hash map for if the attacker's victim has killed a teammate recently
        if e.victim in self.last_kill:
            for teammate_event in self.last_kill[e.victim]:
                time_diff = e.elapsed(teammate_event)
                if time_diff <= 10:
                    self.results[e.attacker] += 1
