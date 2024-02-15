#!/usr/bin/python3
"""
    Module to define the class 'rectangle'
"""

class Rectangle:
    """definition for the class 'Rectangle'"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize the Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """setter to define the private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter to define the private attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """setter to define the private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter to define the private attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """instance attribute for area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """instance attribute for perimeter"""
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 and self.__height == 0:
            return ""
        return ("\n".join('#' * self.__width) for j in range (self.__height))
    def __repr__(self):
        """return a string representation for the Rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
