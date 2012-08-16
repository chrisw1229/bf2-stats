
from processors.awards import AwardProcessor,Column
from models.weapons import ASSAULT, CARBINE, PISTOL, SNIPER
from timer import Timer

class Processor(AwardProcessor):
    '''
    Overview
    This processor tracks the minimum time between kills.
    
    Implementation
    This implementation uses the timer object to automatically compute elapsed
    time based on game ticks as events are processed.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Quick Draw',
                'Shortest Time Between Kills', [
                Column('Players'), Column('Time', Column.TIME, Column.ASC)])

        # Setup the results to store timers instead of numbers
        self.results = dict()

        # Store the last kill events for each player
        self.last_kills = dict()

    def on_kill(self, e):

        # Ignore team kills and suicides
        if not e.valid_kill:
            return

        # Only count non-automatic weapons
        weapon_type = e.weapon.weapon_type
        if (weapon_type != ASSAULT and weapon_type != CARBINE
                and weapon_type != PISTOL and weapon_type != SNIPER):
            return

        # Store the first kill that happens
        if not e.attacker in self.last_kills:
            self.last_kills[e.attacker] = e
            return

        # Check whether the next consecutive kill is the quickest
        elapsed = e.elapsed(self.last_kills[e.attacker])
        if not e.attacker in self.results:
            self.results[e.attacker] = Timer(e.attacker)
            self.results[e.attacker].elapsed = elapsed
        elif elapsed < self.results[e.attacker].elapsed:
            self.results[e.attacker].elapsed = elapsed
        self.last_kills[e.attacker] = e

    def on_spawn(self, e):

        # Reset the last kill when the player respawns
        if e.player in self.last_kills:
            del self.last_kills[e.player]
