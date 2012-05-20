
class Stats(object):

    def __init__(self):

        self.ticked = False # Whether or not the newest event caused the game time to advance
        self.old_tick = 0 # The game time of the older batch of events
        self.new_tick = 0 # The game time of the newest batch of events
        self.old_events = [] # A list of events for the older game time
        self.new_events = [] # A list of events for the newest game time
        self.old_event_types = {} # A map of event type to event for older events
        self.new_event_types = {} # A map of event type to event for newest events

    def add_event(self, event):
        '''
        Adds a log event to the history of this statistics model for use by processors.

        Args:
           event (BaseEvent): Object representation of a log entry.

        Returns:
            None
        '''

        if not event: return

        # Update the event history based on game time ticks
        if event.tick > self.new_tick:
            self.old_tick = self.new_tick
            self.old_events = self.new_events

            self.new_tick = event.tick
            self.new_events = []
            ticked = True
        else:
            ticked = False
        self.new_events.append(event)

        # Update the event history based on event type
        if event.ID in self.new_event_types:
            self.old_event_types[event.ID] = self.new_event_types[event.ID]
        self.new_event_types[event.ID] = event

    def get_old_event(self, event_id):
        '''
        Gets the older/previous registered event that matches the given identifier.

        Args:
           event_id (string): The unique identifier for a type of event.

        Returns:
            event (BaseEvent): An event that occurred at a previous tick.
        '''

        if event_id and event_id in self.old_event_types:
            return self.old_event_types[event_id]
        return None

    def get_new_event(self, event_id):
        '''
        Gets the newest/recent registered event that matches the given identifier.

        Args:
           event_id (string): The unique identifier for a type of event.

        Returns:
            event (BaseEvent): An event that occurred at the most recent tick.
        '''

        if event_id and event_id in self.new_event_types:
            return self.new_event_types[event_id]
        return None

class GameStats(Stats):

    def __init__(self):
        super(GameStats, self).__init__()

        pass

class KitStats(Stats):

    def __init__(self):
        super(KitStats, self).__init__()

        pass

class MapStats(Stats):

    def __init__(self):
        super(MapStats, self).__init__()

        pass

class PlayerStats(Stats):

    def __init__(self):
        super(PlayerStats, self).__init__()
        
        self.kills = 0
        self.deaths = 0

class TeamStats(Stats):

    def __init__(self):
        super(TeamStats, self).__init__()

        pass

class VehicleStats(Stats):

    def __init__(self):
        super(VehicleStats, self).__init__()

        pass

class WeaponStats(Stats):

    def __init__(self):
        super(WeaponStats, self).__init__()

        pass

class StatsManager(object):

    core_processor = None
    live_processor = None
    processors = []
    stats = GameStats()

    games = {}
    kits = {}
    maps = {}
    players = {}
    teams = {}
    vehicles = {}
    weapons = {}

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

        # Update the stats history for the event
        self.stats.add_event(event)

        # Allow each processor to handle the event
        self._fire(event)

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

    def _fire(self, event):
        '''
        Passes the given log event to all the registered processors.

        Args:
           event (BaseEvent): Object representation of a log entry.

        Returns:
            None
        '''

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

# Create a shared singleton instance of the stats manager
stats_mgr = StatsManager()
