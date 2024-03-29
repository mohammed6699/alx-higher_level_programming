#!/usr/bin/python3
""" Module for add two ints"""


def add_integer(a, b=98):
    """
        Function two add 2 numbers

        Args:
            a: int
            b: int equal 98 (default)

        Raises:
            TypeError: a, b must be an integer

        Returns:
         sum of two numbers

    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
