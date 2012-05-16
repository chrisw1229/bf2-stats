
# Create a shared registry of all the vehicle types
registry = []

class Vehicle(object):

    def __init__(self, id, vehicle_type, name, desc):
        self.id = id
        self.vehicle_type = vehicle_type
        self.name = name
        self.desc = desc

def _add(id, vehicle_type, name, desc):
    registry.append(Vehicle(id, vehicle_type, name, desc))

_add('aav_tunguska', 'air_defense', 'Tunguska-M1',
'The Tunguska is a Russian tracked self-propelled anti-aircraft weapon armed with a surface-to-air \
gun and missile system. It is designed to provide day and night protection for infantry and tank \
regiments against low-flying aircraft, helicopters, and cruise missiles in all weather conditions.')

_add('aav_type95', 'air_defense', 'Type 95',
'The Type 95 is a Chinese self-propelled anti-aircraft vehicle. It is armed with four 25 \
millimeter cannons and optionally four fire-and-forget QW-2 infra-red homing missiles.')

_add('ahe_ah1z', 'helicopter', 'AH-1Z',
'The Bell AH-1Z Viper is a twin-engine attack helicopter based on the AH-1W SuperCobra, that was \
developed for the United States Marine Corps. The AH-1Z features a four-blade, bearingless, \
composite main rotor system, uprated transmission, and a new target sighting system.')

_add('ahe_havoc', 'helicopter', 'Mi-28',
'The Mil Mi-28 (NATO reporting name Havoc) is a Russian all-weather, day-night, military tandem, \
two-seat anti-armour attack helicopter. It is a dedicated attack helicopter with no intended \
secondary transport capability, better optimized than the Mil Mi-24 for the role. It carries a \
single gun in an undernose barbette, plus external loads carried on pylons beneath stub wings.')

_add('ahe_z10', 'helicopter', 'WZ-10',
'The WZ-10 is an attack helicopter developed by the People''s Republic of China. It is designed \
primarily for anti-tank missions, but is also believed to have a secondary air-to-air capability.')

_add('air_f35b', 'jet', 'F-35B',
'The Lockheed Martin F-35 Lightning II is a family of single-seat, single-engine, fifth generation \
multirole fighters under development to perform ground attack, reconnaissance, and air defense \
missions with stealth capability. The F-35B is the short takeoff and vertical landing (STOVL) \
variant of the aircraft. Similar in size to the A variant, the B sacrifices about a third of the \
other version''s fuel volume to make room for the vertical flight system. Takeoffs and landing \
with vertical flight systems are by far the riskiest, and in the end, a decisive factor in design.')

_add('air_j10', 'jet', 'J-10',
'The Chengdu J-10 is a multirole fighter aircraft designed and produced by the People''s Republic \
of China''s Chengdu Aircraft Industry Corporation (CAC) for the People''s Liberation Army Air \
Force (PLAAF). Known in the West as the "Vigorous Dragon", the J-10 is a multirole combat aircraft \
capable of all-weather operation.')

_add('air_su30mkk', 'jet', 'Su-30MKK',
'The Sukhoi Su-30MKK is a modification of the Su-27 SK manufactured since 1999 by KnAAPO and \
Shenyang Aircraft Corporation. It is considered an upgraded version of Sukhoi Su-30. It was \
jointly developed by Russia and China, similar to the Su-30MKI. It is a heavy class, all-weather, \
long-range strike fighter, comparable to American F-15E.')

_add('apc_btr90', 'armor', 'BTR-90',
'BTR-90 is an 8x8 wheeled armoured personnel carrier developed in Russia, designed in 1993 and \
first shown publicly in 1994. It is a larger version of the BTR-80 vehicle, fitted with a BMP-2 \
turret. Armour protection is improved compared with the BTR-80, giving protection from 14.5 mm \
projectiles over the frontal arc. It is armed with a 2A42 30 mm auto cannon, coaxial 7.62 mm PKT \
machine gun, AT-5 Spandrel ATGM, as well as a AGS-17 30 mm automatic grenade launcher.')

_add('apc_wz551', 'armor', 'WZ551',
'The WZ551 is a Chinese wheeled armored personnel carrier. It actually consists of two families of \
vehicles with official designations in the People''s Liberation Army as Type 90 and Type 92. \
Roughly 600 WZ551s are in service with the PLA, where they are used by light mechanized infantry.')

_add('ars_d30', 'artillery', 'D-30',
'The D-30, or 122-mm howitzer D-30, is a Soviet howitzer that first entered service in the 1960s. \
It is a robust piece that focuses on the essential features of a towed field gun suitable for all \
conditions. The D-30 has a maximum range of 15.4 kilometers, or over 21 km using RAP ammunition. \
With its striking three-leg mounting the D-30 can be rapidly traversed through 360 degrees.')

_add('ats_hj8', 'ground_defense', 'HJ-8',
'The HJ-8 or Hongjian-8 is a second generation tube-launched, optically tracked, wire-guided \
anti-tank missile system which was originally deployed by the People''s Liberation Army since the \
late 1980s. It is able to defeat explosive reactive armour (ERA).')

_add('ats_tow', 'ground_defense', 'BGM-71',
'The BGM-71 TOW is an anti-tank missile. BGM is a weapon classification that stands for Multiple \
Environment (B), Surface-Attack (G), Missile (M). TOW is an acronym that stands for Tube-launched, \
Optically-tracked, Wire command data link, guided missile. The TOW was first produced in 1970 and \
is one of the two most widely used anti-tank guided missiles by Western nations.')

_add('boat_rib', 'boat', 'RIB',
'A rigid-hulled inflatable boat, (RHIB) or rigid-inflatable boat (RIB) is a light-weight but \
high-performance and high-capacity boat constructed with a solid, shaped hull and flexible tubes \
at the gunwale. The design is stable and seaworthy. The inflatable collar allows the vessel to \
maintain buoyancy even if a large quantity of water is shipped aboard due to bad sea conditions.')

_add('chhmg_kord', 'ground_defense', '6P50',
'The Kord-12.7 mm heavy machine gun is a Russian design that entered service in 1998 replacing the \
older NSV machine gun. Externally the weapon resembles the NSV, however the internal mechanism has \
been extensively reworked, changing from a horizontally pivoting breech block to a rotating bolt \
design. Additionally the gas system has been changed and the muzzle baffle redesigned. These \
changes give the weapon reduced recoil compared with the NSV, allowing greater accuracy during \
sustained fire.')

_add('ch_bipod', 'ground_defense', '?', '?')

_add('chthe_z8', 'helicopter', 'Z-8',
'The Aerospatiale SA 321 Super Frelon is a three-engined heavy transport helicopter produced by \
Aerospatiale of France. The helicopter is still in use in China where the locally produced version \
is known as the Z-8.')

_add('hmg_m2hb', 'ground_defense', 'M2',
'The M2 Machine Gun, Browning .50 Caliber Machine Gun, is a heavy machine gun designed towards the \
end of World War I by John Browning. It is very similar in design to Browning''s earlier M1919 \
Browning machine gun, which was chambered for the .30-06 cartridge. The M2 uses the larger and \
more powerful .50 BMG cartridge, which was named for the gun itself (BMG standing for Browning \
Machine Gun). It is effective against infantry, unarmored or lightly armored vehicles and boats, \
light fortifications and low-flying aircraft.')

_add('igla_djigit', 'air_defense', '9K38',
'The 9K38 Igla is a Russian/Soviet man-portable infrared homing surface-to-air missile (SAM). The \
main improvements over the Igla-1 included much improved resistance against flares and jamming, a \
more sensitive seeker, expanding forward-hemisphere engagement capability to include \
straight-approaching fighters (all-aspect capability) under favourable circumstances, a slightly \
longer range, a higher-impulse, shorter-burning rocket with higher peak velocity (but \
approximately same time of flight to maximum range), and a propellant that performs as high \
explosive when detonated by the warhead''s secondary charge on impact.')

_add('jeep_faav', 'transport', '?', '?')

_add('jep_mec_paratrooper', 'transport', '?', '?')

_add('jep_nanjing', 'transport', '?', '?')

_add('jep_paratrooper', 'transport', '?', '?')

_add('jep_vodnik', 'transport', 'GAZ-3937',
'GAZ-3937 Vodnik is a Russian high-mobility multipurpose military vehicle manufactured by GAZ. It \
is amphibious, and is propelled by it''s wheels in the water. It has a a water-displacing hermetic \
hull which provides improved fording performance and a 4x4-type chassis with independent \
suspension and a centralized system of tire-pressure control. The standard undercarriage with a \
cab can be fitted with a number of different modules with various number of passenger seats and \
cargo compartments, seating up to 10 people. It is powered by a 175 hp (130 kW) diesel engine \
giving a top speed of 112 km/h (4 to 5 km/h when swimming).')

_add('mec_bipod', 'ground_defense', '?', '?')

_add('parachute', 'parachute', 'Parachute',
'A parachute is a device used to slow the motion of an object through an atmosphere by creating \
drag, or in the case of ram-air parachutes, aerodynamic lift. Parachutes are usually made out of \
light, strong cloth, originally silk, now most commonly nylon. Parachutes must slow an object''s \
terminal vertical speed by a minimum 75% in order to be classified as such. Depending on the \
situation, parachutes are used with a variety of loads, including people, food, equipment, space \
capsules, and bombs.')

_add('ruair_mig29', 'jet', 'MiG-29',
'The Mikoyan MiG-29 is a fourth-generation jet fighter aircraft designed in the Soviet Union for \
an air superiority role. Developed in the 1970s by the Mikoyan design bureau, it entered service \
with the Soviet Air Force in 1983, and remains in use by the Russian Air Force as well as in many \
other nations. The MiG-29, along with the Sukhoi Su-27, was developed to counter new American \
fighters such as the McDonnell Douglas F-15 Eagle, and the General Dynamics F-16 Fighting Falcon.')

_add('ruair_su34', 'jet', 'Su-34',
'The Sukhoi Su-34 is a Russian twin-seat fighter-bomber. It is intended to replace the Sukhoi \
Su-24. The aircraft shares most of its wing structure, tail, and engine nacelles with the \
Su-27/Su-30, with canards like the Su-30MKI/Su-33/Su-27M/35 to increase static instability (higher \
manoeuvrability) and to reduce trim drag. The aircraft has an entirely new nose and forward \
fuselage with a cockpit providing side-by-side seating for a crew of two. The Su-34 is powered by \
the AL-31FM1, the same engines as the Su-27SM, but its maximum speed is lower at Mach 1.8+.')

_add('rutnk_t90', 'armor', 'T-90',
'The T-90 is a Russian third-generation main battle tank that is a modernisation of the T-72 (it \
was originally to be called the T-72BU, later renamed to T-90). It is currently the most modern \
tank in service with the Russian Ground Forces and Naval Infantry. Although a development of the \
T-72, the T-90 uses a 125mm 2A46 smoothbore tank gun, 1G46 gunner sights, a new engine, and \
thermal sights. Standard protective measures include a blend of Steel, Composite armour, and \
Kontakt-5 explosive-reactive armor, laser warning receivers, Nakidka camouflage and the Shtora \
infrared ATGM jamming system.')

_add('the_mi17', 'helicopter', 'Mi-17',
'The Mil Mi-17 (also known as the Mi-8M series in Russian service) is a Russian helicopter \
currently in production at two factories in Kazan and Ulan-Ude. Mil Mi-8/17 is a medium \
twin-turbine transport helicopter that can also act as a gunship.')

_add('tnk_type98', 'armor', 'Type 98',
'The Type 99, also known as ZTZ-99 and WZ-123, developed from the Type 98G (in turn, a development \
of the Type 98), is a third generation main battle tank (MBT) fielded by the Chinese People''s \
Liberation Army. It is made to compete with other modern tanks. Although not expected to be \
acquired in large numbers due to its high cost compared to the more economical Type 96, it is \
currently the most advanced MBT fielded by China. The ZTZ99 MBT is a successor to the Type 98G \
tank manufactured for the People''s Liberation Army (PLA).')

_add('us_bipod', 'ground_defense', '?', '?')

_add('usaas_stinger', 'air_defense', 'FIM-92',
'The FIM-92 Stinger is a personal portable infrared homing surface-to-air missile (SAM), which can \
be adapted to fire from ground vehicles and helicopters (as an AAM), developed in the United \
States and entered into service in 1981. Used by the militaries of the U.S. and by 29 other \
countries, the basic Stinger missile has to-date been responsible for 270 confirmed aircraft \
kills. It is manufactured by Raytheon Missile Systems and under license by EADS in Germany, with \
70,000 missiles produced. It is classified as a Man-Portable Air-Defense System (MANPADS).')

_add('usaav_m6', 'air_defense', 'M6',
'The M6 Linebacker is an air defense variant of modified M2A2 ODSs with the TOW missile system \
replaced with a four-tube Stinger missile system. These are due to be retired from U.S. service.')

_add('usair_f18', 'jet', 'F/A-18',
'The McDonnell Douglas (now Boeing) F/A-18 Hornet is a twin-engine supersonic, all-weather \
carrier-capable multirole fighter jet, designed to dogfight and attack ground targets (F/A for \
Fighter/Attack). Designed by McDonnell Douglas and Northrop, the F/A-18 was derived from the \
latter''s YF-17 in the 1970s for use by the United States Navy and Marine Corps. The Hornet is \
also used by the air forces of several other nations. It has been the aerial demonstration \
aircraft for the U.S. Navy''s Flight Demonstration Squadron, the Blue Angels, since 1986.')

_add('usair_f15', 'jet', 'F-15',
'The McDonnell Douglas (now Boeing) F-15 Eagle is a twin-engine, all-weather tactical fighter \
designed by McDonnell Douglas to gain and maintain air superiority in aerial combat. It is \
considered among the most successful modern fighters, with over 100 aerial combat victories with \
no losses in dogfights.')

_add('usapc_lav25', 'armor', 'LAV-25',
'The LAV-25 is an eight-wheeled amphibious reconnaissance vehicle used by the United States Marine \
Corps. It was built by General Dynamics Land Systems Canada and is based on the Swiss MOWAG \
Piranha I 8x8 family of armored fighting vehicles.')

_add('usart_lw155', 'artillery', 'M777',
'The M777 howitzer is a towed 155 mm artillery piece, successor to the M198 howitzer in the United \
States Marine Corps and United States Army. The M777 is also used by the Canadian Army, and has \
been in action in Afghanistan since February 2006 along with the associated GPS-guided Excalibur \
ammunition.')

_add('usjep_hmmwv', 'transport', 'HMMWV',
'The High Mobility Multipurpose Wheeled Vehicle (HMMWV), better known as the Humvee, is a military \
4WD motor vehicle created by AM General. It has largely supplanted the roles formerly served by \
smaller Jeeps such as the M151 1/4-short-ton (230 kg) MUTT, the M561 "Gama Goat", their M718A1 and \
M792 ambulance versions, the CUCV, and other light trucks. Primarily used by the United States \
Armed Forces, it is also used by numerous other countries and organizations and even in civilian \
adaptations. The Hummer series was also inspired by the HMMWVs.')

_add('uslcr_lcac', 'boat', 'LCRL',
'The LCRL or LCR (L) (Landing Craft Rubber Large) was an inflatable boat which could carry ten men \
that was used by the USMC and US Army from 1938 to 1945.')

_add('usthe_uh60', 'helicopter', 'UH-60',
'The UH-60 Black Hawk is a four-bladed, twin-engine, medium-lift utility helicopter manufactured \
by Sikorsky Aircraft. Sikorsky submitted the S-70 design for the United States Army''s Utility \
Tactical Transport Aircraft System (UTTAS) competition in 1972. The Army designated the prototype \
as the YUH-60A and selected the Black Hawk as the winner of the program in 1976, after a fly-off \
competition with the Boeing Vertol YUH-61.')

_add('ustnk_m1a2', 'armor', 'M1A2',
'The M1 Abrams is a third-generation main battle tank produced in the United States. It is named \
after General Creighton Abrams, former Army Chief of Staff and Commander of US military forces in \
Vietnam from 1968 to 1972. Highly mobile, designed for modern armored ground warfare,[9] the M1 is \
well armed and heavily armored. Notable features include the use of a powerful gas turbine engine \
(fueled with JP8 jet fuel), the adoption of sophisticated composite armor, and separate ammunition \
storage in a blow-out compartment for crew safety. Weighing nearly 68 short tons (almost 62 metric \
tons), it is one of the heaviest main battle tanks in service.')

_add('wasp_defence_front', 'air_defense', 'CV-7',
'USS Wasp (CV-7) was a United States Navy aircraft carrier. The eighth Navy ship of that name, she \
was the sole ship of her class. Built to use up the remaining tonnage allowed to the U.S. for \
aircraft carriers under the treaties of the time, she was built on a reduced-size version of the \
Yorktown-class hull.')

_add('wasp_defence_back', 'air_defense', 'CV-7',
'USS Wasp (CV-7) was a United States Navy aircraft carrier. The eighth Navy ship of that name, she \
was the sole ship of her class. Built to use up the remaining tonnage allowed to the U.S. for \
aircraft carriers under the treaties of the time, she was built on a reduced-size version of the \
Yorktown-class hull.')
