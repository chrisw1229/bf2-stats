
from models import model_mgr
from processors.awards import AwardProcessor,Column,PLAYER_COL
from stats import stat_mgr

class Processor(AwardProcessor):
    '''
    Overview
    This processor is awarded to the player with the most top 3 award rankings.

    Implementation
    Use the post processing callback to inspect all the other awards.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Olympian', 'Most Top 3 Awards',
                [PLAYER_COL, Column('Awards', Column.NUMBER, Column.DESC)])

    def post_process(self):

        # Get a list of all the award processors
        processors = stat_mgr.get_processors('awards')

        # Skip the current award
        processors.remove(self)

        for processor in processors:
            results = processor.get_results()
            if len(results) > 0:
                player_id = results[0][0]['id']
                gold = model_mgr.get_player( player_id )
                self.results[gold] += 1

            if len(results) > 1:
                player_id = results[1][0]['id']
                silver = model_mgr.get_player( player_id )
                self.results[silver] += 1

            if len(results) > 2:
                player_id = results[2][0]['id']
                bronze = model_mgr.get_player( player_id )
                self.results[bronze] += 1
