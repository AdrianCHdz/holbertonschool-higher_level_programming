#!/usr/bin/python3
"""
This is the say_my_name module
The function prints the values entered in a specific way
my name is <name> <surename>
and pop errors if ever seem to be one
"""

def say_my_name(first_name, last_name=""):
    """This function recieves two strings
    corresponding to the first name and the last name
    it prints the names of the variables followed by a new line
    """

    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
