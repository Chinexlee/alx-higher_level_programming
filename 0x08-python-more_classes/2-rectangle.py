#!/usr/bin/python3

"""create a class called Rectangle"""


class Rectangle:
    """class rectangle created"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """set/get property of width"""

        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """set/get property of the class height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    def area(self):
        """defining a method area"""

        a = self.__width * self.__height
        return(a)

    def perimeter(self):
        """defining the method perimeter of the class rectangle"""

        if self.__width or self.__height is 0:
            return(int(0))
        elif self.__width or self.__height > 0:
            p = (2 * self.__width) + (2 * self.__height)
            return(p)
