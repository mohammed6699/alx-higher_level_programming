#!/usr/bin/python3
"""
    Defines a Rectangle class
"""


class Rectangle:
    """Representation of class Rectangle"""
    def __init__(self, width=0, height=0):
        """Inisialize the class rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Private instance attribute for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private isitance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Private instance attribute for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private isitance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the premeter of the regtangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
