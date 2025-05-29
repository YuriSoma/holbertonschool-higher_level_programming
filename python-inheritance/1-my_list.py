#!/usr/bin/python3
""" A class that inherits form List """


class MyList(list):
    """
    class inherits from list, then prints the list sorted
    """
    def print_sorted(self):
        print(sorted(self))