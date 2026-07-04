#!/usr/bin/python3
"""Module that raises a NameError exception with a message."""


def raise_exception_msg(message=""):
    """Raise a NameError exception with a given message.

    Args:
        message (str): the message to attach to the exception
    """
    raise NameError(message)
