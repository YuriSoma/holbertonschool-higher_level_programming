#!/usr/bin/python3
""" Function checks if an object is an instance of a class """


def is_same_class(obj, a_class):
    """
    The function will receive an object and a class,
    then compare them:

    Returns True, if the object is an instance of the class,
    otherwise returns False.
    """

    if isinstance(type(obj), a_class):
        return True
    return False
