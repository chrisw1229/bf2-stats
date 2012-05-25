
import cherrypy

from stats import stat_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self, id=None):
        '''
        Provides an index of available awards or details for a specific award based on the given
        award identifier.

        Args:
           id (string): The unique identifier of an award. None indicates an index of all awards
                should be returned.

        Returns:
            awards (list): Returns the list of all awards.
            award (object): Detailed information for a specific award.
        '''
 
        # Handle requests for specific awards
        if id:

            # Get the processor for the requested award
            processor = stat_mgr.get_processor(id)

            # Respond with a summary of the award information
            return { 'id': processor.id, 'name': processor.name, 'desc': processor.desc,
                    'columns' : processor.columns, 'notes': processor.notes,
                    'results': processor.get_results() }

        # Get a list of all the award processors
        processors = stat_mgr.get_processors('awards')

        # Build an index of the available awards
        awards = list()
        for processor in processors:
            awards.append({ 'id': processor.id, 'name': processor.name, 'desc': processor.desc })

        # Sort the index by award name
        awards.sort(key=lambda a: a['name'].lower())
        return awards