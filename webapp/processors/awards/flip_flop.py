from processors.awards import AwardProcessor,Column,PLAYER_COL

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the most number team changes

    Implementation
	Whenever a team event is received the change is cached.

    Notes
	None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Flip Flop', 'Most Team Changes',
                [PLAYER_COL, Column('Teams', Column.NUMBER, Column.DESC)])

	self.lastTeam = dict()

##    def on_spawn(self, e):
##
##        if e.player.name == '6MTZHP':
##            print 'spawn'
##            print e.tick
            
    def on_team(self, e):

##        if e.player.name == '6MTZHP':
##            print 'team'
##            print e.tick
            
        if e.player not in self.lastTeam:
            self.lastTeam[e.player] = e.team
            return

        if e.team != self.lastTeam[e.player]:
            self.lastTeam[e.player] = e.team
            self.results[e.player] += 1
