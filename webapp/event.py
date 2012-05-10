registry = []

class BaseEvent(object):

    ID = None
    CALLBACK = None
    time = None
    consumed = False

    def __init__(self, time, values):
        self.time = time

class AmmoEvent(BaseEvent):

    ID = 'AM'
    CALLBACK = 'on_ammo'

    def __init__(self, time, values):
        super(AmmoEvent, self).__init__(time, values)

        print 'AMMO EVENT: ', values
registry.append(AmmoEvent)

class AssistEvent(BaseEvent):

    ID = 'AS'
    CALLBACK = 'on_assist'

    def __init__(self, time, values):
        super(AssistEvent, self).__init__(time, values)

        print 'ASSIST EVENT: ', values
registry.append(AssistEvent)

class BanEvent(BaseEvent):

    ID = 'BN'
    CALLBACK = 'on_ban'

    def __init__(self, time, values):
        super(BanEvent, self).__init__(time, values)

        print 'BAN EVENT: ', values
registry.append(BanEvent)

class ChatEvent(BaseEvent):

    ID = 'CH'
    CALLBACK = 'on_chat'

    def __init__(self, time, values):
        super(ChatEvent, self).__init__(time, values)

        print 'CHAT EVENT: ', values
registry.append(ChatEvent)

class ClockLimitEvent(BaseEvent):

    ID = 'CL'
    CALLBACK = 'on_clock_limit'

    def __init__(self, time, values):
        super(ClockLimitEvent, self).__init__(time, values)

        print 'CLOCK LIMIT EVENT: ', values
registry.append(ClockLimitEvent)

class CommanderEvent(BaseEvent):

    ID = 'CM'
    CALLBACK = 'on_commander'

    def __init__(self, time, values):
        super(CommanderEvent, self).__init__(time, values)

        print 'COMMANDER EVENT: ', values
registry.append(CommanderEvent)

class ConnectEvent(BaseEvent):

    ID = 'CN'
    CALLBACK = 'on_connect'

    def __init__(self, time, values):
        super(ConnectEvent, self).__init__(time, values)

        print 'CONNECT EVENT: ', values
registry.append(ConnectEvent)

class ControlPointEvent(BaseEvent):

    ID = 'CP'
    CALLBACK = 'on_control_point'

    def __init__(self, time, values):
        super(ControlPointEvent, self).__init__(time, values)

        print 'CONTROL POINT EVENT: ', values
registry.append(ControlPointEvent)

class DisconnectEvent(BaseEvent):

    ID = 'DC'
    CALLBACK = 'on_disconnect'

    def __init__(self, time, values):
        super(DisconnectEvent, self).__init__(time, values)

        print 'DISCONNECT EVENT: ', values
registry.append(DisconnectEvent)

class DeathEvent(BaseEvent):

    ID = 'DT'
    CALLBACK = 'on_death'

    def __init__(self, time, values):
        super(DeathEvent, self).__init__(time, values)

        print 'DEATH EVENT: ', values
registry.append(DeathEvent)

class GameStatusEvent(BaseEvent):

    ID = 'GS'
    CALLBACK = 'on_game_status'

    def __init__(self, time, values):
        super(GameStatusEvent, self).__init__(time, values)

        print 'GAME STATUS EVENT: ', values
registry.append(GameStatusEvent)

class HealEvent(BaseEvent):

    ID = 'HL'
    CALLBACK = 'on_heal'

    def __init__(self, time, values):
        super(HealEvent, self).__init__(time, values)

        print 'HEAL EVENT: ', values
registry.append(HealEvent)

class KickEvent(BaseEvent):

    ID = 'KC'
    CALLBACK = 'on_kick'

    def __init__(self, time, values):
        super(KickEvent, self).__init__(time, values)

        print 'KICK EVENT: ', values
registry.append(KickEvent)

class KitDropEvent(BaseEvent):

    ID = 'KD'
    CALLBACK = 'on_kit_drop'

    def __init__(self, time, values):
        super(KitDropEvent, self).__init__(time, values)

        print 'KIT DROP EVENT: ', values
registry.append(KitDropEvent)

class KillEvent(BaseEvent):

    ID = 'KL'
    CALLBACK = 'on_kill'

    def __init__(self, time, values):
        super(KillEvent, self).__init__(time, values)

        print 'KILL EVENT: ', values
registry.append(KillEvent)

class KitPickupEvent(BaseEvent):

    ID = 'KP'
    CALLBACK = 'on_kit_pickup'

    def __init__(self, time, values):
        super(KitPickupEvent, self).__init__(time, values)

        print 'KIT PICKUP EVENT: ', values
registry.append(KitPickupEvent)

class RepairEvent(BaseEvent):

    ID = 'RP'
    CALLBACK = 'on_repair'

    def __init__(self, time, values):
        super(RepairEvent, self).__init__(time, values)

        print 'REPAIR EVENT: ', values
registry.append(RepairEvent)

class ResetEvent(BaseEvent):

    ID = 'RS'
    CALLBACK = 'on_reset'

    def __init__(self, time, values):
        super(ResetEvent, self).__init__(time, values)

        print 'RESET EVENT: ', values
registry.append(ResetEvent)

class ReviveEvent(BaseEvent):

    ID = 'RV'
    CALLBACK = 'on_revive'

    def __init__(self, time, values):
        super(ReviveEvent, self).__init__(time, values)

        print 'REVIVE EVENT: ', values
registry.append(ReviveEvent)

class ScoreEvent(BaseEvent):

    ID = 'SC'
    CALLBACK = 'on_score'

    def __init__(self, time, values):
        super(ScoreEvent, self).__init__(time, values)

        print 'SCORE EVENT: ', values
registry.append(ScoreEvent)

class SquadLeaderEvent(BaseEvent):

    ID = 'SL'
    CALLBACK = 'on_squad_leader'

    def __init__(self, time, values):
        super(SquadLeaderEvent, self).__init__(time, values)

        print 'SQUAD LEADER EVENT: ', values
registry.append(SquadLeaderEvent)

class SpawnEvent(BaseEvent):

    ID = 'SP'
    CALLBACK = 'on_spawn'

    def __init__(self, time, values):
        super(SpawnEvent, self).__init__(time, values)

        print 'SPAWN EVENT: ', values
registry.append(SpawnEvent)

class SquadEvent(BaseEvent):

    ID = 'SQ'
    CALLBACK = 'on_squad'

    def __init__(self, time, values):
        super(SquadEvent, self).__init__(time, values)

        print 'SQUAD EVENT: ', values
registry.append(SquadEvent)

class ServerStatusEvent(BaseEvent):

    ID = 'SS'
    CALLBACK = 'on_server_status'

    def __init__(self, time, values):
        super(ServerStatusEvent, self).__init__(time, values)

        print 'SERVER STATUS EVENT: ', values
registry.append(ServerStatusEvent)

class TeamDamageEvent(BaseEvent):

    ID = 'TD'
    CALLBACK = 'on_team_damage'

    def __init__(self, time, values):
        super(TeamDamageEvent, self).__init__(time, values)

        print 'TEAM DAMAGE EVENT: ', values
registry.append(TeamDamageEvent)

class TicketLimitEvent(BaseEvent):

    ID = 'TL'
    CALLBACK = 'on_ticket_limit'

    def __init__(self, time, values):
        super(TicketLimitEvent, self).__init__(time, values)

        print 'TICKET LIMIT EVENT: ', values
registry.append(TicketLimitEvent)

class TeamEvent(BaseEvent):

    ID = 'TM'
    CALLBACK = 'on_team'

    def __init__(self, time, values):
        super(TeamEvent, self).__init__(time, values)

        print 'TEAM EVENT: ', values
registry.append(TeamEvent)

class VehicleDestroyEvent(BaseEvent):

    ID = 'VD'
    CALLBACK = 'on_vehicle_destroy'

    def __init__(self, time, values):
        super(VehicleDestroyEvent, self).__init__(time, values)

        print 'VEHICLE DESTROY EVENT: ', values
registry.append(VehicleDestroyEvent)

class VehicleEnterEvent(BaseEvent):

    ID = 'VE'
    CALLBACK = 'on_vehicle_enter'

    def __init__(self, time, values):
        super(VehicleEnterEvent, self).__init__(time, values)

        print 'VEHICLE ENTER EVENT: ', values
registry.append(VehicleEnterEvent)

class VehicleExitEvent(BaseEvent):

    ID = 'VX'
    CALLBACK = 'on_vehicle_exit'

    def __init__(self, time, values):
        super(VehicleExitEvent, self).__init__(time, values)

        print 'VEHICLE EXIT EVENT: ', values
registry.append(VehicleExitEvent)

class WeaponEvent(BaseEvent):

    ID = 'WP'
    CALLBACK = 'on_weapon'

    def __init__(self, time, values):
        super(WeaponEvent, self).__init__(time, values)

        print 'WEAPON EVENT: ', values
registry.append(WeaponEvent)
