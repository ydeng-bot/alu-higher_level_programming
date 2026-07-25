#!/usr/bin/python3
"""Defines a save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file, using a JSON representation.

    Args:
        my_obj: The object to serialize and save.
        filename (str): The path of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
