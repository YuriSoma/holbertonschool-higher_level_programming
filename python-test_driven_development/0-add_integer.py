#!/usr/bin/python3
""" addition Function """


def add_integer(a, b=98):
    """
    add_integer module expects to receive 2 integer
    (or float, to be converted later to int) inputs a and b
    (b has default value = 98).
    It will return the addition of these 2 inputs,
    if inputs aren't integer or float, then it will raise TypeError exception
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
