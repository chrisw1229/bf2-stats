
# import collections
# from processors.awards import AwardProcessor,Column

# TODO

# class Processor(AwardProcessor):
    # '''
    # Overview
    # This processor keeps track of kills against specific players.

    # Implementation
    # Create a hashmap of players with victims as the keys and kills by the attacker
    # as the value. Increment the kill count against the victim.

    # Notes
    # None.
    # '''

    # def __init__(self):
        # AwardProcessor.__init__(self, 'Predator', 'Most Kills Against A Single Player', [
                # Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])
        
        # self.predator = dict()
        # self.prey = dict()
        
    # def on_kill(self, e):

        # # Ignore suicides and team kills
        # if not e.valid_kill:
            # return
            
        # # Update the hash map of events with the current attacker event
        # if e.attacker not in self.predator:
            # self.predator[e.attacker] = []
        # if e.victim not in self.prey:
            # self.predator[e.attacker].append(prey[e.victim] += 1
            
        # # Check the hash map for if the attacker's victim has killed a teammate recently
        # if e.victim in self.prey:
            # for teammate_event in self.prey[e.victim]:
                # time_diff = e.elapsed(teammate_event)
                # if time_diff <= 10:
                    # self.results[e.attacker] += 1
