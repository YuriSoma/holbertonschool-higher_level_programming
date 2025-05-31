#!/usr/bin/python3
""" Defines a class that inherts from another class (BaseGeometry) """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
