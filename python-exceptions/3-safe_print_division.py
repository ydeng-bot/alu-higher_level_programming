#!/usr/bin/python3
"""Module that divides two integers and prints the result via finally."""


def safe_print_division(a, b):
    """Divide two integers and print the result in the finally block.

    Args:
        a (int): the dividend
        b (int): the divisor

    Returns:
        float: the result of the division, or None if division fails
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
