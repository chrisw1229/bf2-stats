
from processors.awards import AwardProcessor,Column,PLAYER_COL
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
        AwardProcessor.__init__(self, 'Fool\'s Gold',
                'Max Death Streak by Turrets',
                [PLAYER_COL, Column('Deaths', Column.NUMBER, Column.DESC)])

        self.current = dict()

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        # Reset counter to 0 for kills
        self.current[e.attacker] = 0

        if e.victim not in self.current:
            self.current[e.victim] = 0

        # Check whether the victim was killed by a station
        attack_vehicle = model_mgr.get_vehicle(e.attacker.vehicle_id)
        if attack_vehicle.group == STATION:

            # Add a station death point update the results with the max
            self.current[e.victim] += 1
            self.results[e.victim] = max(self.results[e.victim], self.current[e.victim])
        else:

            # Reset counter for non turret deaths
            self.current[e.victim] = 0
