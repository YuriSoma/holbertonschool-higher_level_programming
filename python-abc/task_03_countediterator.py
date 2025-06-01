#!/usr/bin/python3
"""A class that extend the iter() function to count the iterations"""


class CountedIterator:
    """
    Extend the four methods of the list class:
    append(), extend(), remove() and pop()

    So, they will print messeges when they are called.
    """
    def __init__(self, iterable):
        self.it = iter(iterable)
        self.count = 0

    def get_count():
        return self.count

    def __next__(self):
        try:
            item = next(self.it)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterate")
