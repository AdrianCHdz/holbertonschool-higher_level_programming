#!/usr/bin/python3
"""docs for module"""


def number_of_lines(filename=""):
    """
    Function that counts the number of line a given file has
    """
    with open(filename, 'r') as f:
        return len(f.readlines())
