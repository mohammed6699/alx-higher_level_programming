#!/usr/bin/python3
"""
    Define a Rectangle class
"""


class Rectangle:
    """Representation of class Rectangle"""
    def __init__(self, width=0, height=0):
        """Inisialize the class of rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """settr for the private insitance width"""
        if type(value) is not int:
            raise TypeError("idth must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """settr for the private insitance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """settr for the private insitance height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """defines the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """defines the premeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height)

    def __str__(self):
        """return the string printed"""
        string = ""
        if self.__width != 0 or self.__height !=0:
            string += '\n'.join("#" * self.__width
                                for i in range(self.__height))
        return string
