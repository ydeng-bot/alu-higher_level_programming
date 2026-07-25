#!/usr/bin/python3
"""Defines a MyInt class that inherits from int with inverted == and !=."""


class MyInt(int):
    """Represents an integer with inverted equality operators."""

    def __eq__(self, value):
        """Return True if self is NOT equal to value."""
        return int(self) != value

    def __ne__(self, value):
        """Return True if self IS equal to value."""
        return int(self) == value
