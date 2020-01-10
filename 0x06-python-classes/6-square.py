#!/usr/bin/python3
class Square:
    """An empty class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """inizialization and conditioning input only to be integer"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) != tuple or \
           (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in position:
            if type(i) is not int:
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
        if self.__size == 0 or (int(self.position[1]) is 0):
            print()
            '''
            qube = ["#" for n in range(self.__size)]
            print(*(["".join(qube) for n in range(self.__size)]), sep="\n")
            '''
        for x in range(self.__size):
            for z in range(self.position[0]):
                print(" ", end="")
            for y in range(self.__size):
                print("#", end="")
            print()
