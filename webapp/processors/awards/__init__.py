
import collections

import models

from processors import BaseProcessor

class AwardProcessor(BaseProcessor):

    def __init__(self, name, desc, columns, notes=''):
        BaseProcessor.__init__(self)

        assert name and len(name) > 0, 'Award processor requires a name.'
        assert desc and len(desc) > 0, 'Award processor requires a description.'
        assert columns and len(columns) > 0, 'Award processor requires at least one column.'

        self.name = name
        self.desc = desc
        self.columns = columns
        self.notes = notes
        self.results = collections.Counter()

    def get_results(self):
        '''
        Gets the results calculated by this award implementation. By default, the results consist of
        a list of lists to essentially create a table. So for each row in the top-level list, we
        have a secondary list that contains all the values applicable for this award. Typically,
        this will just include a player name and a numeric value. Some implementations may override
        this function to produce more complex results, such as additional columns.

        Args:
           None

        Returns:
            results (list): A list of lists to represent a table of result values.
        '''

        return self._dict_to_rows(self.results)

    def _dict_to_rows(self, values):
        '''
        This funtcion converts the given dictionary of players -> value into a table of result
        values that matches the standard format expected by the get_results function. Keys of the
        dictionary should be player objects and values can be any primitive type. After the results
        table is generated, the rows are automatically sorted by the value column.

        Args:
           values (dict)

        Returns:
            results (list): A sorted list of lists to represent a table of result values.
        '''

        if not values: return []

        # Create a list of lists, where each row is a player name and value
        results = []
        for player,value in values.iteritems():
            if player != models.players.EMPTY:
                player_tuple = None
                if self.columns[0].data == Column.PLAYER:
                    player_tuple = {
                        'id': player.id,
                        'name': player.name,
                        'photo': player.photo_s
                    }
                else:
                    player_tuple = player.name
                value = self._format_value(values[player])
                results.append([player_tuple, value])

        # Figure out the column and direction to use when sorting
        sort_index = None
        sort_dir = None
        for index,column in enumerate(self.columns):
            if column.sorted != None:
                sort_index = index
                sort_dir = column.sorted
                break

        # Sort the results if applicable
        if sort_index:
            results.sort(key=lambda row: row[sort_index], reverse=sort_dir)
        return results

    def _format_value(self, value):
        '''
        This function converts the given results value into formatted output
        suitable for display. Typically, results just contain primitive numeric
        values and no additional formatting is required. If the value contains
        an object instance however, it may be desirable to change the output
        format. In such cases, this method can be overridden to provide custom
        value formatting.

        Args:
           value (object)

        Returns:
            value (object): A formatted version of the given value.
        '''
        return value

class Column(object):

    # Data constants
    NUMBER = 'number'
    PERCENT = 'percent'
    PLAYER = 'player'
    STRING = 'string'
    TIME = 'time'

    # Sorted constants
    ASC = True
    DESC = False

    def __init__(self, name, data=STRING, sorted=None):
        self.name = name
        self.data = data
        self.sorted = sorted

    def __repr__(self):
        return self.__dict__

PLAYER_COL = Column('Players', Column.PLAYER)
