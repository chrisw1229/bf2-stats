
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models import weapons
from models import model_mgr

class Processor(AwardProcessor):
    '''
    Overview
        This processor keeps track of kills against players with better weapons.

    Implementation
	store rankings of weapon types and compare rank of attacker and victim weapon types.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Equalizer',
                'Most Kills against Players with Better Weapons',
                [PLAYER_COL, Column('Kills', Column.NUMBER, Column.DESC)])

        self.ranks = dict()
        self.ranks[weapons.TOOL]      = 0
        self.ranks[weapons.COUNTER]   = 1
        self.ranks[weapons.MELEE]     = 2
        self.ranks[weapons.PISTOL]    = 3
        self.ranks[weapons.SNIPER]    = 4
        self.ranks[weapons.SHOTGUN]   = 5
        self.ranks[weapons.CARBINE]   = 6
        self.ranks[weapons.ASSAULT]   = 7
        self.ranks[weapons.GRENADE]   = 8
        self.ranks[weapons.SMG]       = 9
        self.ranks[weapons.LMG]       = 10
        self.ranks[weapons.MINE]      = 11
        self.ranks[weapons.HMG]       = 12
        self.ranks[weapons.CANNON]    = 13
        self.ranks[weapons.ROCKET]    = 14
        self.ranks[weapons.ARTILLERY] = 15

    def on_kill(self, e):

        # Ignore suicides and team kills
        if not e.valid_kill:
            return

        vWeapon = model_mgr.get_weapon(e.victim.weapon_id)
        if e.weapon == weapons.EMPTY or vWeapon == weapons.EMPTY:
            return

        if self.ranks[e.weapon.weapon_type] < self.ranks[vWeapon.weapon_type]:
            self.results[e.attacker] += 1
