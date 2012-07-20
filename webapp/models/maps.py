
# Create a shared registry of all the map types
registry = set()

# Map region constants
ASIA = 'asia'
MIDDLE_EAST = 'middle_east'
UNITED_STATES = 'united_states'

class Map(object):

    def __init__(self, id, name, region, teams, desc):
        self.id = id
        self.name = name
        self.region = region
        self.desc = desc

        self.reset()

    def __repr__(self):
        return self.__dict__

    def reset(self):
        pass

EMPTY = Map('', '', '', ['', ''], '')

def _add(id, name, region, teams, desc):
    registry.add(Map(id, name, region, teams, desc))

_add('dalian_plant', 'Dalian Plant', ASIA, ['us', 'ch'],
'')

_add('daqing_oilfields', 'Daqing Oilfields', ASIA, ['us', 'ch'],
'')

_add('dragon_valley', 'Dragon Valley', ASIA, ['us', 'ch'],
'')

_add('fushe_pass', 'Fushe Pass', ASIA, ['us', 'ch'],
'')

_add('greatwall', 'Great Wall', ASIA, ['eu', 'ch'],
'')

_add('gulf_of_oman', 'Gulf of Oman', MIDDLE_EAST, ['us', 'mec'],
'')

_add('highway_tampa', 'Highway Tampa', MIDDLE_EAST, ['us', 'mec'],
'')

_add('kubra_dam', 'Kubra Dam', MIDDLE_EAST, ['us', 'mec'],
'')

_add('mashtuur_city', 'Mashtuur City', MIDDLE_EAST, ['us', 'mec'],
'')

_add('midnight_sun', 'Midnight Sun', UNITED_STATES, ['us', 'ch'],
'')

_add('operation_blue_pearl', 'Operation Blue Pearl', ASIA, ['us', 'ch'],
'')

_add('operation_clean_sweep', 'Operation Clean Sweep', MIDDLE_EAST, ['us', 'mec'],
'')

_add('operationharvest', 'Operation Harvest', UNITED_STATES, ['us', 'mec'],
'')

_add('operationroadrage', 'Operation Road Rage', UNITED_STATES, ['us', 'mec'],
'')

_add('operationsmokescreen', 'Operation Smoke Screen', MIDDLE_EAST, ['eu', 'mec'],
'')

_add('road_to_jalalabad', 'Road to Jalalabad', MIDDLE_EAST, ['us', 'mec'],
'')

_add('sharqi_peninsula', 'Sharqi Peninsula', MIDDLE_EAST, ['us', 'mec'],
'')

_add('songhua_stalemate', 'Songhua Stalemate', ASIA, ['us', 'ch'],
'')

_add('strike_at_karkand', 'Strike at Karkand', MIDDLE_EAST, ['us', 'mec'],
'')

_add('taraba_quarry', 'Taraba Quarry', MIDDLE_EAST, ['eu', 'mec'],
'')

_add('wake_island_2007', 'Wake Island 2007', ASIA, ['us', 'ch'],
'')

_add('zatar_wetlands', 'Zatar Wetlands', MIDDLE_EAST, ['us', 'mec'],
'')
