#!/usr/bin/python3
""" Defines a class with some methods"""


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
