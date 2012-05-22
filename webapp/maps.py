
# Create a shared registry of all the map types
registry = []

class Map(object):

    def __init__(self, id, name, region, desc):
        self.id = id
        self.name = name
        self.region = region
        self.desc = desc
EMPTY = Map('', '', '', '')

def _add(id, name, region, desc):
    registry.append(Map(id, name, region, desc))

_add('dalian_plant', 'Dalian Plant', 'asia',
'')

_add('daqing_oilfields', 'Daqing Oilfields', 'asia',
'')

_add('dragon_valley', 'Dragon Valley', 'asia',
'')

_add('fushe_pass', 'Fushe Pass', 'asia',
'')

_add('greatwall', 'Great Wall', 'asia',
'')

_add('gulf_of_oman', 'Gulf of Oman', 'middle_east',
'')

_add('hingan_hills', 'Hingan Hills', 'asia',
'')

_add('kubra_dam', 'Kubra Dam', 'middle_east',
'')

_add('mashtuur_city', 'Mashtuur City', 'middle_east',
'')

_add('midnight_sun', 'Midnight Sun', 'united_states',
'')

_add('operation_blue_pearl', 'Operation Blue Pearl', 'asia',
'')

_add('operation_clean_sweep', 'Operation Clean Sweep', 'middle_east',
'')

_add('operationharvest', 'Operation Harvest', 'united_states',
'')

_add('operationroadrage', 'Operation Road Rage', 'united_states',
'')

_add('operationsmokescreen', 'Operation Smoke Screen', 'middle_east',
'')

_add('road_to_jalalabad', 'Road to Jalalabad', 'middle_east',
'')

_add('sharqi_peninsula', 'Sharqi Peninsula', 'middle_east',
'')

_add('songhua_stalemate', 'Songhua Stalemate', 'asia',
'')

_add('strike_at_karkand', 'Strike at Karkand', 'middle_east',
'')

_add('taraba_quarry', 'Taraba Quarry', 'middle_east',
'')

_add('zatar_wetlands', 'Zatar Wetlands', 'middle_east',
'')
