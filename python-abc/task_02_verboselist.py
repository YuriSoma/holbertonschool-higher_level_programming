#!/usr/bin/python3
"""A class inherited from the built-in list class"""


class VerboseList(list):
    """
    Extend the four methods of the list class:
    append(), extend(), remove() and pop()

    So, they will print messeges when they are called.
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
        print("Removed [{}] from the list.".format(value))
        super().remove(value)

    def pop(self, index=-1):
        print("Popped [{}] from the list.".format(self[index]))
        item = super().pop(index)
        return item
