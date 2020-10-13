#!/usr/bin/python3
"""docs for module"""


from json import dumps


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of a string
    """
    return dumps(my_obj)
