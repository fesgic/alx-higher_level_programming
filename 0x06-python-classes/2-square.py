#!/usr/bin/python3
"""
define class square
"""


class Square:
    """
    Initialize a square class
    """
    def __init__(self, size=0):
        """
        Initialize class with fields

        Args:
        size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an interger")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
