
from events import FlagActionEvent
from processors.awards import AwardProcessor,Column,PLAYER_COL
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor is awarded to the player with the most flag captures.

    Implementation
    Count the flag action events of the appropriate type.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Conqueror', 'Most Flag Captures',
                [PLAYER_COL, Column('Captures', Column.NUMBER, Column.DESC)])

    def on_flag_action(self, e):
        if e.action_type == FlagActionEvent.CAPTURE:
            self.results[e.player] += 1
