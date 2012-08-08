
import math
import traceback

from events import DisconnectEvent, GameStatusEvent, ServerStatusEvent
from processors import BaseProcessor
from timer import Timer, timer_mgr

class BaseStats(object):

    def __init__(self):

        # Make sure the resettable values are initialized
        self.reset()

    def reset(self):
        pass

class GameItemStats(object):

    def __init__(self):
        self.deaths = 0
        self.kills = 0
        self.score = 0
        self.teamwork = 0

class GameStats(BaseStats):

    def __init__(self):
        BaseStats.__init__(self)

        self.deaths = 0
        self.kills = 0
        self.players = dict()
        self.score = 0
        self.teamwork = 0

class KitItemStats(object):

    def __init__(self):
        self.deaths = 0
        self.kills = 0
        self.score = 0

class KitStats(BaseStats):

    def __init__(self):
        BaseStats.__init__(self)

        self.deaths = 0
        self.kills = 0
        self.players = dict()
        self.score = 0

class MapItemStats(object):

    def __init__(self):
        self.deaths = 0
        self.kills = 0
        self.score = 0

class MapStats(BaseStats):

    def __init__(self):
        BaseStats.__init__(self)

        self.deaths = 0
        self.kills = 0
        self.players = dict()
        self.score = 0

class PlayerItemStats(object):

    def __init__(self):
        self.deaths = 0
        self.kills = 0
        self.score = 0
        self.wounds = 0

class PlayerStats(BaseStats):

    def __init__(self):
        BaseStats.__init__(self)

        # Cumulative values
        self.assisted_total = 0
        self.assists_total = 0
        self.deaths_total = 0
        self.deaths_streak_max = 0
        self.enemies = dict()
        self.games = 0
        self.healed_total = 0
        self.heals_total = 0
        self.kills_5_total = 0
        self.kills_10_total = 0
        self.kills_ratio_max = 0.0
        self.kills_streak_max = 0
        self.kills_total = 0
        self.kits = dict()
        self.maps = dict()
        self.play_time = Timer()
        self.rank = 0
        self.repairs_total = 0
        self.revived_total = 0
        self.revives_total = 0
        self.score_total = 0
        self.spec_time = Timer()
        self.suicides_total = 0
        self.supplied_total = 0
        self.supplies_total = 0
        self.team_killed_total = 0
        self.team_kills_total = 0
        self.teams = dict()
        self.teamwork_total = 0
        self.vehicles = dict()
        self.weapons = dict()
        self.wounds_total = 0

    def reset(self):

        # Game values
        self.assisted = 0
        self.assists = 0
        self.deaths = 0
        self.deaths_streak = 0
        self.healed = 0
        self.heals = 0
        self.kills = 0
        self.kills_5 = 0
        self.kills_10 = 0
        self.kills_ratio = 0.0
        self.kills_streak = 0
        self.played = False
        self.rank = 0        
        self.repairs = 0
        self.revived = 0
        self.revives = 0
        self.score = 0
        self.suicides = 0
        self.supplied = 0
        self.supplies = 0
        self.team_killed = 0
        self.team_kills = 0
        self.teamwork = 0
        self.wounds = 0

class TeamItemStats(object):

    def __init__(self):
        self.deaths = 0
        self.kills = 0
        self.score = 0

class TeamStats(BaseStats):

    def __init__(self):
        BaseStats.__init__(self)

        self.deaths = 0
        self.kills = 0
        self.players = dict()
        self.score = 0

class VehicleItemStats(object):

    def __init__(self):
        self.deaths = 0
        self.kills = 0

class VehicleStats(BaseStats):

    def __init__(self):
        BaseStats.__init__(self)

        self.deaths = 0
        self.kills = 0
        self.players = dict()

class WeaponItemStats(object):

    def __init__(self):
        self.deaths = 0
        self.kills = 0

class WeaponStats(BaseStats):

    def __init__(self):
        BaseStats.__init__(self)

        self.deaths = 0
        self.kills = 0
        self.players = dict()

class StatManager(object):

    def __init__(self):
        self.processors = list()
        self.id_to_processor = dict()
        self.type_to_processors = dict()

        self.game = None
        self.type_to_stats = dict()

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

        # Reset timers when the server starts
        if isinstance(event, ServerStatusEvent):
            timer_mgr.reset_timers()

        # Reset the stats and timers when a new game starts
        # Store a reference to the current game
        if isinstance(event, GameStatusEvent) and event.game.starting:
            self.game = event.game
            self.reset_stats()
            timer_mgr.reset_timers()

        # Allow each processor to handle the event
        if event and event.CALLBACK:
            for processor in self.processors:

                # Terminate processing if the event was consumed
                if self._process_event(processor, event):
                    break
        else:
            print 'Missing event CALLBACK constant: ', event

        # Update the elapsed time for all enabled timers
        timer_mgr.apply_tick(event.tick)

        # Stop any running timers associated with players that disconnect
        if isinstance(event, DisconnectEvent):
            timer_mgr.stop_player(event.player, event.tick)

        # Reset timers when a game ends
        if isinstance(event, GameStatusEvent) and event.game.ending:
            timer_mgr.reset_timers()

    def reset_stats(self):
        '''
        Resets all the statistic models. This is typically only called when a new game starts.

        Args:
           None

        Returns:
            None
        '''

        for model_to_stats in self.type_to_stats.itervalues():
            for model_stats in model_to_stats.itervalues():
                model_stats.reset()

    def get_stats(self, stats_type):
        '''
        Gets all the statistics objects of the given class type.

        Args:
           stats_type (class): Class definition for the type of statistics
                objects to retrieve.

        Returns:
            stats (list): A list of statistics models of the specified type.
        '''

        if stats_type in self.type_to_stats:
            return self.type_to_stats[stats_type].values()
        return []

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
        return self._get_stats(game, GameStats)

    def get_kit_stats(self, kit):
        '''
        Gets the statistics object for the given kit model.

        Args:
           kit (Kit): Object representation of a kit.

        Returns:
            stats (KitStats): The statistics model associated with the kit.
        '''

        return self._get_stats(kit, KitStats)

    def get_map_stats(self, map):
        '''
        Gets the statistics object for the given map model.

        Args:
           map (Map): Object representation of a map.

        Returns:
            stats (MapStats): The statistics model associated with the map.
        '''

        return self._get_stats(map, MapStats)

    def get_player_stats(self, player):
        '''
        Gets the statistics object for the given player model.

        Args:
           player (Player): Object representation of a player.

        Returns:
            stats (PlayerStats): The statistics model associated with the player.
        '''

        return self._get_stats(player, PlayerStats)

    def get_team_stats(self, team):
        '''
        Gets the statistics object for the given team model.

        Args:
           team (Team): Object representation of a team.

        Returns:
            stats (TeamStats): The statistics model associated with the team.
        '''

        return self._get_stats(team, TeamStats)

    def get_vehicle_stats(self, vehicle):
        '''
        Gets the statistics object for the given vehicle model.

        Args:
           vehicle (Vehicle): Object representation of a vehicle.

        Returns:
            stats (VehicleStats): The statistics model associated with the vehicle.
        '''

        return self._get_stats(vehicle, VehicleStats)

    def get_weapon_stats(self, weapon):
        '''
        Gets the statistics object for the given weapon model.

        Args:
           weapon (Weapon): Object representation of a weapon.

        Returns:
            stats (WeaponStats): The statistics model associated with the weapon.
        '''

        return self._get_stats(weapon, WeaponStats)

    def dist_2d(self, pos1, pos2):
        '''
        Calculates the distance between the given position arrays in 2-dimensional space.

        Args:
           pos1 (array): Array of points in the form [x, z, y, a].
           pos2 (array): Array of points in the form [x, z, y, a].

        Returns:
            distance (float): The distance between two points using the x and y coordinates.
        '''

        # Formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
        if pos1 and len(pos1) == 4 and pos2 and len(pos2) == 4:
            x_dist = math.pow(pos2[0] - pos1[0], 2)
            y_dist = math.pow(pos2[2] - pos1[2], 2)
            return math.sqrt(x_dist + y_dist)

    def dist_3d(self, pos1, pos2):
        '''
        Calculates the distance between the given position arrays in 3-dimensional space.

        Args:
           pos1 (array): Array of points in the form [x, z, y, a].
           pos2 (array): Array of points in the form [x, z, y, a].

        Returns:
            distance (float): The distance between two points using the x, y, and z coordinates.
        '''

        # Formula: sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2)
        if pos1 and len(pos1) == 4 and pos2 and len(pos2) == 4:
            x_dist = math.pow(pos2[0] - pos1[0], 2)
            y_dist = math.pow(pos2[2] - pos1[2], 2)
            z_dist = math.pow(pos2[1] - pos1[1], 2)
            return math.sqrt(x_dist + y_dist + z_dist)

    def dist_alt(self, pos1, pos2):
        '''
        Calculates the altitude or height distance between the given position arrays.

        Args:
           pos1 (array): Array of points in the form [x, z, y, a].
           pos2 (array): Array of points in the form [x, z, y, a].

        Returns:
            distance (float): The distance between two points using the z coordinate.
        '''

        if pos1 and len(pos1) == 4 and pos2 and len(pos2) == 4:
            return math.fabs(pos2[1] - pos1[1])

    def _get_stats(self, model, stats_type):
        if not (model and stats_type): return

        # Make sure there is a mapping for the given type
        if not stats_type in self.type_to_stats:
            self.type_to_stats[stats_type] = dict()
        model_to_stats = self.type_to_stats[stats_type]

        # Make sure there is a mapping for the given model
        if not model in model_to_stats:
            model_to_stats[model] = stats_type()
        return model_to_stats[model]

    def _process_event(self, processor, event):

        # Make sure the processor has the event callback function
        if hasattr(processor, event.CALLBACK):
            try:

                # Pass the universal event callback
                processor.on_event(event)

                # Attempt to invoke the processor callback
                callback = getattr(processor, event.CALLBACK)

                # Terminate processing if the event was consumed
                return callback(event)
            except Exception, err:
                print ('ERROR - Failed to invoke processor callback: [%i] %s.%s[%s]'
                        % (event.tick, processor.__class__.__module__,
                        processor.__class__.__name__, event.CALLBACK))
                traceback.print_exc(err)
        else:
            print 'ERROR - Missing callback: %s.%s[%s]' % (processor.__class__.__module__,
                    processor.__class__.__name__, event.CALLBACK)

# Create a shared singleton instance of the stats manager
stat_mgr = StatManager()
