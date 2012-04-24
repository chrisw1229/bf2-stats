import time

import host
import bf2.PlayerManager
import bf2.GameLogic

from constants import *
from bf2.stats.stats import getStatsMap

logFile = None

def init():
	print 'INIT'

	# Get the current time formatted to name the log file
	timestamp = time.strftime('%Y-%m-%d_%H-%M-%S', time.gmtime())

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
	log('CN', player.getAddress(), player.getProfileId(), player.getName())

def onPlayerDisconnect(player):
	log('DC', player.getAddress(), player.getProfileId(), player.getName())

def onReset(data):
	log('RS', data)

def onGameStatus(status):

	# Determine the name of the new game status
	statusName = None
	if status == bf2.GameStatus.Playing:
		statusName = 'Playing'
	elif status == bf2.GameStatus.EndGame:
		statusName = 'EndGame'
	elif status == bf2.GameStatus.PreGame:
		statusName = 'PreGame'
	elif status == bf2.GameStatus.Paused:
		statusName = 'Paused'
	elif status == bf2.GameStatus.RestartServer:
		statusName = 'RestartServer'
	elif status == bf2.GameStatus.NotConnected:
		statusName = 'NotConnected'
	else:
		statusName = 'Unknown'
	log('GS', statusName)

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
	log('CR', teamId, oldPlayer, newPlayer)

def onChangedSquadLeader(squadId, oldPlayer, newPlayer):
	log('SL', squadId, oldPlayer, newPlayer)

def onChatMessage(playerId, text, channelId, flags):
	log('CM', playerId, text, channelId, flags)

def onControlPointChangedOwner(controlPoint, teamId):
	log('CP', controlPoint, teamId)

def onDropKit(player, kit):
	log('DK', player, kit)

def onEnterVehicle(player, vehicle, freeSoldier = False):
	log('EV', player, vehicle, freeSoldier)

def onExitVehicle(player, vehicle):
	log('XV', player, vehicle)

def onPickupKit(player, kit):
	log('PK', player, kit)

def onPlayerBanned(player, time, type):
	log('BN', player, time, type)

def onPlayerChangedSquad(player, oldSquad, newSquad):
	log('SQ', player, oldSquad, newSquad)

def onPlayerChangeTeams(player, humanHasSpawned):
	log('TM', player, humanHasSpawned)

def onPlayerChangeWeapon(player, oldWeapon, newWeapon):
	log('WP', player, oldWeapon, newWeapon)

def onPlayerDeath(victim, object):
	log('DT', victim, object)

def onPlayerGiveAmmoPoint(giver, object):
	log('AP', giver, object)

def onPlayerHealPoint(giver, object):
	log('HP', giver, object)

def onPlayerKicked(player):
	log('KK', player)

def onPlayerKilled(victim, attacker, weapon, assists, object):
	log('KL', victim, attacker, weapon, assists, object)

def onPlayerRepairPoint(giver, object):
	log('RP', giver, object)

def onPlayerRevived(victim, reviver):
	log('RV', victim, reviver)

def onPlayerScore(player, difference):
	log('SC', player, difference)

def onPlayerSpawn(player, object):
	log('SP', player, object)

def onPlayerTeamDamagePoint(attacker, victim):
	log('TP', attacker, victim)

def onTicketLimitReached(teamId, limitId):
	log('TL', teamId, limitId)

def onTimeLimitReached(value):
	log('RL', value)

def onVehicleDestroyed(vehicle, attacker):
	log('VD', vehicle, attacker)

def log(type, *args):

	# Write the log entry time stamp
	logFile.write(str(int(host.timer_getWallTime())).zfill(5))
	logFile.write(';')

	# Write the required type of log
	logFile.write(type)

	# Write any optional log arguments with delimiters
	for arg in args:
		logFile.write(';')
		logFile.write(str(arg))

	# Make sure the log entry is output to disk immediately
	logFile.write('\n')
	logFile.flush()
