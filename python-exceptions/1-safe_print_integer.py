#!/usr/bin/python3
"""Module that safely prints an integer."""


def safe_print_integer(value):
    """Print an integer using {:d} formatting.

    Args:
        value: value of any type to try to print as an integer

    Returns:
        bool: True if value was correctly printed as an integer,
              False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
