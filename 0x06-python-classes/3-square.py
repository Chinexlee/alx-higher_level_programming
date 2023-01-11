#!/usr/bin/python3

"""defining a class Square"""

class Square:
    """ Representing the class square."""

    def __init__(self, size=0):
        """initializing the class"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
    def area(self):
        """defining the method area"""

        return(self.__size ** 2)
