
from processors.awards import AwardProcessor,Column
from models import model_mgr
from models.vehicles import ARMOR

class Processor(AwardProcessor):
    '''
    Overview
        This processor keeps track of the most deaths from tanks.

    Implementation
        Cache kill events if attacker is in tank

    Notes
    Change to only count deaths while not in a vehicle?
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Tiananmen Square',
                'Most Deaths from Tanks',
                [Column('Players'), Column('Deaths', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        attack_vehicle = model_mgr.get_vehicle(e.attacker.vehicle_id)
        if attack_vehicle.vehicle_type == ARMOR:
            self.results[e.victim] += 1
