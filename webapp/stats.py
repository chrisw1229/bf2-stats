
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
        self.processors = list()
        self.id_to_processor = dict()
        self.type_to_processors = dict()

        self.game = None
        self.game_to_stats = dict()
        self.kit_to_stats = dict()
        self.map_to_stats = dict()
        self.player_to_stats = dict()
        self.team_to_stats = dict()
        self.vehicle_to_stats = dict()
        self.weapon_to_stats = dict()

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

    def add_processor(self, processor):
        '''
        Registers the given processor instance so that it can be used to calculate statistics.

        Args:
            processor (BaseProcessor): The processor instance to register.

        Returns:
            None
        '''

        assert processor and processor.id and processor.processor_type, (
                'Invalid processor registration: %s (%s)' % (id, processor))
        assert not processor.id in self.id_to_processor, 'Duplicate processor registration: %s' % id
        assert isinstance(processor, BaseProcessor), 'Must inherit BaseProcessor: %s' % processor

        self.processors.append(processor)
        self.id_to_processor[processor.id] = processor

        if not processor.processor_type in self.type_to_processors:
            self.type_to_processors[processor.processor_type] = []
        self.type_to_processors[processor.processor_type].append(processor)

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

    def get_processor_types(self):
        '''
        Gets a list of registered processor types.

        Args:
           None

        Returns:
            types (list): Returns a list of registered processor types.
        '''

        return self.type_to_processors.keys()

    def get_processors(self, processor_type):
        '''
        Gets a list of registered processor that match the given type.

        Args:
            processor_type (string): The type of processors to get.

        Returns:
            processors (list): Returns a list of processors based on type.
        '''

        if processor_type and processor_type in self.type_to_processors:
            return self.type_to_processors[processor_type]
        return []

    def process_event(self, event):
        '''
        Takes in a log event and processes it into useful statistics.

        Args:
           event (BaseEvent): Object representation of a log entry.

        Returns:
            None
        '''

        if not event: return

        # Reset the stats when a new game starts
        # Store a reference to the current game
        if isinstance(event, GameStatusEvent) and event.game.starting:
            self.game = event.game
            self.reset_stats()

        # Allow each processor to handle the event
        if event and event.CALLBACK:
            for processor in self.processors:

                # Terminate processing if the event was consumed
                if self._process_event(processor, event):
                    break
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

        self._reset_stats(self.kit_to_stats)
        self._reset_stats(self.map_to_stats)
        self._reset_stats(self.player_to_stats)
        self._reset_stats(self.team_to_stats)
        self._reset_stats(self.vehicle_to_stats)
        self._reset_stats(self.weapon_to_stats)

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

        if not game in self.game_to_stats:
            self.game_to_stats[game] = GameStats()
        return self.game_to_stats[game]

    def get_kit_stats(self, kit):
        '''
        Gets the statistics object for the given kit model.

        Args:
           kit (Kit): Object representation of a kit.

        Returns:
            stats (KitStats): The statistics model associated with the kit.
        '''

        if not kit in self.kit_to_stats:
            self.kit_to_stats[kit] = KitStats()
        return self.kit_to_stats[kit]

    def get_map_stats(self, map):
        '''
        Gets the statistics object for the given map model.

        Args:
           map (Map): Object representation of a map.

        Returns:
            stats (MapStats): The statistics model associated with the map.
        '''

        if not map in self.map_to_stats:
            self.map_to_stats[map] = MapStats()
        return self.map_to_stats[map]

    def get_player_stats(self, player):
        '''
        Gets the statistics object for the given player model.

        Args:
           player (Player): Object representation of a player.

        Returns:
            stats (PlayerStats): The statistics model associated with the player.
        '''

        if not player in self.player_to_stats:
            self.player_to_stats[player] = PlayerStats()
        return self.player_to_stats[player]

    def get_team_stats(self, player):
        '''
        Gets the statistics object for the given team model.

        Args:
           team (Team): Object representation of a team.

        Returns:
            stats (TeamStats): The statistics model associated with the team.
        '''

        if not team in self.team_to_stats:
            self.team_to_stats[team] = TeamStats()
        return self.team_to_stats[team]

    def get_vehicle_stats(self, vehicle):
        '''
        Gets the statistics object for the given vehicle model.

        Args:
           vehicle (Vehicle): Object representation of a vehicle.

        Returns:
            stats (VehicleStats): The statistics model associated with the vehicle.
        '''

        if not vehicle in self.vehicle_to_stats:
            self.vehicle_to_stats[vehicle] = VehicleStats()
        return self.vehicle_to_stats[vehicle]

    def get_weapon_stats(self, weapon):
        '''
        Gets the statistics object for the given weapon model.

        Args:
           weapon (Weapon): Object representation of a weapon.

        Returns:
            stats (WeaponStats): The statistics model associated with the weapon.
        '''

        if not weapon in self.weapon_to_stats:
            self.weapon_to_stats[weapon] = WeaponStats()
        return self.weapon_to_stats[weapon]

    def _reset_stats(self, mapping):
        if mapping:
            for stats in mapping.itervalues():
                stats.reset()

    def _process_event(self, processor, event):

        # Make sure the processor has the event callback function
        if hasattr(processor, event.CALLBACK):
            try:

                # Attempt to invoke the processor callback
                callback = getattr(processor, event.CALLBACK)

                # Terminate processing if the event was consumed
                return callback(event)
            except Exception, err:
                print ('ERROR - Failed to invoke processor callback: %s.%s[%s]'
                        % (processor.__class__.__module__,
                        processor.__class__.__name__, event.CALLBACK))
                traceback.print_exc(err)
        else:
            print 'ERROR - Missing callback: %s.%s[%s]' % (processor.__class__.__module__,
                    processor.__class__.__name__, event.CALLBACK)

# Create a shared singleton instance of the stats manager
stat_mgr = StatManager()
