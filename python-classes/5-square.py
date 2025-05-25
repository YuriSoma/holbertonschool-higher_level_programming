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
    """ A class defines Squares with initializing a private attribute """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size > 0:
            for row in range(self.__size):
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
        else:
            self.__size = value
