#!/usr/bin/python3
"""Module that defines multiple_returns."""


def multiple_returns(sentence):
    """Return a tuple with the length of a string and its first character.

    If the sentence is empty, the first character is None.
    """
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return (len(sentence), first_char)
