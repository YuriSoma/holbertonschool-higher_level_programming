#!/usr/bin/python3
""" A function returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """ The function will receive an object.

        Args:
        obj - A class instance

        Return:
        The dictionary description of the obj
    """

    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
