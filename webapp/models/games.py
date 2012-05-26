
class Game(object):

    STARTING = 'pre'
    PLAYING = 'play'
    ENDING = 'end'

    counter = 0

    def __init__(self, status, map_id, clock_limit, score_limit):
        self.id = str(Game.counter)
        self.status = status
        self.map_id = map_id
        self.clock_limit = clock_limit
        self.score_limit = score_limit
        self.starting = False
        self.playing = False
        self.ending = False

        Game.counter += 1
EMPTY = Game('', '', 0, 0)
