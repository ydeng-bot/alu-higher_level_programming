#!/usr/bin/python3
"""Module that deletes keys with a specific value from a dictionary."""


def complex_delete(a_dictionary, value):
    """Delete all keys with a specific value in a dictionary copy.

    Args:
        a_dictionary (dict): the original dictionary (won't be modified)
        value: the value to search for and remove

    Returns:
        dict: a new dictionary without the keys that had the given value
    """
    new_dict = a_dictionary.copy()
    for key, val in a_dictionary.items():
        if val == value:
            del new_dict[key]
    return new_dict
