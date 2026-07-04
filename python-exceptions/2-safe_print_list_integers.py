#!/usr/bin/python3
"""Module that prints and counts integers from a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the integers among the first x elements of a list.

    Args:
        my_list (list): list containing any type of elements
        x (int): number of elements to access in my_list

    Returns:
        int: the real number of integers printed
    """
    nb_print = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            nb_print += 1
        except (ValueError, TypeError):
            continue
    print()
    return nb_print
