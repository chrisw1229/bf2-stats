
# Create a shared registry of all the team types
registry = set()

class Team(object):

    def __init__(self, id, name, desc):
        self.id = id
        self.name = name
        self.desc = desc

        self.commander_id = None
        self.squad_ids = set()
        self.player_ids = set()

EMPTY = Team('', '', '')

def _add(id, name, desc):
    registry.add(Team(id, name, desc))

_add('ch', 'China',
'')

_add('eu', 'European Union',
'')

_add('mec', 'Mercenaries',
'')

_add('us', 'United States',
'')
