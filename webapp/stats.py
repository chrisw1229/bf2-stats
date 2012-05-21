
from event import GameStatusEvent

class BaseStats(object):

    def __init__(self):

        # Make sure the resettable values are initialized
        self.reset()

    def reset(self):
        pass

class GameStats(BaseStats):

    def __init__(self):
        super(GameStats, self).__init__()

        pass

class KitStats(BaseStats):

    def __init__(self):
        super(KitStats, self).__init__()

        pass

class MapStats(BaseStats):

    def __init__(self):
        super(MapStats, self).__init__()

        pass

class PlayerStats(BaseStats):

    def __init__(self):
        super(PlayerStats, self).__init__()

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
        super(TeamStats, self).__init__()

        pass

class VehicleStats(BaseStats):

    def __init__(self):
        super(VehicleStats, self).__init__()

        pass

class WeaponStats(BaseStats):

    def __init__(self):
        super(WeaponStats, self).__init__()

        pass

class StatsManager(object):

    def __init__(self):
        self.core_processor = None
        self.live_processor = None
        self.processors = []
        self.stats = GameStats()

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

        # Start all the log processors
        for proc in self.processors:
            proc.start()

        print 'STATS MANAGER - STARTED'

    # This method will be called to shutdown the manager
    def stop(self):
        print 'STATS MANAGER - STOPPING'

        # Stop all the log processors
        for proc in reversed(self.processors):
            proc.stop()

        print 'STATS MANAGER - STOPPED'

    def process_event(self, event):
        '''
        Takes in a log event and processes it into useful statistics.

        Args:
           event (BaseEvent): Object representation of a log entry.

        Returns:
            None
        '''

        # Reset the stats when a new game starts
        if isinstance(event, GameStatusEvent) and event.game.is_started():
            self.reset_stats()

        # Allow each processor to handle the event
        if event and event.CALLBACK:
            for processor in self.processors:

                # Attempt to invoke the processor callback
                try:
                    callback = getattr(processor, event.CALLBACK)
                    consumed = callback(event)

                    # Terminate the loop if the processor consumed the event
                    if consumed:
                        break
                except AttributeError:
                    print 'Missing callback for processor: %s[%s]' % (processor, event.callback)
        else:
            print 'Missing callback for event: ', event

    def reset_stats(self):
        '''
        Resets all the statistic models. This is typically only called when a new game starts.

        Args:
           None

        Returns:
            None
        '''

        self.stats.reset()

        for s in self.games.itervalues():
            s.reset()
        for s in self.kits.itervalues():
            s.reset()
        for s in self.maps.itervalues():
            s.reset()
        for s in self.players.itervalues():
            s.reset()
        for s in self.teams.itervalues():
            s.reset()
        for s in self.vehicles.itervalues():
            s.reset()
        for s in self.weapons.itervalues():
            s.reset()

    def get_game_stats(self, game):
        '''
        Gets the statistics object for the given game model.

        Args:
           game (Game): Object representation of a game.

        Returns:
            stats (GameStats): The statistics model associated with the game.
        '''

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

# Create a shared singleton instance of the stats manager
stats_mgr = StatsManager()
