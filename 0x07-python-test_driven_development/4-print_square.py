#!/usr/bin/python3
"""
This is the print_square module
The only function in here has the purpouse of
drawing a grid in the display
"""

def print_square(size):
    """This function prints a "#" to draw
    the "area" of the square with the given size
    to create a grid"""

    if isinstance(size, (int, float)) is False or\
       (isinstance(size, float) is True and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    [(print("#" * size)) for i in range(size)]

if __name__ == "__main__":
    print_square()
