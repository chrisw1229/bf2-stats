import processor.award

class StatManager(object):

    parsers = {}
    processors = []
    previous_time = 0
    current_time = 0
    players = {}

    # This method will be called to initialize the manager
    def start(self):
        print 'STAT MANAGER - STARTING'

        # Register all the parse functions
        self.parsers['AM'] = self.parse_ammo
        self.parsers['BN'] = self.parse_ban
        self.parsers['CH'] = self.parse_chat
        self.parsers['CL'] = self.parse_clock_limit
        self.parsers['CM'] = self.parse_commander
        self.parsers['CN'] = self.parse_connect
        self.parsers['CP'] = self.parse_control_point
        self.parsers['DC'] = self.parse_disconnect
        self.parsers['DT'] = self.parse_death
        self.parsers['GS'] = self.parse_game_status
        self.parsers['HL'] = self.parse_heal
        self.parsers['KC'] = self.parse_kick
        self.parsers['KD'] = self.parse_kit_drop
        self.parsers['KL'] = self.parse_kill
        self.parsers['KP'] = self.parse_kit_pickup
        self.parsers['RP'] = self.parse_repair
        self.parsers['RS'] = self.parse_reset
        self.parsers['RV'] = self.parse_revive
        self.parsers['SC'] = self.parse_score
        self.parsers['SL'] = self.parse_squad_leader
        self.parsers['SP'] = self.parse_spawn
        self.parsers['SQ'] = self.parse_squad
        self.parsers['SS'] = self.parse_server_status
        self.parsers['TD'] = self.parse_team_damage
        self.parsers['TL'] = self.parse_ticket_limit
        self.parsers['TM'] = self.parse_team
        self.parsers['VD'] = self.parse_vehicle_destroy
        self.parsers['VE'] = self.parse_vehicle_enter
        self.parsers['VX'] = self.parse_vehicle_exit
        self.parsers['WP'] = self.parse_weapon

        # Start all the log processors
        self.processors = [processor.award.Processor()]
        for proc in self.processors:
            proc.start()

        print 'STAT MANAGER - STARTED'

    # This method will be called to shutdown the manager
    def stop(self):
        print 'STAT MANAGER - STOPPING'

        # Stop all the log processors
        for proc in reversed(self.processors):
            proc.stop()

        print 'STAT MANAGER - STOPPED'

    def parse(self, line):
        '''
        Takes in a log entry line and parses it into a log data structure more convenient to use.

        Args:
           line (string): Raw log entry from Battle Field 2 mod.

        Returns:
           None
        '''

        # Break the line into individual elements
        elements = line.split(';')
        assert len(elements) > 1, 'Invalid log line %s' % 'line'

        # Extract the log time and type
        timestamp = int(elements[0])
        log_type = str(elements[1])
        values = elements[2:]

        # Update the time values
        self.previous_time = self.current_time
        self.current_time = timestamp

        # Attempt to parse the log entry based on type
        try:
            parseFunc = self.parsers[log_type]
            parseFunc(values)
        except KeyError:
            print 'Unknown log entry type: ', log_type

    def parse_ammo(self, values):
        print 'PARSE AMMO: ', values

    def parse_ban(self, values):
        print 'PARSE BAN: ', values

    def parse_chat(self, values):
        print 'PARSE CHAT: ', values

    def parse_clock_limit(self, values):
        print 'PARSE CLOCK LIMIT: ', values

    def parse_commander(self, values):
        print 'PARSE COMMANDER: ', values

    def parse_connect(self, values):
        print 'PARSE CONNECT: ', values

    def parse_control_point(self, values):
        print 'PARSE CONTROL POINT: ', values

    def parse_disconnect(self, values):
        print 'PARSE DISCONNECT: ', values

    def parse_death(self, values):
        print 'PARSE DEATH: ', values

    def parse_game_status(self, values):
        print 'PARSE GAME STATUS: ', values

    def parse_heal(self, values):
        print 'PARSE HEAL: ', values

    def parse_kick(self, values):
        print 'PARSE KICK: ', values

    def parse_kit_drop(self, values):
        print 'PARSE KIT DROP: ', values

    def parse_kill(self, values):
        print 'PARSE KILL: ', values

    def parse_kit_pickup(self, values):
        print 'PARSE KIT PICKUP: ', values

    def parse_repair(self, values):
        print 'PARSE REPAIR: ', values

    def parse_reset(self, values):
        print 'PARSE RESET: ', values

    def parse_revive(self, values):
        print 'PARSE REVIVE: ', values

    def parse_score(self, values):
        print 'PARSE SCORE: ', values

    def parse_squad_leader(self, values):
        print 'PARSE SQUAD LEADER: ', values

    def parse_spawn(self, values):
        print 'PARSE SPAWN: ', values

    def parse_squad(self, values):
        print 'PARSE SQUAD: ', values

    def parse_server_status(self, values):
        print 'PARSE SERVER STATUS: ', values

    def parse_team_damage(self, values):
        print 'PARSE TEAM DAMAGE: ', values

    def parse_ticket_limit(self, values):
        print 'PARSE TICKET LIMIT: ', values

    def parse_team(self, values):
        print 'PARSE TEAM: ', values

    def parse_vehicle_destroy(self, values):
        print 'PARSE VEHICLE DESTROY: ', values

    def parse_vehicle_enter(self, values):
        print 'PARSE VEHICLE ENTER: ', values

    def parse_vehicle_exit(self, values):
        print 'PARSE VEHICLE EXIT: ', values

    def parse_weapon(self, values):
        print 'PARSE WEAPON: ', values

statMgr = StatManager()
