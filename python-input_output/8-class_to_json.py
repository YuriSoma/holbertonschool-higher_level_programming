#!/usr/bin/python3
""" A script adds all arguments to a Python list,
    and then save them to a file.
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
