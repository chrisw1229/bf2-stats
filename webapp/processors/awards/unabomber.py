from processors.awards import AwardProcessor,Column
from models.weapons import EXPLOSIVE

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the player with the most explosive weapons.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Unabomber', 'Most Explosive Kills', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):
        #Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.weapon.ammo == EXPLOSIVE:
            self.results[e.attacker] += 1
