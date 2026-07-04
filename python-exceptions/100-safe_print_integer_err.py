#!/usr/bin/python3
"""Module that safely prints an integer, with error to stderr."""
import sys


def safe_print_integer_err(value):
    """Print an integer using {:d} formatting, reporting errors to stderr.

    Args:
        value: value of any type to try to print as an integer

    Returns:
        bool: True if value was correctly printed as an integer,
              False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
