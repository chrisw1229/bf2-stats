from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Vengeance is awarded to the player who has the most kills vs. the player who has most recently killed
    them.

    The player who has most recently killed another player is only changed upon a valid kill.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Vengeance',
                'Most Kills Against Your Last Attacker', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

        self.last_killer = dict()

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        self.last_killer[e.victim] = e.attacker

        if e.attacker in self.last_killer and e.victim == self.last_killer[e.attacker]:
            self.results[e.attacker] += 1

