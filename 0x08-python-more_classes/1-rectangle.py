#!/usr/bin/python3

"""
    Define a Rectangle by class 'Rectangle'
"""

class Rectangle:
    """representation of Rectangle class"""
    def __init__(self, width=0, height=0):
        """initialize the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter foe private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property

    def height(self):
        """setter for private instance height"""
        return self.__height
    @height.setter

    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
