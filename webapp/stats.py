
import traceback

from events import GameStatusEvent
from processors import BaseProcessor

class BaseStats(object):

    def __init__(self):

        # Make sure the resettable values are initialized
        self.reset()

    def reset(self):
        pass

class GameStats(BaseStats):

    def __init__(self):
        BaseStats.__init__(self)

        pass

class KitStats(BaseStats):

    def __init__(self):
        BaseStats.__init__(self)

        pass

class MapStats(BaseStats):

    def __init__(self):
        BaseStats.__init__(self)

        pass

class PlayerStats(BaseStats):

    def __init__(self):
        BaseStats.__init__(self)

        # Cumulative values
        self.ammo_points_total = 0
        self.assists_total = 0
        self.deaths_total = 0
        self.death_streak_max = 0
        self.heal_points_total = 0
        self.kills_total = 0
        self.kill_streak_max = 0
        self.repair_points_total = 0
        self.revive_points_total = 0
        self.score_total = 0
        self.suicides_total = 0
        self.team_kills_total = 0
        self.wounds_total = 0

    def reset(self):

        # Game values
        self.ammo_points = 0
        self.assists = 0
        self.deaths = 0
        self.death_streak = 0
        self.heal_points = 0
        self.kills = 0
        self.kill_streak = 0
        self.repair_points = 0
        self.revive_points = 0
        self.score = 0
        self.suicides = 0
        self.team_kills = 0
        self.wounds = 0

class TeamStats(BaseStats):

    def __init__(self):
        BaseStats.__init__(self)

        pass

class VehicleStats(BaseStats):

    def __init__(self):
        BaseStats.__init__(self)

        pass

class WeaponStats(BaseStats):

    def __init__(self):
        BaseStats.__init__(self)

        pass

class StatManager(object):

    def __init__(self):
        self.processors = []
        self.id_to_processor = {}

        self.game = None
        self.games = {}
        self.kits = {}
        self.maps = {}
        self.players = {}
        self.teams = {}
        self.vehicles = {}
        self.weapons = {}

    # This method will be called to initialize the manager
    def start(self):
        print 'STATS MANAGER - STARTING'
        print 'Processors registered: ', len(self.processors)

        # Sort the log processors by priority
        self.processors.sort(key=lambda p: p.priority)

        # Start all the log processors
        for processor in self.processors:
            processor.start()

        print 'STATS MANAGER - STARTED'

    # This method will be called to shutdown the manager
    def stop(self):
        print 'STATS MANAGER - STOPPING'

        # Stop all the log processors
        for processor in reversed(self.processors):
            processor.stop()

        print 'STATS MANAGER - STOPPED'

    def add_processor(self, id, processor):
        '''
        Registers the given processor instance so that it can be used to calculate statistics.

        Args:
            id (string): A unique identifier for the processor which is typically just based on the
                processor's module name.
            processor (BaseProcessor): The processor instance to register.

        Returns:
            None
        '''

        assert id and processor, 'Invalid processor registration: %s (%s)' % (id, processor)
        assert not id in self.id_to_processor, 'Duplicate processor registration: %s' % id
        assert isinstance(processor, BaseProcessor), 'Must inherit BaseProcessor: %s' % processor

        self.processors.append(processor)
        self.id_to_processor[id] = processor

    def get_processor(self, id):
        '''
        Gets the processor instance associated with the given identifier.

        Args:
            id (string): A unique identifier that was previously registered to a processor instance.

        Returns:
            processor (BaseProcessor): The requested processor instance.
        '''

        if id and id in self.id_to_processor:
            return self.id_to_processor[id]

        print 'ERROR - Missing processor reference: ', id
        return None

    def get_processors(self, id_prefix):
        '''
        Gets a list of processor instances that match the given identifier prefix.

        Args:
            id_prefix (string): A partial unique identifier that will be used to match previously
                    registered processor instances.

        Returns:
            processors (list): A list of processor instances that have identifiers starting with the
                    given prefix.
        '''

        results = []
        for id in self.id_to_processor.iterkeys():
            if id.startswith(id_prefix):
                results.append(self.id_to_processor[id])
        return results

    def process_event(self, event):
        '''
        Takes in a log event and processes it into useful statistics.

        Args:
           event (BaseEvent): Object representation of a log entry.

        Returns:
            None
        '''

        # Reset the stats when a new game starts
        # Store a reference to the current game
        if isinstance(event, GameStatusEvent) and event.game.is_starting():
            self.game = event.game
            self.reset_stats()

        # Allow each processor to handle the event
        if event and event.CALLBACK:
            for processor in self.processors:

                # Attempt to invoke the processor callback
                if hasattr(processor, event.CALLBACK):
                    try:
                        callback = getattr(processor, event.CALLBACK)
                        consumed = callback(event)

                        # Terminate the loop if the processor consumed the event
                        if consumed:
                            break
                    except Exception, err:
                        print ('ERROR - Failed to invoke processor callback: %s.%s[%s]'
                                % (processor.__class__.__module__,
                                processor.__class__.__name__, event.CALLBACK))
                        traceback.print_exc(err)
                else:
                    print 'ERROR - Missing callback: %s.%s[%s]' % (processor.__class__.__module__,
                            processor.__class__.__name__, event.CALLBACK)
        else:
            print 'Missing event CALLBACK constant: ', event

    def reset_stats(self):
        '''
        Resets all the statistic models. This is typically only called when a new game starts.

        Args:
           None

        Returns:
            None
        '''

        self._reset_stats(self.kits)
        self._reset_stats(self.maps)
        self._reset_stats(self.players)
        self._reset_stats(self.teams)
        self._reset_stats(self.vehicles)
        self._reset_stats(self.weapons)

    def get_game_stats(self, game):
        '''
        Gets the statistics object for the given game model.

        Args:
           game (Game): Object representation of a game. None will retrieve the statistics for the
                    currently active game.

        Returns:
            stats (GameStats): The statistics model associated with the game.
        '''

        if not game:
            game = self.game

        if not game in self.games:
            self.games[game] = GameStats()
        return self.games[game]

    def get_kit_stats(self, kit):
        '''
        Gets the statistics object for the given kit model.

        Args:
           kit (Kit): Object representation of a kit.

        Returns:
            stats (KitStats): The statistics model associated with the kit.
        '''

        if not kit in self.kits:
            self.kits[kit] = KitStats()
        return self.kits[kit]

    def get_map_stats(self, map):
        '''
        Gets the statistics object for the given map model.

        Args:
           map (Map): Object representation of a map.

        Returns:
            stats (MapStats): The statistics model associated with the map.
        '''

        if not map in self.maps:
            self.maps[map] = MapStats()
        return self.maps[map]

    def get_player_stats(self, player):
        '''
        Gets the statistics object for the given player model.

        Args:
           player (Player): Object representation of a player.

        Returns:
            stats (PlayerStats): The statistics model associated with the player.
        '''

        if not player in self.players:
            self.players[player] = PlayerStats()
        return self.players[player]

    def get_team_stats(self, player):
        '''
        Gets the statistics object for the given team model.

        Args:
           team (Team): Object representation of a team.

        Returns:
            stats (TeamStats): The statistics model associated with the team.
        '''

        if not team in self.teams:
            self.teams[team] = TeamStats()
        return self.teams[team]

    def get_vehicle_stats(self, vehicle):
        '''
        Gets the statistics object for the given vehicle model.

        Args:
           vehicle (Vehicle): Object representation of a vehicle.

        Returns:
            stats (VehicleStats): The statistics model associated with the vehicle.
        '''

        if not vehicle in self.vehicles:
            self.vehicles[vehicle] = VehicleStats()
        return self.vehicles[vehicle]

    def get_weapon_stats(self, weapon):
        '''
        Gets the statistics object for the given weapon model.

        Args:
           weapon (Weapon): Object representation of a weapon.

        Returns:
            stats (WeaponStats): The statistics model associated with the weapon.
        '''

        if not weapon in self.weapons:
            self.weapons[weapon] = WeaponStats()
        return self.weapons[weapon]

    def _reset_stats(self, mapping):
        if mapping:
            for stats in mapping.itervalues():
                stats.reset()

# Create a shared singleton instance of the stats manager
stat_mgr = StatManager()
