#!/usr/bin/python3

"""defining the class square."""


class Square:
    """representing the class square."""

    def __init__(self, size=0, position=(0, 0)):
        """initializing the instances for the class square
        Args:
            size (int): integer representing size of square
            position (int, int): representing the postion of the square
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """defining the method size"""

        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """defining the method position"""

        return(self.__position)

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """defining the method area"""

        a = self.__size * self.__size
        return a

    def my_print(self):
        """defining the method my print"""

        if self.__size == 0:
            print("")
        else:
            for line in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for space in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
