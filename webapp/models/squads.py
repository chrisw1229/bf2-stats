
class Squad(object):

    def __init__(self, id):
        self.id = id

        self.player_ids = set()

        self.reset()

    def __repr__(self):
        return self.__dict__

    def reset(self):
        self.team_id = None
        self.leader_id = None
        self.player_ids.clear()

EMPTY = Squad('')
