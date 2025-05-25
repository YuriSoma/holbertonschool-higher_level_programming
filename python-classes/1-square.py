#!/usr/bin/python3
""" A class that defines a square and initializes a private attribute
    that will get a value (size) when an object created of the class.
"""


class Square:
    """ A class defines Squares with initializing a private attribute """
    def __init__(self, size):
        self.__size = size
