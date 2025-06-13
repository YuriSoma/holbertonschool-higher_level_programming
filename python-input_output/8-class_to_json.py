#!/usr/bin/python3
""" A script adds all arguments to a Python list,
    and then save them to a file.
"""

import json
""" Importing argv method to get all arguments """


def class_to_json(obj):
    """ The function will receive an object.

        Args:
        obj - A class instance

        Return:
        The dictionary description
    """

    return json.loads(obj)
