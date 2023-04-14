#!/usr/bin/python3
"""
Python module: Create a class with
definitions
"""


class Rectangle:
    """
    Defines the class Rectangle
    number_of_instances: increments or decremets based
    on creation or deletion of instances
    print_symbol: symbol for string representation, can
    be of any type but is initialized as #

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            return '\n'.join(str(self.print_symbol) *
                             self.width for _ in range(self.height))

    def __repr__(self):
        x = "Rectangle(" + str(self.__width)
        x += ", " + str(self.__height) + ")"
        return (x)

    """
    Creates bigger_or_equal static method that
    takes two parameters: rect_1, rect_2

    """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        scene_1 = isinstance(rect_1, Rectangle)
        if scene_1:
            if rect_1.area() >= rect_2.area():
                return (rect_1)
            else:
                return (rect_2)
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")

    """
    Creates square class method that
    returns a new Rectangle instance
    """

    @classmethod
    def square(cls, size=0):
        Rectangle.__height = size
        Rectangle.__width = size
        return Rectangle(size, size)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
