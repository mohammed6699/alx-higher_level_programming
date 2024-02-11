#!/usr/bin/python3
"""Module for devide matrix"""

def matrix_divided(matrix, div):
    """
    Devide all elements of the matrix by div
    
    Args:
        matrix: matrix contains the members
        div: number deviide the matrix by

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    return:
        lists: list of the devide matrix
    """
    if not isinstance (div, (int, float)):
        raise TypeError ('div must be a number')
    if not isinstance(matrix, list) or len(raw) == 0:
        raise TypeError ('matrix must be a matrix (list of lists) of integers/floats')
    for row in matrix:
        if len(row) != len(matrix):
            raise TypeError ('Each row of the matrix must have the same size')
    if div == 0:
        raise ZeroDivisionError ('division by zero')

    return [[round(x/div, 2) for x in row] for row in matrix]
if __name__ == "__main__"
import doctest
doctest.testfile("tests/2-matrix_divided.txt")
