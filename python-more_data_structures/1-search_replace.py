#!/usr/bin/python3
"""Module that defines search_replace."""


def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list.

    The original list is not modified.
    """
    return [replace if value == search else value for value in my_list]
