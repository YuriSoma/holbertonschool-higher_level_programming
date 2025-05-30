#!/usr/bin/python3
""" Function checks if an object is an instance of a class """


def is_kind_of_class(obj, a_class):
    """
    The function will receive an object and a class,
    then compare them:

    Returns True, if the object is an instance of the class,
    or the object is instance of a class inherited from the given class.
    Otherwise returns False.
    """

    if type(obj) is a_class or isinstance(obj, type(a_class)):
        return True
    return False
