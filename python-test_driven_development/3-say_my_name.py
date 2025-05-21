#!/usr/bin/python3
""" function that prints:
    My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    The function will get 2 inputs, first_name and last_name,
    (last_name has default value = ""). Then prints:
    My name is <first name> <last name>

    It will raise a TypeError if an input is not string
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
