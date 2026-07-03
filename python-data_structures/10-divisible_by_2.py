#!/usr/bin/python3
"""Module that defines divisible_by_2."""


def divisible_by_2(my_list=[]):
    """Return a list of booleans indicating multiples of 2.

    The new list has the same size as the original, with True at
    positions where the value is divisible by 2, and False otherwise.
    """
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result
