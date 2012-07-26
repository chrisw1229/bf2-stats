from processors.awards import AwardProcessor,Column
from models.vehicles import AIR

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to players in order that they take to the air.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Wright Brothers', 'Order players take to the air.', [
                Column('Players'), Column('Air Vehicle Order', Column.NUMBER, Column.DESC)])

        self.flight_order = 1

    def on_vehicle_enter(self, e):
        if e.vehicle.group == AIR and not e.player in self.results.keys():
            self.results[e.player] = self.flight_order
            self.flight_order += 1
