#!/usr/bin/python3
""" A function convert an object to JSON file """

import json
""" Importing JSON module to convert an object to JSON """


def save_to_json_file(my_obj, filename):
    """ The function will receive an object,
        then save it to JSON file.

        Args:
        my_obj - An object

        Return:
        Nothing, just save the object to the JSON file.
    """

    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
