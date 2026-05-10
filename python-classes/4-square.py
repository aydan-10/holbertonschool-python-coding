#!/usr/bin/python3
"""Kvadratı təyin edən klass modulu."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size=0):
        """Kvadratı ölçüsü ilə inisializasiya edir.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü.
        """
        self.size = size

    @property
    def size(self):
        """Kvadratın ölçüsünü götürmək üçün getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Kvadratın ölçüsünü təyin etmək üçün setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın sahəsini hesablayır."""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı stdout-da # simvolları ilə çap edir."""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
