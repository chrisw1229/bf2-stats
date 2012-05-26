
class Squad(object):

    def __init__(self, id):
        self.id = id
        self.team_id = None
        self.leader_id = None
        self.player_ids = set()
EMPTY = Squad('')
 