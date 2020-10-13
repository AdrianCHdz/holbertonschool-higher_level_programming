#!/usr/bin/python3
def read_file(filename=""):
    """ function that prints a text """
    with open(filename, 'r') as f:
        print("{}".format(f.read()), end="")
