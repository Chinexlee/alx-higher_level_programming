#!/usr/bin/python3

"""create a class called Rectangle"""


class Rectangle:
    """class rectangle created"""

    def __init__(self, width=0, height=0):
        """initializing class Rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """set/get property of the class width"""

        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is int:
            self.__width = value

        elif type(value) != int:
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """set/get property of the class height"""

        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is int:
            self.__height = value

        elif type(value) != int:
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")
