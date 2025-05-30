#!/usr/bin/python3
""" Function checks if an object is an instance of a class """


def inherits_from(obj, a_class):
    """
    The function will receive an object and a class,
    then compare them:

    Returns True, if the object is an instance of the class
    inherited from the given class (directly or indirectly).
    Otherwise returns False.
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
