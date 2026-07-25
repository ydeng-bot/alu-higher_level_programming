#!/usr/bin/python3
"""Defines an append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing search_string.

    Args:
        filename (str): The path of the file to update.
        search_string (str): The string to search for in each line.
        new_string (str): The line to insert after each match.
    """
    with open(filename) as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
