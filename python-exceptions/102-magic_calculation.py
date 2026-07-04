#!/usr/bin/python3
"""Module that performs a magic calculation, replicating given bytecode."""


def magic_calculation(a, b):
    """Perform a magic calculation matching the disassembled bytecode.

    Args:
        a (int): first value
        b (int): second value

    Returns:
        int/float: the result of the calculation
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except Exception:
            result = b + a
            break
    return result
