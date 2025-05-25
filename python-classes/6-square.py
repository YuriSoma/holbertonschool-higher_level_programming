#!/usr/bin/python3
""" A class that defines a square and initializes a private attribute.
    The class also defines a class method that return the Square Area.
    Class will use @property to get size, and @size.setter to set value.

    Class will provide a method that prints a square using # with the size,
    if size = 0, the method will print empty size.

    size has default value = 0.
    size must be int and >= 0, otherwise will raise an error:
    TypeError: if size not integer
    ValueError: if size < 0
"""


class Square:
    """ A class defines Squares with initializing a private attributes """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
