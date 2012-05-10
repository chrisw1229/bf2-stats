
class BaseProcessor(object):

    def start(self):
        pass

    def stop(self):
        pass

    def on_ammo(self, event):
        pass

    def on_assist(self, event):
        pass

    def on_ban(self, event):
        pass

    def on_chat(self, event):
        pass

    def on_clock_limit(self, event):
        pass

    def on_commander(self, event):
        pass

    def on_connect(self, event):
        pass

    def on_control_point(self, event):
        pass

    def on_disconnect(self, event):
        pass

    def on_death(self, event):
        pass

    def on_game_status(self, event):
        pass

    def on_heal(self, event):
        pass

    def on_kick(self, event):
        pass

    def on_kit_drop(self, event):
        pass

    def on_kill(self, event):
        pass

    def on_kit_pickup(self, event):
        pass

    def on_repair(self, event):
        pass

    def on_reset(self, event):
        pass

    def on_revive(self, event):
        pass

    def on_score(self, event):
        pass

    def on_squad_leader(self, event):
        pass

    def on_spawn(self, event):
        pass

    def on_squad(self, event):
        pass

    def on_server_status(self, event):
        pass

    def on_team_damage(self, event):
        pass

    def on_ticket_limit(self, event):
        pass

    def on_team(self, event):
        pass

    def on_vehicle_destroy(self, event):
        pass

    def on_vehicle_enter(self, event):
        pass

    def on_vehicle_exit(self, event):
        pass

    def on_weapon(self, event):
        pass
