#!/usr/bin/python3
class Square:
    """An empty class that defines a square"""
    def __init__(self, size=0):
        """inizialization and conditioning input only to be integer"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
