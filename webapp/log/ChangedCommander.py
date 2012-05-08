
class ChangedCommander(object):
    def __init__(self, data):
        '''
        Creates a new ChangedCommander log entry.

        Args:
           data (list): data[1] = 'CR'
                        data[2] = 'New Team Name'
                        data[3] = 'New Player Name'
        '''
        self.time = data[0]
        self.team = data[2]
        self.player = data[3]
