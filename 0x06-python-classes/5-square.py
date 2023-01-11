#!/usr/bin/python3

"""defining a class square"""


class Square:
    """representing the class square"""

    def __init__(self, size=0):
        """initializing the class

        Args:
            size (int): an integer representing size of square.
        """

        self.size = size

    @property
    def size(self):
        """get/set the properties of the class square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """defining the method area"""

        a = self.__size * self.__size
        return a

    def my_print(self):
        """defining the method my_print"""

        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
