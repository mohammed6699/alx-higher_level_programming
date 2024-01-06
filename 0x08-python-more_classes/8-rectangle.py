#!/usr/bin/python3

"""
    Defines a Rectangle class
"""


class Rectangle:
    """Representation of rectangle class"""
    number_of_instances = 0
    """declare increment and decrement for each instance instantion"""
    print_symbol = '#'
    """Used as symbol for string representation"""

    def __init__(self, width=0, height=0):
        """Inisialize the class rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """print a message for evvery deletion for each rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private insitance width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """settr for the private insitance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private insitance height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """defines the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """defines the premeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns the premeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") * self.height)[:-1]

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return  rect_2
        return rect_1
