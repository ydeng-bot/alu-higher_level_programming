#!/usr/bin/python3
"""Module that divides two lists element by element."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide two lists element by element, handling errors gracefully.

    Args:
        my_list_1 (list): first list (dividends)
        my_list_2 (list): second list (divisors)
        list_length (int): length of the resulting list

    Returns:
        list: a new list of length list_length with the division results
    """
    new_list = []
    for i in range(list_length):
        division = 0
        try:
            division = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(division)
    return new_list
