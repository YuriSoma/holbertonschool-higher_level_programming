#!/usr/bin/python3
"""
Module containing class Shape and subclasses Circle and Rectangle.
"""


class VerboseList(list):
    """
    A class to define a shape.
    """
    def append(self, item):
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, iterable):
        x = 0
        for x in iterable:
            x += 1
        print("Extended the list with [{}] items.".format(x))
        super().extend(iterable)

    def remove(self, value):
        if value in self:
            print("Removed [{}] from the list.".format(value))
            super().remove(value)

    def pop(self, index=-1):
        if index in self:
            print("Popped [{}] from the list.".format(self[index]))
            super().pop(index)
