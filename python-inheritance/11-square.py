#!/usr/bin/python3
""" Defines a class that inherts from another class (BaseGeometry) """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, inherted from the Rectangle class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
