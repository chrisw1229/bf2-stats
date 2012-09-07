from processors.awards import AwardProcessor,Column,PLAYER_COL
from events import event_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the player with the most kills in the last second of a map.

    Implementation
    On game end, get all the events for the last second and cache each kill event in the list.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Buzzer Beater',
                'Most Last Second Kills',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_game_status(self, e):
        if not e.game.ending:
            return
        
        recent = event_mgr.get_history().new_events
        for event in recent:
            if event.TYPE == 'KL':
                if event.valid_kill:
                    self.results[event.attacker] += 1
