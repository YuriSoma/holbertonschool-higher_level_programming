#!/usr/bin/python3
""" A script adds all arguments to a Python list,
    and then save them to a file.
"""

from sys import argv
""" Importing argv method to get all arguments """
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
""" Importing save_to_json_file function to save object to json file """
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
""" Importing load_from_json_file function to load from json file """


if len(argv) > 1:
    tmp_list = []
    for i in range(1, len(argv)):
        tmp_list.append(argv[i])
    try:
        args = load_from_json_file("add_item.json")
    except FileNotFoundError as e:
        args = []
    args.extend(tmp_list)
    save_to_json_file(args, "add_item.json")
