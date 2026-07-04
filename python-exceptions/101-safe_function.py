#!/usr/bin/python3
"""Module that safely executes a function."""
import sys


def safe_function(fct, *args):
    """Execute a function safely, catching any exception.

    Args:
        fct: pointer to the function to execute
        *args: arguments to pass to fct

    Returns:
        The result of fct(*args), or None if an exception occurred
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
