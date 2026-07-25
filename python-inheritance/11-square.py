#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle, with __str__."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {0}/{0}".format(self._Rectangle__width)
