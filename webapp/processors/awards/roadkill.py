from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import model_mgr
from models.vehicles import LAND
from models.weapons import EMPTY

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the players with the most kills by vehicle crush.

    Implementation
    On kill, check if the attacker is driving a land vehicle and the weapon is empty.
    
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Roadkill', 'Most Kills by Vehicle Crush',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):
        #Ignore suicides and team kills
        if not e.valid_kill:
            return

        if not e.attacker.driver:
            return
        
        landCheck = model_mgr.get_vehicle(e.attacker.vehicle_id)
        if landCheck.group != LAND:
            return

        if e.weapon != EMPTY:
            return

        self.results[e.attacker] += 1
