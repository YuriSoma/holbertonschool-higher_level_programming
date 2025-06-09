#!/usr/bin/python3
""" A function reads given files """


def read_file(filename=""):
    """ The function will receive a file path, then prints its content.

        Args:
        filename - the file path (default value is empty string).

        Return:
        No returns, it just prints the reading of the file content.
    """

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
