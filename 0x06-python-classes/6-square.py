#!/usr/bin/python3
"""
define class square
"""


class Square:
    """
    Initialize a square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize class with fields

        Args:
        size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    def area(self):
        """
        Get Area of Square

        Args:
        size: Square having a size
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        get size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set Value of Size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """
        Print to stdout square with character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__position[1]):
                print()

            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """
        get position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Set position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) and isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 1:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
