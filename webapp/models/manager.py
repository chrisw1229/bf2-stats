
import control_points
import games
import kits
import maps
import players
import squads
import teams
import vehicles
import weapons

class ModelManager(object):

    def __init__(self):
        self.debug_enabled = False

        self.control_points = set()
        self.id_to_control_point = dict()
        self.addr_to_control_point = dict()

        self.games = list()
        self.id_to_game = dict()

        self.kits = set()
        self.id_to_kit = dict()
        self.type_to_kits = dict()

        self.maps = set()
        self.id_to_map = dict()

        self.players = set()
        self.id_to_player = dict()
        self.name_to_player = dict()
        self.addr_to_player = dict()

        self.squads = set()
        self.id_to_squad = dict()

        self.teams = set()
        self.id_to_team = dict()

        self.vehicles = set()
        self.id_to_vehicle = dict()
        self.type_to_vehicles = dict()
        self.group_to_vehicles = dict()

        self.weapons = set()
        self.id_to_weapon = dict()
        self.type_to_weapons = dict()

    # This method will be called to initialize the manager
    def start(self):
        print 'MODEL MANAGER - STARTING'

        # Register all the kit models
        self.kits.update(kits.registry)
        for kit in self.kits:
            assert not kit.id in self.id_to_kit, 'Duplicate kit ID: %s' % kit.id
            self.id_to_kit[kit.id] = kit

            if not kit.kit_type in self.type_to_kits:
                self.type_to_kits[kit.kit_type] = set()
            self.type_to_kits[kit.kit_type].add(kit)
        print 'Kits registered: ', len(self.kits)

        # Register all the map models
        self.maps.update(maps.registry)
        for map in self.maps:
            assert not map.id in self.id_to_map, 'Duplicate map ID: %s' % map.id
            self.id_to_map[map.id] = map
        print 'Maps registered: ', len(self.maps)

        # Register all the team models
        self.teams.update(teams.registry)
        for team in self.teams:
            assert not team.id in self.id_to_team, 'Duplicate team ID: %s' % team.id
            self.id_to_team[team.id] = team
        print 'Teams registered: ', len(self.teams)

        # Register all the vehicle models
        self.vehicles.update(vehicles.registry)
        for vehicle in self.vehicles:
            assert not vehicle.id in self.id_to_vehicle, 'Duplicate vehicle ID: %s' % vehicle.id
            self.id_to_vehicle[vehicle.id] = vehicle

            if not vehicle.vehicle_type in self.type_to_vehicles:
                self.type_to_vehicles[vehicle.vehicle_type] = set()
            self.type_to_vehicles[vehicle.vehicle_type].add(vehicle)

            if not vehicle.group in self.group_to_vehicles:
                self.group_to_vehicles[vehicle.group] = set()
            self.group_to_vehicles[vehicle.group].add(vehicle)
        print 'Vehicles registered: ', len(self.vehicles)

        # Register all the weapon models
        self.weapons.update(weapons.registry)
        for weapon in self.weapons:
            assert not weapon.id in self.id_to_weapon, 'Duplicate weapon ID: %s' % weapon.id
            self.id_to_weapon[weapon.id] = weapon

            if not weapon.weapon_type in self.type_to_weapons:
                self.type_to_weapons[weapon.weapon_type] = set()
            self.type_to_weapons[weapon.weapon_type].add(weapon)
        print 'Weapons registered: ', len(self.weapons)

        print 'MODEL MANAGER - STARTED'

    # This method will be called to shutdown the manager
    def stop(self):
        print 'MODEL MANAGER - STOPPING'

        print 'MODEL MANAGER - STOPPED'

    def add_control_point(self, address, pos):
        '''
        Adds or updates the control point model registered for the given address
        and position.

        Args:
            address (string): The map address of the control point.
            pos (Array): The position array of the control point.

        Returns:
            control_point (ControlPoint): Returns the registered control point
                    model.
        '''

        # Handle requests for missing control points
        if not address:
            return control_points.EMPTY

        # Get a model for the control_point
        if not address in self.addr_to_control_point:
            control_point = control_points.ControlPoint(address, pos)
            self.addr_to_control_point[address] = control_point
            self.id_to_control_point[control_point.id] = control_point
            self.control_points.add(control_point)

        return self.addr_to_control_point[address]

    def add_player(self, address, name):
        '''
        Adds or updates the player model registered for the given unique
        composite key.

        Args:
            address (string): The IP address of the player. This could be 'None'
                    for bot players.
            name (string): The name of the player.

        Returns:
            player (Player): Returns the registered player model.
        '''

        # Get a model for the player
        player = self._update_player(address, name)
        if not player: return players.EMPTY

        self._log('Player joined: %s (%s)' % (name, address))
        return player

    def add_squad(self, id):
        '''
        Adds or updates the squad model registered for the given id.

        Args:
            id (string): The id of the squad.

        Returns:
            squad (Squad): Returns the registered squad model.
        '''

        # Handle requests for missing squads
        if not id:
            return squads.EMPTY

        # Get a model for the squad
        if not id in self.id_to_squad:
            squad = squads.Squad(id)
            self.id_to_squad[id] = squad
            self.squads.add(squad)

        return self.id_to_squad[id]

    def get_control_point(self, id):
        '''
        Looks up the control point object associated with the given id.

        Args:
            id (string): The id of the control point to get.

        Returns:
            control_point (ControlPoint): Returns a registered control point
                    model.
        '''

        # Handle requests for missing control points
        if not id:
            return control_points.EMPTY

        # Get a model for the control point
        if id in self.id_to_control_point:
            return self.id_to_control_point[id]

        print 'ERROR - Missing control point reference:', id
        return None

    def get_control_points(self, active=None):
        '''
        Gets a list of all the registered control points.

        Args:
            active (boolean): Indicates whether all control points (None),
                active control points (True), or inactive control points (False)
                should be included in the results.

        Returns:
            control points (list): Returns a list of control point objects.
        '''

        control_points = list(self.control_points)
        if active == None:
            return control_points
        return filter(lambda p: p.active == active, control_points)

    def get_game(self, id=None):
        '''
        Looks up the game object associated with the given id or gets the currently active game if
        no id is provided.

        Args:
            id (string): The id of the game to get. None is equivalent to the current game.

        Returns:
            game (Game): Returns a registered game model.
        '''

        # Handle requests for missing games or the current game
        if not id:
            if len(self.games) == 0:
                return games.EMPTY
            return self.games[-1]

        # Get a model for the game
        if id in self.id_to_game:
            return self.id_to_game[id]

        print 'ERROR - Missing game reference:', id
        return None

    def get_games(self):
        '''
        Gets a list of all the registered games.

        Args:
            None

        Returns:
            games (list): Returns a list of game objects.
        '''

        return list(self.games)

    def get_kit(self, id):
        '''
        Looks up the kit object associated with the given id.

        Args:
            id (string): The id of the kit to get.

        Returns:
            kit (Kit): Returns a registered kit model.
        '''

        # Handle requests for missing kits
        if not id:
            return kits.EMPTY

        # Get a model for the kit
        if id in self.id_to_kit:
            return self.id_to_kit[id]

        print 'ERROR - Missing kit reference:', id
        return None

    def get_kit_types(self):
        '''
        Gets a list of registered kit types.

        Args:
            None

        Returns:
            types (list): Returns a list of registered kit types.
        '''

        return self.type_to_kits.keys()

    def get_kits(self, kit_type=None):
        '''
        Gets a list of registered kits that match the given type.

        Args:
            kit_type (string): The type of kits to get or None to get all kits.

        Returns:
            kits (list): Returns a list of kits based on type.
        '''

        if kit_type and kit_type in self.type_to_kits:
            return list(self.type_to_kits[kit_type])
        return list(self.kits)

    def get_map(self, id):
        '''
        Looks up the map object associated with the given id.

        Args:
            id (string): The id of the map to get.

        Returns:
            map (Map): Returns a registered map model.
        '''

        # Handle requests for missing maps
        if not id:
            return maps.EMPTY

        # Get a model for the map
        if id in self.id_to_map:
            return self.id_to_map[id]

        print 'ERROR - Missing map reference:', id
        return None

    def get_maps(self):
        '''
        Gets a list of all the registered maps.

        Args:
            None

        Returns:
            maps (list): Returns a list of map objects.
        '''

        return list(self.maps)

    def get_player(self, id):
        '''
        Looks up the player object associated with the given id.

        Args:
            id (string): The id of the player to get.

        Returns:
            Player (Player): Returns a registered player model.
        '''

        # Handle requests for missing players
        if not id:
            return players.EMPTY

        # Get a model for the player
        if id in self.id_to_player:
            return self.id_to_player[id]

        print 'ERROR - Missing player reference:', id
        return None

    def get_player_by_name(self, name):
        '''
        Looks up the player object associated with the given name.

        Args:
            name (string): The name of the player to get.

        Returns:
            Player (Player): Returns a registered player model.
        '''

        # Handle requests for missing players
        if not name:
            return players.EMPTY

        # Get a model for the player
        if name in self.name_to_player:
            return self.name_to_player[name]

        print 'ERROR - Missing player reference:', name
        return None

    def get_player_names(self):
        '''
        Gets a sorted list of names for all the player objects.

        Args:
            None

        Returns:
            Names (list): Returns a sorted list of names for all the player objects.
        '''

        names = [p.name for p in self.players]
        names.sort(key=str.lower)
        return names

    def get_players(self, connected=None):
        '''
        Gets a list of all the registered players.

        Args:
            connected (boolean): Indicates whether all players (None), connected
                players (True), or disconnected players (False) should be
                included in the results.

        Returns:
            players (list): Returns a list of player objects.
        '''

        players = list(self.players)
        if connected == None:
            return players
        return filter(lambda p: p.connected == connected, players)

    def get_squad(self, id):
        '''
        Looks up the squad object associated with the given id.

        Args:
            id (string): The id of the squad to get.

        Returns:
            squad (Squad): Returns a registered squad model.
        '''

        # Handle requests for missing squads
        if not id:
            return squads.EMPTY

        # Get a model for the squad
        if id in self.id_to_squad:
            return self.id_to_squad[id]

        print 'ERROR - Missing squad reference:', id
        return None

    def get_squads(self):
        '''
        Gets a list of all the registered squads.

        Args:
            None

        Returns:
            squads (list): Returns a list of squad objects.
        '''

        return list(self.squads)

    def get_team(self, id):
        '''
        Looks up the team object associated with the given id.

        Args:
            id (string): The id of the team to get.

        Returns:
            team (Team): Returns a registered team model.
        '''

        # Handle requests for missing teams
        if not id:
            return teams.EMPTY

        # Get a model for the team
        if id in self.id_to_team:
            return self.id_to_team[id]

        print 'ERROR - Missing team reference:', id
        return None

    def get_teams(self):
        '''
        Gets a list of all the registered teams.

        Args:
            None

        Returns:
            teams (list): Returns a list of team objects.
        '''

        return list(self.teams)

    def get_vehicle(self, id):
        '''
        Looks up the vehicle object associated with the given id.

        Args:
            id (string): The id of the vehicle to get.

        Returns:
            vehicle (Vehicle): Returns a registered vehicle model.
        '''

        # Handle requests for missing vehicles
        if not id:
            return vehicles.EMPTY

        # Get a model for the vehicle
        if id in self.id_to_vehicle:
            return self.id_to_vehicle[id]

        print 'ERROR - Missing vehicle reference:', id
        return None

    def get_vehicle_types(self):
        '''
        Gets a list of registered vehicle types.

        Args:
            None

        Returns:
            types (list): Returns a list of registered vehicle types.
        '''

        return self.type_to_vehicles.keys()

    def get_vehicles(self, vehicle_type=None, vehicle_group=None):
        '''
        Gets a list of registered vehicles that match the given type.

        Args:
            vehicle_type (string): The type of vehicles to get or None to get
                    all vehicles.
            vehicle_group (string): The group of vehicles to get or None to get
                    all vehicles.

        Returns:
            vehicles (list): Returns a list of vehicles based on type.
        '''

        if vehicle_type and vehicle_type in self.type_to_vehicles:
            return list(self.type_to_vehicles[vehicle_type])
        if vehicle_group and vehicle_group in self.group_to_vehicles:
            return list(self.group_to_vehicles[vehicle_group])
        return list(self.vehicles)

    def get_weapon(self, id):
        '''
        Looks up the weapon object associated with the given id.

        Args:
            id (string): The id of the weapon to get.

        Returns:
            weapon (Weapon): Returns a registered weapon model.
        '''

        # Handle requests for missing weapons
        if not id:
            return weapons.EMPTY

        # Get a model for the weapon
        if id in self.id_to_weapon:
            return self.id_to_weapon[id]

        print 'ERROR - Missing weapon reference:', id
        return None

    def get_weapon_types(self):
        '''
        Gets a list of registered weapon types.

        Args:
            None

        Returns:
            types (list): Returns a list of registered weapon types.
        '''

        return self.type_to_weapons.keys()

    def get_weapons(self, weapon_type=None):
        '''
        Gets a list of registered weapons that match the given type.

        Args:
            weapon_type (string): The type of weapons to get or None to get all
                    weapons.

        Returns:
            weapons (list): Returns a list of weapons based on type.
        '''

        if weapon_type and weapon_type in self.type_to_weapons:
            return list(self.type_to_weapons[weapon_type])
        return list(self.weapons)

    def remove_player(self, address, name):
        '''
        Removes the player model registered for the given unique composite key.

        Args:
            address (string): The IP address of the player. This could be 'None'
                    for bot players.
            name (string): The name of the player.

        Returns:
            player (Player): Returns the unregistered player model.
        '''

        # Get a model for the player
        player = self._update_player(address, name)
        if not player: return players.EMPTY

        self._log('Player left: %s (%s)' % (name, address))
        return player

    def remove_squad(self, id):
        '''
        Removes the squad model registered for the given unique id.

        Args:
            id (string): The unique id of a squad.

        Returns:
            squad (Squad): Returns the unregistered squad model.
        '''

        if id and id in self.id_to_squad:
            squad = self.id_to_squad[id]
            self.id_to_squad.remove(id)
            self.squads.remove(squad)
            return squad
        return squads.EMPTY

    def reset_models(self):
        '''
        Resets all the game models. This is typically only called when the
        server restarts or a new game starts.

        Args:
            None

        Returns:
            None
        '''

        for control_point in self.control_points:
            control_point.reset();
        for player in self.players:
            player.reset()
        for game in self.games:
            game.reset()
        for kit in self.kits:
            kit.reset()
        for map_obj in self.maps:
            map_obj.reset()
        for squad in self.squads:
            squad.reset()
        for team in self.teams:
            team.reset()
        for vehicle in self.vehicles:
            vehicle.reset()
        for weapon in self.weapons:
            weapon.reset()

    def set_game_status(self, status, map_id, clock_limit, score_limit):
        '''
        Sets the current game status based on the given parameters.

        Args:
            status (string): The current status of the game.
            map_id (string): The unique identifier of the current map.
            clock_limit (integer): The maximum number of seconds unil game end.
            score_limit (integer): The maximum score until game end.

        Returns:
            game (Game): Returns the registered game model.
        '''

        if not status or not map_id: return games.EMPTY

        game = None
        if status == games.Game.STARTING:

            # Create a new model when the game is starting
            game = games.Game(status, map_id, clock_limit, score_limit)
            self.games.append(game)
            self._log('Game started: %s %s' % (game.id, game.map_id))
        else:

            # Update the game to reflect the new state
            game = self.get_game()
            game.status = status
            game.map_id = map_id
            game.clock_limit = clock_limit
            game.score_limit = score_limit

        # Update the id mapping for the game
        self.id_to_game[game.id] = game

        # Update the game status convenience flags
        game.starting = (status == games.Game.STARTING)
        game.playing = (status == games.Game.PLAYING)
        game.ending = (status == games.Game.ENDING)
        return game

    def set_server_status(self, status, time_stamp):
        '''
        Sets the current server status based on the given parameters.

        Args:
            status (string): The current status of the server.
            time_stamp (string): The real time when the server status changed

        Returns:
            None
        '''

        self._log('Server updated: %s %s' % (status, time_stamp))

    def _update_player(self, address, name):

        # Attempt to get the player by name and then address
        player = None
        if name != 'defaultPlayer' and name in self.name_to_player:
            player = self.name_to_player[name]
        elif address and address in self.addr_to_player:
            player = self.addr_to_player[address]
        else:
            player = players.Player(address, name)

        # Make sure the player model is up to date
        player.address = address
        player.name = name

        # Update the set of player aliases
        player.aliases.add(name)

        # Update the address mapping for human players
        if address:
            self.addr_to_player[address] = player

        # Update the id and name mappings for the player
        self.id_to_player[player.id] = player
        self.name_to_player[name] = player

        # Update the master player index
        self.players.add(player)
        return player

    def _log(self, value):
        if self.debug_enabled:
            print value

# Create a shared singleton instance of the model manager
model_mgr = ModelManager()
