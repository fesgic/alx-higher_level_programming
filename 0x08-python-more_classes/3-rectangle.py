#!/usr/bin/python3
"""
define class Rectangle
"""


class Rectangle:
    """
    Initializes a rectangle class
    """
    def __init__(self, width=0, height=0):
        """ initilize empty class with these values """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ return the width private attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width private attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ return the width of private attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height private attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return area or rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ return perimeter of rectangle """
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns # string represent of rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
