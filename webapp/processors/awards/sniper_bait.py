
from processors.awards import AwardProcessor,Column
from models import model_mgr
from models.vehicles import STATION

class Processor(AwardProcessor):
    '''
    Overview
        This processor keeps track of the most deaths while using turrets.

    Implementation
        Cache kill events if victim is in a turret

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Sniper Bait',
                'Most Deaths While Using Turrets',
                [Column('Players'), Column('Deaths', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        victim_vehicle = model_mgr.get_vehicle(e.victim.vehicle_id)
        if victim_vehicle.group == STATION:
            self.results[e.victim] += 1
