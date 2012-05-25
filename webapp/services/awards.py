
import cherrypy

from stats import stat_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self, id=None):
 
        # Handle requests for specific awards
        if id:

            # Get the processor for the requested award
            processor = stat_mgr.get_processor(id)

            # Convert the column definitions to tuples
            columns = []
            for column in processor.columns:
                columns.append(column.__dict__)

            # Respond with a summary of the award information
            return { 'id': processor.id, 'name': processor.name, 'desc': processor.desc,
                    'columns' : columns, 'notes': processor.notes,
                    'results': processor.get_results() }

        # Get a list of all the award processors
        processors = stat_mgr.get_processors('awards')

        # Build an index of the available awards
        awards = []
        for processor in processors:
            awards.append({ 'id': processor.id, 'name': processor.name, 'desc': processor.desc })

        # Sort the index by award name
        awards.sort(key=lambda a: a['name'].lower())
        return awards