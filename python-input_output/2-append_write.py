#!/usr/bin/python3
""" A function appends a given text to a given file """


def append_write(filename="", text=""):
    """ The function will receive a file path and some text,
        then appends the text to the file.

        Args:
        filename - the file path (default value is empty string).
        text - to be written in the file (default value is empty string).

        Return:
        The number of characters written.
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
