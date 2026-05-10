#!/usr/bin/python3
"""Kvadratı təyin edən klass modulu."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size=0):
        """Kvadratı ölçüsü ilə inisializasiya edir.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Kvadratın sahəsini hesablayır.

        Returns:
            Kvadratın cari sahəsi.
        """
        return self.__size ** 2
