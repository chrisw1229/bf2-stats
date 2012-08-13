
from processors.awards import AwardProcessor,Column
from models.weapons import EXPLOSIVE
from events import event_mgr
from models.players import EMPTY

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most kills while committing suicide.

    Implementation
    On suicide, track the suicide time and add kills from explosives that occurred at the
    same time.  Also go through the history for the suiciding player and add any explosive
    kills in his recent history

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Kamikaze', 'Most Kills While Committing Suicide', [
                Column('Players'), Column('Kills', Column.NUMBER, Column.DESC)])

        self.suicideTime = dict()
        
    def on_kill(self, e):

        if e.suicide:
            self.suicideTime[e.attacker] = e.tick
            recent = event_mgr.get_history(e.attacker).new_events
            for event in recent:
                if event.TYPE == 'KL':
                    if event.valid_kill and event.weapon.ammo == EXPLOSIVE:
                        self.results[e.attacker] += 1

        if not e.valid_kill:
            return

        if e.weapon.ammo != EXPLOSIVE:
            return

        if e.attacker == EMPTY:
            return

        if e.attacker in self.suicideTime and e.tick == self.suicideTime[e.attacker]:
            self.results[e.attacker] += 1
