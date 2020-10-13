#!/usr/bin/python3
"""docs for module"""


from json import dumps


def save_to_json_file(my_obj, filename):
    """
    Function that saves the JSON representation of a
    python object into a file
    """
    with open(filename, 'w') as f:
        f.write(dumps(my_obj))
