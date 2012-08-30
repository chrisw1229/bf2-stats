
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

    def __init__(self, id, kit_type, name, desc, weapon_ids):
        self.id = id
        self.kit_type = kit_type
        self.name = name
        self.desc = desc
        self.weapon_ids = weapon_ids

        self.reset()

    def __repr__(self):
        return self.__dict__

    def reset(self):
        pass

EMPTY = Kit('', '', '', '', [])

def _add(id, kit_type, name, desc, weapon_ids):
    registry.add(Kit(id, kit_type, name, desc, weapon_ids))

_add('ch_assault', ASSAULT, 'China Assault',
'',
['kni_knife', 'chpis_qsz92', 'rurif_gp25', 'rurgl_gp25', 'rurif_ak47', 'hgr_smoke'])

_add('ch_at', ANTI_TANK, 'China Anti-Tank',
'',
['kni_knife', 'chpis_qsz92', 'chrif_type85', 'chat_eryx'])

_add('ch_engineer', ENGINEER, 'China Engineer',
'',
['kni_knife', 'chpis_qsz92', 'chsht_norinco982', 'ushgr_m67', 'at_mine', 'wrench'])

_add('ch_medic', MEDIC, 'China Medic',
'',
['kni_knife', 'chpis_qsz92', 'rurif_ak47', 'ushgr_m67', 'defibrillator', 'medikit'])

_add('ch_sniper', SNIPER, 'China Sniper',
'',
['kni_knife', 'chpis_qsz92_silencer', 'chsni_type88', 'ushgr_m67', 'usmin_claymore'])

_add('ch_specops', SPEC_OPS, 'China Special Ops',
'',
['kni_knife', 'chpis_qsz92_silencer', 'chrif_type95', 'ushgr_m67', 'c4_explosives'])

_add('ch_support', SUPPORT, 'China Support',
'',
['kni_knife', 'chpis_qsz92', 'chlmg_type95', 'ushgr_m67', 'ammokit'])

_add('eu_assault', ASSAULT, 'EU Assault',
'',
[])

_add('eu_at', ANTI_TANK, 'EU Anti-Tank',
'',
[])

_add('eu_engineer', ENGINEER, 'EU Engineer',
'',
[])

_add('eu_medic', MEDIC, 'EU Medic',
'',
[])

_add('eu_sniper', SNIPER, 'EU Sniper',
'',
[])

_add('eu_specops', SPEC_OPS, 'EU Special Ops',
'',
[])

_add('eu_support', SUPPORT, 'EU Support',
'',
[])

_add('mec_assault', ASSAULT, 'MEC Assault',
'',
['kni_knife', 'rupis_baghira', 'rurif_gp30', 'rurgl_gp30', 'rurif_ak101', 'hgr_smoke'])

_add('mec_at', ANTI_TANK, 'MEC Anti-Tank',
'',
['kni_knife', 'rupis_baghira', 'rurif_bizon', 'chat_eryx'])

_add('mec_engineer', ENGINEER, 'MEC Engineer',
'',
['kni_knife', 'rupis_baghira', 'rusht_saiga12', 'ushgr_m67', 'at_mine', 'wrench'])

_add('mec_medic', MEDIC, 'MEC Medic',
'',
['kni_knife', 'rupis_baghira', 'rurif_ak101', 'ushgr_m67', 'defibrillator', 'medikit'])

_add('mec_sniper', SNIPER, 'MEC Sniper',
'',
['kni_knife', 'rupis_baghira_silencer', 'rurif_dragunov', 'ushgr_m67', 'usmin_claymore'])

_add('mec_specops', SPEC_OPS, 'MEC Special Ops',
'',
['kni_knife', 'rupis_baghira_silencer', 'rurrif_ak74u', 'ushgr_m67', 'c4_explosives'])

_add('mec_support', SUPPORT, 'MEC Support',
'',
['kni_knife', 'rupis_baghira', 'rulmg_rpk74', 'ushgr_m67', 'ammokit'])

_add('us_assault', ASSAULT, 'US Assault',
'',
['kni_knife', 'uspis_92fs', 'usrif_m203', 'usrgl_m203', 'usrif_m16a2', 'hgr_smoke'])

_add('us_at', ANTI_TANK, 'US Anti-Tank',
'',
['kni_knife', 'uspis_92fs', 'usrif_mp5_a3', 'usatp_predator'])

_add('us_engineer', ENGINEER, 'US Engineer',
'',
['kni_knife', 'uspis_92fs', 'usrif_remington11-87', 'ushgr_m67', 'at_mine', 'wrench'])

_add('us_medic', MEDIC, 'US Medic',
'',
['kni_knife', 'uspis_92fs', 'usrif_m16a2', 'ushgr_m67', 'defibrillator', 'medikit'])

_add('us_sniper', SNIPER, 'US Sniper',
'',
['kni_knife', 'uspis_92fs_silencer', 'usrif_m24', 'ushgr_m67', 'usmin_claymore'])

_add('us_specops', SPEC_OPS, 'US Special Ops',
'',
['kni_knife', 'uspis_92fs_silencer', 'usrif_m4', 'ushgr_m67', 'c4_explosives'])

_add('us_support', SUPPORT, 'US Support',
'',
['kni_knife', 'uspis_92fs', 'uslmg_m249saw', 'ushgr_m67', 'ammokit'])
