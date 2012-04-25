import datetime
import fpformat

import host
import bf2.PlayerManager
import bf2.GameLogic

from constants import *
from bf2.stats.stats import getStatsMap

logFile = None

def init():
	print 'INIT'

	# Get the current time formatted to name the log file
	timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

	# Build a path to the target log output file
	logFileName = bf2.gameLogic.getModDir() + '/logs/' + '/bf2_' + timestamp + '_log.txt'
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
	print 'DEINIT'

	# Unregister the pre-game callbacks
	host.unregisterHandler('PlayerConnect', onPlayerConnect)
	host.unregisterHandler('PlayerDisconnect', onPlayerDisconnect)
	host.unregisterHandler('Reset', onReset)

	# Unregister the game status callback
	host.unregisterGameStatusHandler(onGameStatus)

	# Cleanup the log file stream
	logFile.close()

def onPlayerConnect(player):
	log('CN', [player.getAddress(), player.getProfileId(), formatPlayerName(player)])

def onPlayerDisconnect(player):
	log('DC', [player.getAddress(), player.getProfileId(), formatPlayerName(player)])

def onReset(data):
	log('RS', [data])

def onGameStatus(status):
	log('GS', [formatStatus(status)])

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
	teamName = formatTeam(player.getTeam())
	oldId = oldPlayer.getProfileId()
	oldName = formatPlayerName(oldPlayer)
	newId = newPlayer.getProfileId()
	newName = formatPlayerName(newPlayer)

	log('CR', [teamName, oldId, oldName, newId, newName])

def onChangedSquadLeader(squadId, oldPlayer, newPlayer):
	values = []
	values.extend([squadId])
	values.extend(formatPlayer(oldPlayer))
	values.extend(formatPlayer(newPlayer))

	log('SL', values)

def onChatMessage(playerId, text, channelId, flags):
	log('CM', [playerId, text, channelId, flags])

def onControlPointChangedOwner(controlPoint, teamId):
	log('CP', [controlPoint, teamId])

def onDropKit(player, kit):
	values = []
	values.extend(formatPlayer(player))
	values.extend([formatKit(kit)])

	log('DK', values)

def onEnterVehicle(player, vehicle, freeSoldier = False):
	values = []
	values.extend(formatPlayer(player))
	values.extend([formatVehicle(vehicle), freeSoldier])

	log('EV', values)

def onExitVehicle(player, vehicle):
	values = []
	values.extend(formatPlayer(player))
	values.extend([formatVehicle(vehicle)])

	log('XV', values)

def onPickupKit(player, kit):
	values = []
	values.extend(formatPlayer(player))
	values.extend([formatKit(kit)])

	log('PK', values)

def onPlayerBanned(player, time, type):
	values = []
	values.extend(formatPlayer(player))
	values.extend([time, type])

	log('BN', [player, time, type])

def onPlayerChangedSquad(player, oldSquad, newSquad):
	values = []
	values.extend(formatPlayer(player))
	values.extend([oldSquad, newSquad])

	log('SQ', [player, oldSquad, newSquad])

def onPlayerChangeTeams(player, humanHasSpawned):
	values = []
	values.extend(formatPlayer(player))
	values.extend([humanHasSpawned])

	log('TM', values)

def onPlayerChangeWeapon(player, oldWeapon, newWeapon):
	values = []
	values.extend(formatPlayer(player))
	values.extend([formatWeapon(oldWeapon), formatWeapon(newWeapon)])

	log('WP', values)

def onPlayerDeath(victim, object):
	values = []
	values.extend(formatPlayer(victim))
	values.extend([object])

	log('DT', values)

def onPlayerGiveAmmoPoint(giver, object):
	values = []
	values.extend(formatPlayer(giver))
	values.extend([object])

	log('AP', values)

def onPlayerHealPoint(giver, object):
	values = []
	values.extend(formatPlayer(giver))
	values.extend([object])

	log('HP', values)

def onPlayerKicked(player):
	log('KK', formatPlayer(player))

def onPlayerKilled(victim, attacker, weapon, assists, object):
	values = []
	values.extend(formatPlayer(victim))
	values.extend(formatPlayer(attacker))
	values.extend([formatWeapon(weapon), assists, object])

	log('KL', values)

def onPlayerRepairPoint(giver, object):
	values = []
	values.extend(formatPlayer(giver))
	values.extend([object])

	log('RP', values)

def onPlayerRevived(victim, reviver):
	values = []
	values.extend(formatPlayer(victim))
	values.extend(formatPlayer(reviver))

	log('RV', values)

def onPlayerScore(player, difference):
	values = []
	values.extend(formatPlayer(player))
	values.extend([difference])

	log('SC', values)

def onPlayerSpawn(player, object):
	values = []
	values.extend(formatPlayer(player))
	values.extend([object])

	log('SP', values)

def onPlayerTeamDamagePoint(attacker, victim):
	values = []
	values.extend(formatPlayer(victim))
	values.extend(formatPlayer(attacker))

	log('TP', values)

def onTicketLimitReached(teamId, limitId):
	log('TL', [teamId, limitId])

def onTimeLimitReached(value):
	log('RL', [value])

def onVehicleDestroyed(vehicle, attacker):
	values = []
	values.extend([formatVehicle(vehicle)])
	values.extend(formatPlayer(attacker))

	log('VD', values)

def formatKit(kit):
	kitName = None
	if kit != None:
		kitName = kit.templateName.lower()
	return kitName

def formatPlayer(player):
	playerId = player.getProfileId()
	playerName = formatPlayerName(player)
	playerTeam = formatTeam(player.getTeam())
	playerVehicle = player.getVehicle()
	playerPosition = formatPosition(playerVehicle.getPosition())

	values = [playerId, playerName, playerTeam]
	values.extend(playerPosition)
	return values

def formatPlayerName(player):
	name = None
	if player != None:
		name = player.getName().strip()
	return name

def formatPosition(position):
	worldSize = bf2.gameLogic.getWorldSize()
	scale = [512.0 / worldSize[0], 1, 512.0 / worldSize[1]]
	scaled = [position[0] * scale[0], position[1] * scale[1], position[2] * scale[2]]
	return [fpformat.fix(scaled[0], 1), fpformat.fix(scaled[1], 1), fpformat.fix(scaled[2], 1)]

def formatStatus(status):
	name = None
	if status == bf2.GameStatus.Playing:
		name = 'Playing'
	elif status == bf2.GameStatus.EndGame:
		name = 'EndGame'
	elif status == bf2.GameStatus.PreGame:
		name = 'PreGame'
	elif status == bf2.GameStatus.Paused:
		name = 'Paused'
	elif status == bf2.GameStatus.RestartServer:
		name = 'RestartServer'
	elif status == bf2.GameStatus.NotConnected:
		name = 'NotConnected'
	else:
		name = 'Unknown'
	return name

def formatTeam(team):
	name = None
	if team != None:
		name = bf2.gameLogic.getTeamName(team).lower()
	return name

def formatVehicle(vehicle):
	name = None
	if vehicle != None:
		name = vehicle.templateName.lower()
	return name

def formatWeapon(weapon):
	name = None
	if weapon != None:
		name = weapon.templateName.lower()
	return name

def log(type, values = None):

	# Validate the given parameters
	assert type != None and len(type) == 2, 'Invalid log type: %s' % `type`

	# Write the log entry time stamp
	logFile.write(str(int(host.timer_getWallTime())).zfill(5))
	logFile.write(';')

	# Write the required type of log
	logFile.write(type)

	# Write any optional log values with delimiters
	if values:
		for value in values:
			logFile.write(';')
			logFile.write(str(value))
		
	# Make sure the log entry is output to disk immediately
	logFile.write('\n')
	logFile.flush()
