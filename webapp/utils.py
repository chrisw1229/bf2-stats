
import inspect
import json

import cherrypy

class JsonEncoder(json.JSONEncoder):

    def default(self, o):
        '''
        Converts the given object into a value that is supported by the standard JSON encoder.

        Args:
           o (*): Any potential value that needs to be converted.

        Returns:
            value (*): A converted value suitable for default encoding.
        '''

        if isinstance(o, set):

            # Convert set objects to lists
            return list(o)
        elif hasattr(o, '__repr__'):

            # Convert custom objects using their preferred representation
            return o.__repr__()
        elif hasattr(o, '__dict__'):

            # Convert arbitrary objects using their class definition dictionary
            return o.__dict__

        # Apply the default encoder rules
        return json.JSONEncoder.default(self, o)

# Create a singleton reference to the encode function
json_encode = JsonEncoder().iterencode

def json_handler(*args, **kwargs):
    '''
    This is a custom callback function that handles JSON encoding for a CherryPy request.

    Args:
       args (*): Any potential ordered arguments from CherryPy.
       kwargs (*): Any potential keyword arguments from CherryPy.

    Returns:
        json (string): The JSON-encoded version of a response model.
    '''

    # Use the previous request handler to get the raw response value
    value = cherrypy.serving.request._json_inner_handler(*args, **kwargs)

    # Encode the value using the custom class above
    return json_encode(value)
