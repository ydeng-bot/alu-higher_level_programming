#!/usr/bin/python3
"""Module that defines square_matrix_simple."""


def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix.

    Returns a new matrix of the same size, without modifying the
    original matrix.
    """
    return [[value ** 2 for value in row] for row in matrix]
