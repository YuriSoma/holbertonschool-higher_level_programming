#!/usr/bin/python3
""" This module has two functions, for serializaion and deserialization """
import json


def serialize_and_save_to_file(data, filename):
    """
    A function serializes and saves to a file.

    Args:
    data - A Python Dictionary with data.
    filename - The filename of the output JSON file.
    """
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    A function loads from file and deserializes.

    Args:
    filename - The filename of the input JSON file.

    Return:
    returns a Python Dictionary with the deseialized JSON data from the file.
    """
    with open(filename, "r") as f:
        dct = json.load(f)
    return dct
