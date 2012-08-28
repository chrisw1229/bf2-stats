
from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the number of players that assisted in killing a player.

    Implementation
    This implementation takes advantage of the fact that every kill event is guaranteed to be
    immediately followed by its associatd assists. Whenever a kill event is received, the kill event
    is cached. When a subsequent assist occurs, then the victim of the event gets an award point for
    the assist.

    Notes
    Make sure the assist count is reset for each kill and that the award points are given based on
    the current sequence of assists, rather than being accumulated for the entire session. Do not
    count suicides or team kills.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Bullet Magnet',
                'Most Players Assisting Your Death',
                [PLAYER_COL, Column('Assists', Column.NUMBER, Column.DESC)])

        # Keep track of the last kill event
        self.last_kill = None

        # Count the number of assists for each kill
        self.assist_count = 0

    def on_assist(self, e):
        if self.last_kill:

            # Increment the assist count
            self.assist_count += 1

            # Update the award points for the original victim
            self.results[self.last_kill.victim] = self.assist_count

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            self.last_kill = None
            return

        # Reset the assist count
        self.assist_count = 0

        # Store the last kill event so we can adjust based on subsequent assists
        self.last_kill = e
