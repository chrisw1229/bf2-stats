from processors.awards import AwardProcessor,Column,PLAYER_COL
from events import event_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the player with the most kills by c4 loaded jeeps.

    Implementation
    On vehicle destroy, track the time and add kills from c4 that occurred at the
    same time in subsequent kill events.  Also go through the history for the attacker
    and add any c4 kills in his recent history.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Jeep Jihad',
                'Most Kills by C4 Loaded Jeeps',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

        self.time = dict()

    def on_vehicle_destroy(self, e):

        if e.attacker == e.driver:
            self.time[e.attacker] = e.tick
            recent = event_mgr.get_history(e.attacker).new_events
            for event in recent:
                if event.TYPE == 'KL':
                    if event.valid_kill and event.weapon.id == 'c4_explosives':
                        self.results[e.attacker] += 1

    def on_kill(self, e):
        #Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.attacker in self.time and e.weapon.id == 'c4_explosives':
            if e.tick == self.time[e.attacker]:
                self.results[e.attacker] += 1
