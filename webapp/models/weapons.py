
# Create a shared registry of all the weapon types
registry = set()

# Weapon type constants
ASSAULT = 'assault_rifle'
CARBINE = 'carbine_rifle'
CANNON = 'cannon'
GRENADE = 'grenade'
HMG = 'heavy_machine_gun'
LMG = 'light_machine_gun'
MELEE = 'melee'
MINE = 'mine'
PISTOL = 'pistol'
ROCKET = 'rocket'
SHOTGUN = 'shotgun'
SNIPER = 'sniper_rifle'
SMG = 'sub_machine_gun'
TOOL = 'tool'

# Weapon group constants
SOLDIER = 'soldier'
VEHICLE = 'vehicle'

# Ammo type constants
PRECISION = 'precision'
EXPLOSIVE = 'explosive'

class Weapon(object):

    def __init__(self, id, weapon_type, group, ammo, make, model, name,
            game_desc, real_desc):
        self.id = id
        self.weapon_type = weapon_type
        self.group = group
        self.ammo = ammo
        self.make = make
        self.model = model
        self.name = name
        self.game_desc = game_desc
        self.real_desc = real_desc

        self.reset()

    def __repr__(self):
        return self.__dict__

    def reset(self):
        pass

EMPTY = Weapon('', '', '', '', '', '', '', '', '')

def _add(id, weapon_type, group, ammo, make, model, name, game_desc, real_desc):
    registry.add(Weapon(id, weapon_type, group, ammo, make, model, name,
            game_desc, real_desc))

_add('aas_seasparrow', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('aav_tunguska_gun', CANNON, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('aav_tunguska_sa19launcher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('aav_type95_qw2launcher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('aav_type95guns', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('ahe_ah1z_cogunner_hellfirelaunchertv', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('ahe_ah1z_gun', CANNON, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('ahe_ah1z_hydralauncher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('ahe_havoc_gun', CANNON, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('ahe_havoc_atakalauncher_tv', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('ahe_havoc_s8launcher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('ahe_z10_gun', CANNON, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('ahe_z10_hj8launcher_tv', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('air_a10_us_bomblauncher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('ahe_z10_s8launcher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('air_f35b_sidewinderlauncher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('air_j10_cannon', CANNON, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('air_j10_archerlauncher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('air_su30mkk_30mmcannon', CANNON, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('air_su30mkk_archerlauncher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('air_su30mkk_kedgelauncher_laser', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('air_su39_canon', CANNON, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('ammokit', TOOL, SOLDIER, PRECISION,
'', '', 'Ammunition Bag',
'In Battlefield 2, ammunition is dispensed either by the Ammo Bags from Support Class or Supply \
Crate deployed by the Commander. The Ammo Bags can be held to replenish the player''s own ammo or \
those of others and they can be dropped as well. The Supply Crates are typically requested by \
Squad leaders and supply ammo to any player within range of the crate.',
'')

_add('apc_btr90__barrel', CANNON, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('apc_btr90_hj8launcher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('apc_wz551_barrel', CANNON, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('apc_wz551_hj8launcher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('ars_d30_barrel', CANNON, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('at_mine', MINE, SOLDIER, EXPLOSIVE,
'', 'M15', 'Anti-Tank Mine',
'The Anti-Tank Mine is issued to the Engineer Kit in Battlefield 2. Like Mines from its \
predecessors, the Anti-Tank Mine is very effective against vehicles, especially armored ones. It \
is a pressure mine, meaning that in order for it to detonate, a vehicle must drive over the mine. \
A single mine can destroy any vehicle on land. However, enemy Engineers can use the wrench to \
disarm the mine and use it against your team. Like Anti-Personnel Mines used by the Sniper kit, it \
should be placed in areas where drivers won''t expect it. However, since the Engineer kit will \
have 5 of these mines ready to be used, it can be placed in open areas. The Anti-Tank Mine in \
Battlefield 2 is modeled off the American-made M15 mine.',
'Anti-tank or AT mines are similar too AP (anti-personal) mines but they require more pressure to \
detonate, i.e. the weight of a vehicle. AT mines have used shaped charges to cut through armour \
since world war 2. They achieve either a mobility kill by disabling a tanks tracks e.t.c. or a \
catastrophic kill that disables vehicle and crew. The fact they have a higher trigger pressure \
means they are prevented from being set off by infantry. AT mines are very good for preventing \
enemy vehicles approaching certain areas but they do not discriminate and can be set off by your \
own sides vehicles as well.')

_add('ats_hj8_launcher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('ats_tow_launcher', ROCKET, VEHICLE, EXPLOSIVE,
'', 'BGM-71', 'BGM-71 TOW',
'',
'The BGM-71 TOW is an anti-tank missile. BGM is a weapon classification that stands for Multiple \
Environment (B), Surface-Attack (G), Missile (M). TOW is an acronym that stands for Tube-launched, \
Optically-tracked, Wire command data link, guided missile. The TOW was first produced in 1970 and \
is one of the two most widely used anti-tank guided missiles by Western nations.')

_add('c4_explosives', MINE, SOLDIER, EXPLOSIVE,
'', 'C-4', '',
'In Battlefield 2, C4 is issued to the Special Forces Kit. It is most commonly used to destroy \
enemy armored vehicles, as well as enemy installations such as Artillery and UAV Trailers.',
'C4 or composition 4 is a variety of plastic explosive used by the military for demolition or as \
an AP (anti-personal) device. It is an explosive compound mixed with a plastic binder that makes \
the explosive more manageable and stable meaning a detonator and blasting cap are required to set \
off a two phase blast. Military issue M112 blocks of C4 weighing in at 1.25 pounds can easily \
demolish a truck but with the gases expanding at about 8050 m/s, you must be clear of the blast \
radius as you cannot outrun the explosion.')

_add('chat_eryx', ROCKET, SOLDIER, EXPLOSIVE,
'MBDA', 'ERYX', '',
'The ERYX is issued as the default anti-tank weapon for the MEC and PLA Anti-Tank kits. The ERYX \
is very effective against heavy vehicles, as well as light vehicles. When firing at a stationary \
target zoom in and line up the target and fire. Keep in mind that it is still guidable if the \
target moves. Hold down the fire button after firing to keep the view zoomed in for better \
accuracy. As with all launchers, aim for the vulnerable areas of tanks, and other enemy armored \
vehicles.',
'The Eryx is a short-range anti-armour system that entered service in 1994 and is produced by MBDA \
of France and by Aerospatiale of Canada. This weapon can destroy static and moving tanks including \
those fitted with ERA (explosive reactive armour) from ranges of 50 m to 600 m. The system \
consists of a missile and a launch tube and can be fired from the shoulder or from a prone \
position using a tripod. The missile is wire-guided, optically tracked with SACLOS guidance \
(semi-automatic command to line-of-sight) and can be fired on all terrains including confined \
spaces due to the thrust vector control. The Eryx can be armed and ready within 5 seconds and is \
capable of firing 5 missiles in 2 minutes. With the misile being armed with a 137 mm tandem, \
shaped charge high explosive warhead it is capable of penetrating 900 mm of ERA. All in all a very \
effective anti-armour weapon that will also easily destroy other types of vehicles and even \
concrete bunkers.')

_add('chhmg_kord', HMG, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('chhmg_type85', HMG, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('chlmg_type95', LMG, SOLDIER, PRECISION,
'Norinco', 'QBB-95', 'Type 95',
'In Battlefield 2, the Type 95 is the light machine gun issued to the People''s Liberation Army \
Support Kit. When prone, the machine gun has medium accuracy over distance (which rapidly \
deteriorates with extended automatic fire), and delivers decent damage. It carries a hundred-round \
magazine and has a short reload period when compared to the other weapons in its class. It can \
also be found mounted in some maps, with infinite ammo and high accuracy. However, the mounted \
version has no ironsights , and is prone to overheating.',
'The Type 95 or QBZ-95 is available in three versions and an export version assault rifle, the \
QBZ-97. There is a standard 5.8 mm assault rifle, a shortened variant carbine and the squad \
machine gun. The type 95 machine gun uses ammunition specifically designed by the Chinese in the \
late 80s, a 5.8 mm shell that is fed from a 75 round drum. The weapon is constructed partly of \
polymer and with a range of 600 m this is a very effective lightweight mid to long range weapon \
that is best used from prone with its bipod and sights.')

_add('chlmg_type95_stationary', LMG, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('chpis_qsz92', PISTOL, SOLDIER, PRECISION,
'Norinco', 'QSZ-92', 'Type 92',
'The 92FS is the USMC''s and European Union''s standard sidearm in the game. Its stopping power \
and accuracy are similar to that of other handguns in the game. However, it is widely considered \
that the M9 has the most user friendly iron sights in the game. Its magazine capacity is 15 \
rounds, identical to that of the MEC''s MR-444 and Chinese QSZ-92. There is also a suppressed \
version but is only issued to the Special Ops Kit and Sniper Kit.',
'The QSZ-92 (Qin-Shang Zu, meaning pistol system) was developed for use with Chinese forces in the \
late 90''s and has been in active service with the PLA and Chinese police force. Two models of \
this weapon are available, one that chambers DAP-92 9 mmammo (armour piercing) and one that \
chambers 5.8 mm ammo. The QSZ has a frame made from polymer and has a double action trigger \
mechanism and ambidextrous safety lever. It is fitted with a fixed sight with luminous inserts for \
low light but has rails under the barrel for the addition of a laser sight or flashlight. This \
weapon had an effective range of 50 m and has a magazine capacity of 15 rounds of either type of \
ammunition.')

_add('chpis_qsz92_silencer', PISTOL, SOLDIER, PRECISION,
'Norinco', 'QSZ-92', 'Type 92 Silencer',
'The 92FS is the USMC''s and European Union''s standard sidearm in the game. Its stopping power \
and accuracy are similar to that of other handguns in the game. However, it is widely considered \
that the M9 has the most user friendly iron sights in the game. Its magazine capacity is 15 \
rounds, identical to that of the MEC''s MR-444 and Chinese QSZ-92. There is also a suppressed \
version but is only issued to the Special Ops Kit and Sniper Kit. This version includes a silencer \
for increased stealth.',
'The QSZ-92 (Qin-Shang Zu, meaning pistol system) was developed for use with Chinese forces in the \
late 90''s and has been in active service with the PLA and Chinese police force. Two models of \
this weapon are available, one that chambers DAP-92 9 mmammo (armour piercing) and one that \
chambers 5.8 mm ammo. The QSZ has a frame made from polymer and has a double action trigger \
mechanism and ambidextrous safety lever. It is fitted with a fixed sight with luminous inserts for \
low light but has rails under the barrel for the addition of a laser sight or flashlight. This \
weapon had an effective range of 50 m and has a magazine capacity of 15 rounds of either type of \
ammunition.')

_add('chrif_type85', SMG, SOLDIER, PRECISION,
'Norinco', '', 'Type 85',
'In Battlefield 2, the Type 85 is used by the PLA Anti-Tank Kit. The Type 85 has low accuracy, \
even when sighted, it also delivers only moderate damage. However, it has a high rate of fire \
(like the other sub machineguns), and has the fastest reload rate of the submachineguns.',
'The Type 85 silenced sub-machine gun made by Norinco is mainly an export weapon that is a simpler \
and lighter version of the Type 64 sub-machine gun. The Type 85 uses a 7.62 x 25 mm Type 64 \
silenced cartridge but can also chamber a Type 51 pistol cartridge although the latter makes a lot \
more noise. This weapon has an effective range of 200 m and uses a blow-back, selective fire \
action and is fed by a 30 round box magazine. The Type 85 is an ideal close quarter combat weapon \
but not so ideal at medium and longer ranges.')

_add('chrif_type95', CARBINE, SOLDIER, PRECISION,
'Norinco', 'QBZ-97B', 'Type 97',
'In Battlefield 2, the QBZ-97 is the standard primary weapon of the Spec Ops Kit for the PLA. It \
is the most accurate of the basic level carbines, and when prone is more accurate than the G36C. \
The iron sights are similar to that of the G36C''s or G3''s though, as it has an open/aperature \
sight with the focus created from the front post just like the G36C and the G3.',
'The QBZ-97 is a Chinese export version of the rarely seen QBZ-95 and it first appeared outside of \
the PLA in 1997. Both weapons are internally the same but the 97 was designed to use Nato 5.56 x \
45 ammunition. It is a gas operated, rotating bolt action, magazine fed semi/automatic weapon \
capable of 650 rpm. Featuring the same design as the 95 and other Bullpup rifles means this weapon \
cannot be shouldered on the left as spent casings are ejected from the right side. The design also \
prevents using the weapon effectively whilst prone due to the placing of the sights leaving your \
head exposed. The QBZ is a very accurate weapon made from modern materials meaning it is also very \
lightweight.')

_add('chsht_norinco982', SHOTGUN, SOLDIER, PRECISION, 'Norinco', 'N982', '',
'The NOR982 is a 12-gauge, pump-action combat shotgun issued to the PLA Engineer kit. Like the \
other pump-action shotguns, it is capable of achieving one-hit kills at medium-close distances, \
and inflicting decent damage beyond there. It has a low rate of fire and a slow reload rate.',
'The Norinco 982 was first manafactured in China by the Norinco arms company and it was aimed at \
the global arms market for law enforcement purposes. The Norinco is a 12 gauge pump action shotgun \
that has a 5 + 1 shell capacity and features ghost ring sights and a black matte finish. The \
Norinco is an effective close range weapon and is currently the standard armament of the PLA \
infantry. With the time it takes to reload and the large scatter pattern the Norinco is of little \
use at medium-long ranges.')

_add('chsht_protecta', SHOTGUN, SOLDIER, PRECISION,
'Hilton Walker', 'DAO-12', 'Armsel Striker',
'In Battlefield 2, the DAO-12 is the Tier One unlock for the Anti-Tank Kit. Unlike most unlocks, \
it is a completely different type of weapon from the defaults; the DAO-12 is a Semi-Automatic, 12 \
gauge shotgun whereas the Anti-Tank soldier would normally get a Sub-Machine Gun such as the MP5 \
or PP-19. This means that it is more powerful than the default weapon, but it has a significantly \
shorter effective range.',
'The Armsel Striker, or DAO-12, is a South African revolver-like shotgun designed by Hilton Walker \
of the Sentinel Arms Company, originally stationed in Rhodesia (now Zimbabwe). With the original \
design having flaws, Walker redesigned the weapon in the 1980s, resulting in the Protecta model \
that has found its way around the world today. This weapon has earned itself the nickname of \
"Street Sweeper" for it''s large shell capacity and high effective fire rate.')

_add('chsni_type88', SNIPER, SOLDIER, PRECISION,
'Norinco', 'QBU-88', 'Type 88',
'In Battlefield 2, the Type 88 is the standard Sniper Rifle for the PLA in the game. It''s better \
than its MEC counterpart, the SVD, despite having lower damage, as it has higher accuracy and a \
more user-friendly scope view. A Type 88 will kill unarmored infantry in 3 hits, while an armored \
soldier may take up to 4 hits at times. A headshot will provide an instantaneous kill.',
'The Type 88 marksmen rifle or QBU-88 is a gas operated, semi-automatic rifle that was intended to \
fire semi-automatic at greater distances than other assault rifles rather than as soley a sniper \
rifle. Currently used by the PLA and Chinese police forces it features iron sights but can be \
equiped with a 4x telescopic or night sight. The Type 88 was made for heavy loading of a 5.8 x 42 \
mm cartridge but can also fire standard 5.8 mm ammunition. This is a very effective rifle up to a \
distance of around 800 m and with 10 rounds and semi-auto fire it allows you that extra chance of \
finishing the enemy off.')

_add('coaxial_browning', HMG, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('coaxial_mg_china', HMG, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('coaxial_mg_mec', HMG, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('defibrillator', TOOL, SOLDIER, PRECISION,
'', '', 'Defibrillator',
'The Defibrillator, or "Shock Paddles", is an item in the Medic Kit. It can revive any critically \
wounded ally to full health. A heartbeat icon is used to represent downed allies. The \
defribrillator can also be used on enemy players, instantly killing them, much like knives. The \
defibrillator functions like a bullet weapon: the "weapon''s" crosshairs must be on a target in \
range. It does not matter what part of the body is targeted, so long as it belongs to a critically \
wounded ally or healthy enemy. Because a player''s body parts may sometimes clip through walls, \
targeting them can allow the player to revive or kill them.',
'Defibrillation is a common treatment for life-threatening cardiac dysrhythmias, ventricular \
fibrillation, and pulseless ventricular tachycardia. Defibrillation consists of delivering a \
therapeutic dose of electrical energy to the affected heart with a device called a defibrillator. \
This depolarizes a critical mass of the heart muscle, terminates the dysrhythmia, and allows \
normal sinus rhythm to be reestablished by the body''s natural pacemaker, in the sinoatrial node \
of the heart. Defibrillators can be external, transvenous, or implanted, depending on the type of \
device used or needed. Some external units, known as automated external defibrillators (AEDs), \
automate the diagnosis of treatable rhythms, meaning that lay responders or bystanders are able to \
use them successfully with little, or in some cases no training at all.')

_add('eurif_famas', ASSAULT, SOLDIER, PRECISION,
'', '', '',
'',
'')

_add('eurif_fnp90', SMG, SOLDIER, PRECISION,
'', '', '',
'',
'')

_add('eurif_hk21', LMG, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('eurif_hk53a3', CARBINE, SOLDIER, PRECISION,
'', '', '',
'',
'')

_add('eurofighter_missiles', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('f18_autocannon', CANNON, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('f18_sidewinderlauncher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('firingport_ak', LMG, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('firingport_m16', LMG, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('gbgr_sa80a2_l85', GRENADE, SOLDIER, EXPLOSIVE,
'', '', '',
'',
'')

_add('gbrif_l96a1', SNIPER, SOLDIER, PRECISION,
'', '', '',
'',
'')

_add('gbrif_benelli_m4', SHOTGUN, SOLDIER, PRECISION,
'', '', '',
'',
'')

_add('gbrif_hk21', LMG, SOLDIER, PRECISION,
'', '', '',
'',
'')

_add('gbrif_sa80a2_l85', ASSAULT, SOLDIER, PRECISION,
'', '', '',
'',
'')

_add('hgr_smoke', GRENADE, SOLDIER, EXPLOSIVE,
'', '', 'Smoke Grenade',
'The Smoke Grenade is included in the Assault kit in the game Battlefield 2. Instead of having a \
spherical shape like the frag grenade, it has a cylindrical shape (sort of looks like a tiny can). \
It is thrown like a frag grenade (default Left-Mouse-Button for normal throw, default \
Right-Mouse-Button for a controlled distance throw), but instead releases smoke. The smoke grenade \
has many uses.',
'')

_add('hmg_m134_gun', HMG, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('hmg_m2hb', HMG, VEHICLE, PRECISION,
'Browning', 'M2', 'Browning M2',
'',
'The M2 Machine Gun, Browning .50 Caliber Machine Gun, is a heavy machine gun designed towards the \
end of World War I by John Browning. It is very similar in design to Browning''s earlier M1919 \
Browning machine gun, which was chambered for the .30-06 cartridge. The M2 uses the larger and \
more powerful .50 BMG cartridge, which was named for the gun itself (BMG standing for Browning \
Machine Gun). It is effective against infantry, unarmored or lightly armored vehicles and boats, \
light fortifications and low-flying aircraft.')

_add('igla_djigit_launcher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('kni_knife', MELEE, SOLDIER, PRECISION,
'', '', 'Combat Knife',
'In Battlefield 2, the Knife is issued to every kit, and can kill in a single hit. Unlike previous \
games, the combat knife''s skin does not change between factions: there is a single game file \
related to the knife, which is used for all soldiers, rather than multiple for each faction.',
'Most modern combat knives are approximately 7 inch in length and made of carbon steel with an \
epoxy coating to protect the knife and prevent light reflection. The knife is a hand to hand \
combat weapon that can prove vital when out of ammunition or when silence is necessary.')

_add('medikit', TOOL, SOLDIER, PRECISION,
'', '', 'Medical Bag',
'In Battlefield 2, the Medic Bag issued to the Medic kit. It takes the form of a bag with medical \
supplies inside and strapped tight. It gradually heals player for a short period of time or can be \
thrown on the ground to instantly heal players to full health. The Medkits are also very useful as \
bait for enemy infantry. The player can use one to lure an enemy toward a booby trap (e.g. a \
Claymore anti-personnel mine).',
'')

_add('ruair_archerlauncher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('ruair_mig29_30mmcannon', CANNON, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('ruair_su34_250kgbomblauncher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('ruair_su34_30mmcannon', CANNON, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('ruair_su34_archerlauncher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('rulmg_pkm', LMG, SOLDIER, PRECISION,
'Kalashnikov', 'PKM', '',
'In Battlefield 2, the PKM is the Tier One unlock for the Support Kit in Battlefield 2. It is both \
more powerful and more accurate than the other support weapons, and is one of the two weapons most \
commonly employed in "Dolphin diving" (the other being the M95).',
'The PKM is a Soviet general purpose machine gun variant of the PK machine gun, designed by \
Mikhail Kalashnikov in the early 1960s. It was put into service with the Soviet armed forces and \
currently in production in Russia. It fires 7.62x54mmR rounds at a rate of fire of around 750 \
rounds per minute up to an effective range of 1500 meters (1640 yards).')

_add('rulmg_rpk74', LMG, SOLDIER, PRECISION,
'Kalashnikov', 'RPK-74', '',
'The RPK-74 appears in Battlefield 2 as the main weapon for the MEC''s Support Kit. Compared to \
the PLA''s QBB-95 and USMC''s M249 SAW, it has lower accuracy than the two, as the sights are \
somewhat hard to use at long range. It''s rate of fire is also slower than the two, so in close \
quarters, RPK-74 users might be at a disadvantage. However, the RPK-74 boasts higher stopping \
power than the two.',
'The RPK-74 was introduced in the late 70''s and quickly became the standard squad machine gun for \
the Russians replacing both the RPK and the PKM. It uses a gas-actuated rotating bolt fire action \
and can fire 600 rounds per minute although realisticly this is more like 150 rpm. This weapon is \
fed from 45 round box magazines using 5.45 x 39 mm calibre ammo and has an effective range of \
around 460 m. The RPK is not to be used without its bipod and should be fired prone in short \
bursts to avoid overheating, at which point you have to wait for it to cool down.')

_add('rulmg_rpk74_stationary', LMG, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('rupis_baghira', PISTOL, SOLDIER, PRECISION,
'Izhevsk Mechanical Plant', 'MR-444', 'Baghira',
'In Battlefield 2, the MR-444 is the standard sidearm of the Middle Eastern Coalition, and comes \
both with and without a suppressor (The former available only to the Special Forces and Sniper \
kits). It can kill in about five rounds, has a 15-round magazine, a low firecap, and decent \
accuracy at close to medium range.',
'The Baghira is a modern pistol designed in Russia at the Izhevsk Mechanical plant and it was \
built to replace the Makarov pistols. The frame is thermosetting plastic and the mechanical parts \
are constructed of steel so it is lightweight. This 9 mm calibre handgun can be fitted with 3 \
different chambers and uses a detachable, box-type, double-column magazine. The baghira, as with \
most pistols, is a useful close combat weapon that makes the difference when out of ammunition.')

_add('rupis_baghira_silencer', PISTOL, SOLDIER, PRECISION,
'Izhevsk Mechanical Plant', 'MR-444', 'Baghira Silencer',
'In Battlefield 2, the MR-444 is the standard sidearm of the Middle Eastern Coalition, and comes \
both with and without a suppressor (The former available only to the Special Forces and Sniper \
kits). It can kill in about five rounds, has a 15-round magazine, a low firecap, and decent \
accuracy at close to medium range. This version includes a silencer for increased stealth.',
'The Baghira is a modern pistol designed in Russia at the Izhevsk Mechanical plant and it was \
built to replace the Makarov pistols. The frame is thermosetting plastic and the mechanical parts \
are constructed of steel so it is lightweight. This 9 mm calibre handgun can be fitted with 3 \
different chambers and uses a detachable, box-type, double-column magazine. The baghira, as with \
most pistols, is a useful close combat weapon that makes the difference when out of ammunition.')

_add('rurgl_gp25', GRENADE, SOLDIER, EXPLOSIVE,
'KBP Instrument Design Bureau', 'GP-25', 'Bonfire',
'In Battlefield 2, the GP-25 is attached to the AK-47, issued uniquely to the PLA Assault kit. It \
replaces the standard hand grenades available with the PLA Medic''s AK-47.',
'The GP-25 "Kostyor" is an under-barrel grenade launcher designed in the Soviet Union by KBP \
Instrument Design Bureau in 1978. It was an upgraded version of the BG-15, which was initially \
designed to fit the AK-47. It has been made compatible to fit with many Kalashnikov-style rifles. \
It uses a 40mm caseless grenade and can be shot at an effective range of 400 meters at a muzzle \
velocity of around 76.5 meters per second. A new modern version of the GP-25 is the GP-30, which \
is attached to more modern Kalashnikov firearms such as the AK-101.')

_add('rurgl_gp30', GRENADE, SOLDIER, EXPLOSIVE,
'KBP Instrument Design Bureau', 'GP-30', 'Shoe',
'The GP-30 appears in Battlefield 2 attached to the AK-101 assault rifle used by the MEC. It is \
nearly identical to the GP-25 as their only difference is their sighting system.',
'The GP-30 Obuvka ("Shoe"), is a Russian Under-Barrel Grenade Launchers for the AK and AN series \
of Assault Rifles. The main production version, the GP-25 has a different sighting system. The \
latest version the GP-30 is an evolved version of the GP-25, being lighter, easier to make, and \
easier to use.')

_add('rurif_ak47', ASSAULT, SOLDIER, PRECISION,
'Kalashnikov', 'AK-47', '',
'In Battlefield 2, the AK-47 is the standard primary weapon for the PLA''s Assault and Medic kits. \
Like the other factions, the PLA''s AK-47 is equipped with several extra magazines and an \
underslung GP-25, whereas the Medic''s AK-47 has considerably less ammunition and no underslung \
attachment. It has one of the highest damage ratings of the assault rifles, just slightly less \
than the G3 at 38 points of damage per round, but has a low rate of fire and moderate recoil and \
spread. The AK-47 can also be set to either full-auto or semi-auto.',
'The AK-47 is a Soviet assault rifle designed by Mikhail Kalashnikov in 1947. It is known as the \
most used and most produced firearm in the world, with an approximated 75,000,000 AK-47s produced, \
and a total of around 100,000,000 AK-types produced. It was often copied, or modified into unique \
weapons such as the Chinese Type 56, the Israeli Galil, AKM, RPK and a more modern AK-74. It was \
first put into service with the Soviet Armed Forces and other nations of the Warsaw Pact, and is \
still in service with many countries today, such as Vietnam, North Korea, Iraq, and many African \
countries. It became an icon, not just used widely by some paramilitary and guerilla forces, but \
also an Cultural effect have made it popular in some action television programs, films/movies, \
printed media, and video games. The AK-47 fires the 7.62x39mm M43 cartridge from a typically \
30-round magazine at a rate of fire of approximately 600 rounds per minute, up to an effective \
range of 350-400 meters.')

_add('rurif_ak74u', CARBINE, SOLDIER, PRECISION,
'Kalashnikov', 'AKS-74U', '',
'The AK-74U in Battlefield 2 is the standard primary weapon for the Spec Ops Kit on the MEC team. \
It comes with a Kobra Red Dot Sight and sports desert camouflage. It has the highest stopping \
power of all the standard Spec Ops Kit weapons; compared to its American counterpart, the M4A1 \
Carbine, it does more damage at the cost of lower accuracy and sight magnification.',
'Designed by the Russian Kalashnikov, the AK-74U assault rifle is an accurate and deadly weapon \
from short to long ranges, up to around 500 m. It has a curved magazine like the AK-47 and a \
magazine capacity of 30 rounds which can be fired in full-auto, and semi-auto modes. This weapon \
features a folding stock and is fitted with a red-dot scope which when zoomed proves to be very \
effective.')

_add('rurif_ak101', ASSAULT, SOLDIER, PRECISION,
'Kalashnikov', 'AK-101', '',
'In Battlefield 2, the AK-101 is utilized by the MEC as their service rifle for both the Assault \
and Medic kits. The former''s version of the rifle features and underslung GP-30 grenade launcher, \
whereas the latter is not equipped with any attachments. The two operate in exactly the same \
manner otherwise. The AK-101 is a relatively high-damage assault rifle, third after the G3 (with \
40 points of damage) and the AK-47 (with 38 points of damage) at 37 points of damage per round. \
The AK-101 features a 30-round magazine and the same spread and recoil figures as the AK-47, as \
well as the same rate of fire, but has a slightly longer reload animation.',
'The AK-101 was designed in Russia by Mikhail Kalashnikov for the Nato market and uses standard \
Nato 5.56 x 45 mm calibre cartridges. This rifle features three firing modes, semi, 3 shot bursts, \
and full auto and can fire 600 rpm. Used primarily for army forces the AK is a reliable weapon \
that uses modern materials and features a folding plastic stock, and a side mounting plate for \
optical attachments. This weapon is a good all rounder and will take out enemies close, medium, \
and at far range, when in the right mode but it will rapidly deplete it''s ammo in full auto and \
so this has to be watched. ')

_add('rurif_bizon', SMG, SOLDIER, PRECISION,
'Izhmash', 'PP-19', 'Bizon',
'In Battlefield 2, the PP-19 is issued to the MEC Anti-Tank Kit. It is very similar to the MP5, \
with the exception of the additional 15 rounds to each magazine. This gives the PP-19 a slight \
advantage over the other submachine guns.',
'Another weapon designed at the Izhevsk Mechanical plant (Izhmash), the PP-19 is a sub-machine gun \
developed in the early nineties for use by Russian security and law enforcement for close quarter \
combat. It uses a blowback firing operation and the ammo is fed from a mostly plastic helical \
magazine in semi-auto or full-auto fire. It features a folding stock made of stamped steel and can \
be shouldered or handheld. With its 45 rounds this weapon can be a good short range weapon but at \
100 m or more it may be a better idea to use a pistol.')

_add('rurif_dragunov', SNIPER, SOLDIER, PRECISION,
'Izhmash', 'SVD', 'Dragunov',
'In Battlefield 2, the SVD is the default primary weapon for the MEC Sniper kit. When compared \
with the USMC M24, The SVD has less power and accuracy, as well as less magnification. However, \
the SVD is semi-automatic, giving it a faster fire rate. It takes a minimum of two rounds to kill, \
provided one is a headshot, and a potential maximum of three rounds.',
'The SVD Dragunov is so called after its Russian maker Evgeniy Fedorovich Dragunov, it was \
designed by him between 1958 and 1963. It is common amongst Eastern Bloc countries and was the \
first purpose-built precision marksmens rifle. Due to the rifles reliability and accuracy this \
weapon is still in use with Soviet agencies today. It is a gas operated semi-automatic rifle using \
7.62 x 54R mm calibre ammo and has a range with the scope of over 1200 m although it was intended \
to be accurate at more like 600 m. The Dragunov is ideal and was designed for giving infantry a \
larger operating distance.')

_add('rurif_gp25', ASSAULT, SOLDIER, PRECISION,
'KBP Instrument Design Bureau', 'GP-25', 'Bonfire',
'In Battlefield 2, the GP-25 is attached to the AK-47, issued uniquely to the PLA Assault kit. It \
replaces the standard hand grenades available with the PLA Medic''s AK-47.',
'The GP-25 "Kostyor" is an under-barrel grenade launcher designed in the Soviet Union by KBP \
Instrument Design Bureau in 1978. It was an upgraded version of the BG-15, which was initially \
designed to fit the AK-47. It has been made compatible to fit with many Kalashnikov-style rifles. \
It uses a 40mm caseless grenade and can be shot at an effective range of 400 meters at a muzzle \
velocity of around 76.5 meters per second. A new modern version of the GP-25 is the GP-30, which \
is attached to more modern Kalashnikov firearms such as the AK-101.')

_add('rurif_gp30', ASSAULT, SOLDIER, PRECISION,
'KBP Instrument Design Bureau', 'GP-30', 'Shoe',
'The GP-30 appears in Battlefield 2 attached to the AK-101 assault rifle used by the MEC. It is \
nearly identical to the GP-25 as their only difference is their sighting system.',
'The GP-30 Obuvka ("Shoe"), is a Russian Under-Barrel Grenade Launchers for the AK and AN series \
of Assault Rifles. The main production version, the GP-25 has a different sighting system. The \
latest version the GP-30 is an evolved version of the GP-25, being lighter, easier to make, and \
easier to use.')

_add('rurrif_ak74u', CARBINE, SOLDIER, PRECISION,
'Kalashnikov', 'AKS-74U', '',
'The AK-74U in Battlefield 2 is the standard primary weapon for the Spec Ops Kit on the MEC team. \
It comes with a Kobra Red Dot Sight and sports desert camouflage. It has the highest stopping \
power of all the standard Spec Ops Kit weapons; compared to its American counterpart, the M4A1 \
Carbine, it does more damage at the cost of lower accuracy and sight magnification.',
'Designed by the Russian Kalashnikov, the AK-74U assault rifle is an accurate and deadly weapon \
from short to long ranges, up to around 500 m. It has a curved magazine like the AK-47 and a \
magazine capacity of 30 rounds which can be fired in full-auto, and semi-auto modes. This weapon \
features a folding stock and is fitted with a red-dot scope which when zoomed proves to be very \
effective.')

_add('rusht_saiga12', SHOTGUN, SOLDIER, PRECISION,
'Izhmash', 'S12K', 'Saiga-12',
'In Battlefield 2, the S12K is the default weapon for the Engineer kit for the MEC team. It is the \
first semi-automatic shotgun players will most likely get at their disposal. The weapon is \
potentially more forgiving than the pump-action USMC and PLA shotguns; it is usually not capable \
of a one-hit kill, but its magazine-feeding mechanism and its semi-automatic firemode allows one \
to follow up the first round much faster than with a pump-action shotgun. It is very similar to \
the Engineer class Tier one unlock weapon, the MK3A1 Jackhammer, as both have the same magazine \
capacity, fire rate, and range, although the MK3A1 boasts a higher damage output per pellet at \
close range.',
'The S12K or Saiga-12 semi-automatic shotgun is manafactured and produced by Izhmash primarily for \
Russian law enforcement and security units. The design was based loosely around the AK-47 but this \
weapon has only one firing mode. The S12K uses smaller shell sizes than conventional pump-action \
shotguns and therefore it causes less damage although it is ready to fire again more quickly. As \
with all shotguns it will kill point blank but has bad recoil and added to that you can quickly \
and ineffectively use up all your ammo, it can be wise to switch to a pistol.')

_add('rutnk_t90_barrel', CANNON, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('she_ec635_cannons', CANNON, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('she_littlebird_miniguns', CANNON, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('tnk_c2_barrel', CANNON, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('tnk_type98_barrel', CANNON, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('usaas_stinger_launcher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('usaav_m6_barrel', CANNON, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('usaav_m6_stinger_launcher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('usair_f15_autocannon', CANNON, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('usair_f15_mavericklauncherlaser', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('usair_f15_250kgbomblauncher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('usair_f15_sidewinderlauncher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('usapc_lav25_barrel', CANNON, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('usapc_lav25_towlauncher', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('usart_lw155_barrel', CANNON, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('usatp_predator', ROCKET, SOLDIER, EXPLOSIVE,
'Lockheed Martin', 'FGM-172', 'Predator SRAW',
'In Battlefield 2, the SRAW is issued to the USMC Anti-Tank kit. Like its counterpart weapon in \
the other factions, the ERYX, the SRAW is a semi-guided anti-tank missile launcher. Once fired, if \
the player continues aiming down the sights they can control the missile for a short time.',
'The short range assault weapon (SRAW) was developed for the USMC as an anti-armour weapon for use \
against targets including tanks, buildings and bunkers in urban surroundings. The SRAW uses a \
point and shoot, fire and forget inertial guidance system that corrects in flight disturbances \
like crosswinds. It can be fired safely from enclosed places within the ranges of 17 m to 600 m \
meaning the personnel using it can remain relatively safe from return fire.')

_add('ushgr_m67', GRENADE, SOLDIER, EXPLOSIVE,
'', 'M67', '',
'In Battlefield 2, Hand Grenades are standard issue to each playable faction. They are found on \
all Kits except the Assault Kit, which replaces them with an under-barrel grenade launcher, and \
the Anti-Tank Kit, which uses a rocket launcher instead. As the G3 unlock for Assault has no \
grenade launcher, the Kit comes with grenades when it is used. They have the same stats for each \
team, as well as using the same model (an M67 Fragmentation Grenade). All Kits except the Assault \
and Anti-Tank Kits receives 4 grenades.',
'Fragmentation grenades consist of a metal body and an explosive charge that is delayed after \
pulling the pin from 4-4.8 seconds. They can be thrown 35-40 metres and have a blast radius of \
5-10 metres but the fragments can travel further and cause less serious damage. They can be very \
effective in urban surroundings most especially when clearing enemy held up in small areas such as \
rooms in buildings, however the use use a hand grenade in such circumstances does not garauntee \
all fatalities and caution should still be taken.')

_add('uslmg_m249saw', LMG, SOLDIER, PRECISION,
'Fabrique Nationale de Herstal', 'M249', 'SAW',
'The M249SAW in Battlefield 2 is the first weapon unlocked in the Support kit for the United \
States Marine Corps. The M249 also appears as a turret that will spawn near certain control points \
that are held by the USMC, although without usable ironsights and infinite ammo. It is tied with \
the Chinese Type 95 LMG for the highest accuracy and lowest power. When compared to its MEC \
counterpart the RPK-74, it has a much lower power output, but is far more accurate. Though having \
a high rate of fire, it is fairly inaccurate when standing up, due to its default high spread. \
Therefore, it is a good idea to go prone to maintain an acceptable amount of accuracy. In \
addition, it has a very long reload time, which can be disadvantageous during combat.',
'The M249 squad automatic weapon (SAW) is in use by the US army and USMC forces. Arriving mid \
eighties it replaced the Browning automatic rifle and is primarily used to support infantry in \
defensive and offensive roles. The SAW is a gas operated, lightweight and handheld weapon that can \
be fired from a bipod or from different hand positions. It uses standard 200 round disintegrating \
belt ammunition but can also make use of M16 rifle magazines as well. With an effective 1000 m \
range and large ammunition capacity this gun increases your sides firepower considerably.')

_add('uslmg_m249saw_stationary', LMG, VEHICLE, PRECISION,
'', '', '',
'',
'')

_add('usmin_claymore', MINE, SOLDIER, EXPLOSIVE,
'Macleod', 'M18A1', 'Claymore',
'In Battlefield 2, the Claymore is issued to the Sniper Kit for the USMC , MEC and the PLA. It is \
useful as a safeguard for when the player is sitting in a good spot for sniping as it can protect \
the player from enemies trying to sneak up on them from behind to take them out.',
'The claymore is a C4 based explosive containing 1.5 pounds of C4 and embedded with 700 steel \
balls. It has a lethal range of 50 meters but will cause casualties up to 100, friendlies should \
remain at over 250 m away from the front of this device and should remain in a covered postion 100 \
m from rear and sides. The M18 can be employed with AT mines to prevent dismounted infantry \
approaching, and snipers can make safe their position by employing these devices in a rear \
defensive position like at the top of a ladder.')

_add('uspis_92fs', PISTOL, SOLDIER, PRECISION,
'Beretta', '92FS', 'Berretta 92',
'The 92FS is the USMC''s and European Union''s standard sidearm in the game. Its stopping power \
and accuracy are similar to that of other handguns in the game. However, it is widely considered \
that the M9 has the most user friendly iron sights in the game. Its magazine capacity is 15 \
rounds, identical to that of the MEC''s MR-444 and Chinese QSZ-92. There is also a suppressed \
version but is only issued to the Special Ops Kit and Sniper Kit.',
'The beretta 92FS is a semi-automatic, double action pistol commonly used by law enforcement \
agencies and the US armed forces. It features a Brunton finish for durability and has a magazine \
capacity of 15 rounds. The 92FS is very light and lethal, and with an improved magazine release is \
also very quick to reload. As with all sidearms it can prove invaluable when switched to in combat \
stuations with slower loading weapons or when out of primary ammunition.')

_add('uspis_92fs_silencer', PISTOL, SOLDIER, PRECISION,
'Beretta', '92FS Silencer', 'Berretta 92 Silencer',
'The 92FS is the USMC''s and European Union''s standard sidearm in the game. Its stopping power \
and accuracy are similar to that of other handguns in the game. However, it is widely considered \
that the M9 has the most user friendly iron sights in the game. Its magazine capacity is 15 \
rounds, identical to that of the MEC''s MR-444 and Chinese QSZ-92. There is also a suppressed \
version but is only issued to the Special Ops Kit and Sniper Kit. This version includes a silencer \
for increased stealth.',
'The beretta 92FS is a semi-automatic, double action pistol commonly used by law enforcement \
agencies and the US armed forces. It features a Brunton finish for durability and has a magazine \
capacity of 15 rounds. The 92FS is very light and lethal, and with an improved magazine release is \
also very quick to reload. As with all sidearms it can prove invaluable when switched to in combat \
stuations with slower loading weapons or when out of primary ammunition.')

_add('usrgl_m203', GRENADE, SOLDIER, EXPLOSIVE,
'Colt', 'M203', '',
'The M203 in Battlefield 2 is used as an attachment for assault rifles. It fires a 40mm grenade \
out of a tube located on the bottom of the barrel of a gun. On impact creates an explosion that \
can kill an enemy or destroy a vehicle. It is only used by the Assault class.',
'The M203 is a single-shot, 40mm grenade launcher that can be attached to many rifles via barrel \
mounts or Picatinny rails, but was originally designed for the U.S. M16 family of Rifles, which \
include the M4A1 and the HK416 Carbines.')

_add('usrif_g3a3', ASSAULT, SOLDIER, PRECISION,
'Heckler & Koch', 'G3A3', 'H&K G3',
'The G3 is the Tier 1 unlock for the Assault Kit in Battlefield 2. The rifle itself is more \
powerful than the default assault rifles, as the weapon is a battle rifle which uses full-sized \
7.62x51mm rifle rounds. However, it is made significantly less attractive to players because of \
the smaller magazine capacity (only 20 rounds compared to 30 for other assault rifles) and lack of \
a grenade launcher. However, some players actually prefer it, because they find the iron sight \
easer to use than the other assault weapons and in certain situations, having regular grenades is \
more useful than having a grenade launcher, e.g. when the enemy is on the other side of a hill.',
'The G3, or Heckler and Koch HK-Gerat-3, is a battle rifle designed in 1959 and manufactured by \
German small arms producer Heckler & Koch. It is a selective-fire weapon chambered for the \
7.62x51mm NATO cartridge, is typically fed from a 20-round detachable box magazine, and has a fire \
rate of 500 to 600 rounds per minute depending on the variant. There are four variants of the G3 \
that currently exist. The most recent incarnation of the rifle is the A4 variant, which possesses \
a collapsible stock.')

_add('usrif_g36c', CARBINE, SOLDIER, PRECISION,
'Heckler & Koch', 'G36C', 'H&K Gewehr 36',
'The G36C is the Tier One unlock for the Special Forces kit in Battlefield 2. It is one of the \
more accurate Spec Ops Carbines in game. It is noticeably more accurate than the USMC''s M4 and \
the PLA''s Type 95 Carbines, but less powerful than the MEC''s AKS-74u. However, it lacks the \
Tasco or Kobra sights of either the M4 or AKS-74u. Unlike the other stock Carbines used by each \
army, the G36C has a foregrip on it, which effectively lowers the amount of recoil when shooting.',
'The Heckler & Koch G36C is a German carbine produced and manufactured by small arms designer \
Heckler & Koch. The weapon uses 5.56x45mm NATO rounds fed by non-standard translucent 30-round \
magazines, with a rate of fire of 750 rounds per minute. It is a variant of the original G36K \
carbine, which is solely based on the original G36.')

_add('usrif_m4', CARBINE, SOLDIER, PRECISION,
'Colt', 'M4', '',
'The M4 Carbine is the standard primary weapon for the USMC''s Special Forces kit. It has a \
Aimpoint M2 Sight attached to it, enabling an un-obstructed field of view when aiming. The M4 \
Carbine has reasonably high accuracy but with a low damage output. However, the lack of stopping \
power is balanced out by the weapons rate of fire. This makes the weapon very effective for many \
situations. When compared to its MEC counterpart, the AKS-74u, it has better accuracy and a better \
sight, but has a lack of stopping power. When compared to its PLA counterpart, the QBZ-97, it has \
identical stats for damage output and accuracy, but the M4 is considered superior because of its \
Aimpoint M2 Sight, while the QBZ-97 has only iron sights.',
'The M4 Carbine was originally developed by the US government by Colt firearms to replace the \
M16A2 and M16 guns. It is shorter and lighter than its predecessors and is gas operated, air \
cooled, magazine fed, selective fire firearm with a collaspible stock. It is used by many US \
agencies including USMC, Delta force, and the Navy SEALS for close to mid range urban combat and a \
variant is also used by the British SAS. The Carbine uses 5.56 mm ammo and has a 30 round magazine \
capacity. It has a fully automatic and single shot firing mode and can be fitted with night \
vision, laser sights, bipods and even the M203 grenade launcher. With all its features this weapon \
will not let you down when you most need it.')

_add('usrif_m16a2', ASSAULT, SOLDIER, PRECISION,
'Colt', 'M16A2', '',
'The United States Marine Corps in Battlefield 2 uses the M16A2 as its primary weapon for the \
Assault and Medic kits. It fires in three-round bursts, with each burst doing a moderate amount of \
damage. The M16A2 included in Assault kits comes with an M203 grenade launcher, while the M16 used \
by the Medic has no attachments at all. The Assault kit''s M16A2 will have six plus one magazines, \
while the Medic kit''s has four plus one magazines.',
'This gun was produced as an improved version of the m16A1 and has become the industry standard \
that other guns are compared to as well as the standard for the marine corps for the last 30 \
years. It is lightweight, air-cooled, gas operated rifle with 30 round capacity and can be \
switched to automatic, 3 round bursts, or semi-automatic, single shot modes. This weapon has a \
fully adjustable rear site and has a compensator that keeps the muzzle down in semi-automatic \
mode. The M16A2 can also fire 40 mm grenades when used in conjunction with the M203 grenade \
launcher making this an effective gun for many combat situations.')

_add('usrif_m24', SNIPER, SOLDIER, PRECISION,
'Remington', 'M24', 'SWS',
'The M24 is the default sniper rifle for the USMC. Its scope crosshairs are similar to that of the \
Chinese Type 88 with the traditional intersection line arrangement, but the lines go to each end \
of the scope. As a bolt-action rifle, the M24 does have its limitations, especially in fire rate. \
A headshot with this weapon, like all Sniper Rifles, will result in an instant kill. Otherwise, \
two body hits are required to kill a target. Because of its thin scope lines, it is recommended to \
use the M24 for long range shooting before acquiring the British L96A1 sniper rifle, which has \
scope lines even thinner than the M24''s. Like many of the usable sniper rifles in the game, it \
does not have the kind of penetration needed to kill truck drivers and helicopter pilots.',
'The M24 is a sniper weapon system (SWS) first fielded in 1988 by the US army and the Isreali \
Defence forces. It is currently in use and has seen action in both Gulf wars although it is not a \
gun used by the USMC and there is a new version on the way, the M24A2. The stock is made of a \
combination of kevlar,graphite and fiberglass bonded with epoxy resin meaning this gun can handle \
the most harsh environments. With a maximum effective range of 800 m and using five 7.62 calibre \
bullets this gun is an extremely accurate and effective long range weapon. As with all stealth \
weapons it is important for personnel using them to remain undetected possibly using the M18 \
claymore.')

_add('ussni_m82a1', SNIPER, SOLDIER, PRECISION,
'Barrett', 'M82A1', '',
'The M82A1 seems to be a weapon which was cut midway though Battlefield 2''s development. It has a \
different texture sheet and animations than the M95, which is a similar weapon. In addition, the \
horizontal line on its scope is shorter on both sides. Its file directories lack the "sounds" and \
"ai" files of the other weapons, but it did have its animations and meshes. The M82A1 weapon icon. \
Unlike another cut item, the M82A1 is replaced by another weapon when the files are modified to \
include it in the game. However, its icon is still visible, both in the kit selection screen and \
from the BFHQ screen. On the BFHQ screen, its title is "M95" and its description is that of the \
Jackhammer.',
'The M82 is a recoil-operated, semi-automatic anti-materiel rifle developed by the American \
Barrett Firearms Manufacturing company. A heavy SASR (Special Application Scoped Rifle), it is \
used by many units and armies around the world. It is also called the "Light Fifty" for its .50 \
caliber BMG (12.7 mm) chambering. The weapon is found in two variants-the original M82A1 (and A3) \
and the bullpup M82A2. The M82A2 is no longer manufactured, though the XM500 can be seen as its \
successor.')

_add('usrif_m203', ASSAULT, SOLDIER, PRECISION,
'Colt', 'M203', '',
'The M16 feautres a 3-round burst firing mode, which is very effective at close range, and medium \
ranges. It will take a couple of well-placed bursts to take down an enemy. Switch to semi-auto and \
zoom your view in and the M16 will make a decent long-range weapon to pick off enemies from afar. \
While the M16 is the most accurate of the standard Assault Rifles, it suffers from a ~20% \
reduction in damage per shot compared to the AK-101 or AK-47. The lower damage of the M16 is \
partially offset by its higher rate of fire; it is capable of firing a three-shot burst 50% faster \
than the others, which can be important if the target is moving.',
'This gun was produced as an improved version of the m16A1 and has become the industry standard \
that other guns are compared to as well as the standard for the marine corps for the last 30 \
years. It is lightweight, air-cooled, gas operated rifle with 30 round capacity and can be \
switched to automatic, 3 round bursts, or semi-automatic, single shot modes. This weapon has a \
fully adjustable rear site and has a compensator that keeps the muzzle down in semi-automatic \
mode. The M16A2 can also fire 40 mm grenades when used in conjunction with the M203 grenade \
launcher making this an effective gun for many combat situations.')

_add('usrif_mp5_a3', SMG, SOLDIER, PRECISION,
'Heckler & Koch', 'MP5A3', '',
'The MP5 is the standard submachine gun of the USMC, US Navy SEALs and SAS Anti-Tank Kit. It fires \
at 900 rounds per minute from a 30-round magazine, but it has low damage and accuracy, and a \
fairly long reload.',
'The MP5 was originally introduced in 1966 by the German company Heckler and Koch but not imported \
to the US till the 70''s where it was adopted as the sub-machine gun for military and SWAT forces. \
The MP5 can be shouldered or fired by hand and is accurate and reliable as well as being flexible \
with six assembly groups and ambidextrous safety selector lever. It features automatic and single \
shot modes so making sure which mode you are in can save your life.')

_add('usrif_remington11-87', SHOTGUN, SOLDIER, PRECISION,
'Remington', 'M11-87', '',
'In Battlefield 2, the M11-87 is issued to the USMC Engineer Kit. A hit with this pump shotgun can \
kill in one shot up to medium-short range, and multiple targets can be damaged with each shot. In \
addition, there is no accuracy benefit (or detriment) for the different stances, though the zoom \
feature which stands in place of ironsights will reduce recoil.',
'The M11-87 and Nor982 are both 12 gauge pump action shotguns with a 7 round magazine capacity. \
These guns are not accurate due to large blast patterns and should be used as a close range weapon \
switching to a pistol for medium to longer range shots. Due to the delay between shots it is \
important to hit the target the first time as you may not get another chance.')

_add('usrif_sa80', ASSAULT, SOLDIER, PRECISION,
'Heckler & Koch', 'L85A1', '',
'The L85A1 (referred to in the game files as SA80A2[2]) is a Tier One unlock for the Medic Kit and \
the primary weapon for the European Union Assault Class. It features a SUSAT scope instead of the \
iron sights. Some players feel that the high-precision sight seen through the scope makes the \
weapon appear more accurate than it actually is. As a matter of fact, its ability to accurately \
hit targets at some distance in full-auto firing mode is lost after more than three shots have \
been fired in full-auto. The G36E is more accurate, although it doesn''t mount any scope.',
'The L85 is a bullpup assault rifle designed in the 1970s and 80s, developed from the SA80, to \
become the service rifle of the Armed Forces of Britain. It fires the 5.56x45mm NATO round and is \
fed from a 30 round detachable STANAG box magazine with an effective range of up to 850 meters \
depending on the variant and a 650 rounds per minute fire rate.')

_add('ustnk_m1a2_barrel', CANNON, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')

_add('ussht_jackhammer', SHOTGUN, SOLDIER, PRECISION,
'Pancor', 'MK3A1', 'Jackhammer',
'In Battlefield 2, the MK3A1 is the Tier one unlock for the Engineer Kit. Its main advantage is \
its fully-automatic firing mode, being only matched in fire rate by the MEC S12K. The shotgun is a \
valid replacement for the American M11-87 and Chinese NOR982 Pump-Action shotguns, as the MK3A1 \
has more power per shot, as well as boasting fully automatic fire.',
'The Pancor MK3A1 or "The Jackhammer" is a 12-gauge, gas-operated, fully automatic shotgun. It was \
developed by John Anderson in 1984 and patented in 1987. Its cumbersome design never led it to be \
fully produced; there are few (according to some reports, only two) prototypes in existence.')

_add('ussni_m95_barret', SNIPER, SOLDIER, PRECISION,
'Barrett', 'M95', '',
'In Battlefield 2, the M95 is the Tier One unlock for the Sniper kit. The M95 is a bolt action \
rifle, with a magazine of five rounds (Similar to all the bolt-action rifles such as the M24 SWS). \
Its main improvement is a more powerful cartridge, the .50 BMG. The M95 is the only small arms \
able to deal 95% damage when fired on any part of the enemy (save for the lethal headshots) and to \
penetrate reinforced glass.',
'The M95 is a bullpup, bolt-action, anti-materiel sniper rifle chambered for .50 BMG (12.7x99 mm), \
designed by Barrett Firearms Manufacturing in 1995. It''s very useful in anti-materiel situations \
due to its incredibly large .50 Caliber round, which easily penetrates heavy armor. It uses a \
triangular bolt head and, because of its bullpup configuration, is fairly short for a sniper \
rifle. Furthermore, its recoil is remarkably low.')

_add('wrench', TOOL, SOLDIER, PRECISION,
'', '', 'Wrench',
'In Battlefield 2, the Wrench is issued to the Engineer kit. After a short animation, where the \
user widens the mouth of the wrench, the player can use it to repair friendly or neutral vehicles. \
It can also rebuild bridges which have been damaged or destroyed by C4 or other explosives.',
'')

_add('xpak2_tiger_missiles', ROCKET, VEHICLE, EXPLOSIVE,
'', '', '',
'',
'')
