#!/usr/bin/python3
""" Defines a class that inherts from another class (BaseGeometry) """


class BaseGeometry:
    """
    The area(self) method here raises an Exception with a message,
    and the "integer_validator" method validates the value.
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """
        Intializing a Rectangle with:
        private validated width and
        private validated height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
