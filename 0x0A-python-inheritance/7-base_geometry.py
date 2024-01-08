#!/usr/bin/python3
"""Module for BaseGeometry"""
class BaseGeometry:
    """Module for BaseGeometry class"""
    def area(self):
        """function that raises exception with massage"""
        raise Exception ("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates the value"""
       """
        Args:
            name: string
            value: int

        Raises:
            TypeError: if value is not int
            Valueerror: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
