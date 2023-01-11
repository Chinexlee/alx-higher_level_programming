#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        return(size.__size)
    @size.setter
    def size(self, value):
        if type(value) is int:
            self.__size = value
        elif type(value) != int:
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be >= 0"

    def area(self):
        ar = self.__size * self.__size
        return ar
