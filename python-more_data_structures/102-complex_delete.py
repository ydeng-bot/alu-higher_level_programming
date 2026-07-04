#!/usr/bin/python3
"""Module that deletes keys with a specific value from a dictionary."""


def complex_delete(a_dictionary, value):
    """Delete all keys with a specific value directly from a dictionary.

    Args:
        a_dictionary (dict): the dictionary to modify (in place)
        value: the value to search for and remove

    Returns:
        dict: the same dictionary, with matching keys removed
    """
    keys_to_delete = [key for key, val in a_dictionary.items()
                       if val == value]
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary
