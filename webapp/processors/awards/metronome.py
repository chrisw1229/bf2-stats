from processors.awards import AwardProcessor,Column,PLAYER_COL
from math import sqrt

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the standard deviation of time between kills
    and gives the award to the player with the lowest calculated value.

    This implies that player had the most consitent amount of time between kills.

    Implementation
    Uses a running sum and a running sum of squares to calculate the standard
    deviation.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Metronome',
                'Most Consistent Time Between Kills',
                [PLAYER_COL, Column('Seconds Deviation', Column.NUMBER, Column.ASC)])

        self.last_kill_time = dict()
        self.kills = dict()
        self.sum = dict()
        self.sum_squares = dict()

    def on_kill(self, e):

        #Ignore suicides and team kills
        if not e.valid_kill:
            return

        if not e.attacker in self.last_kill_time.keys():
            #Set initial values for calculating this award
            self.last_kill_time[e.attacker] = e.tick
            self.kills[e.attacker] = 1
            self.sum[e.attacker] = 0
            self.sum_squares[e.attacker] = 0
        else:
            time_since_last_kill = e.tick - self.last_kill_time[e.attacker]

            self.last_kill_time[e.attacker] = e.tick
            self.kills[e.attacker] += 1
            self.sum[e.attacker] += time_since_last_kill
            self.sum_squares[e.attacker] += time_since_last_kill * time_since_last_kill

            mean = self.sum[e.attacker] / self.kills[e.attacker]

            self.results[e.attacker] = round(sqrt((self.sum_squares[e.attacker] / self.kills[e.attacker]) - (mean * mean)))

