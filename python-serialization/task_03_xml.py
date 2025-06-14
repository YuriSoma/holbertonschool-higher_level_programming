#!/usr/bin/python3
""" Serializing and Deserializing with XML """
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes to XML and saves to a file.

    Args:
    dictionary - Python dictionary.
    filename - File to save the XML.

    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize XML .

    Args:
    filename - XML source file.

    Return:
    dict - Deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dct = {}
    for child in root:
        dct[child.tag] = child.text

    return dct
