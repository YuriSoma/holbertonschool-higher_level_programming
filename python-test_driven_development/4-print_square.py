#!/usr/bin/python3
""" function that prints:
    a square using #, and the passed input "size" is its size.
"""


def print_square(size):
    """
    The function will get 1 input, size (Square size),
    then prints: prints a square as the passed size.

    If "size" is not int:
    it will raise a TypeError if an input is not string,
    or if it < 0:
    it will raise ValueError.
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    
    if size == 0:
        print('')
    else:
        for i in range(size):
            for n in range(size):
                print('#', end="")
            print("")
