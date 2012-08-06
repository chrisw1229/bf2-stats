
from processors.awards import AwardProcessor,Column
from models import model_mgr
from models.vehicles import STATION

class Processor(AwardProcessor):
    '''
    Overview
        This processor keeps track of the maximum death streak against turrets.

    Implementation
    Whenever a kill event is received, the counter is reset for the attacker.
    The counter is also reset for the victim if the vehicle isn't in the STATION group.
    If the vehicle is in the STATION group, the victim's counter is increased and
    the result is set to the current maximum

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Fools Gold', 'Max Death Streak by Turrets',
                                [Column('Players'), Column('Deaths', Column.NUMBER, Column.DESC)])

        self.current = dict()
    
    def on_kill(self, e):
        # Reset counter to 0 for kills
        self.current[e.attacker] = 0
        
        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        if e.victim not in self.current:
            self.current[e.victim] = 0

        attack_vehicle = model_mgr.get_vehicle(e.attacker.vehicle_id)
        if attack_vehicle.group == STATION:
            self.current[e.victim] += 1

            if e.victim not in self.results:
                self.results[e.victim] = self.current[e.victim]
                
            if self.current[e.victim] > self.results[e.victim]:
                self.results[e.victim] = self.current[e.victim]
        else:
            # Reset counter for non turret deaths
            self.current[e.victim] = 0
