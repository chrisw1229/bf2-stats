
class Squad(object):

    def __init__(self, id):
        self.id = id
        self.team_id = None
        self.leader_id = None
        self.player_ids = set()

    def __repr__(self):
        return self.__dict__

EMPTY = Squad('')
 