
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
EMPTY = Kit('', '', '', '')

def _add(id, kit_type, name, desc):
    registry.add(Kit(id, kit_type, name, desc))

_add('ch_assault', ASSAULT, ASSAULT,
'')

_add('ch_at', ANTI_TANK, 'Anti-Tank',
'')

_add('ch_engineer', ENGINEER, 'Engineer',
'')

_add('ch_medic', MEDIC, 'Medic',
'')

_add('ch_sniper', SNIPER, 'Sniper',
'')

_add('ch_specops', SPEC_OPS, 'Special Ops',
'')

_add('ch_support', SUPPORT, 'Support',
'')

_add('mec_assault', ASSAULT, 'Assault',
'')

_add('mec_at', ANTI_TANK, 'Anti-Tank',
'')

_add('mec_engineer', ENGINEER, 'Engineer',
'')

_add('mec_medic', MEDIC, 'Medic',
'')

_add('mec_sniper', SNIPER, 'Sniper',
'')

_add('mec_specops', SPEC_OPS, 'Special Ops',
'')

_add('mec_support', SUPPORT, 'Support',
'')

_add('us_assault', ASSAULT, 'Assault',
'')

_add('us_at', ANTI_TANK, 'Anti-Tank',
'')

_add('us_engineer', ENGINEER, 'Engineer',
'')

_add('us_medic', MEDIC, 'Medic',
'')

_add('us_sniper', SNIPER, 'Sniper',
'')

_add('us_specops', SPEC_OPS, 'Special Ops',
'')

_add('us_support', SUPPORT, 'Support',
'')
