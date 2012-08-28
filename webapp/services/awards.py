
import cherrypy

from stats import stat_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self, id=None):
        '''
        Provides an index of available awards or details for a specific award
        based on the given award identifier.

        Args:
           id (string): The unique identifier of an award. None indicates an
           index of all awards should be returned.

        Returns:
            awards (list): Returns the list of all awards.
            award (object): Detailed information for a specific award.
        '''
 
        # Handle requests for specific awards
        if id:
            return self.get_award(id)

        # Handle requests for the full award index
        return self.get_awards()

    def get_award(self, id):
        '''
        Provides details for a specific award based on the given award
        identifier.

        Args:
           id (string): The unique identifier of an award.

        Returns:
            award (object): Detailed information for a specific award.
        '''

        # Get the processor for the requested award
        processor = stat_mgr.get_processor(id)
        if not processor: raise cherrypy.HTTPError(404)

        processors = stat_mgr.get_processors(processor.processor_type)
        prev_id = None
        if processor.type_index > 0:
            prev_id = processors[processor.type_index - 1].id
        next_id = None
        if processor.type_index < len(processors) - 1:
            next_id = processors[processor.type_index + 1].id

        # Respond with a summary of the award information
        return { 'id': processor.id, 'name': processor.name,
                'desc': processor.desc, 'columns' : processor.columns,
                'notes': processor.notes, 'rows': processor.get_results(),
                'prev_id': prev_id, 'next_id': next_id }

    def get_awards(self):
        '''
        Provides an index of available awards.

        Args:
            None

        Returns:
            awards (list): Returns the list of all awards.
        '''

        # Get a list of all the award processors
        processors = stat_mgr.get_processors('awards')

        # Build an index of the available awards
        awards = list()
        for processor in processors:
            awards.append({ 'id': processor.id, 'name': processor.name,
                    'desc': processor.desc })

        # Sort the index by award name
        awards.sort(key=lambda a: a['name'].lower())
        return awards
