
import cherrypy
import os.path

from stats import stat_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self, id=None):
        '''
        Provides a full game state model that includes all the kill packets
        parsed for the game with the given identifier.

        Args:
           id (string): The unique identifier of the game to include in the
                            response.

        Returns:
            state (GameState): Returns the full game state including kill
                            packets.
        '''

        # Use the replay stats processor to get the requested state
        processor = stat_mgr.get_processor('replays')
        if processor:
            if id and id != 'index.json':
                id = os.path.splitext(id)[0]
                return processor.get_game_state(id)
        return None
