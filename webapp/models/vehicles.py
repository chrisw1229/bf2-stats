
# Create a shared registry of all the vehicle types
registry = set()

# Vehicle type constants
AIR_DEF = 'air_defense'
ARMOR = 'armor'
ARTILLERY = 'artillery'
BOAT = 'boat'
GROUND_DEF = 'ground_defense'
HELICOPTER = 'helicopter'
JET = 'jet'
PARACHUTE = 'parachute'
SENSOR = 'sensor'
TRANSPORT = 'transport'

# Vehicle group constants
AIR = 'air'
LAND = 'land'
SEA = 'sea'
STATION = 'station'

class Vehicle(object):

    def __init__(self, id, vehicle_type, group, model, name, slot_ids,
            weapon_ids, desc, cost):
        self.id = id
        self.vehicle_type = vehicle_type
        self.group = group
        self.model = model
        self.name = name
        self.slot_ids = set(slot_ids)
        self.weapon_ids = set(weapon_ids)
        self.desc = desc
        self.cost = cost #in millions of dollars

        self.reset()

    def __repr__(self):
        return self.__dict__

    def reset(self):
        pass

EMPTY = Vehicle('', '', '', '', '', [], [], '',0)

def _add(id, vehicle_type, group, model, name, slot_ids, weapon_ids, desc, cost):
    registry.add(Vehicle(id, vehicle_type, group, model, name, slot_ids,
            weapon_ids, desc, cost))

_add('aav_tunguska', AIR_DEF, LAND, 'Tunguska', 'Tunguska Grison',
['aav_tunguska_driver', 'aav_tunguska_cupolabase'],
['aav_tunguska_gun', 'aav_tunguska_sa19launcher'],
'The Tunguska is a Russian tracked self-propelled anti-aircraft weapon armed with a surface-to-air \
gun and missile system. It is designed to provide day and night protection for infantry and tank \
regiments against low-flying aircraft, helicopters, and cruise missiles in all weather conditions.',
16.0)

_add('aav_type95', AIR_DEF, LAND, 'Type 95', 'Type 95',
['aav_type95_driver', 'aav_type95_passenger'],
['aav_type95guns', 'aav_type95_qw2launcher'],
'The Type 95 is a Chinese self-propelled anti-aircraft vehicle. It is armed with four 25 \
millimeter cannons and optionally four fire-and-forget QW-2 infra-red homing missiles.',
4.0)

_add('ahe_ah1z', HELICOPTER, AIR, 'AH-1Z', 'AH-1Z Viper',
['ahe_ah1z_driver', 'ahe_ah1z_cogunner'],
['ahe_ah1z_hydralauncher', 'ahe_ah1z_gun', 'ahe_ah1z_cogunner_hellfirelaunchertv', 'ahe_ah1z_flarelauncher'],
'The Bell AH-1Z Viper is a twin-engine attack helicopter based on the AH-1W SuperCobra, that was \
developed for the United States Marine Corps. The AH-1Z features a four-blade, bearingless, \
composite main rotor system, uprated transmission, and a new target sighting system.',
31.0)

_add('ahe_havoc', HELICOPTER, AIR, 'Mi-28', 'Mi-28 Havoc',
['ahe_havoc_driver', 'ahe_havoc_cogunner'],
['ahe_havoc_s8launcher', 'ahe_havoc_gun', 'ahe_havoc_atakalauncher_tv'],
'The Mil Mi-28 (NATO reporting name Havoc) is a Russian all-weather, day-night, military tandem, \
two-seat anti-armour attack helicopter. It is a dedicated attack helicopter with no intended \
secondary transport capability, better optimized than the Mil Mi-24 for the role. It carries a \
single gun in an undernose barbette, plus external loads carried on pylons beneath stub wings.',
15.0)

_add('ahe_z10', HELICOPTER, AIR, 'Z-10', 'Z-10',
['ahe_z10_driver', 'ahe_z10_cogunner'],
['ahe_z10_s8launcher', 'ahe_z10_gun', 'ahe_z10_hj8launcher_tv'],
'The WZ-10 is an attack helicopter developed by the People''s Republic of China. It is designed \
primarily for anti-tank missions, but is also believed to have a secondary air-to-air capability.',
35.0)

_add('air_a10', JET, AIR, 'A-10', 'A-10 Thunderbolt II',
['air_a10_driver'],
['air_a10_us_bomblauncher'],
'',
11.8)

_add('air_f35b', JET, AIR, 'F-35B', 'F-35B Lightning II',
['air_f35b_driver'],
['air_f35b_autocannon', 'air_f35b_sidewinderlauncher', 'air_f35b_bomblauncher'],
'The Lockheed Martin F-35 Lightning II is a family of single-seat, single-engine, fifth generation \
multirole fighters under development to perform ground attack, reconnaissance, and air defense \
missions with stealth capability. The F-35B is the short takeoff and vertical landing (STOVL) \
variant of the aircraft. Similar in size to the A variant, the B sacrifices about a third of the \
other version''s fuel volume to make room for the vertical flight system. Takeoffs and landing \
with vertical flight systems are by far the riskiest, and in the end, a decisive factor in design.',
236.8)

_add('air_j10', JET, AIR, 'J-10', 'J-10 Vanguard',
['air_j10_driver'],
['air_j10_cannon', 'air_j10_archerlauncher'],
'The Chengdu J-10 is a multirole fighter aircraft designed and produced by the People''s Republic \
of China''s Chengdu Aircraft Industry Corporation (CAC) for the People''s Liberation Army Air \
Force (PLAAF). Known in the West as the "Vigorous Dragon", the J-10 is a multirole combat aircraft \
capable of all-weather operation.',
50.0)

_add('air_su30mkk', JET, AIR, 'Su-30MKK', 'Su-30MKK Flanker-G',
['air_su30mkk_driver', 'air_su30mkk_gunner'],
['air_su30mkk_30mmcannon', 'air_su30mkk_archerlauncher', 'air_su30mkk_kedgelauncher_laser'],
'The Sukhoi Su-30MKK is a modification of the Su-27 SK manufactured since 1999 by KnAAPO and \
Shenyang Aircraft Corporation. It is considered an upgraded version of Sukhoi Su-30. It was \
jointly developed by Russia and China, similar to the Su-30MKI. It is a heavy class, all-weather, \
long-range strike fighter, comparable to American F-15E.',
53.0)

_add('air_su39', JET, AIR, 'Su-39', 'Su-39 Frogfoot',
['air_su39_driver'],
['air_su39_canon'],
'',
11.0)

_add('aircontroltower', SENSOR, STATION, 'ACT', 'Air Control Tower',
[],
[],
'',
0.0)

_add('aircontroltower_mec', SENSOR, STATION, 'ACT', 'Air Control Tower',
[],
[],
'',
0.0)

_add('apc_btr90', ARMOR, LAND, 'BTR-90', 'BTR-90',
['apc_btr90_driver', 'apc_btr90_passenger_rf', 'apc_btr90_passenger_lf', 'apc_btr90_passenger_rb',
        'apc_btr90_passenger_lb'],
['apc_btr90__barrel', 'apc_btr90_hj8launcher', 'firingport_ak'],
'BTR-90 is an 8x8 wheeled armoured personnel carrier developed in Russia, designed in 1993 and \
first shown publicly in 1994. It is a larger version of the BTR-80 vehicle, fitted with a BMP-2 \
turret. Armour protection is improved compared with the BTR-80, giving protection from 14.5 mm \
projectiles over the frontal arc. It is armed with a 2A42 30 mm auto cannon, coaxial 7.62 mm PKT \
machine gun, AT-5 Spandrel ATGM, as well as a AGS-17 30 mm automatic grenade launcher.',
3.1)

_add('apc_wz551', ARMOR, LAND, 'WZ551', 'WZ551',
['apc_wz551_driver', 'apc_wz551_rearpassenger_left', 'apc_wz551_rearpassenger_stern',
        'apc_wz551_rearpassenger_right_front', 'apc_wz551_rearpassenger_right_rear'],
['apc_wz551_barrel', 'apc_wz551_hj8launcher', 'firingport_ak'],
'The WZ551 is a Chinese wheeled armored personnel carrier. It actually consists of two families of \
vehicles with official designations in the People''s Liberation Army as Type 90 and Type 92. \
Roughly 600 WZ551s are in service with the PLA, where they are used by light mechanized infantry.',
0.4)

_add('ars_d30', ARTILLERY, STATION, 'D-30', 'D-30 Howitzer',
[],
['ars_d30_barrel'],
'The D-30, or 122-mm howitzer D-30, is a Soviet howitzer that first entered service in the 1960s. \
It is a robust piece that focuses on the essential features of a towed field gun suitable for all \
conditions. The D-30 has a maximum range of 15.4 kilometers, or over 21 km using RAP ammunition. \
With its striking three-leg mounting the D-30 can be rapidly traversed through 360 degrees.',
0.1)

_add('ats_hj8', GROUND_DEF, STATION, 'HJ-8', 'HJ-8 Red Arrow',
['ats_hj8_driver'],
['ats_hj8_launcher'],
'The HJ-8 or Hongjian-8 is a second generation tube-launched, optically tracked, wire-guided \
anti-tank missile system which was originally deployed by the People''s Liberation Army since the \
late 1980s. It is able to defeat explosive reactive armour (ERA).',
0.5)

_add('ats_tow', GROUND_DEF, STATION, 'BGM-71', 'BGM-71 TOW',
['ats_tow_driver'],
['ats_tow_launcher'],
'The BGM-71 TOW is an anti-tank missile. BGM is a weapon classification that stands for Multiple \
Environment (B), Surface-Attack (G), Missile (M). TOW is an acronym that stands for Tube-launched, \
Optically-tracked, Wire command data link, guided missile. The TOW was first produced in 1970 and \
is one of the two most widely used anti-tank guided missiles by Western nations.',
0.18)

_add('boat_rib', BOAT, SEA, 'RIB', 'Rigid Inflatable Boat (RIB)',
['boat_rib_driver', 'boat_rib_gunpod', 'boat_rib_passengerfrontleft_cupolabase',
        'boat_rib_passengerfrontright_cupolabase', 'boat_rib_passengerrearleft_cupolabase',
        'boat_rib_passengerrearright_cupolabase'],
['uslmg_m249saw_stationary'],
'A rigid-hulled inflatable boat, (RHIB) or rigid-inflatable boat (RIB) is a light-weight but \
high-performance and high-capacity boat constructed with a solid, shaped hull and flexible tubes \
at the gunwale. The design is stable and seaworthy. The inflatable collar allows the vessel to \
maintain buoyancy even if a large quantity of water is shipped aboard due to bad sea conditions.',
0.00001)

_add('chhmg_kord', GROUND_DEF, STATION, 'Kord', 'Kord 6P50',
[],
[],
'The Kord-12.7 mm heavy machine gun is a Russian design that entered service in 1998 replacing the \
older NSV machine gun. Externally the weapon resembles the NSV, however the internal mechanism has \
been extensively reworked, changing from a horizontally pivoting breech block to a rotating bolt \
design. Additionally the gas system has been changed and the muzzle baffle redesigned. These \
changes give the weapon reduced recoil compared with the NSV, allowing greater accuracy during \
sustained fire.',
0.001)

_add('ch_bipod', GROUND_DEF, STATION, 'Bipod', 'China Bipod',
['ch_bipod_driver'],
['chlmg_type95_stationary'],
'?',
0.0)

_add('chthe_z8', HELICOPTER, AIR, 'Z-8', 'Z-8 Super Frelon',
['chthe_z8_driver', 'chthe_z8_llavett_cupolabase', 'chthe_z8_rlavett_cupolabase',
        'chthe_z8_rpassenger', 'chthe_z8_lpassenger', 'chthe_z8_rearpassenger'],
['chhmg_type85', 'chthe_z8_flarelauncher'],
'The Aerospatiale SA 321 Super Frelon is a three-engined heavy transport helicopter produced by \
Aerospatiale of France. The helicopter is still in use in China where the locally produced version \
is known as the Z-8.',
15.0)

_add('hmg_m2hb', GROUND_DEF, STATION, 'M2', 'Browning M2',
['hmg_m2hb_driver'],
['hmg_m2hb'],
'The M2 Machine Gun, Browning .50 Caliber Machine Gun, is a heavy machine gun designed towards the \
end of World War I by John Browning. It is very similar in design to Browning''s earlier M1919 \
Browning machine gun, which was chambered for the .30-06 cartridge. The M2 uses the larger and \
more powerful .50 BMG cartridge, which was named for the gun itself (BMG standing for Browning \
Machine Gun). It is effective against infantry, unarmored or lightly armored vehicles and boats, \
light fortifications and low-flying aircraft.',
0.0001)

_add('igla_djigit', AIR_DEF, STATION, 'Igla', 'Igla 9K38',
['igla_djigit_driver'],
['igla_djigit_launcher'],
'The 9K38 Igla is a Russian/Soviet man-portable infrared homing surface-to-air missile (SAM). The \
main improvements over the Igla-1 included much improved resistance against flares and jamming, a \
more sensitive seeker, expanding forward-hemisphere engagement capability to include \
straight-approaching fighters (all-aspect capability) under favourable circumstances, a slightly \
longer range, a higher-impulse, shorter-burning rocket with higher peak velocity (but \
approximately same time of flight to maximum range), and a propellant that performs as high \
explosive when detonated by the warhead''s secondary charge on impact.',
0.08)

_add('jeep_faav', TRANSPORT, LAND, 'FAAV', 'FAAV Jeep',
['jeep_faav_driver', 'jeep_faav_rear_passenger', 'jeep_faav_front_gun'],
['hmg_m2hb', 'uslmg_m249saw_stationary'],
'?',
0.045)

_add('jep_mec_paratrooper', TRANSPORT, LAND, 'Paratrooper', 'MEC Paratrooper Jeep',
['jep_mec_paratrooper_driver', 'jep_mec_paratrooper_gunbase', 'jep_mec_front_gunpos'],
['chhmg_kord', 'rulmg_rpk74_stationary'],
'?',
0.045)

_add('jep_nanjing', TRANSPORT, LAND, 'Nanjing', 'Nanjing Jeep',
['jep_nanjing_driver', 'jep_nanjing_cupolabase', 'jep_nanjing_passenger_rr',
        'jep_nanjing_passenger_rl'],
['chhmg_type85'],
'?',
0.045)

_add('jep_paratrooper', TRANSPORT, LAND, 'Paratrooper', 'Paratrooper Jeep',
['jep_paratrooper_driver', 'jep_paratrooper_gunbase', 'jep_paratrooper_front_gunpos'],
['chhmg_type85', 'chlmg_type95_stationary'],
'?',
0.045)

_add('jep_vodnik', TRANSPORT, LAND, 'GAZ-3937', 'GAZ-3937 Vodnik Jeep',
['jep_vodnik_driver', 'jep_vodnik_cupolabase', 'jep_vodnik_codriver', 'jep_vodnik_rearpassenger'],
['chhmg_kord'],
'GAZ-3937 Vodnik is a Russian high-mobility multipurpose military vehicle manufactured by GAZ. It \
is amphibious, and is propelled by it''s wheels in the water. It has a a water-displacing hermetic \
hull which provides improved fording performance and a 4x4-type chassis with independent \
suspension and a centralized system of tire-pressure control. The standard undercarriage with a \
cab can be fitted with a number of different modules with various number of passenger seats and \
cargo compartments, seating up to 10 people. It is powered by a 175 hp (130 kW) diesel engine \
giving a top speed of 112 km/h (4 to 5 km/h when swimming).',
0.045)

_add('mec_bipod', GROUND_DEF, STATION, 'Bipod', 'MEC Bipod',
['mec_bipod_driver'],
['rulmg_rpk74_stationary'],
'?',
0.0)

_add('mobileradar_us_dest', SENSOR, STATION, 'Radar', 'US Mobile Radar',
[],
[],
'',
0.0)

_add('parachute', PARACHUTE, AIR, 'Parachute', 'Parachute',
['parachute_driver'],
[],
'A parachute is a device used to slow the motion of an object through an atmosphere by creating \
drag, or in the case of ram-air parachutes, aerodynamic lift. Parachutes are usually made out of \
light, strong cloth, originally silk, now most commonly nylon. Parachutes must slow an object''s \
terminal vertical speed by a minimum 75% in order to be classified as such. Depending on the \
situation, parachutes are used with a variety of loads, including people, food, equipment, space \
capsules, and bombs.',
0.0)

_add('ruair_mig29', JET, AIR, 'MiG-29', 'MiG-29 Fulcrum',
['ruair_mig29_driver'],
['ruair_mig29_30mmcannon', 'ruair_archerlauncher', 'ruair_mig29_bomblauncher_1'],
'The Mikoyan MiG-29 is a fourth-generation jet fighter aircraft designed in the Soviet Union for \
an air superiority role. Developed in the 1970s by the Mikoyan design bureau, it entered service \
with the Soviet Air Force in 1983, and remains in use by the Russian Air Force as well as in many \
other nations. The MiG-29, along with the Sukhoi Su-27, was developed to counter new American \
fighters such as the McDonnell Douglas F-15 Eagle, and the General Dynamics F-16 Fighting Falcon.',
29.0)

_add('ruair_su34', JET, AIR, 'Su-34', 'Su-34 Fullback',
['ruair_su34_driver', 'ruair_su34_copilot'],
['ruair_su34_30mmcannon', 'ruair_su34_archerlauncher', 'ruair_su34_250kgbomblauncher'],
'The Sukhoi Su-34 is a Russian twin-seat fighter-bomber. It is intended to replace the Sukhoi \
Su-24. The aircraft shares most of its wing structure, tail, and engine nacelles with the \
Su-27/Su-30, with canards like the Su-30MKI/Su-33/Su-27M/35 to increase static instability (higher \
manoeuvrability) and to reduce trim drag. The aircraft has an entirely new nose and forward \
fuselage with a cockpit providing side-by-side seating for a crew of two. The Su-34 is powered by \
the AL-31FM1, the same engines as the Su-27SM, but its maximum speed is lower at Mach 1.8+.',
36.0)

_add('rutnk_t90', ARMOR, LAND, 'T-90', 'T-90',
['rutnk_t90_driver', 'rutnk_t90_cupolabase'],
['rutnk_t90_barrel', 'coaxial_mg_mec', 'chhmg_kord'],
'The T-90 is a Russian third-generation main battle tank that is a modernisation of the T-72 (it \
was originally to be called the T-72BU, later renamed to T-90). It is currently the most modern \
tank in service with the Russian Ground Forces and Naval Infantry. Although a development of the \
T-72, the T-90 uses a 125mm 2A46 smoothbore tank gun, 1G46 gunner sights, a new engine, and \
thermal sights. Standard protective measures include a blend of Steel, Composite armour, and \
Kontakt-5 explosive-reactive armor, laser warning receivers, Nakidka camouflage and the Shtora \
infrared ATGM jamming system.',
4.25)

_add('she_ec635', HELICOPTER, AIR, 'EC635', 'Eurocopter EC635',
['she_ec635_driver', 'she_ec635_leftpassenger', 'she_ec635_rightpassenger'],
['she_ec635_cannons'],
'',
43.0)
     
_add('she_littlebird', HELICOPTER, AIR, 'MH-6', 'MH-6 Little Bird',
['she_littlebird_driver', 'she_littlebird_leftspassenger', 'she_littlebird_rightpassenger'],
['she_littlebird_miniguns'],
'',
1.2)

_add('the_mi17', HELICOPTER, AIR, 'Mi-17', 'Mi-17 Hip',
['the_mi17_driver', 'the_mi17_llavett_cupolabase', 'the_mi17_rlavett_cupolabase',
        'the_mi17_cargo_passenger_left', 'the_mi17_cargo_passenger_right',
        'the_mi17_cargo_passenger_middle'],
[],
'The Mil Mi-17 (also known as the Mi-8M series in Russian service) is a Russian helicopter \
currently in production at two factories in Kazan and Ulan-Ude. Mil Mi-8/17 is a medium \
twin-turbine transport helicopter that can also act as a gunship.',
7.1)

_add('tnk_type98', ARMOR, LAND, 'Type 98', 'Type 98',
['tnk_type98_driver', 'tnk_type98_cupolabase'],
['tnk_type98_barrel', 'coaxial_mg_china', 'chhmg_type85', 'tnk_type98_smokelauncher'],
'The Type 99, also known as ZTZ-99 and WZ-123, developed from the Type 98G (in turn, a development \
of the Type 98), is a third generation main battle tank (MBT) fielded by the Chinese People''s \
Liberation Army. It is made to compete with other modern tanks. Although not expected to be \
acquired in large numbers due to its high cost compared to the more economical Type 96, it is \
currently the most advanced MBT fielded by China. The ZTZ99 MBT is a successor to the Type 98G \
tank manufactured for the People''s Liberation Army (PLA).',
4.5)

_add('us_bipod', GROUND_DEF, STATION, 'Bipod', 'US Bipod',
['us_bipod_driver'],
['uslmg_m249saw_stationary'],
'?',
0.0)

_add('usaas_stinger', AIR_DEF, STATION, 'FIM-92', 'FIM-92 Stinger',
['usaas_stinger_driver'],
['usaas_stinger_launcher'],
'The FIM-92 Stinger is a personal portable infrared homing surface-to-air missile (SAM), which can \
be adapted to fire from ground vehicles and helicopters (as an AAM), developed in the United \
States and entered into service in 1981. Used by the militaries of the U.S. and by 29 other \
countries, the basic Stinger missile has to-date been responsible for 270 confirmed aircraft \
kills. It is manufactured by Raytheon Missile Systems and under license by EADS in Germany, with \
70,000 missiles produced. It is classified as a Man-Portable Air-Defense System (MANPADS).',
0.038)

_add('usaav_m6', AIR_DEF, LAND, 'M6', 'M6 Linebacker',
['usaav_m6_driver', 'usaav_m6_cupolabase'],
['usaav_m6_barrel', 'usaav_m6_stinger_launcher'],
'The M6 Linebacker is an air defense variant of modified M2A2 ODSs with the TOW missile system \
replaced with a four-tube Stinger missile system. These are due to be retired from U.S. service.',
3.1)

_add('usair_f18', JET, AIR, 'F/A-18', 'F/A-18 Hornet',
['usair_f18_driver'],
['f18_autocannon', 'f18_sidewinderlauncher'],
'The McDonnell Douglas (now Boeing) F/A-18 Hornet is a twin-engine supersonic, all-weather \
carrier-capable multirole fighter jet, designed to dogfight and attack ground targets (F/A for \
Fighter/Attack). Designed by McDonnell Douglas and Northrop, the F/A-18 was derived from the \
latter''s YF-17 in the 1970s for use by the United States Navy and Marine Corps. The Hornet is \
also used by the air forces of several other nations. It has been the aerial demonstration \
aircraft for the U.S. Navy''s Flight Demonstration Squadron, the Blue Angels, since 1986.',
57.0)

_add('usair_f15', JET, AIR, 'F-15', 'F-15 Eagle',
['usair_f15_driver', 'usair_f15_guidedmissilecontroller'],
['usair_f15_autocannon', 'usair_f15_sidewinderlauncher', 'usair_f15_mavericklauncherlaser', 'usair_f15_250kgbomblauncher'],
'The McDonnell Douglas (now Boeing) F-15 Eagle is a twin-engine, all-weather tactical fighter \
designed by McDonnell Douglas to gain and maintain air superiority in aerial combat. It is \
considered among the most successful modern fighters, with over 100 aerial combat victories with \
no losses in dogfights.',
30.0)

_add('usapc_lav25', ARMOR, LAND, 'LAV-25', 'LAV-25 APC',
['usapc_lav25_driver', 'usapc_lav25_rearpassenger_l', 'usapc_lav25_rearpassenger_r',
        'usapc_lav25_rearpassenger_bl', 'usapc_lav25_rearpassenger_br'],
['usapc_lav25_barrel', 'usapc_lav25_towlauncher', 'firingport_m16'],
'The LAV-25 is an eight-wheeled amphibious reconnaissance vehicle used by the United States Marine \
Corps. It was built by General Dynamics Land Systems Canada and is based on the Swiss MOWAG \
Piranha I 8x8 family of armored fighting vehicles.',
0.9)

_add('usart_lw155', ARTILLERY, STATION, 'M777', 'M777 Howitzer',
[],
['usart_lw155_barrel'],
'The M777 howitzer is a towed 155 mm artillery piece, successor to the M198 howitzer in the United \
States Marine Corps and United States Army. The M777 is also used by the Canadian Army, and has \
been in action in Afghanistan since February 2006 along with the associated GPS-guided Excalibur \
ammunition.',
1.17)

_add('usjep_hmmwv', TRANSPORT, LAND, 'HMMWV', 'HMMWV',
['usjep_hmmwv_driver', 'usjep_hmmwv_cupolabase', 'usjep_hmmwv_codriver',
        'usjep_hmmwv_rear_passenger'],
['hmg_m2hb'],
'The High Mobility Multipurpose Wheeled Vehicle (HMMWV), better known as the Humvee, is a military \
4WD motor vehicle created by AM General. It has largely supplanted the roles formerly served by \
smaller Jeeps such as the M151 1/4-short-ton (230 kg) MUTT, the M561 "Gama Goat", their M718A1 and \
M792 ambulance versions, the CUCV, and other light trucks. Primarily used by the United States \
Armed Forces, it is also used by numerous other countries and organizations and even in civilian \
adaptations. The Hummer series was also inspired by the HMMWVs.',
0.14)

_add('uslcr_lcac', BOAT, SEA, 'LCRL', 'LCRL Boat',
[],
[],
'The LCRL or LCR (L) (Landing Craft Rubber Large) was an inflatable boat which could carry ten men \
that was used by the USMC and US Army from 1938 to 1945.',
0.0)

_add('usthe_uh60', HELICOPTER, AIR, 'UH-60', 'UH-60 Black Hawk',
['usthe_uh60_driver', 'usthe_uh60_left_gunner', 'usthe_uh60_right_gunner', 'usthe_uh60_copilot',
        'usthe_uh60_passenger2', 'usthe_uh60_passenger1'],
['hmg_m134_gun', 'usthe_uh60_flarelauncher'],
'The UH-60 Black Hawk is a four-bladed, twin-engine, medium-lift utility helicopter manufactured \
by Sikorsky Aircraft. Sikorsky submitted the S-70 design for the United States Army''s Utility \
Tactical Transport Aircraft System (UTTAS) competition in 1972. The Army designated the prototype \
as the YUH-60A and selected the Black Hawk as the winner of the program in 1976, after a fly-off \
competition with the Boeing Vertol YUH-61.',
21.3)

_add('ustnk_m1a2', ARMOR, LAND, 'M1A2', 'M1A2 Abrams',
['ustnk_m1a2_driver', 'ustnk_m1a2_cupolabase'],
['ustnk_m1a2_barrel', 'coaxial_browning', 'hmg_m2hb', 'ustnk_m1a2_smokelauncher'],
'The M1 Abrams is a third-generation main battle tank produced in the United States. It is named \
after General Creighton Abrams, former Army Chief of Staff and Commander of US military forces in \
Vietnam from 1968 to 1972. Highly mobile, designed for modern armored ground warfare,[9] the M1 is \
well armed and heavily armored. Notable features include the use of a powerful gas turbine engine \
(fueled with JP8 jet fuel), the adoption of sophisticated composite armor, and separate ammunition \
storage in a blow-out compartment for crew safety. Weighing nearly 68 short tons (almost 62 metric \
tons), it is one of the heaviest main battle tanks in service.',
8.58)

_add('wasp_defence', AIR_DEF, STATION, 'Wasp', 'Wasp Aircraft Carrier',
['wasp_defence_front', 'wasp_defence_back'],
[],
'USS Wasp (CV-7) was a United States Navy aircraft carrier. The eighth Navy ship of that name, she \
was the sole ship of her class. Built to use up the remaining tonnage allowed to the U.S. for \
aircraft carriers under the treaties of the time, she was built on a reduced-size version of the \
Yorktown-class hull.',
750.0)

_add('xp2_musclecar_01', TRANSPORT, LAND, 'Car', 'Muscle Car',
['xp2_musclecar_01_driver', 'xp2_musclecar_01_passenger'],
[],
'?',
0.02)

_add('xpak2_eurofighter', JET, AIR, 'Eurofighter', 'Eurofighter Typhoon',
['xpak2_eurofighter_driver'],
['eurofighter_autocannon', 'eurofighter_missiles', 'eurofighter_bomb_launcher'],
'?',
196.0)

_add('xpak2_faav', TRANSPORT, LAND, 'FAAV', 'Euro FAAV Jeep',
['xpak2_faav_driver', 'xpak2_faav_front_gun', 'xpak2_faav_rear_passenger'],
[],
'?',
0.0155)

_add('xpak2_hmmwv', TRANSPORT, LAND, 'HMMWV', 'Euro HMMWV',
['xpak2_hmmwv_driver', 'xpak2_hmmwv_codriver', 'xpak2_hmmwv_cupolabase'],
[],
'?',
0.14)

_add('xpak2_lav25', ARMOR, LAND, 'LAV-25', 'Euro LAV-25 APC',
['xpak2_lav25_driver', 'xpak2_lav25_rearpassenger_l', 'xpak2_lav25_rearpassenger_br'],
[],
'The LAV-25 is an eight-wheeled amphibious reconnaissance vehicle used by the United States Marine \
Corps. It was built by General Dynamics Land Systems Canada and is based on the Swiss MOWAG \
Piranha I 8x8 family of armored fighting vehicles.',
0.9)

_add('xpak2_semi', TRANSPORT, LAND, 'Truck', 'Semi-Truck',
['xpak2_semi_driver', 'xpak2_semi_passenger'],
[],
'?',
0.1)

_add('xpak2_tiger', HELICOPTER, AIR, 'EC665', 'Eurocopter EC665 Tiger',
['xpak2_tiger_driver', 'xpak2_tiger_gunner'],
['xpak2_tiger_missiles'],
'?',
89.7)

_add('xpak2_tnkl2a6', ARMOR, LAND, 'L2A6', 'L2A6 Leopard',
['xpak2_tnkl2a6_driver'],
[],
'?',
0.4)

_add('xpak2_tnkc2', ARMOR, LAND, 'C2', 'C2 Challenger',
['xpak2_tnkc2_driver', 'tnk_c2_gunner'],
['tnk_c2_barrel'],
'?',
0.5)
