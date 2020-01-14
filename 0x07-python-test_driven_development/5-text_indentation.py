#!/usr/bin/python3
"""
This is the add_integer module
The function adds two integers or floats

"""

def text_indentation(text):
    """This function adds to variables 'a' and 'b' which
    can be either float or int and returns the value
    casted to int"""
    if type(text) != str:
        
    n = 0
    while n < len(text):
        if text[n] == "." or text[n] == "?":
            print(text[n], end="\n")
            print()
            n += 2
        print(text[n], end="")
        n += 1
    """
    try:
        [print(a, end='') for a in text if a != "."]
    except StopIteration as n:
        print(n, end="\n")
        pass
    """
