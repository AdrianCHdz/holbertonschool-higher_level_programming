#!/usr/bin/python3
"""docs for module"""


def read_lines(filename="", nb_lines=0):
    """
    Function that prints the number of lines given
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        if nb_lines >= len(lines) or nb_lines <= 0:
            nb_lines = len(lines)
        for n, _ in zip(lines, range(nb_lines)):
            print(n, end="")
