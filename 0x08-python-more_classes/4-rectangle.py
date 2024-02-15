#!/usr/bin/python3
"""
    Module to define Recatngle class
"""

class Rectangle:
    """ definition for class 'Rectangle'"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the instance width"""
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
        """setter for the instance height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """for define and calculate the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """module to return the preimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) +(self.__height * 2)

    def __str__(self):
        if self.__width == 0 and self.__height == 0:
            return ""
        return ("\n".join('#' * self.__width for j in range(self.__height)))

    def __repr__(self):
        """return a string representation of the rectangle """
        return "Rectangle({:d}, {:d}".format(self.__width, self.__height)
