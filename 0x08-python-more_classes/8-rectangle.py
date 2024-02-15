#!/usr/bin/python3

"""
    Module to defne the class 'Rectangle'
"""

class Rectangle:
    """definition for the class attribute Rectangle"""
    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize the Rectangle class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """setter to define the private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """setter to define the private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """instance for area"""
        return (self.width * self.height)

    def perimeter(self):
        """instance for perimeter"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        if self.width == 0 and self.height == 0:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        """string representation of Rectangle"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) +")"

    def __del__(self):
        """instance for deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_2
        return rect_1
