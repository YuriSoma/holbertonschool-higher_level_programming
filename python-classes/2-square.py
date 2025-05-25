#!/usr/bin/python3
""" A class that defines a square and initializes a private attribute
    that will get a value (size) when an object created of the class.

    Size must be int and >= 0, otherwise will raise an error:
    TypeError: if size not integer
    ValueError: if size < 0
"""


class Square:
    """ A class defines Squares with initializing a private attribute """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
