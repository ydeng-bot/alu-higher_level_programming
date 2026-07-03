#!/usr/bin/python3
"""Module that defines simple_delete."""


def simple_delete(a_dictionary, key=""):
    """Delete a key in a dictionary.

    If the key doesn't exist, the dictionary is left unchanged.
    """
    a_dictionary.pop(key, None)
    return a_dictionary
