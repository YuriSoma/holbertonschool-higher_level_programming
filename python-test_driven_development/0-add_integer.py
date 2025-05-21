#!/usr/bin/python3
"""
    add_integer module expects to receive 2 integer
    (or float, to be converted later to int) inputs a and b
    (b has default value = 98).
    It will return the addition of these 2 inputs,
    if inputs aren't integer or float, then it will raise TypeError exception
    
"""
def add_integer(a, b=98):
    """ addition Function """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
