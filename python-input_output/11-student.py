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

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            res = {}

            for i in range(len(attrs)):
                for x in obj:
                    if attrs[i] == x:
                        res[x] = obj[x]
            return res

        return obj


def reload_from_json(self, json):
    """ Replaces all attributes of the Student instance """
    for attr in json:
        self.__dict__[attr] = json[attr]
