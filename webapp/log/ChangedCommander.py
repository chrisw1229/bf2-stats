
class ChangedCommander(object):
    def __init__(self, data):
        '''
        Creates a new ChangedCommander log entry.

        Args:
           data (list): data[0] = 'CR'
                        data[1] = 'New Team Name'
                        data[2] = 'New Player Name'
        '''
        self.team = data[1]
        self.player = data[2]
