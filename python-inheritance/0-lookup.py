#!/usr/bin/python3
""" Function that returns a list object """


def lookup(obj):
    """
    Receives an object then returns a list 
    of available attributes and methods of it.
    """

    return dir(obj)
