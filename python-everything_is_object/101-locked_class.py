#!/usr/bin/python3
"""Defines a LockedClass that only allows a first_name attribute."""


class LockedClass:
    """Represents a class that locks out new instance attributes."""

    __slots__ = ["first_name"]
