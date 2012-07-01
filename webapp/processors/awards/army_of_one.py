
from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of kills for each player that do not include any
    assisting help from other players.

    Implementation
    This implementation takes advantage of the fact that every kill event is guaranteed to be
    immediately followed by its associatd assists. Whenever a kill event is received, the attacker
    gets an award point and the kill event is cached. If there are no subsequent assists, then the
    point stands as is. If there is at least one assist event received, then we remove the most
    recently awarded point.

    Notes
    Make sure a point is only subtracted once, since a kill could have multiple assists. Do not
    count suicides or team kills.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Army of One', 'Most Kills Without Assists', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

        # Keep track of the last kill event
        self.last_kill = None

    def on_assist(self, e):

        # Only adjust award points for the first associated assist
        if self.last_kill:

            # Subtract the last awarded point
            self.results[self.last_kill.attacker] -= 1
            self.last_kill = None

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            self.last_kill = None
            return

        # Give the attacker an award point for now
        self.results[e.attacker] += 1

        # Store the last kill event so we can adjust based on subsequent assists
        self.last_kill = e
