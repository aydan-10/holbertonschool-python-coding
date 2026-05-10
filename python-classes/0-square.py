#!/usr/bin/python3
"""Kvadratı təyin edən klass modulu."""


class Square:
    """Kvadratı təmsil edən klass."""
    def __init__(self, size):
        """Kvadratı ölçüsü ilə inisializasiya edir.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü.
        """
        self.__size = size
