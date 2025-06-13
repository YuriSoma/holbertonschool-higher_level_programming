#!/usr/bin/python3
""" Student class
"""


class Student:
    """ Creates instances of Students"""

    def __init__(self, first_name, last_name, age):
        """ Instantiation method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method that returns directory description """
        return self.__dict__.copy()
