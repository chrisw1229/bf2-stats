
# Create a shared registry of all the map types
registry = set()

# Map region constants
ASIA = 'asia'
MIDDLE_EAST = 'middle_east'
UNITED_STATES = 'united_states'

class Map(object):

    def __init__(self, id, name, region, teams, briefing, mode):
        self.id = id
        self.name = name
        self.region = region
        self.briefing = briefing
        self.mode = mode

        self.reset()

    def __repr__(self):
        return self.__dict__

    def reset(self):
        pass

EMPTY = Map('', '', '', ['', ''], '', '')

def _add(id, name, region, teams, briefing, mode):
    registry.add(Map(id, name, region, teams, briefing, mode))

_add('dalian_plant', 'Dalian Plant', ASIA, ['us', 'ch'],
'US Rapid Deployment forces are advancing to capture the Dalian Plant nuclear \
facility and force disruptions to the electrical grid in northern China. \
Elements of the Second Army of the People\'s Republic of China have moved \
forward to serve as an improvised defensive force. This location is of vital \
strategic importance to both sides, for a major reduction of the generating \
capacity of the PLA forces would allow rapid consolidation of US units \
dispersed throughout this vast region.',
'This is a Conquest: Head-on map. Your team will win if you cause your \
opponent\'s tickets to reach zero. You can increase the rate at which they \
lose tickets by holding at least half of the control points on this map.')

_add('daqing_oilfields', 'Daqing Oilfields', ASIA, ['us', 'ch'],
'American forces striking south are now poised to seize this crucial logistic \
component in China\'s ongoing war effort, seeking to both divert petroleum \
resources while simultaneously hindering PLA mechanized efforts in this \
sector. The stakes are high in this head-on collision between advancing US \
brigades and the defending Chinese forces, with both sides advised to \
cautiously advance through this volatile landscape.',
'This is a Conquest: Head-on map. Your team will win if you cause your \
opponent\'s tickets to reach zero. You can increase the rate at which they \
lose tickets by holding at least half of the control points on this map.')

_add('dragon_valley', 'Dragon Valley', ASIA, ['us', 'ch'],
'Ancient legends of this "fairyland on earth," tell of a yellow dragon that \
helped a king channel flood waters into the sea. Currently, American military \
forces are converging upon this idyllic valley, to secure a foothold in the \
Minshan mountain range. Elements of the US Marines are on the offensive in \
this sector, while the forces of the People\'s Republic of China are called \
upon to defend ancient ancestral lands, in what promises to be a bitter \
engagement.',
'This is a Conquest: Assault map. The force that causes the opponent\'s \
tickets to reach zero wins. The defending force can reduce the attacking \
force\'s tickets gradually by holding all of the control points on the map. \
The attacking force can gradually reduce the defending force\'s tickets by \
holding all of the control points on the map.')

_add('fushe_pass', 'Fushe Pass', ASIA, ['us', 'ch'],
'China\'s rich mining areas in the northeastern highland have become contested \
by rapidly deploying American and Chinese forces. The narrow canyons carved \
into this region channel both forces into inevitable head-on confrontations as \
each seeks to secure the prized uranium mines with their advancing forces. In \
the context of this double assault, success will favor the bold, given the \
constrained nature of this rugged battlefield.',
'This is a Conquest: Head-on map. Your team will win if you cause your \
opponent\'s tickets to reach zero. You can increase the rate at which they \
lose tickets by holding at least half of the control points on this map.')

_add('greatwall', 'Great Wall', ASIA, ['eu', 'ch'],
'A newly negotiated peace with Russia has allowed the European Union to launch \
an attack into mainland China from the north. The EU forces hope to breach the \
Great Wall of China and establish a base for future operations before \
continuing south to the coast, but their supply lines are dangerously thin. If \
the Chinese forces can head off the assault and hold them back long enough, \
the EU will have no choice but to retreat back into Russia. It\'s vital for \
them to link up with American forces attacking from the coast, or a sustained \
assault on China will be impossible!',
'This is a Conquest: Head-on map. Your team will win if you cause your \
opponent\'s tickets to reach zero. You can increase the rate at which they \
lose tickets by holding at least half of the control points on this map.')

_add('gulf_of_oman', 'Gulf of Oman', MIDDLE_EAST, ['us', 'mec'],
'A USMC Marine Expeditionary Unit (MEU) has landed on this Persian Gulf beach \
during the night in the hopes of quickly seizing the nearby MEC airbase. The \
stakes are high for both sides. The Marines face possibly being driven into \
the sea and destroyed. The MEC forces could lose a key airbase and open the \
door for US forces to take strategic oilfields. Both sides have been using the \
morning to prepare for a final assault.',
'This is a Conquest: Head-on map. Your team will win if you cause your \
opponent\'s tickets to reach zero. You can increase the rate at which they \
lose tickets by holding at least half of the control points on this map.')

_add('highway_tampa', 'Highway Tampa', MIDDLE_EAST, ['us', 'mec'],
'As the most direct path for supplies and re-enforcements for both sides this \
expanse of the Arabian Peninsula has been dubbed Highway Tampa by the U.S. \
forces. In order to ensure safe passage of critical new Intel technologies \
through the supply route the U.S. forces must hold off the encroaching MEC \
mobile divisions.',
'This is a Conquest: Head-on map. Your team will win if you cause your \
opponent\'s tickets to reach zero. You can increase the rate at which they \
lose tickets by holding at least half of the control points on this map.')

_add('kubra_dam', 'Kubra Dam', MIDDLE_EAST, ['us', 'mec'],
'Active Component brigades of the US Marines are deploying toward a key dam \
site in the Saudi desert, intent upon control of this strategic location. To \
counter the threat, MEC forces are advancing their own mobile brigades to \
blunt the US spearhead. This rough desert terrain contains a mix of terrain \
types, requiring the utmost in tactical flexibility by both US and MEC \
soldiers. The ultimate objective of both sides in this battle is to gain \
control of the entire Kubra Dam sector.',
'This is a Conquest: Assault map. The force that causes the opponent\'s \
tickets to reach zero wins. The defending force can reduce the attacking \
force\'s tickets gradually by holding all of the control points on the map. \
The attacking force can gradually reduce the defending force\'s tickets by \
holding all of the control points on the map.')

_add('mashtuur_city', 'Mashtuur City', MIDDLE_EAST, ['us', 'mec'],
'Leading elements of the US ground force must capture Mashtuur City, a primary \
Middle East axis of advance. In response, MEC units are rushing forward to \
hold the city at all costs. In this double assault upon a key urban asset, all \
elements of modern warfare are likely to be deployed, attempting to secure \
vital CPs that dot the city. Victory will go to the side that controls the \
majority of Mashtuur when hostilities cease.',
'This is a Conquest: Head-on map. Your team will win if you cause your \
opponent\'s tickets to reach zero. You can increase the rate at which they \
lose tickets by holding at least half of the control points on this map.')

_add('midnight_sun', 'Midnight Sun', UNITED_STATES, ['us', 'ch'],
'The Chinese have made landfall on American soil, securing the Alaskan Port of \
Valdez and the oil that flows in from the Alaskan pipeline. The victory was \
quick, with most American forces preoccupied with MEC forces in the South. The \
Chinese have begun pushing upriver, skirmishing with the outnumbered but \
determined American soldiers, intent on making the Chinese pay for every inch \
of American soil. US Reinforcements have arrived, and the battle for the land \
of the midnight sun is about to begin.',
'This is a Conquest: Head-on map. Your team will win if you cause your \
opponent\'s tickets to reach zero. You can increase the rate at which they \
lose tickets by holding at least half of the control points on this map.')

_add('operation_blue_pearl', 'Operation Blue Pearl', ASIA, ['us', 'ch'],
'American forces have pushed east where the PLA forces have gathered to make a \
strategic stand against the approaching enemy. As the main route into the \
region, this will be a critical confrontation for both armies. A win for the \
U.S. Forces will position them for a possible quick close of the war, but a \
win for the PLA Forces will temporarily cripple the Americans progression and \
allow ample time for reinforcements.',
'This is a Conquest: Assault map. The force that causes the opponent\'s \
tickets to reach zero wins. The defending force can reduce the attacking \
force\'s tickets gradually by holding all of the control points on the map. \
The attacking force can gradually reduce the defending force\'s tickets by \
holding all of the control points on the map.')

_add('operation_clean_sweep', 'Operation Clean Sweep', MIDDLE_EAST, ['us', 'mec'],
'This vital entrance to the Persian Gulf is held by local MEC forces who have \
established a strong defensive presence on the scattered islands of the \
waterway. For the US Rapid Deployment force to clear the waterway they must \
first deploy air assets to disable a key MEC power station, after which the US \
force must enter the channel and capture the islands defended by these \
determined MEC fighters.',
'This is a Conquest: Assault map. The force that causes the opponent\'s \
tickets to reach zero wins. The defending force can reduce the attacking \
force\'s tickets gradually by holding all of the control points on the map. \
The attacking force can gradually reduce the defending force\'s tickets by \
holding all of the control points on the map.')

_add('operationharvest', 'Operation Harvest', UNITED_STATES, ['us', 'mec'],
'Units of the MEC Second Armoured have fought their way from a beachhead \
landing in the Delaware Bay to here in the Pennsylvania Dutch farmland of \
Lancaster County. This bold push is to cut off American units moving south to \
reinforce Washington D.C., a city under siege by MEC forces. This \
agriculturally rich area of American culture is about to erupt, as battle \
hardened units of America\'s Armoured and Cavalry Divisions muster to stop the \
MEC Second Armoured advance head on.',
'This is a Conquest: Head-on map. Your team will win if you cause your \
opponent\'s tickets to reach zero. You can increase the rate at which they \
lose tickets by holding at least half of the control points on this map.')

_add('operationroadrage', 'Operation Road Rage', UNITED_STATES, ['us', 'mec'],
'The MEC forces have made landfall on the Eastern Coast of the United States, \
and are preparing to push inland. Caught by surprise, the US Marines are \
deploying nearby, hastily preparing a base of operations to stop the MEC \
advance. The key objective for both armies is a highway junction in the middle \
of the battlefield that grants access to nearly every key military target in \
the area. Whoever controls this overpass controls most of the Eastern Seaboard!',
'This is a Conquest: Head-on map. Your team will win if you cause your \
opponent\'s tickets to reach zero. You can increase the rate at which they \
lose tickets by holding at least half of the control points on this map.')

_add('operationsmokescreen', 'Operation Smoke Screen', MIDDLE_EAST, ['eu', 'mec'],
'War continues to rage for the precious oil in the Middle East. The EU has \
come to aid their allies, confronting the MEC head-on in one of the most \
brutal battles of the war. Multiple assaults on both fronts have pushed the \
armies back to their bases, decimating the middle ground and leaving the oil \
field a smoking ruin. Even though the oil reserves have been destroyed, what \
remains beneath the scorched desert sand makes this a battleground worth \
fighting for.',
'This is a Conquest: Head-on map. Your team will win if you cause your \
opponent\'s tickets to reach zero. You can increase the rate at which they \
lose tickets by holding at least half of the control points on this map.')

_add('road_to_jalalabad', 'Road to Jalalabad', MIDDLE_EAST, ['us', 'mec'],
'The American war machine has thundered over to the eastern border of \
Afghanistan in its continued battle against the MEC. Jalalabad dominates the \
entrances to the Laghman and Kunar valleys, and is the first stop for men and \
supplies streaming across the Pakistani border into Afghanistan. It\'s a \
crucial training and logistical outpost of the MEC forces, who are holed up in \
the heart of the city awaiting an impending US onslaught with bated breath. \
This city is a strategic capture point and must be taken at any cost!',
'This is a Conquest: Assault map. The force that causes the opponent\'s \
tickets to reach zero wins. The defending force can reduce the attacking \
force\'s tickets gradually by holding all of the control points on the map. \
The attacking force can gradually reduce the defending force\'s tickets by \
holding all of the control points on the map.')

_add('sharqi_peninsula', 'Sharqi Peninsula', MIDDLE_EAST, ['us', 'mec'],
'This vital position on the Persian Gulf possesses a TV station with a \
powerful transmitter, allowing it to aid propaganda support for the ongoing \
MEC campaign. US Rapid Deployment forces have captured this coastal position \
and now face a determined counterattack by converging MEC forces. This lazy \
seaside resort of villas, markets and beach houses is about to become a modern \
battlefield as US forces attempt to hold on to their newly-captured \
communications prize.',
'This is a Conquest: Assault map. The force that causes the opponent\'s \
tickets to reach zero wins. The defending force can reduce the attacking \
force\'s tickets gradually by holding all of the control points on the map. \
The attacking force can gradually reduce the defending force\'s tickets by \
holding all of the control points on the map.')

_add('songhua_stalemate', 'Songhua Stalemate', ASIA, ['us', 'ch'],
'Newly formed Active Component brigades of the US Marines advance from the \
Russian plains into the territories of the People\'s Republic of China where \
rapidly deployed Chinese forces mass to counter the assault. The stalemated \
situation along the Songhua River has deteriorated into reciprocal assaults by \
both sides, each seeking to capture this vital transportation artery. Stakes \
are high in this double assault that involves control of a main gateway to \
Southern Manchuria.',
'This is a Conquest: Double assault map. You reduce opponent\'s tickets by \
holding more than half of the control points on the map. You win by capturing \
all control points or by reducing the opponent\'s tickets to zero.')

_add('strike_at_karkand', 'Strike at Karkand', MIDDLE_EAST, ['us', 'mec'],
'Control of the industrial facility and harbor at Karkand motivate this \
assault by US forces, where they find MEC forces marshalling to defend the \
industrial city and determined to meet this attack with stiff resistance. The \
terrain surrounding Karkand sufficiently opens to allow for sweeping fields of \
fire but the open ground increases the danger posed by anti-vehicle missiles \
and sniping. It is thus vital for both sides to secure firebases in Karkand\'s \
sheltered city center.',
'This is a Conquest: Assault map. The force that causes the opponent\'s \
tickets to reach zero wins. The defending force can reduce the attacking \
force\'s tickets gradually by holding all of the control points on the map. \
The attacking force can gradually reduce the defending force\'s tickets by \
holding all of the control points on the map.')

_add('taraba_quarry', 'Taraba Quarry', MIDDLE_EAST, ['eu', 'mec'],
'The EU forces are en route to reinforce an American division that has been \
cut off from the front lines. The MEC have moved to intercept them, and both \
armies are about to meet at the Taraba Quarry, the only crossing point of the \
Taraba River this side of the Caspian Sea. If the MEC can hold their side of \
the river, the Americans will be cut off and surrounded. The EU must break \
through the enemy lines before the Americans are overrun!',
'This is a Conquest: Head-on map. Your team will win if you cause your \
opponent\'s tickets to reach zero. You can increase the rate at which they \
lose tickets by holding at least half of the control points on this map.')

_add('wake_island_2007', 'Wake Island 2007', ASIA, ['us', 'ch'],
'In a surprise move, forces of the People\'s Liberation Army have attacked and \
captured Wake Island in a bid to threaten US lines of supply. USMC forces have \
been short-stopped from their deployment in Manchuria to respond to this new \
threat. The airbase on Wake Island is the lynchpin of the Chinese air threat, \
however it is highly susceptible to ground attack from either the northern or \
southern approaches of the island.',
'This is a Conquest: Head-on map. Your team will win if you cause your \
opponent\'s tickets to reach zero. You can increase the rate at which they \
lose tickets by holding at least half of the control points on this map.')

_add('zatar_wetlands', 'Zatar Wetlands', MIDDLE_EAST, ['us', 'mec'],
'The Zatar Wetlands along the Red Sea coastline possess vital natural gas \
resources, but create a difficult battlefield for US and MEC forces. Small \
tributaries break the landscape into isolated islands whose soggy marshes \
inhibit heavy vehicles. As American forces advance, MEC forces possess an \
initial advantage in the air. Control of an abandoned airfield is crucial \
early in the battle, after which supply line protection will become an \
additional consideration.',
'This is a Conquest: Head-on map. Your team will win if you cause your \
opponent\'s tickets to reach zero. You can increase the rate at which they \
lose tickets by holding at least half of the control points on this map.')
