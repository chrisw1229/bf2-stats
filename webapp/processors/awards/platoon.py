from processors.awards import AwardProcessor,Column

class Processor(AwardProcessor):
    '''
    Overview
    This award is given to the players with the most team kills of fellow squad members.

    Implementation
    On kill, check the victim and attacker's squad id. Increment attacker's total.
    
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Platoon', 'Most Teamkills of Squadmates', [
                Column('Players'), Column('Teamkills', Column.NUMBER, Column.DESC)])

    def on_kill(self, e):
        
        if e.attacker.squad_id != None and e.attacker.squad_id == e.victim.squad_id:
            self.results[e.attacker] += 1

