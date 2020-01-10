#!/usr/bin/python3
class Square:
    """An empty class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """inizialization and conditioning input only to be integer"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if len(position) != 2 or \
           type(position[0]) != int or \
                type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position) != tuple or \
           position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.position[1]):
                print()
            for x in range(self.__size):
                for z in range(self.position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print()
