#!/usr/bin/python3
"""docs for module"""


from json import loads


def from_json_string(my_str):
    """
    Function that returns the obj of a JSON representation
    """
    return loads(my_str)
