from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the person with the most kills by front projectile shots

    Implementation
	Whenever a kill or death event is received it's cached if the weapon is the proper type
    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Fireworks', 'Most Kills by Front Projectiles', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.ASC)])
		
    def on_kill(self, e):
        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.weapon.ammo == EXPLOSIVE:
            self.results[e.attacker] += 1
