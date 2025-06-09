#!/usr/bin/python3
""" A function that returns a python object represented by a JSON string """

import json
""" Importing JSON module to convert json string to python object """


def from_json_string(my_str):
    """ The function will receive a JSON string,
        then returns a python object represented by the JSON string.

        Args:
        my_str - JSON string

        Return:
        The python object, represented by it.
    """

    return json.loads(my_str)
