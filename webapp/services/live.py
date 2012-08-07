
import cherrypy

from stats import stat_mgr

@cherrypy.expose()
@cherrypy.tools.json_out()
class Handler:

    def GET(self, packet_type=None, tick=None, _=None):
        '''
        Provides a list of log packets that were parsed since the given threshold.

        Args:
           packet_type (string): The type of log packets to include in the response. None indicates
                            all log types should be included.
           tick (long): A threshold after which log packets should be included.
           _ (long): A timestamp used to ensure the browser does not cache the request.

        Returns:
            packets (list): Returns the list of updated log packets.
        '''

        # Convert the tick value to a number
        if tick:
            tick = int(tick)

        # Use the live stats processor to get the requested packets
        processor = stat_mgr.get_processor('live')
        if processor:
            return processor.get_packets(packet_type, tick)
        return None
