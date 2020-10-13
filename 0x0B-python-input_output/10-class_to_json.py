#!/usr/bin/python3
"""docs for module"""


def class_to_json(obj):
    """
    Function that returns the dictionay description
    with a simple structure for JSON serializaiton of an obj
    """
    return obj.__dict__
