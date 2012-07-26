from processors.awards import AwardProcessor,Column
from models.vehicles import AIR
from timer import Timer

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the player who enters an air vehicle the fastest from spawn.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Wright Brothers', 'Fastest to an Air Vehicle', [
                Column('Players'), Column('Time to Air Vehicle (sec.)', Column.NUMBER, Column.ASC)])

        self.spawn_times = dict()

    def on_spawn(self, e):
        self.spawn_times[e.player] = e.tick

    def on_vehicle_enter(self, e):
        if e.vehicle.group == AIR:
            enter_time = e.tick - self.spawn_times[e.player]
            air_timer = Timer()
            air_timer.elapsed = enter_time

            if self.results[e.player] != 0:
                if air_timer.elapsed < self.results[e.player].elapsed:
                    self.results[e.player] = air_timer
            else:
                self.results[e.player] = air_timer
