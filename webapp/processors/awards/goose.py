
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import players
from models.vehicles import AIR
from models import model_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most deaths from ejecting

    Implementation
    Set the eject status to false on spawning.
	Check to make sure a player has exited aircraft at altitude.
	When a player is killed see if the attacker is nobody.
	Parachutes should not be counted unless the player never gets in one or
    gets in one, but gets out of it too soon.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Goose',
                'Most Deaths from Ejections',
                [PLAYER_COL, Column('Deaths', Column.NUMBER, Column.DESC)])

        self.eject = dict()

    def on_spawn(self, e):
        self.eject[e.player] = False

    def on_vehicle_enter(self, e):

        # Clear the eject flag if the player enters any vehicle
        # Parachutes are included here since that could prevent death
        self.eject[e.player] = False

    def on_vehicle_exit(self, e):

        # Check whether a player ejected from an aircraft at altitude
        # Parachutes are included here since that could still cause death
        if e.vehicle.group == AIR and e.player_pos[1] > 30:
            self.eject[e.player] = True
        else:

            # Clear the eject flag if the player gets out of any other vehicle
            # Exiting a parachute on the ground should not be counted
            self.eject[e.player] = False

    def on_kill(self, e):

        # Check whether the victim died to nobody
        if e.attacker == players.EMPTY and self.eject[e.victim] == True:
            self.results[e.victim] += 1
