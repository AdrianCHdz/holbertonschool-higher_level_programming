#!/usr/bin/python3
"""docs for module"""


from json import loads


def load_from_json_file(filename):
    """
    Function that saves the JSON representation of a
    python object into a file
    """
    with open(filename, 'r') as f:
        return loads(f.read())
