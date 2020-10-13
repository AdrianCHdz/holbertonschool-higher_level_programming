#!/usr/bin/python3
"""docs for module"""


def append_write(filename="", text=""):
    """
    Function that appends into a given file a text
    """
    with open(filename, 'a+') as f:
        return f.write(text)
