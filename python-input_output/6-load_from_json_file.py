#!/usr/bin/python3
""" A function creates an object from JSON file """

import json
""" Importing JSON module to convert JSON to an object """


def load_from_json_file(filename):
    """ The function will receive JSON file,
        then creates a python object from it.

        Args:
        filename - A JSON file

        Return:
        A python object.
    """

    with open(filename) as f:
        return f.read(filename)
