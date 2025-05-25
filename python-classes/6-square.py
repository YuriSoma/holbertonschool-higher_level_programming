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
        if self.__size > 0:
            for i in range(0, self.__position[1]):
                print('')

            for row in range(self.__size):
                for col in range(0, self.__position[0]):
                    print(' ', end="")
                for col in range(self.__size):
                    print('#', end="")
                print('')
        else:
            print('')

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
                not value[0] >= 0 or
                not isinstance(value[0], int) or
                len(value) != 2 or
                not value[1] >= 0 or
                not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
