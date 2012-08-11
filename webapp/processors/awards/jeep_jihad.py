from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the player with the most kills by c4 loaded jeeps.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Jeep Jihad', 'Most Kills by C4 Loaded Jeeps', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

        self.exit_times = dict()

    def on_vehicle_exit(self, e):
        self.exit_times[e.player] = e.tick

    def on_kill(self, e):
        #Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.attacker in self.exit_times and e.weapon.id == 'c4_explosives':
            #need to experiment with the time limit, probably need to reduce this
            if e.tick - self.exit_times[e.attacker] <= 2:
                self.results[e.attacker] += 1
