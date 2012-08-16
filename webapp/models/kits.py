
# Create a shared registry of all the kit types
registry = set()

# Kit type constants
ASSAULT = 'assault'
ANTI_TANK = 'anti_tank'
ENGINEER = 'engineer'
MEDIC = 'medic'
SNIPER = 'sniper'
SPEC_OPS = 'spec_ops'
SUPPORT = 'support'

class Kit(object):

    def __init__(self, id, kit_type, name, desc):
        self.id = id
        self.kit_type = kit_type
        self.name = name
        self.desc = desc

        self.reset()

    def __repr__(self):
        return self.__dict__

    def reset(self):
        pass

EMPTY = Kit('', '', '', '')

def _add(id, kit_type, name, desc):
    registry.add(Kit(id, kit_type, name, desc))

_add('ch_assault', ASSAULT, 'China Assault',
'')

_add('ch_at', ANTI_TANK, 'China Anti-Tank',
'')

_add('ch_engineer', ENGINEER, 'China Engineer',
'')

_add('ch_medic', MEDIC, 'China Medic',
'')

_add('ch_sniper', SNIPER, 'China Sniper',
'')

_add('ch_specops', SPEC_OPS, 'China Special Ops',
'')

_add('ch_support', SUPPORT, 'China Support',
'')

_add('eu_assault', ASSAULT, 'EU Assault',
'')

_add('eu_at', ANTI_TANK, 'EU Anti-Tank',
'')

_add('eu_engineer', ENGINEER, 'EU Engineer',
'')

_add('eu_medic', MEDIC, 'EU Medic',
'')

_add('eu_sniper', SNIPER, 'EU Sniper',
'')

_add('eu_specops', SPEC_OPS, 'EU Special Ops',
'')

_add('eu_support', SUPPORT, 'EU Support',
'')

_add('mec_assault', ASSAULT, 'MEC Assault',
'')

_add('mec_at', ANTI_TANK, 'MEC Anti-Tank',
'')

_add('mec_engineer', ENGINEER, 'MEC Engineer',
'')

_add('mec_medic', MEDIC, 'MEC Medic',
'')

_add('mec_sniper', SNIPER, 'MEC Sniper',
'')

_add('mec_specops', SPEC_OPS, 'MEC Special Ops',
'')

_add('mec_support', SUPPORT, 'MEC Support',
'')

_add('us_assault', ASSAULT, 'US Assault',
'')

_add('us_at', ANTI_TANK, 'US Anti-Tank',
'')

_add('us_engineer', ENGINEER, 'US Engineer',
'')

_add('us_medic', MEDIC, 'US Medic',
'')

_add('us_sniper', SNIPER, 'US Sniper',
'')

_add('us_specops', SPEC_OPS, 'US Special Ops',
'')

_add('us_support', SUPPORT, 'US Support',
'')
