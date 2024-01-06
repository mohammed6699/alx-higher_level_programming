#!/usr/bin/python3
"""
    Defines a Rechtangle class
"""


class Rectangle:
    """Representation of class Rectangle"""
    def __init__(self, width=0, height=0):
        """Inisialize the class of rectangle"""
        self.width = width
        self.height = height

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
        string == ""
        if self.__width != 0 or self.__height != 0:
            string += '\n'.join("#" * self.__width
                                for i in range(self.__height))
        return string

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """print a message for evvery deletion for each rectangle"""
        print("Bye rectangle...")
