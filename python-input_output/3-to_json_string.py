#!/usr/bin/python3
""" A function that returns the JSON representation of an object """

import json
""" Importing JSON module to convert python to json strin """


def to_json_string(my_obj):
    """ The function will receive an object,
        then returns the JSON representation of it.

        Args:
        my_obj - An object (String)

        Return:
        The JSON representation of it.
    """

    return json.dumps(my_obj)
