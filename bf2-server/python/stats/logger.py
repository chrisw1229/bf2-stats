import datetime
import fpformat

import host
import bf2.GameLogic
import bf2.ObjectManager
import bf2.PlayerManager

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
    host.registerHandler('PlayerConnect', on_connect, 1)
    host.registerHandler('PlayerDisconnect', on_disconnect, 1)
    host.registerHandler('Reset', on_reset, 1)

    # Register the game status callback
    host.registerGameStatusHandler(on_game_status)

def deinit():
    print 'LOGGER - DEINIT'

    # Log the change in server status
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log('SS', 'stop', timestamp)

    # Cleanup the log file stream
    log_file.close()

def on_connect(player):
    try:
        player_addr = format_player_addr(player)
        player_name = format_player(player)

        log('CN', player_addr, player_name)
    except Exception, err:
        error('connect', err)

def on_disconnect(player):
    try:
        player_addr = format_player_addr(player)
        player_name = format_player(player)

        log('DC', player_addr, player_name)
    except Exception, err:
        error('disconnect', err)

def on_game_status(status):
    try:

        # Log the game status
        map_name = bf2.serverSettings.getMapName()
        if len(map_name) == 0:
            map_name = None
        time_limit = bf2.serverSettings.getTimeLimit()
        score_limit = bf2.serverSettings.getScoreLimit()
        log('GS', format_status(status), map_name, time_limit, score_limit)

        # Log the initial control point states when the game starts
        if status == bf2.GameStatus.Playing:
            control_points = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ControlPoint')
            for control_point in control_points:
                if hasattr(control_point, 'triggerId'):
                    flag_top = 0
                    if control_point.flagPosition == 0:
                        flag_top = 1
                    on_control_point(control_point, flag_top)

        # Update the callback function registrations
        if status == bf2.GameStatus.Playing:
            host.registerHandler('ChangedCommander', on_commander)
            host.registerHandler('ChangedSquadLeader', on_squad_leader)
            host.registerHandler('ChatMessage', on_chat)
            host.registerHandler('ControlPointChangedOwner', on_control_point)
            host.registerHandler('DropKit', on_kit_drop)
            host.registerHandler('EnterVehicle', on_vehicle_enter)
            host.registerHandler('ExitVehicle', on_vehicle_exit)
            host.registerHandler('PickupKit', on_kit_pickup)
            host.registerHandler('PlayerBanned', on_ban)
            host.registerHandler('PlayerChangedSquad', on_squad)
            host.registerHandler('PlayerChangeTeams', on_team)
            host.registerHandler('PlayerChangeWeapon', on_weapon)
            host.registerHandler('PlayerDeath', on_death)
            host.registerHandler('PlayerGiveAmmoPoint', on_ammo)
            host.registerHandler('PlayerHealPoint', on_heal)
            host.registerHandler('PlayerKicked', on_kick)
            host.registerHandler('PlayerKilled', on_kill)
            host.registerHandler('PlayerRepairPoint', on_repair)
            host.registerHandler('PlayerRevived', on_revive)
            host.registerHandler('PlayerScore', on_score)
            host.registerHandler('PlayerSpawn', on_spawn)
            host.registerHandler('PlayerTeamDamagePoint', on_team_damage)
            host.registerHandler('TicketLimitReached', on_ticket_limit)
            host.registerHandler('TimeLimitReached', on_clock_limit)
            host.registerHandler('VehicleDestroyed', on_vehicle_destroy)
    except Exception, err:
        error('game_status', err)

def on_reset(data):
    try:
        log('RS', data)
    except Exception, err:
        error('reset', err)

def on_ammo(giver, bf2_object):
    try:
        receiver = get_owner(bf2_object)
        receiver_name = format_player(receiver)
        receiver_pos = format_player_pos(receiver)
        giver_name = format_player(giver)
        giver_pos = format_player_pos(giver)

        log('AM', receiver_name, receiver_pos, giver_name, giver_pos)
    except Exception, err:
        error('ammo', err)

def on_ban(player, time, ban_type):
    try:
        player_name = format_player(player)

        log('BN', player_name, time, ban_type)
    except Exception, err:
        error('ban', err)

def on_chat(player_index, text, channel_id, flags):
    try:

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
        if text.startswith('HUD_CHAT_DEADPREFIX'):
            text = text[len('HUD_CHAT_DEADPREFIX'):]

        # Format the channel name
        channel_name = channel_id.lower()

        log('CH', channel_name, player_name, text)
    except Exception, err:
        error('chat', err)

def on_clock_limit(value):
    try:
        log('CL', value)
    except Exception, err:
        error('clock_limit', err)

def on_commander(team_id, old_player, new_player):
    try:
        team_name = format_team(new_player.getTeam())
        new_player_name = format_player(new_player)

        log('CM', team_name, new_player_name)
    except Exception, err:
        log('commander', err)

def on_control_point(control_point, flag_top):
    try:
        cp_id = control_point.triggerId
        cp_pos = format_pos(control_point)
        flag_state = format_flag_state(control_point.flagPosition)
        team_name = format_team(control_point.cp_getParam('team'))

        log('CP', cp_id, cp_pos, flag_state, team_name)
    except Exception, err:
        error('control_point', err)

def on_death(victim, bf2_object):
    try:
        victim_name = format_player(victim)
        victim_pos = format_player_pos(victim)

        log('DT', victim_name, victim_pos)
    except Exception, err:
        error('death', err)

def on_heal(giver, bf2_object):
    try:
        receiver = get_owner(bf2_object)
        receiver_name = format_player(receiver)
        receiver_pos = format_player_pos(receiver)
        giver_name = format_player(giver)
        giver_pos = format_player_pos(giver)

        log('HL', receiver_name, receiver_pos, giver_name, giver_pos)
    except Exception, err:
        error('heal', err)

def on_kick(player):
    try:
        player_name = format_player(player)

        log('KC', player_name)
    except Exception, err:
        error('kick', err)

def on_kill(victim, attacker, weapon, assists, bf2_object):
    try:
        vehicle = None
        if (attacker == None and weapon == None and bf2_object != None
                and hasattr(bf2_object, 'lastDrivingPlayerIndex')):

            # Find the last driver for empty vehicle kills
            attacker = bf2.playerManager.getPlayerByIndex(bf2_object.lastDrivingPlayerIndex)
            vehicle = bf2_object
        elif attacker != None and not is_soldier(attacker.getVehicle()):

            # Get the current vehicle for the attacker
            vehicle = attacker.getVehicle()

        victim_name = format_player(victim)
        victim_pos = format_player_pos(victim)
        attacker_name = format_player(attacker)
        attacker_pos = format_player_pos(attacker)
        weapon_name = format_weapon(weapon)
        vehicle_name = format_vehicle(vehicle)

        log('KL', victim_name, victim_pos, attacker_name, attacker_pos, weapon_name, vehicle_name)
    except Exception, err:
        error('kill', err)

    # Log any assists to the kill
    try:
        if assists:
            for assist in assists:
                assister = assist[0]
                assister_name = format_player(assister)
                assister_pos = format_player_pos(assister)
                assist_type = format_assist_type(assist[1])

                log('AS', assister_name, assister_pos, assist_type)
    except Exception, err:
        error('assist', err)

def on_kit_drop(player, kit):
    try:
        player_name = format_player(player)
        player_pos = format_player_pos(player)
        kit_name = format_kit(kit)

        log('KD', player_name, player_pos, kit_name)
    except Exception, err:
        error('kit_drop', err)

def on_kit_pickup(player, kit):
    try:
        player_name = format_player(player)
        player_pos = format_player_pos(player)
        kit_name = format_kit(kit)

        log('KP', player_name, player_pos, kit_name)
    except Exception, err:
        error('kit_pickup', err)

def on_repair(giver, vehicle):
    try:
        vehicle_name = format_vehicle(vehicle)
        vehicle_pos = format_pos(vehicle)
        giver_name = format_player(giver)
        giver_pos = format_player_pos(giver)

        log('RP', vehicle_name, vehicle_pos, giver_name, giver_pos)
    except Exception, err:
        error('repair', err)

def on_revive(receiver, giver):
    try:
        receiver_name = format_player(receiver)
        receiver_pos = format_player_pos(receiver)
        giver_name = format_player(giver)
        giver_pos = format_player_pos(giver)

        log('RV', receiver_name, receiver_pos, giver_name, giver_pos)
    except Exception, err:
        error('revive', err)

def on_score(player, difference):
    try:
        player_name = format_player(player)

        log('SC', player_name, difference)
    except Exception, err:
        error('score', err)

def on_spawn(player, bf2_object):
    try:
        player_name = format_player(player)
        player_pos = format_player_pos(player)
        team_name = format_team(player.getTeam())

        log('SP', player_name, player_pos, team_name)
    except Exception, err:
        error('spawn', err)

def on_squad(player, old_squad_id, new_squad_id):
    try:
        player_name = format_player(player)
        squad_name = format_player_squad(player)

        log('SQ', player_name, squad_name)
    except Exception, err:
        error('squad', err)

def on_squad_leader(squad_id, old_player, new_player):
    try:
        squad_name = format_player_squad(new_player)
        new_player_name = format_player(new_player)

        log('SL', squad_name, new_player_name)
    except Exception, err:
        log('squad_leader', err)

def on_team(player, human_has_spawned):
    try:
        player_name = format_player(player)
        team_name = format_team(player.getTeam())

        log('TM', player_name, team_name)
    except Exception, err:
        error('team', err)

def on_team_damage(attacker, bf2_object):
    try:
        victim = get_owner(bf2_object)
        victim_name = format_player(victim)
        victim_pos = format_player_pos(victim)
        attacker_name = format_player(attacker)
        attacker_pos = format_player_pos(attacker)

        log('TD', victim_name, victim_pos, attacker_name, attacker_pos)
    except Exception, err:
        error('team_damage', err)

def on_ticket_limit(team_id, limit_id):
    try:
        team_name = format_team(team_id)

        log('TL', team_name, limit_id)
    except Exception, err:
        error('ticket_limit', err)

def on_vehicle_destroy(vehicle, attacker):
    try:

        # Ignore the actual soldier model vehicle type
        if is_soldier(vehicle):
            return

        vehicle_name = format_vehicle(vehicle)
        vehicle_pos = format_pos(vehicle)
        attacker_name = format_player(attacker)
        attacker_pos = format_player_pos(attacker)

        log('VD', vehicle_name, vehicle_pos, attacker_name, attacker_pos)
    except Exception, err:
        error('vehicle_destroy', err)

def on_vehicle_enter(player, vehicle, free_soldier=False):
    try:

        # Ignore the actual soldier model vehicle type
        if is_soldier(vehicle):
            return

        player_name = format_player(player)
        player_pos = format_player_pos(player)
        vehicle_name = format_vehicle(vehicle)
        vehicle_slot = format_vehicle_slot(vehicle)
        free_flag = format_bool(free_soldier)

        log('VE', player_name, player_pos, vehicle_name, vehicle_slot, free_flag)
    except Exception, err:
        error('vehicle_enter', err)

def on_vehicle_exit(player, vehicle):
    try:

        # Ignore the actual soldier model vehicle type
        if is_soldier(vehicle):
            return

        player_name = format_player(player)
        player_pos = format_player_pos(player)
        vehicle_name = format_vehicle(vehicle)
        vehicle_slot = format_vehicle_slot(vehicle)

        log('VX', player_name, player_pos, vehicle_name, vehicle_slot)
    except Exception, err:
        error('vehicle_exit', err)

def on_weapon(player, old_weapon, new_weapon):
    try:
        player_name = format_player(player)
        player_pos = format_player_pos(player)
        new_weapon_name = format_weapon(new_weapon)

        log('WP', player_name, player_pos, new_weapon_name)
    except Exception, err:
        error('weapon', err)

def format_assist_type(assist_type):
    if assist_type == 1:
        return 'target'
    elif assist_type == 2:
        return 'damage'
    elif assist_type == 3:
        return 'driver'
    return None

def format_bool(value):
    return value == True or value == 1

def format_flag_state(flag_state):
    if flag_state == 0:
        return 'top'
    elif flag_state == 1:
        return 'middle'
    elif flag_state == 2:
        return 'bottom'
    return flag_state

def format_kit(kit):
    if kit and kit.templateName:
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
        return format_pos(player.getVehicle())
    return None

def format_player_squad(player):
    if player and player.getSquadId():
        return format_team(player.getTeam()) + '_' + str(player.getSquadId())
    return None

def format_pos(bf2_object):
    if bf2_object:
        pos = bf2_object.getPosition()
        rot = bf2_object.getRotation()
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
        root_vehicle = bf2.objectManager.getRootParent(vehicle)
        if (root_vehicle and root_vehicle.templateName):
            vehicle_name = root_vehicle.templateName.lower()
            if vehicle_name != 'multiplayerfreecamera':
                if vehicle_name.startswith('wasp_defence'):
                    vehicle_name = 'wasp_defence'
                return vehicle_name
    return None

def format_vehicle_slot(vehicle):
    if vehicle and vehicle.templateName:
        root_vehicle = bf2.objectManager.getRootParent(vehicle)
        if root_vehicle and root_vehicle.templateName:
            vehicle_name = vehicle.templateName.lower()
            if (root_vehicle.templateName == vehicle.templateName
                    and not vehicle_name.startswith('wasp_defence')):
                vehicle_name += '_driver'
            return vehicle_name
        return vehicle.templateName.lower()
    return None

def format_weapon(weapon):
    if weapon and weapon.templateName:
        return weapon.templateName.lower()
    return None

def is_soldier(vehicle):
    return (vehicle and vehicle.templateName
            and getVehicleType(vehicle.templateName) == VEHICLE_TYPE_SOLDIER)

def get_owner(bf2_object):
    if bf2_object and bf2_object.isPlayerControlObject:
        players = bf2_object.getOccupyingPlayers()
        if players and len(players) > 0:
            return players[0]
    return None

def error(callback_type, exception):
    log('ER', callback_type + ' event callback failed: ', exception)

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
