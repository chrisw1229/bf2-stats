import datetime
import fpformat

import host
import bf2.PlayerManager
import bf2.GameLogic

from constants import *
from bf2.stats.stats import getStatsMap

log_file = None

def init():
    print 'LOGGER - INIT'

    # Build a path to the target log output file
    log_name = bf2.gameLogic.getModDir() + '/logs/' + '/bf2_game_log.txt'
    print 'Creating log file: ', log_name

    # Open the log file in line-buffered append mode
    global log_file
    try:
        log_file = open(log_name, 'a', 1)
    except IOError:
        print 'Unable to open log file: ', log_name
        return

    # Log the change in server status
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log('SS', 'start', timestamp)

    # Register the pre-game callbacks
    host.registerHandler('PlayerConnect', on_player_connect, 1)
    host.registerHandler('PlayerDisconnect', on_player_disconnect, 1)
    host.registerHandler('Reset', on_reset, 1)

    # Register the game status callback
    host.registerGameStatusHandler(on_game_status)

def deinit():
    print 'LOGGER - DEINIT'

    # Unregister the pre-game callbacks
    host.unregisterHandler('PlayerConnect', on_player_connect)
    host.unregisterHandler('PlayerDisconnect', on_player_disconnect)
    host.unregisterHandler('Reset', on_reset)

    # Unregister the game status callback
    host.unregisterGameStatusHandler(on_game_status)

    # Log the change in server status
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log('SS', 'stop', timestamp)

    # Cleanup the log file stream
    log_file.close()

def on_player_connect(player):
    player_addr = format_player_addr(player)
    player_name = format_player(player)

    log('CN', player_addr, player_name)

def on_player_disconnect(player):
    player_addr = format_player_addr(player)
    player_name = format_player(player)

    log('DC', player_addr, player_name)

def on_reset(data):
    log('RS', data)

def on_game_status(status):

    # Log the game status
    if status == bf2.GameStatus.Playing:
        map_name = bf2.serverSettings.getMapName()
        time_limit = bf2.serverSettings.getTimeLimit()
        score_limit = bf2.serverSettings.getScoreLimit()

        log('GS', format_status(status), map_name, time_limit, score_limit)
    else:
        log('GS', format_status(status))

    # Update the callback function registrations
    if status == bf2.GameStatus.Playing:
        host.registerHandler('ChangedCommander', on_changed_commander)
        host.registerHandler('ChangedSquadLeader', on_changed_squad_leader)
        host.registerHandler('ChatMessage', on_chat_message)
        host.registerHandler('ControlPointChangedOwner', on_control_point_changed_owner)
        host.registerHandler('DropKit', on_drop_kit)
        host.registerHandler('EnterVehicle', on_enter_vehicle)
        host.registerHandler('ExitVehicle', on_exit_vehicle)
        host.registerHandler('PickupKit', on_pickup_kit)
        host.registerHandler('PlayerBanned', on_player_banned)
        host.registerHandler('PlayerChangedSquad', on_player_changed_squad)
        host.registerHandler('PlayerChangeTeams', on_player_change_teams)
        host.registerHandler('PlayerChangeWeapon', on_player_change_weapon)
        host.registerHandler('PlayerDeath', on_player_death)
        host.registerHandler('PlayerGiveAmmoPoint', on_player_give_ammo_point)
        host.registerHandler('PlayerHealPoint', on_player_heal_point)
        host.registerHandler('PlayerKicked', on_player_kicked)
        host.registerHandler('PlayerKilled', on_player_killed)
        host.registerHandler('PlayerRepairPoint', on_player_repair_point)
        host.registerHandler('PlayerRevived', on_player_revived)
        host.registerHandler('PlayerScore', on_player_score)
        host.registerHandler('PlayerSpawn', on_player_spawn)
        host.registerHandler('PlayerTeamDamagePoint', on_player_team_damage_point)
        host.registerHandler('TicketLimitReached', on_ticket_limit_reached)
        host.registerHandler('TimeLimitReached', on_time_limit_reached)
        host.registerHandler('VehicleDestroyed', on_vehicle_destroyed)
    elif status == bf2.GameStatus.EndGame:
        host.unregisterHandler('ChangedCommander', on_changed_commander)
        host.unregisterHandler('ChangedSquadLeader', on_changed_squad_leader)
        host.unregisterHandler('ChatMessage', on_chat_message)
        host.unregisterHandler('ControlPointChangedOwner', on_control_point_changed_owner)
        host.unregisterHandler('DropKit', on_drop_kit)
        host.unregisterHandler('EnterVehicle', on_enter_vehicle)
        host.unregisterHandler('ExitVehicle', on_exit_vehicle)
        host.unregisterHandler('PickupKit', on_pickup_kit)
        host.unregisterHandler('PlayerBanned', on_player_banned)
        host.unregisterHandler('PlayerChangedSquad', on_player_changed_squad)
        host.unregisterHandler('PlayerChangeTeams', on_player_change_teams)
        host.unregisterHandler('PlayerChangeWeapon', on_player_change_weapon)
        host.unregisterHandler('PlayerDeath', on_player_death)
        host.unregisterHandler('PlayerGiveAmmoPoint', on_player_give_ammo_point)
        host.unregisterHandler('PlayerHealPoint', on_player_heal_point)
        host.unregisterHandler('PlayerKicked', on_player_kicked)
        host.unregisterHandler('PlayerKilled', on_player_killed)
        host.unregisterHandler('PlayerRepairPoint', on_player_repair_point)
        host.unregisterHandler('PlayerRevived', on_player_revived)
        host.unregisterHandler('PlayerScore', on_player_score)
        host.unregisterHandler('PlayerSpawn', on_player_spawn)
        host.unregisterHandler('PlayerTeamDamagePoint', on_player_team_damage_point)
        host.unregisterHandler('TicketLimitReached', on_ticket_limit_reached)
        host.unregisterHandler('TimeLimitReached', on_time_limit_reached)
        host.unregisterHandler('VehicleDestroyed', on_vehicle_destroyed)

def on_changed_commander(team_id, old_player, new_player):
    team_name = format_team(team_id)
    new_player_name = format_player(new_player)

    log('CR', team_name, new_player_name)

def on_changed_squad_leader(squad_id, old_player, new_player):
    new_player_name = format_player(new_player)

    log('SL', squad_id, new_player_name)

def on_chat_message(player_index, text, channel_id, flags):

    # Determine the name of the player that sent the message
    player_name = player_index
    if player_index < 0:
        player_name = 'Server'
    else:
        player = bf2.playerManager.getPlayerByIndex(player_index)
        if player:
            player_name = format_player(player)

    # Remove localization prefixes from messages
    if text.startswith('HUD_TEXT_CHAT_TEAM'):
        text = text[len('HUD_TEXT_CHAT_TEAM'):]
    elif text.startswith('HUD_TEXT_CHAT_SQUAD'):
        text = text[len('HUD_TEXT_CHAT_SQUAD'):]
    elif text.startswith('HUD_CHAT_DEADPREFIX'):
        text = text[len('HUD_CHAT_DEADPREFIX'):]

    # Format the channel name
    channel_name = channel_id.lower()

    log('CM', channel_name, player_name, text)

def on_control_point_changed_owner(control_point, team_id):
    team_name = format_team(team_id)

    log('CP', control_point, team_name)

def on_drop_kit(player, kit):
    player_name = format_player(player)
    player_pos = format_player_pos(player)
    kit_name = format_kit(kit)

    log('DK', player_name, player_pos, kit_name)

def on_enter_vehicle(player, vehicle, free_soldier=False):

    # Ignore the actual soldier model vehicle type
    if is_soldier(vehicle):
        return

    player_name = format_player(player)
    player_pos = format_player_pos(player)
    vehicle_name = format_vehicle(vehicle)

    log('EV', player_name, player_pos, vehicle_name, free_soldier)

def on_exit_vehicle(player, vehicle):

    # Ignore the actual soldier model vehicle type
    if is_soldier(vehicle):
        return

    player_name = format_player(player)
    player_pos = format_player_pos(player)
    vehicle_name = format_vehicle(vehicle)

    log('XV', player_name, player_pos, vehicle_name)

def on_pickup_kit(player, kit):
    player_name = format_player(player)
    player_pos = format_player_pos(player)
    kit_name = format_kit(kit)

    log('PK', player_name, player_pos, kit_name)

def on_player_banned(player, time, ban_type):
    player_name = format_player(player)

    log('BN', player_name, time, ban_type)

def on_player_changed_squad(player, old_squad_id, new_squad_id):
    player_name = format_player(player)

    log('SQ', player_name, new_squad_id)

def on_player_change_teams(player, human_has_spawned):
    player_name = format_player(player)
    team_name = format_team(player.getTeam())

    log('TM', player_name, team_name)

def on_player_change_weapon(player, old_weapon, new_weapon):
    player_name = format_player(player)
    player_pos = format_player_pos(player)
    new_weapon_name = format_weapon(new_weapon)

    log('WP', player_name, player_pos, new_weapon_name)

def on_player_death(victim, bf2_object):
    victim_name = format_player(victim)
    victim_pos = format_player_pos(victim)

    log('DT', victim_name, victim_pos, bf2_object)

def on_player_give_ammo_point(giver, bf2_object):
    giver_name = format_player(giver)
    giver_pos = format_player_pos(giver)

    log('AP', giver_name, giver_pos, bf2_object)

def on_player_heal_point(giver, bf2_object):
    giver_name = format_player(giver)
    giver_pos = format_player_pos(giver)

    log('HP', giver_name, giver_pos, bf2_object)

def on_player_kicked(player):
    player_name = format_player(player)

    log('KK', player_name)

def on_player_killed(victim, attacker, weapon, assists, bf2_object):
    victim_name = format_player(victim)
    victim_pos = format_player_pos(victim)
    attacker_name = format_player(attacker)
    attacker_pos = format_player_pos(attacker)
    weapon_name = format_weapon(weapon)

    log('KL', victim_name, victim_pos, attacker_name, attacker_pos, weapon_name, assists, bf2_object)

def on_player_repair_point(giver, bf2_object):
    giver_name = format_player(giver)
    giver_pos = format_player_pos(giver)

    log('RP', giver_name, giver_pos, bf2_object)

def on_player_revived(victim, reviver):
    victim_name = format_player(victim)
    victim_pos = format_player_pos(victim)
    reviver_name = format_player(reviver)
    reviver_pos = format_player_pos(reviver)

    log('RV', victim_name, victim_pos, reviver_name, reviver_pos)

def on_player_score(player, difference):
    player_name = format_player(player)

    log('SC', player_name, difference)

def on_player_spawn(player, bf2_object):
    player_name = format_player(player)
    player_pos = format_player_pos(player)
    team_name = format_team(player.getTeam())

    log('SP', player_name, player_pos, team_name)

def on_player_team_damage_point(attacker, victim):
    victim_name = format_player(victim)
    victim_pos = format_player_pos(victim)
    attacker_name = format_player(attacker)
    attacker_pos = format_player_pos(attacker)

    log('TP', victim_name, victim_pos, attacker_name, attacker_pos)

def on_ticket_limit_reached(team_id, limit_id):
    team_name = format_team(team_id)

    log('TL', team_name, limit_id)

def on_time_limit_reached(value):
    log('CL', value)

def on_vehicle_destroyed(vehicle, attacker):

    # Ignore the actual soldier model vehicle type
    if is_soldier(vehicle):
        return

    vehicle_name = format_vehicle(vehicle)
    vehicle_pos = format_vehicle_pos(vehicle)
    attacker_name = format_player(attacker)
    attacker_pos = format_player_pos(attacker)

    log('VD', vehicle_name, vehicle_pos, attacker_name, attacker_pos)

def format_kit(kit):
    if kit:
        return kit.templateName.lower()
    return None

def format_player(player):
    if player:
        return player.getName().strip()
    return None

def format_player_addr(player):
    if player and player.getAddress() != 'N/A':
        return player.getAddress()
    return None

def format_player_pos(player):
    if player:
        return format_vehicle_pos(player.getVehicle())
    return None

def format_vehicle_pos(vehicle):
    if vehicle:
        pos = vehicle.getPosition()
        rot = vehicle.getRotation()
        if pos and len(pos) == 3 and rot and len(rot) == 3:
            return (fpformat.fix(pos[0], 1) + ','
                    + fpformat.fix(pos[1], 1) + ','
                    + fpformat.fix(pos[2], 1) + ','
                    + fpformat.fix(rot[0], 1))
    return None

def format_status(status):
    if status == bf2.GameStatus.Playing:
        return 'play'
    elif status == bf2.GameStatus.EndGame:
        return 'end'
    elif status == bf2.GameStatus.PreGame:
        return 'pre'
    elif status == bf2.GameStatus.Paused:
        return 'pause'
    elif status == bf2.GameStatus.RestartServer:
        return 'restart'
    elif status == bf2.GameStatus.NotConnected:
        return 'idle'
    return None

def format_team(team_id):
    if team_id:
        return bf2.gameLogic.getTeamName(team_id).lower()
    return None

def format_vehicle(vehicle):
    if vehicle:
        return vehicle.templateName.lower()
    return None

def format_weapon(weapon):
    if weapon:
        return weapon.templateName.lower()
    return None

def is_soldier(vehicle):
    return vehicle and getVehicleType(vehicle.templateName) == VEHICLE_TYPE_SOLDIER

def log(log_type, *args):

    # Validate the given parameters
    assert log_type and len(log_type) == 2, 'Invalid log type: %s' % `log_type`

    # Write the log entry time stamp
    log_file.write(str(int(host.timer_getWallTime())).zfill(5))
    log_file.write(';')

    # Write the required type of log
    log_file.write(log_type)

    # Write any optional log values with delimiters
    if args:
        for arg in args:
            log_file.write(';')
            log_file.write(str(arg))

    # Make sure the log entry is output to disk immediately
    log_file.write('\n')
    log_file.flush()
