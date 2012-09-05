
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
            print processor.name
            results = processor.get_results()
            sort_index = None
            sort_dir = None
            for index,column in enumerate(processor.columns):
                if column.sorted != None:
                    sort_index = index
                    sort_dir = column.sorted
                    break
                
            if sort_index:
                results.sort(key=lambda row: row[sort_index], reverse=sort_dir)

            if len(results) > 1:
                results[1]
            
