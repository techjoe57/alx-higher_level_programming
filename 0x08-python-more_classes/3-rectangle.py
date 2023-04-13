#!/usr/bin/python3
"""
Python module: Create a class with
definitions
"""


class Rectangle:
    """Defines the class Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """The width property setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """The property height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        rec_area = self.__height * self.__width
        return rec_area

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        rec_perim = (2 * self.__width) + (2 * self.__height)
        return rec_perim

    def __str__(self):
        return '\n'.join('#' * self.width for _ in range(self.height))
