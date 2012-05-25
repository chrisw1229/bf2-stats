
import collections

from processors import BaseProcessor

class AwardProcessor(BaseProcessor):

    def __init__(self, name, desc, columns, notes=None):
        BaseProcessor.__init__(self)

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
            results.append([ player.name, values[player] ])

        # Sort the results in descending order by value
        results.sort(key=lambda row: row[1], reverse=True)
        return results
