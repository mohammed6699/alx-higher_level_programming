#!/usr/bin/python3
"""
    Defines a Rectangle class
"""


class Rectangle:
    """Representation of Rectangle class"""
    def __init__(self, width=0, height=0):
        """Inisialize the class rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for the private attribute width"""
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
        """setter for the private attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Defines the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        string = ""
        if self.__width != 0 or self.__height != 0:
            string += '\n' .join("#" * self.__width
                                for i in range(self.__height))
        return string

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
