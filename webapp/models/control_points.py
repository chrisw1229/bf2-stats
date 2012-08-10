
class ControlPoint(object):

    FLAG_TOP = 'top'
    FLAG_MIDDLE = 'middle'
    FLAG_BOTTOM = 'bottom'

    counter = 0

    def __init__(self, address, pos):
        self.id = str(ControlPoint.counter)
        self.address = address
        self.pos = pos

        self.status = None
        self.team_id = None
        self.trigger_id = None

        self.reset()

        ControlPoint.counter += 1

    def __repr__(self):
        return self.__dict__

    def reset(self):
        self.active = False

EMPTY = ControlPoint('', [0, 0, 0, 0])
