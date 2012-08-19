from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the players with the most team damage received.

    Implementation
    Cache team damage events
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Scapegoat', 'Most Damage Received from Teammates', [
                Column('Players'), Column('Damage', Column.NUMBER, Column.DESC)])

    def on_team_damage(self, e): #add in team kills?
        self.results[e.victim] += 1
