#!/usr/bin/python3
"""
This is the add_integer module
The function adds two integers or floats

"""

def add_integer(a, b=98):
    """This function adds to variables 'a' and 'b' which
    can be either float or int and returns the value
    casted to int"""

    if isinstance(a, (float, int)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (float, int)) is False:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
