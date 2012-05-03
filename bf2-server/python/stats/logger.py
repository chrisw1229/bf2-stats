import datetime
import fpformat

import host
import bf2.PlayerManager
import bf2.GameLogic

from constants import *
from bf2.stats.stats import getStatsMap

logFile = None

def init():
	print 'LOGGER - INIT'

	# Build a path to the target log output file
	logFileName = bf2.gameLogic.getModDir() + '/logs/' + '/bf2_game_log.txt'
	print 'Creating log file: ', logFileName

	# Open the log file in line-buffered write mode
	global logFile
	try:
		logFile = open(logFileName, 'w', 1)
	except IOError:
		print 'Unable to open log file: ', logFileName
		return

	# Register the pre-game callbacks
	host.registerHandler('PlayerConnect', onPlayerConnect, 1)
	host.registerHandler('PlayerDisconnect', onPlayerDisconnect, 1)
	host.registerHandler('Reset', onReset, 1)

	# Register the game status callback
	host.registerGameStatusHandler(onGameStatus)

def deinit():
	print 'LOGGER - DEINIT'

	# Unregister the pre-game callbacks
	host.unregisterHandler('PlayerConnect', onPlayerConnect)
	host.unregisterHandler('PlayerDisconnect', onPlayerDisconnect)
	host.unregisterHandler('Reset', onReset)

	# Unregister the game status callback
	host.unregisterGameStatusHandler(onGameStatus)

	# Cleanup the log file stream
	logFile.close()

def onPlayerConnect(player):
	playerAddr = formatPlayerAddr(player)
	playerId = player.getProfileId()
	playerIndex = player.index
	playerName = formatPlayer(player)

	log('CN', playerAddr, playerId, playerIndex, playerName)

def onPlayerDisconnect(player):
	playerAddr = formatPlayerAddr(player)
	playerId = player.getProfileId()
	playerIndex = player.index
	playerName = formatPlayer(player)

	log('DC', playerAddr, playerId, playerIndex, playerName)

def onReset(data):
	log('RS', data)

def onGameStatus(status):
	log('GS', formatStatus(status))

	# Update the callback function registrations
	if status == bf2.GameStatus.Playing:
		host.registerHandler('ChangedCommander', onChangedCommander)
		host.registerHandler('ChangedSquadLeader', onChangedSquadLeader)
		host.registerHandler('ChatMessage', onChatMessage)
		host.registerHandler('ControlPointChangedOwner', onControlPointChangedOwner)
		host.registerHandler('DropKit', onDropKit)
		host.registerHandler('EnterVehicle', onEnterVehicle)
		host.registerHandler('ExitVehicle', onExitVehicle)
		host.registerHandler('PickupKit', onPickupKit)
		host.registerHandler('PlayerBanned', onPlayerBanned)
		host.registerHandler('PlayerChangedSquad', onPlayerChangedSquad)
		host.registerHandler('PlayerChangeTeams', onPlayerChangeTeams)
		host.registerHandler('PlayerChangeWeapon', onPlayerChangeWeapon)
		host.registerHandler('PlayerDeath', onPlayerDeath)
		host.registerHandler('PlayerGiveAmmoPoint', onPlayerGiveAmmoPoint)
		host.registerHandler('PlayerHealPoint', onPlayerHealPoint)
		host.registerHandler('PlayerKicked', onPlayerKicked)
		host.registerHandler('PlayerKilled', onPlayerKilled)
		host.registerHandler('PlayerRepairPoint', onPlayerRepairPoint)
		host.registerHandler('PlayerRevived', onPlayerRevived)
		host.registerHandler('PlayerScore', onPlayerScore)
		host.registerHandler('PlayerSpawn', onPlayerSpawn)
		host.registerHandler('PlayerTeamDamagePoint', onPlayerTeamDamagePoint)
		host.registerHandler('TicketLimitReached', onTicketLimitReached)
		host.registerHandler('TimeLimitReached', onTimeLimitReached)
		host.registerHandler('VehicleDestroyed', onVehicleDestroyed)
	elif status == bf2.GameStatus.EndGame:
		host.unregisterHandler('ChangedCommander', onChangedCommander)
		host.unregisterHandler('ChangedSquadLeader', onChangedSquadLeader)
		host.unregisterHandler('ChatMessage', onChatMessage)
		host.unregisterHandler('ControlPointChangedOwner', onControlPointChangedOwner)
		host.unregisterHandler('DropKit', onDropKit)
		host.unregisterHandler('EnterVehicle', onEnterVehicle)
		host.unregisterHandler('ExitVehicle', onExitVehicle)
		host.unregisterHandler('PickupKit', onPickupKit)
		host.unregisterHandler('PlayerBanned', onPlayerBanned)
		host.unregisterHandler('PlayerChangedSquad', onPlayerChangedSquad)
		host.unregisterHandler('PlayerChangeTeams', onPlayerChangeTeams)
		host.unregisterHandler('PlayerChangeWeapon', onPlayerChangeWeapon)
		host.unregisterHandler('PlayerDeath', onPlayerDeath)
		host.unregisterHandler('PlayerGiveAmmoPoint', onPlayerGiveAmmoPoint)
		host.unregisterHandler('PlayerHealPoint', onPlayerHealPoint)
		host.unregisterHandler('PlayerKicked', onPlayerKicked)
		host.unregisterHandler('PlayerKilled', onPlayerKilled)
		host.unregisterHandler('PlayerRepairPoint', onPlayerRepairPoint)
		host.unregisterHandler('PlayerRevived', onPlayerRevived)
		host.unregisterHandler('PlayerScore', onPlayerScore)
		host.unregisterHandler('PlayerSpawn', onPlayerSpawn)
		host.unregisterHandler('PlayerTeamDamagePoint', onPlayerTeamDamagePoint)
		host.unregisterHandler('TicketLimitReached', onTicketLimitReached)
		host.unregisterHandler('TimeLimitReached', onTimeLimitReached)
		host.unregisterHandler('VehicleDestroyed', onVehicleDestroyed)

def onChangedCommander(teamId, oldPlayer, newPlayer):
	teamName = formatTeam(newPlayer.getTeam())
	newPlayerName = formatPlayer(newPlayer)

	log('CR', teamName, newPlayerName)

def onChangedSquadLeader(squadId, oldPlayer, newPlayer):
	newPlayerName = formatPlayer(newPlayer)

	log('SL', squadId, newPlayerName)

def onChatMessage(playerId, text, channelId, flags):

	# Determine the name of the player that sent the message
	playerName = playerId
	if playerId < 0:
		playerName = 'Server'
	else:
		player = bf2.playerManager.getPlayerByIndex(playerId)
		if player:
			playerName = formatPlayer(player)

	# Remove localization prefixes from messages
	if text.startswith('HUD_TEXT_CHAT_TEAM'):
		text = text[len('HUD_TEXT_CHAT_TEAM'):]
	elif text.startswith('HUD_TEXT_CHAT_SQUAD'):
		text = text[len('HUD_TEXT_CHAT_SQUAD'):]
	elif text.startswith('HUD_CHAT_DEADPREFIX'):
		text = text[len('HUD_CHAT_DEADPREFIX'):]

	# Format the channel name
	channelName = channelId.lower()

	log('CM', channelName, playerName, text)

def onControlPointChangedOwner(controlPoint, teamId):
	log('CP', controlPoint, teamId)

def onDropKit(player, kit):
	playerName = formatPlayer(player)
	playerPos = formatPlayerPos(player)
	kitName = formatKit(kit)

	log('DK', playerName, playerPos, kitName)

def onEnterVehicle(player, vehicle, freeSoldier = False):
	playerName = formatPlayer(player)
	playerPos = formatPlayerPos(player)
	vehicleName = formatVehicle(vehicle)

	log('EV', playerName, playerPos, vehicleName, freeSoldier)

def onExitVehicle(player, vehicle):
	playerName = formatPlayer(player)
	playerPos = formatPlayerPos(player)
	vehicleName = formatVehicle(vehicle)

	log('XV', playerName, playerPos, vehicleName)

def onPickupKit(player, kit):
	playerName = formatPlayer(player)
	playerPos = formatPlayerPos(player)
	kitName = formatKit(kit)

	log('PK', playerName, playerPos, kitName)

def onPlayerBanned(player, time, type):
	playerName = formatPlayer(player)

	log('BN', playerName, time, type)

def onPlayerChangedSquad(player, oldSquadId, newSquadId):
	playerName = formatPlayer(player)

	log('SQ', playerName, newSquadId)

def onPlayerChangeTeams(player, humanHasSpawned):
	playerName = formatPlayer(player)
	teamName = formatTeam(player.getTeam())

	log('TM', playerName, teamName)

def onPlayerChangeWeapon(player, oldWeapon, newWeapon):
	playerName = formatPlayer(player)
	playerPos = formatPlayerPos(player)
	newWeaponName = formatWeapon(newWeapon)

	log('WP', playerName, playerPos, newWeaponName)

def onPlayerDeath(victim, object):
	victimName = formatPlayer(victim)
	victimPos = formatPlayerPos(victim)

	log('DT', victimName, victimPos, object)

def onPlayerGiveAmmoPoint(giver, object):
	giverName = formatPlayer(giver)
	giverPos = formatPlayerPos(giver)

	log('AP', giverName, giverPos, object)

def onPlayerHealPoint(giver, object):
	giverName = formatPlayer(giver)
	giverPos = formatPlayerPos(giver)

	log('HP', giverName, giverPos, object)

def onPlayerKicked(player):
	playerName = formatPlayer(player)

	log('KK', playerName)

def onPlayerKilled(victim, attacker, weapon, assists, object):
	victimName = formatPlayer(victim)
	victimPos = formatPlayerPos(victim)
	attackerName = formatPlayer(attacker)
	attackerPos = formatPlayerPos(attacker)
	weaponName = formatWeapon(weapon)

	log('KL', victimName, victimPos, attackerName, attackerPos, weaponName, assists, object)

def onPlayerRepairPoint(giver, object):
	giverName = formatPlayer(giver)
	giverPos = formatPlayerPos(giver)

	log('RP', giverName, giverPos, object)

def onPlayerRevived(victim, reviver):
	victimName = formatPlayer(victim)
	victimPos = formatPlayerPos(victim)
	reviverName = formatPlayer(reviver)
	reviverPos = formatPlayerPos(reviver)

	log('RV', victimName, victimPos, reviverName, reviverPos)

def onPlayerScore(player, difference):
	playerName = formatPlayer(player)

	log('SC', playerName, difference)

def onPlayerSpawn(player, object):
	playerName = formatPlayer(player)
	playerPos = formatPlayerPos(player)
	playerTeam = formatTeam(player.getTeam())

	log('SP', playerName, playerPos, playerTeam)

def onPlayerTeamDamagePoint(attacker, victim):
	victimName = formatPlayer(victim)
	victimPos = formatPlayerPos(victim)
	attackerName = formatPlayer(attacker)
	attackerPos = formatPlayerPos(attacker)

	log('TP', victimName, victimPos, attackerName, attackerPos)

def onTicketLimitReached(teamId, limitId):
	teamName = formatTeam(teamId)

	log('TL', teamName, limitId)

def onTimeLimitReached(value):
	log('CL', value)

def onVehicleDestroyed(vehicle, attacker):
	vehicleName = formatVehicle(vehicle)
	vehiclePos = formatPos(vehicle.getPosition())
	attackerName = formatPlayer(attacker)
	attackerPos = formatPlayerPos(attacker)

	log('VD', vehicleName, vehiclePos, attackerName, attackerPos)

def formatKit(kit):
	if kit:
		return kit.templateName.lower()
	return None

def formatPlayer(player):
	if player:
		return player.getName().strip()
	return None

def formatPlayerAddr(player):
	if player and player.getAddress() != 'N/A':
		return player.getAddress()
	return None

def formatPlayerPos(player):
	if player and player.getVehicle():
		return formatPos(player.getVehicle().getPosition())
	return None

def formatPos(position):
	if position and len(position) == 3:
		return (fpformat.fix(position[0], 1) + ','
				+ fpformat.fix(position[1], 1) + ','
				+ fpformat.fix(position[2], 1))
	return None

def formatStatus(status):
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

def formatTeam(team):
	if team:
		return bf2.gameLogic.getTeamName(team).lower()
	return None

def formatVehicle(vehicle):
	if vehicle:
		return vehicle.templateName.lower()
	return None

def formatWeapon(weapon):
	if weapon:
		return weapon.templateName.lower()
	return None

def log(type, *args):

	# Validate the given parameters
	assert type and len(type) == 2, 'Invalid log type: %s' % `type`

	# Write the log entry time stamp
	logFile.write(str(int(host.timer_getWallTime())).zfill(5))
	logFile.write(';')

	# Write the required type of log
	logFile.write(type)

	# Write any optional log values with delimiters
	if args:
		for arg in args:
			logFile.write(';')
			logFile.write(str(arg))
		
	# Make sure the log entry is output to disk immediately
	logFile.write('\n')
	logFile.flush()
