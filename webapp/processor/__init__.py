
class BaseProcessor(object):

    def start(self):
        pass

    def stop(self):
        pass

    def on_kill(self, victim, attacker, weapon):
        pass
