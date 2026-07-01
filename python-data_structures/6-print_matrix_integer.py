#!/usr/bin/python3
"""Module that defines print_matrix_integer."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers.

    Each row is printed on its own line, with values separated
    by a single space.
    """
    for row in matrix:
        line = ""
        for i in range(len(row)):
            line += "{:d}".format(row[i])
            if i != len(row) - 1:
                line += " "
        print(line)
