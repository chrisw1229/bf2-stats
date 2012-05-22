
# Create a shared registry of all the kit types
registry = []

class Kit(object):

    def __init__(self, id, kit_type, name, desc):
        self.id = id
        self.kit_type = kit_type
        self.name = name
        self.desc = desc
EMPTY = Kit('', '', '', '')

def _add(id, kit_type, name, desc):
    registry.append(Kit(id, kit_type, name, desc))

_add('ch_assault', 'assault', 'Assault',
'')

_add('ch_at', 'anti_tank', 'Anti-Tank',
'')

_add('ch_engineer', 'engineer', 'Engineer',
'')

_add('ch_medic', 'medic', 'Medic',
'')

_add('ch_sniper', 'sniper', 'Sniper',
'')

_add('ch_specops', 'spec_ops', 'Special Ops',
'')

_add('ch_support', 'support', 'Support',
'')

_add('mec_assault', 'assault', 'Assault',
'')

_add('mec_at', 'anti_tank', 'Anti-Tank',
'')

_add('mec_engineer', 'engineer', 'Engineer',
'')

_add('mec_medic', 'medic', 'Medic',
'')

_add('mec_sniper', 'sniper', 'Sniper',
'')

_add('mec_specops', 'spec_ops', 'Special Ops',
'')

_add('mec_support', 'support', 'Support',
'')

_add('us_assault', 'assault', 'Assault',
'')

_add('us_at', 'anti_tank', 'Anti-Tank',
'')

_add('us_engineer', 'engineer', 'Engineer',
'')

_add('us_medic', 'medic', 'Medic',
'')

_add('us_sniper', 'sniper', 'Sniper',
'')

_add('us_specops', 'spec_ops', 'Special Ops',
'')

_add('us_support', 'support', 'Support',
'')
