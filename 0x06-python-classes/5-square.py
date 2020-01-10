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

    def area(self):
        """returns the area of the Square object"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Setting of getter that will get the private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print()
