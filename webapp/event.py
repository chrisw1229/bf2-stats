
import time

from parse import parse_mgr
from model import model_mgr

# Create a shared registry of all the event types
registry = []

class BaseEvent(object):

    ID = None
    CALLBACK = None

    def __init__(self, tick, values):
        self.timestamp = int(round(time.time() * 1000))
        self.tick = tick

class AmmoEvent(BaseEvent):

    ID = 'AM'
    CALLBACK = 'on_ammo'

    def __init__(self, tick, values):
        super(AmmoEvent, self).__init__(tick, values)

        assert len(values) == 4, 'AmmoEvent - Wrong number of values: %i' % len(values)
 
        self.receiver = model_mgr.get_player(values[0])
        self.receiver_pos = parse_mgr.parse_pos(values[1])
        self.giver = model_mgr.get_player(values[2])
        self.giver_pos = parse_mgr.parse_pos(values[3])
registry.append(AmmoEvent)

class AssistEvent(BaseEvent):

    ID = 'AS'
    CALLBACK = 'on_assist'

    def __init__(self, tick, values):
        super(AssistEvent, self).__init__(tick, values)

        assert len(values) == 3, 'AssistEvent - Wrong number of values: %i' % len(values)

        self.assister = model_mgr.get_player(values[0])
        self.assister_pos = parse_mgr.parse_pos(values[1])
        self.assist_type = values[2]
registry.append(AssistEvent)

class BanEvent(BaseEvent):

    ID = 'BN'
    CALLBACK = 'on_ban'

    def __init__(self, tick, values):
        super(BanEvent, self).__init__(tick, values)

        assert len(values) == 3, 'BanEvent - Wrong number of values: %i' % len(values)

        self.player = model_mgr.get_player(values[0])
        self.duration = values[1]
        self.ban_type = values[2]
registry.append(BanEvent)

class ChatEvent(BaseEvent):

    ID = 'CH'
    CALLBACK = 'on_chat'

    def __init__(self, tick, values):
        super(ChatEvent, self).__init__(tick, values)

        assert len(values) == 3, 'ChatEvent - Wrong number of values: %i' % len(values)

        self.channel = values[0]
        self.player = model_mgr.get_player(values[1])
        self.text = values[2]
registry.append(ChatEvent)

class ClockLimitEvent(BaseEvent):

    ID = 'CL'
    CALLBACK = 'on_clock_limit'

    def __init__(self, tick, values):
        super(ClockLimitEvent, self).__init__(tick, values)

        assert len(values) == 1, 'ClockLimitEvent - Wrong number of values: %i' % len(values)

        self.value = values[0]
registry.append(ClockLimitEvent)

class CommanderEvent(BaseEvent):

    ID = 'CM'
    CALLBACK = 'on_commander'

    def __init__(self, tick, values):
        super(CommanderEvent, self).__init__(tick, values)

        assert len(values) == 2, 'CommanderEvent - Wrong number of values: %i' % len(values)

        self.team = values[0]
        self.player = model_mgr.get_player(values[1])
registry.append(CommanderEvent)

class ConnectEvent(BaseEvent):

    ID = 'CN'
    CALLBACK = 'on_connect'

    def __init__(self, tick, values):
        super(ConnectEvent, self).__init__(tick, values)

        assert len(values) == 2, 'ConnectEvent - Wrong number of values: %i' % len(values)

        self.player = model_mgr.get_player(values[1])
registry.append(ConnectEvent)

class ControlPointEvent(BaseEvent):

    ID = 'CP'
    CALLBACK = 'on_control_point'

    def __init__(self, tick, values):
        super(ControlPointEvent, self).__init__(tick, values)

        assert len(values) == 4, 'ControlPointEvent - Wrong number of values: %i' % len(values)

        self.control_point = values[0]
        self.control_point_pos = parse_mgr.parse_pos(values[1])
        self.flag_state = values[2]
        self.team = values[3]
registry.append(ControlPointEvent)

class DisconnectEvent(BaseEvent):

    ID = 'DC'
    CALLBACK = 'on_disconnect'

    def __init__(self, tick, values):
        super(DisconnectEvent, self).__init__(tick, values)

        assert len(values) == 2, 'DisconnectEvent - Wrong number of values: %i' % len(values)

        self.player = model_mgr.get_player(values[1])
registry.append(DisconnectEvent)

class DeathEvent(BaseEvent):

    ID = 'DT'
    CALLBACK = 'on_death'

    def __init__(self, tick, values):
        super(DeathEvent, self).__init__(tick, values)

        assert len(values) == 2, 'DeathEvent - Wrong number of values: %i' % len(values)

        self.player = model_mgr.get_player(values[0])
        self.player_pos = parse_mgr.parse_pos(values[1])
registry.append(DeathEvent)

class GameStatusEvent(BaseEvent):

    ID = 'GS'
    CALLBACK = 'on_game_status'

    def __init__(self, tick, values):
        super(GameStatusEvent, self).__init__(tick, values)

        assert len(values) == 4, 'GameStatusEvent - Wrong number of values: %i' % len(values)

        self.status = values[0]
        self.map = values[1]
        self.tick = values[2]
        self.score = values[3]
registry.append(GameStatusEvent)

class HealEvent(BaseEvent):

    ID = 'HL'
    CALLBACK = 'on_heal'

    def __init__(self, tick, values):
        super(HealEvent, self).__init__(tick, values)

        assert len(values) == 4, 'HealEvent - Wrong number of values: %i' % len(values)

        self.receiver = model_mgr.get_player(values[0])
        self.receiver_pos = parse_mgr.parse_pos(values[1])
        self.giver = model_mgr.get_player(values[2])
        self.giver_pos = parse_mgr.parse_pos(values[3])
registry.append(HealEvent)

class KickEvent(BaseEvent):

    ID = 'KC'
    CALLBACK = 'on_kick'

    def __init__(self, tick, values):
        super(KickEvent, self).__init__(tick, values)

        assert len(values) == 1, 'KickEvent - Wrong number of values: %i' % len(values)

        self.player = model_mgr.get_player(values[0])
registry.append(KickEvent)

class KitDropEvent(BaseEvent):

    ID = 'KD'
    CALLBACK = 'on_kit_drop'

    def __init__(self, tick, values):
        super(KitDropEvent, self).__init__(tick, values)

        assert len(values) == 3, 'KitDropEvent - Wrong number of values: %i' % len(values)

        self.player = model_mgr.get_player(values[0])
        self.player_pos = parse_mgr.parse_pos(values[1])
        self.kit = values[2]
registry.append(KitDropEvent)

class KillEvent(BaseEvent):

    ID = 'KL'
    CALLBACK = 'on_kill'

    def __init__(self, tick, values):
        super(KillEvent, self).__init__(tick, values)

        assert len(values) == 5, 'KillEvent - Wrong number of values: %i' % len(values)

        self.victim = model_mgr.get_player(values[0])
        self.victim_pos = parse_mgr.parse_pos(values[1])
        self.attacker = model_mgr.get_player(values[2])
        self.attacker_pos = parse_mgr.parse_pos(values[3])
        self.weapon = values[4]
registry.append(KillEvent)

class KitPickupEvent(BaseEvent):

    ID = 'KP'
    CALLBACK = 'on_kit_pickup'

    def __init__(self, tick, values):
        super(KitPickupEvent, self).__init__(tick, values)

        assert len(values) == 3, 'KitPickupEvent - Wrong number of values: %i' % len(values)

        self.player = model_mgr.get_player(values[0])
        self.player_pos = parse_mgr.parse_pos(values[1])
        self.kit = values[2]
registry.append(KitPickupEvent)

class RepairEvent(BaseEvent):

    ID = 'RP'
    CALLBACK = 'on_repair'

    def __init__(self, tick, values):
        super(RepairEvent, self).__init__(tick, values)

        assert len(values) == 4, 'RepairEvent - Wrong number of values: %i' % len(values)

        self.vehicle = model_mgr.get_vehicle(values[0])
        self.vehicle_pos = parse_mgr.parse_pos(values[1])
        self.giver = model_mgr.get_player(values[2])
        self.giver_pos = parse_mgr.parse_pos(values[3])
registry.append(RepairEvent)

class ResetEvent(BaseEvent):

    ID = 'RS'
    CALLBACK = 'on_reset'

    def __init__(self, tick, values):
        super(ResetEvent, self).__init__(tick, values)

        assert len(values) == 1, 'ResetEvent - Wrong number of values: %i' % len(values)

        self.data = values[0]
registry.append(ResetEvent)

class ReviveEvent(BaseEvent):

    ID = 'RV'
    CALLBACK = 'on_revive'

    def __init__(self, tick, values):
        super(ReviveEvent, self).__init__(tick, values)

        assert len(values) == 4, 'ReviveEvent - Wrong number of values: %i' % len(values)

        self.receiver = model_mgr.get_player(values[0])
        self.receiver_pos = parse_mgr.parse_pos(values[1])
        self.giver = model_mgr.get_player(values[2])
        self.giver_pos = parse_mgr.parse_pos(values[3])
registry.append(ReviveEvent)

class ScoreEvent(BaseEvent):

    ID = 'SC'
    CALLBACK = 'on_score'

    def __init__(self, tick, values):
        super(ScoreEvent, self).__init__(tick, values)

        assert len(values) == 2, 'ScoreEvent - Wrong number of values: %i' % len(values)

        self.player = model_mgr.get_player(values[0])
        self.value = int(values[1])
registry.append(ScoreEvent)

class SquadLeaderEvent(BaseEvent):

    ID = 'SL'
    CALLBACK = 'on_squad_leader'

    def __init__(self, tick, values):
        super(SquadLeaderEvent, self).__init__(tick, values)

        assert len(values) == 2, 'SquadLeaderEvent - Wrong number of values: %i' % len(values)

        self.squad = values[0]
        self.player = model_mgr.get_player(values[1])
registry.append(SquadLeaderEvent)

class SpawnEvent(BaseEvent):

    ID = 'SP'
    CALLBACK = 'on_spawn'

    def __init__(self, tick, values):
        super(SpawnEvent, self).__init__(tick, values)

        assert len(values) == 3, 'SpawnEvent - Wrong number of values: %i' % len(values)

        self.player = model_mgr.get_player(values[0])
        self.player_pos = parse_mgr.parse_pos(values[1])
        self.team = values[2]
registry.append(SpawnEvent)

class SquadEvent(BaseEvent):

    ID = 'SQ'
    CALLBACK = 'on_squad'

    def __init__(self, tick, values):
        super(SquadEvent, self).__init__(tick, values)

        assert len(values) == 2, 'SquadEvent - Wrong number of values: %i' % len(values)

        self.player = model_mgr.get_player(values[0])
        self.squad = values[1]
registry.append(SquadEvent)

class ServerStatusEvent(BaseEvent):

    ID = 'SS'
    CALLBACK = 'on_server_status'

    def __init__(self, tick, values):
        super(ServerStatusEvent, self).__init__(tick, values)

        assert len(values) == 2, 'ServerStatusEvent - Wrong number of values: %i' % len(values)

        self.status = values[0]
        self.status_time = values[1]
registry.append(ServerStatusEvent)

class TeamDamageEvent(BaseEvent):

    ID = 'TD'
    CALLBACK = 'on_team_damage'

    def __init__(self, tick, values):
        super(TeamDamageEvent, self).__init__(tick, values)

        assert len(values) == 4, 'TeamDamageEvent - Wrong number of values: %i' % len(values)

        self.victim = model_mgr.get_player(values[0])
        self.victim_pos = parse_mgr.parse_pos(values[1])
        self.attacker = model_mgr.get_player(values[2])
        self.attacker_pos = parse_mgr.parse_pos(values[3])
registry.append(TeamDamageEvent)

class TicketLimitEvent(BaseEvent):

    ID = 'TL'
    CALLBACK = 'on_ticket_limit'

    def __init__(self, tick, values):
        super(TicketLimitEvent, self).__init__(tick, values)

        assert len(values) == 2, 'TicketLimitEvent - Wrong number of values: %i' % len(values)

        self.team = values[0]
        self.value = int(values[1])
registry.append(TicketLimitEvent)

class TeamEvent(BaseEvent):

    ID = 'TM'
    CALLBACK = 'on_team'

    def __init__(self, tick, values):
        super(TeamEvent, self).__init__(tick, values)

        assert len(values) == 2, 'TeamEvent - Wrong number of values: %i' % len(values)

        self.player = model_mgr.get_player(values[0])
        self.team = values[1]
registry.append(TeamEvent)

class VehicleDestroyEvent(BaseEvent):

    ID = 'VD'
    CALLBACK = 'on_vehicle_destroy'

    def __init__(self, tick, values):
        super(VehicleDestroyEvent, self).__init__(tick, values)

        assert len(values) == 4, 'VehicleDestroyEvent - Wrong number of values: %i' % len(values)

        self.vehicle = model_mgr.get_vehicle(values[0])
        self.vehicle_pos = parse_mgr.parse_pos(values[1])
        self.attacker = model_mgr.get_player(values[2])
        self.attacker_pos = parse_mgr.parse_pos(values[3])
registry.append(VehicleDestroyEvent)

class VehicleEnterEvent(BaseEvent):

    ID = 'VE'
    CALLBACK = 'on_vehicle_enter'

    def __init__(self, tick, values):
        super(VehicleEnterEvent, self).__init__(tick, values)

        assert len(values) == 5, 'VehicleEnterEvent - Wrong number of values: %i' % len(values)

        self.player = model_mgr.get_player(values[0])
        self.player_pos = parse_mgr.parse_pos(values[1])
        self.vehicle = model_mgr.get_vehicle(values[2])
        self.vehicle_slot = values[3]
        self.free_soldier = values[4]
registry.append(VehicleEnterEvent)

class VehicleExitEvent(BaseEvent):

    ID = 'VX'
    CALLBACK = 'on_vehicle_exit'

    def __init__(self, tick, values):
        super(VehicleExitEvent, self).__init__(tick, values)

        assert len(values) == 4, 'VehicleExitEvent - Wrong number of values: %i' % len(values)

        self.player = model_mgr.get_player(values[0])
        self.player_pos = parse_mgr.parse_pos(values[1])
        self.vehicle = model_mgr.get_vehicle(values[2])
        self.vehicle_slot = values[3]
registry.append(VehicleExitEvent)

class WeaponEvent(BaseEvent):

    ID = 'WP'
    CALLBACK = 'on_weapon'

    def __init__(self, tick, values):
        super(WeaponEvent, self).__init__(tick, values)

        assert len(values) == 3, 'WeaponEvent - Wrong number of values: %i' % len(values)

        self.player = model_mgr.get_player(values[0])
        self.player_pos = parse_mgr.parse_pos(values[1])
        self.weapon = values[2]
registry.append(WeaponEvent)
