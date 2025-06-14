#!/usr/bin/python3
""" Converting CSV Data to JSON Format """
import json
import csv


def convert_csv_to_json(csv_file):
    """
    Function writes data to data.json

    Args:
    csv_file - csv file to be converted
    data.json - JSON file for the converted csv

    Return:
    False on fauiler, True on success.
    """

    data = []
    try:
        with open(csv_file) as cf:
            c = csv.DictReader(cf)
            for row in c:
                data.append(row)

    except Exception as e:
        return False

    try:
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        return False
    return True
