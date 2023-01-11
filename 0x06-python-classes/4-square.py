#!/usr/bin/python3

"""defining a class square"""

class Square:
    """representing the class square"""

    def __init__(self, size=0):
        """initializing the class

        Args:
            size (int): size of the square
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """ get and set the current method"""

        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) is int:
            self.__size = value
        elif type(value) != int:
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """defining the method area"""

        ar = self.__size * self.__size
        return ar
