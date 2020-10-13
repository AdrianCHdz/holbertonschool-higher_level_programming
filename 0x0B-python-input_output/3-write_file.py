#!/usr/bin/python3
"""docs for module"""


def write_file(filename="", text=""):
    """
    Function that writes in a file
    """
    with open(filename, 'w+') as f:
        return f.write(text)
