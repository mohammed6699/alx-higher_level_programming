#!/usr/bin/python3

"""
    module to define the area and prameter by class Rectangle
"""

class Rectangle:
    """rep. for the class Rectangle"""
    def __init__(self, width=0, height=0):
        """initialize the the class rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """module to return area of rectangel"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
