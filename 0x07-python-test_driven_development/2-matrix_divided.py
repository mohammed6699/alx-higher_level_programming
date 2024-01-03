#!/usr/bin/python3
"""Module for matrix_divided method"""

def matrix_divided(matrix, div):
    """Divides all elements of the marix

    Args:
        matrix: list of element
        div:number devided by
    Returns:
        lists: list represents all elements divided by div
    Raises:
        TypeError: if the list of lists is not (int, float)
        TypeError: if therow is not equal to matrix size
        TypeError: if the number divided by is not (int, float)
        TypeError: if div is equal to 0
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    docttest.testfile("tests/2-matrix_divided.txt")
