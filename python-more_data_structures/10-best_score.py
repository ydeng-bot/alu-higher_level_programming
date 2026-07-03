#!/usr/bin/python3
"""Module that defines best_score."""


def best_score(a_dictionary):
    """Return the key with the biggest integer value.

    Returns None if the dictionary is empty or None.
    """
    if not a_dictionary:
        return None
    best_key = None
    best_value = None
    for key, value in a_dictionary.items():
        if best_value is None or value > best_value:
            best_key = key
            best_value = value
    return best_key
